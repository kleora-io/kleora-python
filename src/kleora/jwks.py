"""The JWKS caches.

One cache per issuer, keyed by `{issuer}/.well-known/jwks.json`. Three rules,
shared with `@kleora-io/node` so that a Node service and a Python service
in front of the same issuer behave identically:

* the document is good for its `Cache-Control` max-age (300 s by default);
* an unknown `kid` triggers **one** refetch, and never more often than every
  `min_refresh_interval` seconds — a token naming a key that does not exist
  must not be a way to make an application hammer the issuer. The floor counts
  from the last fetch of any kind; the TTL's own refresh is not throttled by it,
  or a document whose `max-age` is shorter than the floor would never be
  refreshed. A *failed* fetch is: retrying it once per verified token during the
  stale window would turn an issuer's bad minute into a stampede;
* a failed fetch keeps serving the keys already held until twice the TTL has
  passed, then verification fails closed.

**Failing closed is `issuer_unavailable`, not `unknown_kid`.** While a document
is still usable its contents are an answer, so a `kid` it does not list is a bad
token and belongs to whoever sent it. Past twice the TTL — or before the first
successful fetch — there is no document to answer from, and what went wrong is
the issuer being unreachable: our infrastructure, retryable, a 503 rather than a
401. The cached set is the whole discriminator, exactly as in
`@kleora-io/node`; a middleware that could not tell the two apart would send
every caller back to re-authenticate against an issuer that is already down.

Rotation is why the second rule can be this strict: a new key is published as
`next` before it signs anything, so
a cache that refreshed on its TTL already holds the `kid` a rotated key signs
with. The refetch is the recovery path, not the normal one.

`JWKSCache` is thread-safe: one lock covers the decision *and* the fetch, so N
threads that miss together make one request between them rather than N.
`AsyncJWKSCache` is the same algorithm under an `asyncio.Lock`.
"""

from __future__ import annotations

import asyncio
import re
import threading
import time
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from types import TracebackType
from typing import Any

import httpx
from jwt import PyJWK
from jwt.exceptions import PyJWTError

from ._environments import normalise_issuer
from ._meta import USER_AGENT
from .errors import TokenError

DEFAULT_TTL = 300.0
"""Fallback TTL, in seconds, when the document carries no `max-age`."""

DEFAULT_MIN_REFRESH_INTERVAL = 60.0
"""Floor between two fetches to one issuer, in seconds."""

DEFAULT_TIMEOUT = 5.0

MIN_TTL = 60.0
MAX_TTL = 86400.0
"""The band a document's own `max-age` is clamped into.

`Cache-Control: max-age=0` is a real answer — an intermediary that does not want
the document cached — and taking it literally would fetch the JWKS once per
verified token. Refusing it and falling back to the default is worse still: an
issuer that says "do not cache" would get five minutes and a ten-minute stale
window. A floor of a minute honours the intent at a bounded cost, and the day's
ceiling stops a mistyped `max-age` pinning a rotated-away key for years.
"""

JWKS_PATH = "/.well-known/jwks.json"

_HEADERS = {"User-Agent": USER_AGENT, "Accept": "application/json"}
_MAX_AGE = re.compile(r"(?:^|,)\s*max-age\s*=\s*\"?(\d+)\"?", re.IGNORECASE)


@dataclass(frozen=True, slots=True)
class _Document:
    """One fetched JWK Set and what its freshness is measured against."""

    keys: Mapping[str, PyJWK]
    fetched_at: float
    ttl: float


def _max_age(headers: Mapping[str, str]) -> float | None:
    """The `max-age` of a `Cache-Control` header, clamped, if it has one."""

    match = _MAX_AGE.search(headers.get("cache-control", ""))
    if match is None:
        return None
    return min(max(float(match.group(1)), MIN_TTL), MAX_TTL)


def _is_signing_key(member: Mapping[str, object]) -> bool:
    """Whether a JWK is one this verifier could ever use.

    An issuer's JWKS document publishes exactly one shape —
    `EC` / `P-256` / `use: sig` / `alg: ES256` — and the verifier accepts
    exactly one algorithm, so anything else in the set is noise at best. At
    worst it is an `oct` or RSA entry under the `kid` a token names, which the
    pinned PyJWT would refuse (it compares the token's `alg` to the key's own)
    but only because of a guard that lives in a dependency with no upper bound.
    The filter puts that guard here, where this package can keep it.
    """

    return (
        member.get("kty") == "EC"
        and member.get("crv") == "P-256"
        and member.get("alg") in (None, "ES256")
        and member.get("use") in (None, "sig")
    )


def _read_keys(payload: object) -> dict[str, PyJWK] | None:
    """Every usable key of an RFC 7517 JWK Set, by `kid`.

    `None` when the payload is not a JWK Set at all — that is a failed fetch,
    not an empty one, and must not replace keys that still verify tokens. A
    single unparseable member is skipped instead: the rest of the set is still
    the truth about the issuer, and the missing `kid` surfaces as
    `unknown_kid` rather than as an exception from a background refresh.

    An **empty** result is a failed fetch too, and `_accept` treats it as one: a
    document with no member this verifier could ever use is an issuer that has
    published nothing, which is the outage rather than a set of zero keys to
    answer from. `@kleora-io/node` draws the line in the same place
    ("published no usable key").
    """

    if not isinstance(payload, dict):
        return None
    members = payload.get("keys")
    if not isinstance(members, list):
        return None

    keys: dict[str, PyJWK] = {}
    for member in members:
        if not isinstance(member, dict):
            continue
        kid = member.get("kid")
        if not isinstance(kid, str) or not _is_signing_key(member):
            continue
        try:
            keys[kid] = PyJWK.from_dict(member)
        except (PyJWTError, ValueError, TypeError, KeyError):
            continue
    return keys


class _JWKSBase:
    """State and decisions shared by the sync and async caches.

    Everything here is pure or a state update; the two subclasses add the fetch,
    which is the only part that differs between `httpx.Client` and
    `httpx.AsyncClient`.
    """

    def __init__(
        self,
        issuer: str,
        ttl: float = DEFAULT_TTL,
        min_refresh_interval: float = DEFAULT_MIN_REFRESH_INTERVAL,
        *,
        clock: Callable[[], float] = time.monotonic,
    ) -> None:
        self.issuer = normalise_issuer(issuer)
        self.url = f"{self.issuer}{JWKS_PATH}"
        self.ttl = ttl
        self.min_refresh_interval = min_refresh_interval
        self._clock = clock
        self._document: _Document | None = None
        self._last_attempt: float | None = None
        self._last_failure_at: float | None = None
        self._last_failure: Exception | None = None

    def _fresh(self, document: _Document, now: float) -> bool:
        return now - document.fetched_at < document.ttl

    def _usable(self, document: _Document, now: float) -> bool:
        """Within twice the TTL: the window a stale set may still be served in."""

        return now - document.fetched_at < document.ttl * 2

    def _may_fetch(self, now: float) -> bool:
        """The unknown-`kid` floor: at most one fetch per `min_refresh_interval`."""

        return self._last_attempt is None or now - self._last_attempt >= self.min_refresh_interval

    def _may_refresh(self, now: float) -> bool:
        """The TTL's own refresh, throttled only after a failure."""

        return (
            self._last_failure_at is None
            or now - self._last_failure_at >= self.min_refresh_interval
        )

    def _lookup(self, kid: str, now: float) -> PyJWK | None:
        document = self._document
        if document is None or not self._usable(document, now):
            return None
        return document.keys.get(kid)

    def _accept(self, payload: object, headers: Mapping[str, str], now: float) -> None:
        keys = _read_keys(payload)
        if keys is None:
            self._record_failure(now, ValueError(f"{self.url} did not answer with a JWK Set"))
            return
        if not keys:
            self._record_failure(now, ValueError(f"{self.url} published no usable key"))
            return
        self._last_attempt = now
        self._last_failure_at = None
        self._last_failure = None
        max_age = _max_age(headers)
        self._document = _Document(
            keys=keys, fetched_at=now, ttl=self.ttl if max_age is None else max_age
        )

    def _record_failure(self, now: float, error: Exception) -> None:
        self._last_attempt = now
        self._last_failure_at = now
        self._last_failure = error

    def _readable(self, now: float) -> bool:
        """Whether a document this cache may still answer from is held at all.

        The discriminator between the two codes below, and the only one: not
        "did the last fetch fail" — a failure inside the stale window is
        survivable and the keys already held are still the issuer's own answer —
        but "is there anything left to answer with".
        """

        document = self._document
        return document is not None and self._usable(document, now)

    def _failure(self, kid: str, now: float) -> TokenError:
        """The right error when the lookup found nothing.

        `unknown_kid` while a usable document is held: it was read, and it does
        not list that `kid`, so the token is bad. `issuer_unavailable` otherwise
        — nothing has been fetched successfully within twice the TTL, which is
        the issuer being unreachable and not a verdict on anybody's token. A
        middleware answers the first 401 and the second 503.
        """

        if self._readable(now):
            return self._unknown(kid)
        reason = f": {self._last_failure}" if self._last_failure else ""
        return TokenError("issuer_unavailable", f"{self.url} could not be read{reason}")

    def _unknown(self, kid: str) -> TokenError:
        reason = f"; the last fetch failed: {self._last_failure}" if self._last_failure else ""
        return TokenError(
            "unknown_kid",
            f"no key {kid!r} in {self.url} "
            f"(refetched at most once every {self.min_refresh_interval:g}s){reason}",
        )


class JWKSCache(_JWKSBase):
    """The signing keys of one issuer, cached and refreshed on demand.

    ```python
    cache = JWKSCache("https://acme.kleora.eu")
    key = cache.get_key(kid)
    ```

    Pass `client` to share an `httpx.Client` (or to hand the cache a transport
    in a test); the cache closes only a client it made itself. `clock` exists
    for the same reason and defaults to `time.monotonic`, which no wall-clock
    correction can move backwards.
    """

    def __init__(
        self,
        issuer: str,
        ttl: float = DEFAULT_TTL,
        min_refresh_interval: float = DEFAULT_MIN_REFRESH_INTERVAL,
        *,
        client: httpx.Client | None = None,
        clock: Callable[[], float] = time.monotonic,
        timeout: float = DEFAULT_TIMEOUT,
    ) -> None:
        super().__init__(issuer, ttl, min_refresh_interval, clock=clock)
        self._timeout = timeout
        self._client = client
        self._owns_client = client is None
        self._lock = threading.Lock()

    def get_key(self, kid: str) -> PyJWK:
        """The key named by `kid`, fetching or refetching only when the rules allow.

        Raises `TokenError("unknown_kid")` when a document this cache may still
        answer from does not list the key, including when the refetch floor
        forbids looking again, and `TokenError("issuer_unavailable")` when
        nothing has been fetched successfully within twice the TTL.
        """

        with self._lock:
            now = self._clock()
            document = self._document
            if (document is None or not self._fresh(document, now)) and self._may_refresh(now):
                self._fetch(now)

            found = self._lookup(kid, now)
            if found is not None:
                return found

            if self._may_fetch(now):
                self._fetch(now)
                found = self._lookup(kid, now)
                if found is not None:
                    return found

            raise self._failure(kid, now)

    def _http(self) -> httpx.Client:
        if self._client is None:
            self._client = httpx.Client(timeout=self._timeout)
        return self._client

    def _fetch(self, now: float) -> None:
        try:
            response = self._http().get(self.url, headers=_HEADERS)
            response.raise_for_status()
            payload: Any = response.json()
        except (httpx.HTTPError, ValueError) as error:
            self._record_failure(now, error)
            return
        self._accept(payload, response.headers, now)

    def close(self) -> None:
        if self._owns_client and self._client is not None:
            self._client.close()
            self._client = None

    def __enter__(self) -> JWKSCache:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.close()


class AsyncJWKSCache(_JWKSBase):
    """`JWKSCache` over `httpx.AsyncClient`, with the same rules and an `asyncio.Lock`."""

    def __init__(
        self,
        issuer: str,
        ttl: float = DEFAULT_TTL,
        min_refresh_interval: float = DEFAULT_MIN_REFRESH_INTERVAL,
        *,
        client: httpx.AsyncClient | None = None,
        clock: Callable[[], float] = time.monotonic,
        timeout: float = DEFAULT_TIMEOUT,
    ) -> None:
        super().__init__(issuer, ttl, min_refresh_interval, clock=clock)
        self._timeout = timeout
        self._client = client
        self._owns_client = client is None
        self._lock = asyncio.Lock()

    async def get_key(self, kid: str) -> PyJWK:
        """As `JWKSCache.get_key`; concurrent misses coalesce into one request."""

        async with self._lock:
            now = self._clock()
            document = self._document
            if (document is None or not self._fresh(document, now)) and self._may_refresh(now):
                await self._fetch(now)

            found = self._lookup(kid, now)
            if found is not None:
                return found

            if self._may_fetch(now):
                await self._fetch(now)
                found = self._lookup(kid, now)
                if found is not None:
                    return found

            raise self._failure(kid, now)

    def _http(self) -> httpx.AsyncClient:
        if self._client is None:
            self._client = httpx.AsyncClient(timeout=self._timeout)
        return self._client

    async def _fetch(self, now: float) -> None:
        try:
            response = await self._http().get(self.url, headers=_HEADERS)
            response.raise_for_status()
            payload: Any = response.json()
        except (httpx.HTTPError, ValueError) as error:
            self._record_failure(now, error)
            return
        self._accept(payload, response.headers, now)

    async def aclose(self) -> None:
        if self._owns_client and self._client is not None:
            await self._client.aclose()
            self._client = None

    async def __aenter__(self) -> AsyncJWKSCache:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        await self.aclose()
