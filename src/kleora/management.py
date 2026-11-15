"""The management API clients.

Both clients **wrap** `kleora._generated`, they do not restate it: the
generated tree is the whole typed surface of the API and is regenerated from
the deployed management API document whenever a schema moves, so a second
hand-written copy of any operation would be a copy that goes stale. What is
added here is the three things a generator cannot know about:

* the credential — accepted through the constructor only, never read from the
  environment behind the caller's back, never logged, and shown in `repr` as
  its literal prefix and nothing more;
* the environment guard — a `kl_test_` key must not reach a production issuer
  or a `kl_live_` key a sandbox one. With `issuer` given it is decided at construction, before a
  single request; without it, on the first call, from `GET /me`;
* the error shape — every non-2xx response becomes `ApiError` carrying the
  RFC 9457 problem, raised from an `httpx` response hook so that no operation
  can forget it.

Calls go through the generated operations, which is what keeps them typed:

```python
from kleora import ManagementClient
from kleora._generated.api.apps import list_apps

with ManagementClient(api_key=key) as kleora:
    apps = list_apps.sync(client=kleora.api())
```
"""

from __future__ import annotations

import asyncio
import threading
from collections.abc import Callable, Iterator, Mapping, Sequence
from contextlib import AbstractContextManager, contextmanager, nullcontext
from contextvars import ContextVar
from types import TracebackType
from typing import Any

import httpx

from ._environments import (
    EnvironmentKind,
    classify_api_key,
    classify_issuer,
    normalise_issuer,
    redact_api_key,
)
from ._generated.api.me import me as me_operation
from ._generated.client import AuthenticatedClient
from ._generated.models.me_environment import MeEnvironment
from ._generated.models.me_out import MeOut
from ._meta import USER_AGENT
from .errors import ApiError, EnvironmentMismatch, KleoraError, ProblemError

DEFAULT_BASE_URL = "https://api.kleora.io"
DEFAULT_TIMEOUT = 10.0

API_PREFIX = "/api/v1"

_REQUEST_ID: ContextVar[str | None] = ContextVar("kleora_request_id", default=None)
"""The `X-Request-Id` for the call being made in this context, if any.

A context variable and a request hook, rather than a header on a client: the
generated `with_headers` mutates the live `httpx.Client`\'s default headers and
returns a copy whose client field resets to `None`, so labelling one call would
both stamp the id on every later call through the base client and build a second
connection pool nothing closes. A value scoped to the call cannot outlive it,
and one client keeps one pool.
"""


def _stamp_request_id(request: httpx.Request) -> None:
    """`httpx` request hook: label this request if the caller labelled the call.

    Nothing is invented when the caller supplied nothing — the *server*
    generates an `X-Request-Id` when the request carries none, and an id
    minted here would be one no client could correlate anything with.
    """

    value = _REQUEST_ID.get()
    if value is not None:
        request.headers["X-Request-Id"] = value


async def _astamp_request_id(request: httpx.Request) -> None:
    """`_stamp_request_id` for `httpx.AsyncClient`, which awaits its hooks."""

    _stamp_request_id(request)


def _normalise_base_url(base_url: str) -> str:
    """The API origin, however the caller spelled it.

    The generated operations carry `/api/v1` in every path, and the settings a
    customer copies from the docs (`django-kleora`'s `API_BASE`) carry it
    too. Accepting both spellings here is one line; the alternative is a support
    thread about `/api/v1/api/v1/me`.
    """

    trimmed = base_url.rstrip("/")
    if trimmed.endswith(API_PREFIX):
        trimmed = trimmed[: -len(API_PREFIX)]
    return trimmed


def _problem(response: httpx.Response) -> ApiError:
    """The `ApiError` for a response that has already been read."""

    body: object
    try:
        body = response.json()
    except ValueError:
        body = None

    if not isinstance(body, dict):
        detail = response.text[:200].strip() or None
        return ApiError(
            type="about:blank",
            status=response.status_code,
            title=response.reason_phrase or "Error",
            detail=detail,
            request_id=response.headers.get("x-request-id"),
        )

    return ApiError(
        type=_string(body, "type") or "about:blank",
        status=_integer(body, "status") or response.status_code,
        title=_string(body, "title") or response.reason_phrase or "Error",
        detail=_string(body, "detail"),
        errors=_problem_errors(body.get("errors")),
        instance=_string(body, "instance"),
        request_id=_string(body, "request_id") or response.headers.get("x-request-id"),
    )


def _string(body: Mapping[str, Any], name: str) -> str | None:
    value = body.get(name)
    return value if isinstance(value, str) else None


def _integer(body: Mapping[str, Any], name: str) -> int | None:
    value = body.get(name)
    return value if isinstance(value, int) and not isinstance(value, bool) else None


def _problem_errors(value: object) -> Sequence[ProblemError]:
    if not isinstance(value, list):
        return ()
    entries: list[ProblemError] = []
    for item in value:
        if not isinstance(item, dict):
            continue
        field = item.get("field")
        entries.append(
            ProblemError(
                field=field if isinstance(field, str) else None,
                message=_string(item, "message") or "",
                code=_string(item, "code") or "",
            )
        )
    return entries


@contextmanager
def _labelled(value: str) -> Iterator[None]:
    token = _REQUEST_ID.set(value)
    try:
        yield
    finally:
        _REQUEST_ID.reset(token)


def _httpx_arguments(
    httpx_args: Mapping[str, Any] | None,
    on_request: Callable[[httpx.Request], Any],
    on_response: Callable[[httpx.Response], Any],
) -> dict[str, Any]:
    """The caller's `httpx` configuration with the problem hook appended.

    `httpx_args` reaches `httpx.Client` unchanged — a proxy, a transport, a
    client certificate — which is also how a test hands the client a
    `MockTransport` without a running server. The problem hook goes *last* so a
    caller's own response hook still sees an error response before it becomes an
    `ApiError`, and it cannot be replaced: an operation that returned a problem
    body as if it were a result is the failure mode this package exists to
    prevent.
    """

    arguments = dict(httpx_args or {})
    hooks = dict(arguments.get("event_hooks") or {})
    hooks["request"] = [*(hooks.get("request") or []), on_request]
    hooks["response"] = [*(hooks.get("response") or []), on_response]
    arguments["event_hooks"] = hooks
    return arguments


class _ManagementBase:
    """Credential handling, the base URL and the environment comparison.

    The sync and async clients differ only in how they reach `GET /me`.
    """

    def __init__(
        self,
        *,
        api_key: str,
        base_url: str = DEFAULT_BASE_URL,
        issuer: str | None = None,
    ) -> None:
        self._api_key = api_key
        self._key_kind: EnvironmentKind = classify_api_key(api_key)
        self._base_url = _normalise_base_url(base_url)
        self._issuer = normalise_issuer(issuer) if issuer is not None else None
        self._environment: MeEnvironment | None = None
        self._guarded = False
        self._guard_error: EnvironmentMismatch | None = None

        if self._issuer is not None:
            issuer_kind = classify_issuer(self._issuer)
            if issuer_kind != self._key_kind:
                raise EnvironmentMismatch(
                    f"the API key is a {self._key_kind} key and {self._issuer} "
                    f"is a {issuer_kind} issuer"
                )

    def request_id(self, value: str) -> AbstractContextManager[None]:
        """Label every request made inside the block with `X-Request-Id: value`.

        ```python
        with kleora.request_id("req_01J…"):
            list_apps.sync(client=kleora.api())
        ```

        The label is scoped to the block and to the context that entered it — a
        thread or an `asyncio` task — so it can neither outlive the call it was
        meant for nor reach a call made concurrently beside it.
        """

        return _labelled(value)

    @property
    def base_url(self) -> str:
        """The API origin requests are made against."""

        return self._base_url

    @property
    def environment(self) -> MeEnvironment | None:
        """What `GET /me` said the key's environment is, once the guard has run."""

        return self._environment

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}(api_key={redact_api_key(self._api_key)!r}, "
            f"base_url={self._base_url!r})"
        )

    def _headers(self) -> dict[str, str]:
        return {"User-Agent": USER_AGENT}

    def _apply(self, principal: MeOut) -> None:
        """Record the environment `GET /me` reported, or refuse the pairing.

        A principal with no environment is a console user or a tenant member,
        and the constructor has already established through `classify_api_key`
        that this credential is neither. An API-key principal always carries an
        environment in `GET /me`, so a response without one
        is a surface this client does not understand — and passing the guard
        because there was nothing to compare would be the wrong reading of it.
        """

        environment = principal.environment
        if not isinstance(environment, MeEnvironment):
            raise KleoraError(
                "GET /me reported no environment for an API key; "
                "this client cannot check the credential against it"
            )

        if environment.kind != self._key_kind:
            raise EnvironmentMismatch(
                f"the API key is a {self._key_kind} key but its environment "
                f"{environment.issuer} is {environment.kind}"
            )
        if self._issuer is not None and normalise_issuer(environment.issuer) != self._issuer:
            raise EnvironmentMismatch(
                f"the configured issuer is {self._issuer} but the key belongs to "
                f"{environment.issuer}"
            )

        self._environment = environment
        self._guarded = True

    def _replay_guard(self) -> bool:
        """`True` when the guard has already decided; re-raises a refusal.

        A mismatch is a property of the configuration, so once it is known every
        later call refuses locally rather than sending the key again.
        """

        if self._guard_error is not None:
            raise self._guard_error
        return self._guarded

    def _record(self, principal: MeOut | None) -> None:
        if principal is None:
            raise KleoraError("GET /me did not answer with a principal")
        try:
            self._apply(principal)
        except EnvironmentMismatch as error:
            self._guard_error = error
            raise


class ManagementClient(_ManagementBase):
    """The management API, synchronously.

    ```python
    kleora = ManagementClient(api_key=key, issuer="https://acme-sandbox.kleora.eu")
    principal = kleora.me()
    ```
    """

    def __init__(
        self,
        *,
        api_key: str,
        base_url: str = DEFAULT_BASE_URL,
        issuer: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        httpx_args: Mapping[str, Any] | None = None,
    ) -> None:
        super().__init__(api_key=api_key, base_url=base_url, issuer=issuer)
        self._client = AuthenticatedClient(
            base_url=self._base_url,
            token=api_key,
            headers=self._headers(),
            timeout=httpx.Timeout(timeout),
            httpx_args=_httpx_arguments(httpx_args, _stamp_request_id, _raise_on_problem),
        )
        self._guard_lock = threading.Lock()

    def api(self) -> AuthenticatedClient:
        """The generated client, guarded — pass it to any generated operation.

        Always the same object, and therefore always the same `httpx.Client` and
        the same connection pool. The first call runs the environment guard,
        which costs one `GET /me`; every later one is decided from what that
        answered. To label a call, wrap it in `request_id`.
        """

        self._ensure_environment()
        return self._client

    def me(self, *, request_id: str | None = None) -> MeOut:
        """`GET /me`: who the credential belongs to and what it may do."""

        self._ensure_environment()
        with _labelled(request_id) if request_id is not None else nullcontext():
            return _principal(me_operation.sync(client=self._client))

    def _ensure_environment(self) -> None:
        if self._replay_guard():
            return
        with self._guard_lock:
            if self._replay_guard():
                return
            self._record(_principal_or_none(me_operation.sync(client=self._client)))

    def close(self) -> None:
        """Close the connection pool. Idempotent; the client is not reusable after."""

        self._client.get_httpx_client().close()

    def __enter__(self) -> ManagementClient:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.close()


class AsyncManagementClient(_ManagementBase):
    """`ManagementClient` over `httpx.AsyncClient`."""

    def __init__(
        self,
        *,
        api_key: str,
        base_url: str = DEFAULT_BASE_URL,
        issuer: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        httpx_args: Mapping[str, Any] | None = None,
    ) -> None:
        super().__init__(api_key=api_key, base_url=base_url, issuer=issuer)
        self._client = AuthenticatedClient(
            base_url=self._base_url,
            token=api_key,
            headers=self._headers(),
            timeout=httpx.Timeout(timeout),
            httpx_args=_httpx_arguments(httpx_args, _astamp_request_id, _araise_on_problem),
        )
        self._guard_lock = asyncio.Lock()

    async def api(self) -> AuthenticatedClient:
        """As `ManagementClient.api`; awaits the guard's `GET /me` on first use."""

        await self._ensure_environment()
        return self._client

    async def me(self, *, request_id: str | None = None) -> MeOut:
        """`GET /me`: who the credential belongs to and what it may do."""

        await self._ensure_environment()
        with _labelled(request_id) if request_id is not None else nullcontext():
            return _principal(await me_operation.asyncio(client=self._client))

    async def _ensure_environment(self) -> None:
        if self._replay_guard():
            return
        async with self._guard_lock:
            if self._replay_guard():
                return
            self._record(_principal_or_none(await me_operation.asyncio(client=self._client)))

    async def aclose(self) -> None:
        """Close the connection pool. Idempotent; the client is not reusable after."""

        await self._client.get_async_httpx_client().aclose()

    async def __aenter__(self) -> AsyncManagementClient:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        await self.aclose()


def _raise_on_problem(response: httpx.Response) -> None:
    """`httpx` response hook: every 4xx and 5xx leaves as `ApiError`."""

    if response.status_code < 400:
        return
    response.read()
    raise _problem(response)


async def _araise_on_problem(response: httpx.Response) -> None:
    if response.status_code < 400:
        return
    await response.aread()
    raise _problem(response)


def _principal_or_none(parsed: object) -> MeOut | None:
    """The `MeOut` of a `GET /me`, or `None` when the response was not one.

    The generated operation's return type includes `Problem`, which the response
    hook has already turned into a raised `ApiError` — so reaching it here means
    a 2xx that is not a principal.
    """

    return parsed if isinstance(parsed, MeOut) else None


def _principal(parsed: object) -> MeOut:
    principal = _principal_or_none(parsed)
    if principal is None:
        raise KleoraError("GET /me did not answer with a principal")
    return principal
