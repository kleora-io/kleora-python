"""Local access-token verification.

Seven checks, in order, and nothing else: no call to
`/oauth/userinfo`, no request except the issuer's JWKS document. Verification
that needed a round trip to us would put our availability in front of every one
of a customer's API requests.
"""

from __future__ import annotations

import threading
import time
from typing import Any

import jwt
from jwt import PyJWK
from jwt.exceptions import InvalidSignatureError, PyJWTError
from jwt.types import Options

from ._environments import classify_issuer, normalise_issuer
from .claims import Claims
from .errors import EnvironmentMismatch, TokenError
from .jwks import AsyncJWKSCache, JWKSCache

ALGORITHM = "ES256"
DEFAULT_CLOCK_TOLERANCE = 60.0

TOKEN_TYPES = frozenset({"at+jwt", "application/at+jwt"})
"""What `typ` may say on an access token.

RFC 9068 §2.1 writes it `at+jwt`, and RFC 7515 §4.1.9 lets a `typ` omit the
`application/` prefix — so both spellings are the same media type and both are
accepted, case-insensitively, as media types are. Nothing else is: the ID token
carries the same `alg`, the same `kid` and the same signature over the same key
and differs from an access token *only* here, so without this check the one thing
standing between the two is which claims each happens to carry.
"""

# Claim checks happen here rather than in PyJWT so that each failure gets its
# own `TokenError` code and a message that names the value that failed.
_DECODE_OPTIONS: Options = {
    "verify_signature": True,
    "verify_exp": False,
    "verify_iat": False,
    "verify_nbf": False,
    "verify_aud": False,
    "verify_iss": False,
}

# Keyed by the *configured* issuer — an application's own setting, never
# anything a token supplied — so the two dictionaries are bounded by how many
# issuers the process is configured for, which is one for almost every process.
# Nothing evicts, and each entry owns an `httpx` client for the life of the
# process; a caller that needs a cache to end holds its own and closes it.
_CACHES: dict[str, JWKSCache] = {}
_CACHES_LOCK = threading.Lock()
_ASYNC_CACHES: dict[str, AsyncJWKSCache] = {}
_ASYNC_CACHES_LOCK = threading.Lock()


def shared_cache(issuer: str) -> JWKSCache:
    """The process-wide `JWKSCache` for one issuer.

    What `verify_access_token` uses when the caller passes no `jwks`: a cache
    per verification would fetch the document per verification, which is the
    one thing the cache exists to prevent.
    """

    key = normalise_issuer(issuer)
    with _CACHES_LOCK:
        cache = _CACHES.get(key)
        if cache is None:
            cache = _CACHES[key] = JWKSCache(key)
        return cache


def shared_async_cache(issuer: str) -> AsyncJWKSCache:
    """`shared_cache` for `verify_access_token_async`.

    One cache, and therefore one `asyncio.Lock` and one `httpx.AsyncClient`, per
    issuer per *process* — not per event loop. That is right for an ASGI
    application, which has one loop; a process that runs several loops in turn
    (repeated `asyncio.run`) should build its own `AsyncJWKSCache` per loop and
    pass it as `jwks`, because a client bound to a closed loop cannot fetch.
    """

    key = normalise_issuer(issuer)
    with _ASYNC_CACHES_LOCK:
        cache = _ASYNC_CACHES.get(key)
        if cache is None:
            cache = _ASYNC_CACHES[key] = AsyncJWKSCache(key)
        return cache


def verify_access_token(
    token: str,
    *,
    issuer: str,
    audience: str,
    jwks: JWKSCache | None = None,
    clock_tolerance: float = DEFAULT_CLOCK_TOLERANCE,
) -> Claims:
    """Verify a Kleora access token and return its `Claims`.

    `audience` is the `client_id` the token was issued to or the environment's
    `api_audience`; `aud` must contain it. Raises `TokenError` for anything
    about the token, and `EnvironmentMismatch` when a token minted by a sandbox
    environment arrives at a production issuer or the reverse.
    """

    issuer = normalise_issuer(issuer)
    cache = jwks if jwks is not None else shared_cache(issuer)
    key = cache.get_key(_kid(token))
    return _verified(token, key, issuer=issuer, audience=audience, clock_tolerance=clock_tolerance)


async def verify_access_token_async(
    token: str,
    *,
    issuer: str,
    audience: str,
    jwks: AsyncJWKSCache | None = None,
    clock_tolerance: float = DEFAULT_CLOCK_TOLERANCE,
) -> Claims:
    """`verify_access_token` over `AsyncJWKSCache`.

    The verification itself is CPU work on one signature; only the JWKS fetch
    is I/O, which is what this exists to keep off an event loop's thread.
    """

    issuer = normalise_issuer(issuer)
    cache = jwks if jwks is not None else shared_async_cache(issuer)
    key = await cache.get_key(_kid(token))
    return _verified(token, key, issuer=issuer, audience=audience, clock_tolerance=clock_tolerance)


def _kid(token: str) -> str:
    """Step 1: the header must say `ES256`, say `at+jwt`, and name a key.

    All three are read before the JWKS is consulted, so a token this SDK will
    not verify cannot provoke a request to the issuer. Nothing here is trusted
    beyond deciding *which* key to verify with and *whether* to bother — every
    claim is read after the signature does.
    """

    try:
        header = jwt.get_unverified_header(token)
    except PyJWTError as error:
        raise TokenError("malformed", f"unreadable token header: {error}") from error

    algorithm = header.get("alg")
    if algorithm != ALGORITHM:
        raise TokenError(
            "malformed",
            f"unsupported alg {algorithm!r}: Kleora signs access tokens with {ALGORITHM}",
        )

    token_type = header.get("typ")
    if token_type is None:
        raise TokenError(
            "invalid_type",
            "the token header names no typ; an access token is RFC 9068 'at+jwt'",
        )
    if not isinstance(token_type, str) or token_type.lower() not in TOKEN_TYPES:
        raise TokenError(
            "invalid_type",
            f"typ is {token_type!r}, not 'at+jwt': this is not an access token "
            "(an ID token carries typ 'JWT' and the same signature)",
        )

    kid = header.get("kid")
    if not isinstance(kid, str) or not kid:
        raise TokenError("malformed", "the token header names no kid")
    return kid


def _verified(
    token: str,
    key: PyJWK,
    *,
    issuer: str,
    audience: str,
    clock_tolerance: float,
) -> Claims:
    """Steps 3 to 7, on a token whose key is already resolved."""

    try:
        payload: dict[str, Any] = jwt.decode(
            token, key=key, algorithms=[ALGORITHM], options=_DECODE_OPTIONS
        )
    except InvalidSignatureError as error:
        raise TokenError("invalid_signature", f"signature does not verify: {error}") from error
    except PyJWTError as error:
        raise TokenError("malformed", f"undecodable token: {error}") from error

    if _text(payload, "iss") != issuer:
        raise TokenError(
            "issuer_mismatch",
            f"iss is {payload.get('iss')!r}, expected {issuer!r}",
        )

    aud = _audience(payload)
    if audience not in aud:
        raise TokenError(
            "audience_mismatch",
            f"aud is {list(aud)!r}, expected it to contain {audience!r}",
        )

    now = time.time()
    exp = _number(payload, "exp")
    if now > exp + clock_tolerance:
        raise TokenError(
            "expired",
            f"expired at {exp} and the clock tolerance is {clock_tolerance:g}s",
        )
    iat = _number(payload, "iat")
    if iat > now + clock_tolerance:
        # `malformed`, not `expired`: `expired` is the code a resource server
        # maps to "refresh and retry", and a clock-skewed issuer would answer
        # that retry with another token whose `iat` is just as far ahead. The
        # accurate statement is that this token's timestamps are unusable.
        raise TokenError(
            "malformed",
            f"iat is {iat}, more than the {clock_tolerance:g}s clock tolerance in the future",
        )

    env = _text(payload, "env")
    expected = classify_issuer(issuer)
    if env != expected:
        raise EnvironmentMismatch(f"the token says env {env!r} but {issuer} is a {expected} issuer")

    return Claims(
        iss=issuer,
        sub=_text(payload, "sub"),
        aud=aud,
        exp=exp,
        iat=iat,
        jti=_text(payload, "jti"),
        client_id=_text(payload, "client_id"),
        scope=_text(payload, "scope"),
        env=env,
        amr=_texts(payload, "amr"),
        roles=_texts(payload, "roles"),
        permissions=_texts(payload, "permissions"),
        permissions_truncated=payload.get("permissions_truncated") is True,
        tenant=_optional_text(payload, "tenant"),
        tenant_slug=_optional_text(payload, "tenant_slug"),
        email=_optional_text(payload, "email"),
        email_verified=_optional_bool(payload, "email_verified"),
    )


def _malformed(name: str, value: object, expected: str) -> TokenError:
    return TokenError("malformed", f"claim {name!r} is {value!r}, expected {expected}")


def _text(payload: dict[str, Any], name: str) -> str:
    value = payload.get(name)
    if not isinstance(value, str):
        raise _malformed(name, value, "a string")
    return value


def _optional_text(payload: dict[str, Any], name: str) -> str | None:
    value = payload.get(name)
    if value is None:
        return None
    if not isinstance(value, str):
        raise _malformed(name, value, "a string or nothing")
    return value


def _optional_bool(payload: dict[str, Any], name: str) -> bool | None:
    value = payload.get(name)
    if value is None:
        return None
    if not isinstance(value, bool):
        raise _malformed(name, value, "a boolean or nothing")
    return value


def _number(payload: dict[str, Any], name: str) -> int:
    value = payload.get(name)
    if isinstance(value, bool) or not isinstance(value, int | float):
        raise _malformed(name, value, "seconds since the epoch")
    return int(value)


def _texts(payload: dict[str, Any], name: str) -> tuple[str, ...]:
    value = payload.get(name)
    if value is None:
        return ()
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise _malformed(name, value, "an array of strings")
    return tuple(str(item) for item in value)


def _audience(payload: dict[str, Any]) -> tuple[str, ...]:
    """`aud` is always an array from us; RFC 7519 allows the string form too."""

    value = payload.get("aud")
    if isinstance(value, str):
        return (value,)
    return _texts(payload, "aud")
