"""Regenerate the generated clients from the OpenAPI documents Kleora serves.

    uv run python scripts/generate_client.py

Fetches two deployed documents and writes two committed copies and two trees:

* The management API (https://api.kleora.io/api/v1/openapi.json,
  `MANAGEMENT_OPENAPI_URL` overrides it) → `openapi/management-v1.json` and
  `kleora._generated`. `openapi-python-client` writes the whole of what this
  package knows about the management API's wire; `kleora.management` wraps it.
* The end-user self-service API (https://id.kleora.eu/account/v1/openapi.json,
  `ACCOUNT_OPENAPI_URL` overrides it) → `openapi/account-v1.json` and
  `kleora._generated_account`. `kleora.account` wraps it, with methods named
  for the operation rather than the route. The unit tests read the committed
  copy, so they hold the wrappers to the document without the network.

Each document is written with its keys sorted, so the committed copy changes only
when the API does, and the tree is generated from that copy. CI runs this script
and fails when anything differs from what is committed, so a change to the
deployed API surfaces as a red check rather than as a client that silently
disagrees with the server.

Three things happen that the generator does not do itself. Its output is a
package directory named after the document, so it is generated into a temporary
directory and moved into place. It leaves its own `.ruff_cache` behind, which is
a build artefact and not part of the client. And every file gets the banner that
says where it came from, because a tree with no banner is a tree somebody
eventually edits by hand.
"""

import json
import os
import shutil
import subprocess
import tempfile
import urllib.request
from pathlib import Path

SDK = Path(__file__).resolve().parent.parent

MANAGEMENT_URL = "https://api.kleora.io/api/v1/openapi.json"
ACCOUNT_URL = "https://id.kleora.eu/account/v1/openapi.json"

# The documents' hosts refuse the default `Python-urllib/x.y` agent with a 403,
# so the request names itself.
USER_AGENT = "kleora-python-generator"

MANAGEMENT_BANNER = f"""# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# ({MANAGEMENT_URL}). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
"""

ACCOUNT_BANNER = f"""# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed self-service API document
# ({ACCOUNT_URL}). `kleora.account` wraps this tree; nothing outside the
# package imports it.
"""

#: `(url, committed copy, destination, banner)` for each tree.
TREES: tuple[tuple[str, Path, Path, str], ...] = (
    (
        os.environ.get("MANAGEMENT_OPENAPI_URL") or MANAGEMENT_URL,
        SDK / "openapi" / "management-v1.json",
        SDK / "src" / "kleora" / "_generated",
        MANAGEMENT_BANNER,
    ),
    (
        os.environ.get("ACCOUNT_OPENAPI_URL") or ACCOUNT_URL,
        SDK / "openapi" / "account-v1.json",
        SDK / "src" / "kleora" / "_generated_account",
        ACCOUNT_BANNER,
    ),
)

# The only edits made to the generator's output, all inside `client.py`, each
# declared as `(line, replacement, how many times that line must appear)`. The
# count is the drift guard: a generator that renames a method or a field would
# otherwise leave the patch silently unapplied, and a silent no-op here is either
# a type surface nothing checks or a bearer token back in `repr`.
#
# The first two are `mypy --strict`'s only complaint about this tree.
# `Client.__exit__` takes `*args: object` and forwards them to
# `httpx.Client.__exit__`, whose three parameters are typed precisely;
# openapi-python-client 0.29 has written it that way since the context managers
# were added. The ignore is narrow — one error code, on the four forwarding
# calls — and `warn_unused_ignores` (strict) turns it into an error of its own
# the day upstream types the signature, so it cannot outlive the defect.
#
# The third and fourth keep the management bearer token out of every accidental
# rendering of the client. `AuthenticatedClient` is an attrs `@define` class and
# `token` is a plain public field, so `repr(client)`, an f-string, a traceback
# frame or a structured log line prints the credential in full.
# `field(repr=False)` is attrs' own answer; `field` is already imported by the
# generated module, and the field stays mandatory because no default is given.
#
# Hiding `token` is not enough on its own, which is what the fourth patch is
# for: `get_httpx_client` writes `Authorization: Bearer <token>` into `_headers`
# the first time a request is made, so from then on the credential is back in
# the repr through a different field. `_headers` is hidden on both classes — the
# line is identical in each, and a header dictionary is where a credential ends
# up whichever class is holding it.
PATCHES: tuple[tuple[str, str, int], ...] = (
    (
        "        self.get_httpx_client().__exit__(*args, **kwargs)",
        "        self.get_httpx_client().__exit__(*args, **kwargs)  # type: ignore[arg-type]",
        2,
    ),
    (
        "        await self.get_async_httpx_client().__aexit__(*args, **kwargs)",
        "        await self.get_async_httpx_client().__aexit__(*args, **kwargs)"
        "  # type: ignore[arg-type]",
        2,
    ),
    ("    token: str", "    token: str = field(repr=False)", 1),
    (
        '    _headers: dict[str, str] = field(factory=dict, kw_only=True, alias="headers")',
        "    _headers: dict[str, str] = field("
        'factory=dict, kw_only=True, alias="headers", repr=False)',
        2,
    ),
)
CLIENT = ("client.py",)


def fetch(url: str, copy: Path) -> None:
    """Write the document at `url` to `copy`, keys sorted, array order kept."""
    request = urllib.request.Request(
        url, headers={"Accept": "application/json", "User-Agent": USER_AGENT}
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        document = json.load(response)
    copy.parent.mkdir(parents=True, exist_ok=True)
    copy.write_text(
        json.dumps(document, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {copy.relative_to(SDK)} from {url}")


def generate(document: Path, into: Path) -> None:
    subprocess.run(
        [
            "openapi-python-client",
            "generate",
            "--path",
            str(document),
            "--meta",
            "none",
            "--output-path",
            str(into),
            "--overwrite",
        ],
        check=True,
        cwd=into.parent,
    )


def patch(module: Path) -> None:
    """Apply `PATCHES` to `module`, or fail saying which line has moved."""
    lines = module.read_text(encoding="utf-8").splitlines(keepends=True)
    for needle, replacement, expected in PATCHES:
        found = [index for index, line in enumerate(lines) if line.rstrip("\n") == needle]
        if len(found) != expected:
            raise SystemExit(
                f"{module.name}: expected {expected} occurrences of {needle.strip()!r}, "
                f"found {len(found)}; the generator's output has moved and "
                f"scripts/generate_client.py needs rereading"
            )
        for index in found:
            lines[index] = replacement + "\n"
    module.write_text("".join(lines), encoding="utf-8")


def write_tree(document: Path, destination: Path, banner: str) -> None:
    """Generate one tree into a temporary directory, patch it, and move it into place."""
    with tempfile.TemporaryDirectory() as workspace:
        generated = Path(workspace) / destination.name
        generate(document, generated)
        shutil.rmtree(generated / ".ruff_cache", ignore_errors=True)
        patch(generated.joinpath(*CLIENT))
        for module in sorted(generated.rglob("*.py")):
            module.write_text(banner + module.read_text(encoding="utf-8"), encoding="utf-8")

        if destination.exists():
            shutil.rmtree(destination)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(generated), str(destination))

    print(f"wrote {destination.relative_to(SDK)} from {document.relative_to(SDK)}")


def main() -> int:
    for url, copy, _, _ in TREES:
        fetch(url, copy)
    for _, copy, destination, banner in TREES:
        write_tree(copy, destination, banner)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
