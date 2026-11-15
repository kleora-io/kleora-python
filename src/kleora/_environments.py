"""Classifying an issuer and an API key as production or sandbox.

Both halves of the environment guard reduce to one comparison: a `kl_test_` key
belongs to a sandbox environment and a `kl_live_` key to a production one, and
an issuer says which it is in its host — the sandbox form of
`https://{slug}.kleora.eu` is `https://{slug}-sandbox.kleora.eu`.

The host half of that is `classify_host`, and it is **one rule for every SDK**:
whether the first DNS label ends in `-sandbox`. `@kleora-io/browser` and
`@kleora-io/node` implement the same test, and all three carry the same table
of boundary cases in their tests, so a disagreement fails somewhere rather than
waiting to be discovered by a customer.
"""

from __future__ import annotations

import re
from typing import Literal
from urllib.parse import urlsplit

from .errors import KleoraError

EnvironmentKind = Literal["production", "sandbox"]

# A sandbox issuer's first label is its App's slug plus this.
SANDBOX_SUFFIX = "-sandbox"
KEY_PREFIXES: dict[str, EnvironmentKind] = {
    "kl_live_": "production",
    "kl_test_": "sandbox",
}

# A `:port` on the end of a host, which `URL.host` carries in the TypeScript
# packages and `urlsplit(...).hostname` does not carry here. Stripped in both,
# so the same host string classifies the same way in every SDK.
_PORT_SUFFIX = re.compile(r":\d+$")


def classify_host(host: str) -> EnvironmentKind:
    """`sandbox` when the host's **first** DNS label ends in `-sandbox`.

    The one rule, shared with `@kleora-io/browser` and `@kleora-io/node`
    (both carry the same table of boundary cases). It is the inverse of how the
    platform mints an issuer: `{slug}.{base}` for production and
    `{slug}-sandbox.{base}` for sandbox, an App slug is a *single* DNS label,
    and no slug may end in `-sandbox` — so the first label ends in `-sandbox`
    if and only if the environment is, for any base domain, scheme or port.

    Sandbox issuers used to be `{slug}.sandbox.{base}`, and the rule was "the
    second label is `sandbox`"; that shape is minted nowhere any more. Before
    that it was a substring test for `.sandbox.`, which a base domain carrying the label —
    `corp.sandbox.internal`, say, whose *production* issuer is
    `acme.corp.sandbox.internal` — reads as sandbox. Anchoring the test to the
    one label the platform controls is what keeps the guard from relaxing: a
    base domain never reaches the first label.

    Compared case-insensitively, with any `:port` ignored.
    """

    first = _PORT_SUFFIX.sub("", host.lower()).split(".")[0]
    return (
        "sandbox"
        if len(first) > len(SANDBOX_SUFFIX) and first.endswith(SANDBOX_SUFFIX)
        else "production"
    )


def normalise_issuer(issuer: str) -> str:
    """An issuer compares by exact string, so only a trailing `/` is forgiven.

    An access token's `iss` is the environment's issuer exactly, with no trailing
    slash; a configured value copied out of a browser bar
    tends to carry one, and rejecting every token for it would be a bad trade.
    """

    return issuer.rstrip("/")


def classify_issuer(issuer: str) -> EnvironmentKind:
    """`classify_host` over the issuer's host, which an issuer must have."""

    split = urlsplit(issuer)
    host = split.hostname or split.path.split("/")[0].split(":")[0]
    if not host:
        raise KleoraError(f"{issuer!r} is not a usable issuer: it names no host")
    return classify_host(host)


def classify_api_key(api_key: str) -> EnvironmentKind:
    """The environment a key's prefix says it belongs to.

    An unrecognised prefix is a `KleoraError` rather than an
    `EnvironmentMismatch`: nothing mismatches, the value simply is not a
    Kleora API key, and saying so is more useful than naming an environment
    it never claimed.
    """

    for prefix, kind in KEY_PREFIXES.items():
        if api_key.startswith(prefix):
            return kind
    raise KleoraError(
        "api_key is not a Kleora API key: it starts with neither 'kl_live_' nor 'kl_test_'"
    )


def redact_api_key(api_key: str) -> str:
    """What a `repr` may show: the literal prefix and nothing random.

    The console displays a key's prefix — the literal plus the first eight
    random characters — but a `repr` reaches tracebacks and log
    lines that nobody chose, so this shows the eight-character literal only.
    """

    for prefix in KEY_PREFIXES:
        if api_key.startswith(prefix):
            return f"{prefix}…"
    return "…"
