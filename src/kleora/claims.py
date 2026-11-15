"""The verified access token."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Claims:
    """What a verified Kleora access token says.

    Frozen, and the repeated members are tuples rather than lists: a verified
    token is a value, and a caller that mutated `permissions` would be editing
    an authorisation decision in place. `in`, iteration, indexing and `len`
    read the same as on a list, which is all the quickstart does with them.

    `tenant`, `tenant_slug`, `email` and `email_verified` are `None` when the
    claim is absent — a session with no resolved tenant, or a scope without
    `email`. `roles` and `permissions` are then empty, never `None`.
    """

    iss: str
    sub: str
    aud: tuple[str, ...]
    exp: int
    iat: int
    jti: str
    client_id: str
    scope: str
    env: str
    amr: tuple[str, ...]
    roles: tuple[str, ...] = ()
    permissions: tuple[str, ...] = ()
    permissions_truncated: bool = False
    tenant: str | None = None
    tenant_slug: str | None = None
    email: str | None = None
    email_verified: bool | None = None
