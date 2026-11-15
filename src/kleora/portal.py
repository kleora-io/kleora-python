"""The hosted account portal's URL.

```
{issuer}/account[/{section}]?client_id={client_id}&return_to={url}
```

A pure function, keyword-only, for a server rendering the link into a page.
The same rules as `@kleora-io/browser`'s and `@kleora-io/node`'s `accountPortalUrl`, and
the same cases in `tests/test_portal.py` as in theirs.

**The portal is offered only for a Client whose `allowed_scopes` include
`self_service`** (that list is the consent, because there is no consent
screen). For any other Client this URL still opens,
and every portal page says that managing the account there is not offered. The
URL cannot tell the two apart; the issuer decides when the page loads.

Link it as a new tab or a top-level navigation, **never a frame**: every issuer
document refuses to be framed (`frame-ancestors 'none'`).
"""

from __future__ import annotations

from typing import Literal, get_args
from urllib.parse import urlencode, urlsplit

from .errors import KleoraError

AccountPortalSection = Literal["profile", "password", "security", "sessions", "danger"]
"""The portal's sections, in the order it lists them — the `PortalSection` enum of
`openapi/account-v1.json`, which `tests/test_portal.py` holds equal.

`danger` exists only where the Environment offers self-deletion; linking to it
elsewhere lands on the portal's own not-found page.
"""

ACCOUNT_PORTAL_SECTIONS: tuple[AccountPortalSection, ...] = get_args(AccountPortalSection)


def _invalid(message: str) -> KleoraError:
    # `KleoraError('invalid_configuration')` in the TypeScript packages, whose
    # errors carry a `code`; this package's `KleoraError` carries a message.
    return KleoraError(f"invalid configuration: {message}")


def _absolute(name: str, value: str) -> None:
    split = urlsplit(value)
    if split.scheme not in {"http", "https"} or not split.netloc:
        raise _invalid(f"{name} must be an absolute http(s) URL, got {value!r}")


def _assert_return_to(value: str) -> None:
    """Refuse a `return_to` of the wrong *shape*, never one that is merely unregistered.

    The three rules for a Client's registered URI: absolute `http`/`https`, no
    fragment, no userinfo. A value breaking one can never equal a
    `post_logout_redirect_uris` entry, so the issuer would silently drop the link.
    Membership is the issuer's to check — this package cannot know the list, and a
    check that passes locally and fails in production is worse than none.
    """

    _absolute("return_to", value)
    split = urlsplit(value)
    if "#" in value:
        raise _invalid(f"return_to must not carry a fragment, got {value!r}")
    if split.username is not None or split.password is not None or "@" in split.netloc:
        raise _invalid(f"return_to must not carry userinfo, got {value!r}")


def account_portal_url(
    *,
    issuer: str,
    client_id: str,
    section: AccountPortalSection | None = None,
    return_to: str | None = None,
) -> str:
    """The account portal's URL for `client_id`'s users — no request is made.

    Works only for a Client that lists `self_service` in `allowed_scopes`; for any
    other, the portal renders its "not offered" sentence. `return_to` becomes the
    portal's "back" link only when it equals one of the Client's
    `post_logout_redirect_uris` exactly, and is otherwise ignored by the issuer.
    """

    _absolute("issuer", issuer)
    if not client_id:
        raise _invalid("client_id must not be empty")
    if section is not None and section not in ACCOUNT_PORTAL_SECTIONS:
        raise _invalid(
            f"section must be one of {', '.join(ACCOUNT_PORTAL_SECTIONS)}; got {section!r}"
        )
    if return_to is not None:
        _assert_return_to(return_to)

    path = "/account" if section is None else f"/account/{section}"
    query: dict[str, str] = {"client_id": client_id}
    if return_to is not None:
        query["return_to"] = return_to
    return f"{issuer.rstrip('/')}{path}?{urlencode(query)}"
