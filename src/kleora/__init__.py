"""The Kleora Python SDK.

Two halves that never do each other's job:

* **verification** — `verify_access_token` and the `JWKSCache` behind it. Local,
  offline apart from the issuer's JWKS document, and the only part of this
  package that sits on a customer's request path.
* **administration** — `ManagementClient` and `AsyncManagementClient` over the
  management API, wrapping the generated client under `kleora._generated`.
* **self-service** — `AccountClient` over `/account/v1/*`, called with an end
  user's own `self_service` token and wrapping `kleora._generated_account`, and
  `account_portal_url`, the hosted account portal's URL. Both work
  only for a Client that lists `self_service` in `allowed_scopes`.

The generated trees are regenerated from the OpenAPI documents Kleora serves
(`scripts/generate_client.py`) and are never edited by hand; import from them
directly for the operations this module does not re-export.
"""

from ._environments import EnvironmentKind, classify_api_key, classify_issuer
from ._meta import USER_AGENT, __version__
from .account import AccountClient
from .claims import Claims
from .errors import (
    ApiError,
    EnvironmentMismatch,
    KleoraError,
    ProblemError,
    TokenError,
    TokenErrorCode,
)
from .jwks import AsyncJWKSCache, JWKSCache
from .management import AsyncManagementClient, ManagementClient
from .portal import ACCOUNT_PORTAL_SECTIONS, AccountPortalSection, account_portal_url
from .verify import verify_access_token, verify_access_token_async

__all__ = [
    "ACCOUNT_PORTAL_SECTIONS",
    "USER_AGENT",
    "AccountClient",
    "AccountPortalSection",
    "ApiError",
    "AsyncJWKSCache",
    "AsyncManagementClient",
    "Claims",
    "EnvironmentKind",
    "EnvironmentMismatch",
    "JWKSCache",
    "KleoraError",
    "ManagementClient",
    "ProblemError",
    "TokenError",
    "TokenErrorCode",
    "__version__",
    "account_portal_url",
    "classify_api_key",
    "classify_issuer",
    "verify_access_token",
    "verify_access_token_async",
]
