"""The management clients: the guard, the credential and the error shape.

Every case runs against an `httpx.MockTransport`, so the suite proves what the
client sends and when it sends nothing at all.
"""

from __future__ import annotations

import asyncio
from typing import Any

import httpx
import pytest
from conftest import API_BASE, ISSUER, LIVE_KEY, SANDBOX_ISSUER, TEST_KEY

from kleora import (
    USER_AGENT,
    ApiError,
    AsyncManagementClient,
    EnvironmentMismatch,
    KleoraError,
    ManagementClient,
)
from kleora._generated.api.me import me as me_operation
from kleora._generated.models.me_out import MeOut

ENVIRONMENT_ID = "0f8f0a4e-2a3b-4c5d-8e9f-0a1b2c3d4e5f"


def me_document(*, kind: str = "sandbox", issuer: str = SANDBOX_ISSUER) -> dict[str, Any]:
    """`GET /me` as an API key sees it."""

    return {
        "principal": {"kind": "api_key", "subject_id": "1f2e3d4c-5b6a-4978-8899-aabbccddeeff"},
        "account": None,
        "tenant": None,
        "memberships": [],
        "permissions": ["users:read", "clients:read"],
        "environment": {
            "id": ENVIRONMENT_ID,
            "kind": kind,
            "issuer": issuer,
            "app": {"id": "9a8b7c6d-5e4f-4a3b-8291-0f1e2d3c4b5a", "slug": "acme"},
        },
    }


class Recorder:
    """A transport that records every request and answers from a queue.

    The last response stands for every request after it, so a test that cares
    about one call does not have to enumerate the guard's.
    """

    def __init__(self, *responses: httpx.Response) -> None:
        self.responses = list(responses)
        self.requests: list[httpx.Request] = []

    def handle(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        if not self.responses:
            return httpx.Response(200, json=me_document())
        return self.responses.pop(0) if len(self.responses) > 1 else self.responses[0]

    def transport(self) -> httpx.MockTransport:
        return httpx.MockTransport(self.handle)

    @property
    def paths(self) -> list[str]:
        return [request.url.path for request in self.requests]

    @property
    def ids(self) -> list[str | None]:
        """The `X-Request-Id` of every request, in order, `None` where absent."""

        return [request.headers.get("x-request-id") for request in self.requests]


def client(recorder: Recorder, **kwargs: Any) -> ManagementClient:
    kwargs.setdefault("api_key", TEST_KEY)
    kwargs.setdefault("base_url", API_BASE)
    return ManagementClient(httpx_args={"transport": recorder.transport()}, **kwargs)


def async_client(recorder: Recorder, **kwargs: Any) -> AsyncManagementClient:
    kwargs.setdefault("api_key", TEST_KEY)
    kwargs.setdefault("base_url", API_BASE)
    return AsyncManagementClient(httpx_args={"transport": recorder.transport()}, **kwargs)


# The environment guard --------------------------------------------------


def test_a_test_key_with_a_production_issuer_refuses_at_construction() -> None:
    recorder = Recorder()

    with pytest.raises(EnvironmentMismatch) as raised:
        client(recorder, issuer=ISSUER)

    assert "sandbox" in str(raised.value)
    assert recorder.requests == []


def test_a_live_key_with_a_sandbox_issuer_refuses_at_construction() -> None:
    recorder = Recorder()

    with pytest.raises(EnvironmentMismatch):
        client(recorder, api_key=LIVE_KEY, issuer=SANDBOX_ISSUER)

    assert recorder.requests == []


def test_without_an_issuer_the_guard_fires_on_the_first_call() -> None:
    recorder = Recorder(httpx.Response(200, json=me_document(kind="production", issuer=ISSUER)))
    kleora = client(recorder)

    assert recorder.requests == []

    with pytest.raises(EnvironmentMismatch) as raised:
        kleora.api()

    assert recorder.paths == ["/api/v1/me"]
    assert "production" in str(raised.value)


def test_a_refused_pairing_is_not_sent_a_second_time() -> None:
    recorder = Recorder(httpx.Response(200, json=me_document(kind="production", issuer=ISSUER)))
    kleora = client(recorder)

    for _ in range(3):
        with pytest.raises(EnvironmentMismatch):
            kleora.api()

    assert len(recorder.requests) == 1


def test_a_matching_pairing_records_the_environment_and_guards_locally() -> None:
    recorder = Recorder()
    kleora = client(recorder, issuer=SANDBOX_ISSUER)

    kleora.api()
    kleora.api()
    kleora.api()

    assert len(recorder.requests) == 1
    environment = kleora.environment
    assert environment is not None
    assert environment.kind == "sandbox"
    assert environment.issuer == SANDBOX_ISSUER
    assert str(environment.id) == ENVIRONMENT_ID


def test_a_configured_issuer_that_is_not_the_key_s_own_is_refused() -> None:
    """Same kind, different environment: the guard compares the issuer too."""

    recorder = Recorder(
        httpx.Response(200, json=me_document(issuer="https://other-sandbox.kleora.eu"))
    )
    kleora = client(recorder, issuer=SANDBOX_ISSUER)

    with pytest.raises(EnvironmentMismatch) as raised:
        kleora.api()

    assert "other-sandbox.kleora.eu" in str(raised.value)


def test_a_principal_without_an_environment_is_not_a_satisfied_guard() -> None:
    """An API key always has one; a `GET /me` without one is a surface we do not know."""

    document = me_document()
    document["environment"] = None
    recorder = Recorder(httpx.Response(200, json=document))
    kleora = client(recorder, issuer=SANDBOX_ISSUER)

    with pytest.raises(KleoraError) as raised:
        kleora.api()

    assert not isinstance(raised.value, EnvironmentMismatch)
    assert "no environment" in str(raised.value)


def test_a_value_that_is_not_a_kleora_key_is_refused_before_anything_else() -> None:
    with pytest.raises(KleoraError) as raised:
        ManagementClient(api_key="sk_live_something_else")

    assert "kl_live_" in str(raised.value)


def test_the_api_key_is_never_read_from_the_environment(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """A credential arrives through the constructor or not at all."""

    monkeypatch.setenv("KLEORA_API_KEY", LIVE_KEY)

    with pytest.raises(TypeError):
        ManagementClient()  # type: ignore[call-arg]


# The credential ---------------------------------------------------------


def test_repr_shows_the_prefix_and_nothing_random() -> None:
    kleora = client(Recorder(), issuer=SANDBOX_ISSUER)

    rendered = repr(kleora)

    assert "kl_test_…" in rendered
    assert TEST_KEY not in rendered
    assert "K" * 8 not in rendered


def test_the_generated_client_hides_the_token_too() -> None:
    """The counted `field(repr=False)` patches, asserted from outside.

    `token` is not the whole of it: the generated client copies
    `Authorization: Bearer <key>` into its header dictionary the first time it
    builds an `httpx.Client`, so the repr is checked after a request has been
    made rather than before.
    """

    recorder = Recorder()
    kleora = client(recorder, issuer=SANDBOX_ISSUER)
    generated = kleora.api()

    assert recorder.requests
    assert TEST_KEY not in repr(generated)
    assert TEST_KEY not in repr(generated.get_httpx_client())


def test_the_key_is_sent_as_a_bearer_token() -> None:
    recorder = Recorder()
    kleora = client(recorder, issuer=SANDBOX_ISSUER)

    kleora.api()

    assert recorder.requests[0].headers["authorization"] == f"Bearer {TEST_KEY}"


# HTTP conventions -------------------------------------------------------


def test_every_request_names_the_package_in_its_user_agent() -> None:
    recorder = Recorder()
    kleora = client(recorder, issuer=SANDBOX_ISSUER)

    kleora.api()

    assert recorder.requests[0].headers["user-agent"] == USER_AGENT
    assert USER_AGENT.startswith("kleora-python/")


def test_a_caller_s_request_id_is_forwarded() -> None:
    recorder = Recorder()
    kleora = client(recorder, issuer=SANDBOX_ISSUER)

    kleora.me(request_id="req_01J000000000000000000000")

    assert recorder.requests[-1].headers["x-request-id"] == "req_01J000000000000000000000"


def test_a_request_id_labels_one_call_and_no_other() -> None:
    """The header is scoped to the call, not stamped on the client.

    A labelled call followed by an unlabelled one must not make the server echo
    a stale id, which would correlate two unrelated operations in the audit log
    of whoever reads it.
    """

    recorder = Recorder()
    kleora = client(recorder, issuer=SANDBOX_ISSUER)

    kleora.me(request_id="REQ-1")
    kleora.me()
    me_operation.sync(client=kleora.api())

    assert recorder.ids == [None, "REQ-1", None, None]


def test_the_request_id_block_labels_every_call_inside_it() -> None:
    recorder = Recorder()
    kleora = client(recorder, issuer=SANDBOX_ISSUER)
    kleora.api()

    with kleora.request_id("REQ-2"):
        me_operation.sync(client=kleora.api())
        me_operation.sync(client=kleora.api())
    me_operation.sync(client=kleora.api())

    assert recorder.ids == [None, "REQ-2", "REQ-2", None]


def test_one_client_and_one_pool_for_the_life_of_the_client() -> None:
    """A per-call header must not cost a second connection pool nothing closes."""

    recorder = Recorder()
    with client(recorder, issuer=SANDBOX_ISSUER) as kleora:
        kleora.me(request_id="REQ-1")
        pool = kleora.api().get_httpx_client()

        assert kleora.api() is kleora.api()
        assert kleora.api().get_httpx_client() is pool
        assert not pool.is_closed

    assert pool.is_closed


def test_the_async_client_labels_one_call_and_closes_one_pool() -> None:
    recorder = Recorder()

    async def run() -> httpx.AsyncClient:
        async with async_client(recorder, issuer=SANDBOX_ISSUER) as kleora:
            await kleora.me(request_id="REQ-1")
            await kleora.me()
            pool = (await kleora.api()).get_async_httpx_client()
            assert (await kleora.api()) is (await kleora.api())
            return pool

    pool = asyncio.run(run())

    assert recorder.ids == [None, "REQ-1", None]
    assert pool.is_closed


def test_a_base_url_that_already_names_the_version_is_not_doubled() -> None:
    recorder = Recorder()
    kleora = client(recorder, base_url=f"{API_BASE}/api/v1/", issuer=SANDBOX_ISSUER)

    kleora.api()

    assert recorder.paths == ["/api/v1/me"]


def test_the_generated_operations_run_through_the_guarded_client() -> None:
    recorder = Recorder()
    kleora = client(recorder, issuer=SANDBOX_ISSUER)

    principal = me_operation.sync(client=kleora.api())

    assert isinstance(principal, MeOut)
    assert list(principal.permissions) == ["users:read", "clients:read"]


# Problems ---------------------------------------------------------------


def test_a_problem_response_becomes_an_api_error() -> None:
    problem = {
        "type": "https://kleora.io/problems/validation-error",
        "title": "Request body failed validation",
        "status": 422,
        "detail": "1 field is invalid",
        "instance": "/api/v1/environments/9f1c/clients",
        "request_id": "req_01J",
        "errors": [
            {
                "field": "redirect_uris[1]",
                "message": "must be an absolute URL",
                "code": "invalid_url",
            }
        ],
    }
    recorder = Recorder(
        httpx.Response(200, json=me_document()),
        httpx.Response(422, json=problem, headers={"Content-Type": "application/problem+json"}),
    )
    kleora = client(recorder, issuer=SANDBOX_ISSUER)

    with pytest.raises(ApiError) as raised:
        kleora.me()

    error = raised.value
    assert error.type == "https://kleora.io/problems/validation-error"
    assert error.status == 422
    assert error.detail == "1 field is invalid"
    assert error.instance == "/api/v1/environments/9f1c/clients"
    assert error.request_id == "req_01J"
    assert len(error.errors) == 1
    assert error.errors[0].field == "redirect_uris[1]"
    assert error.errors[0].code == "invalid_url"


def test_the_request_id_comes_off_the_header_when_the_document_omits_it() -> None:
    """An older deployment, or an error something in front of the API wrote.

    The body first, the `X-Request-Id` response header otherwise. The header
    here disagrees with nothing, because the document has no `request_id` at
    all — which is exactly the case the fallback exists for.
    """
    recorder = Recorder(
        httpx.Response(
            404,
            json={
                "type": "https://kleora.io/problems/not-found",
                "title": "Not found",
                "status": 404,
            },
            headers={
                "Content-Type": "application/problem+json",
                "X-Request-Id": "req_from_the_header",
            },
        )
    )
    kleora = client(recorder, issuer=SANDBOX_ISSUER)

    with pytest.raises(ApiError) as raised:
        kleora.api()

    assert raised.value.request_id == "req_from_the_header"


def test_the_document_wins_over_the_header() -> None:
    """A server that sent both sends one value; the body is the one that is read.

    The two headers disagree here only so that the assertion can tell which was
    used — the server assigns the id once and puts it in both places.
    """
    recorder = Recorder(
        httpx.Response(
            404,
            json={
                "type": "https://kleora.io/problems/not-found",
                "title": "Not found",
                "status": 404,
                "request_id": "req_from_the_document",
            },
            headers={
                "Content-Type": "application/problem+json",
                "X-Request-Id": "req_from_the_header",
            },
        )
    )
    kleora = client(recorder, issuer=SANDBOX_ISSUER)

    with pytest.raises(ApiError) as raised:
        kleora.api()

    assert raised.value.request_id == "req_from_the_document"


def test_the_request_id_is_none_when_neither_half_carried_one() -> None:
    recorder = Recorder(
        httpx.Response(404, json={"type": "x", "title": "Not found", "status": 404})
    )
    kleora = client(recorder, issuer=SANDBOX_ISSUER)

    with pytest.raises(ApiError) as raised:
        kleora.api()

    assert raised.value.request_id is None


def test_a_problem_on_the_guard_s_own_request_is_an_api_error() -> None:
    recorder = Recorder(
        httpx.Response(
            401,
            json={
                "type": "https://kleora.io/problems/unauthenticated",
                "title": "Unauthenticated",
                "status": 401,
            },
        )
    )
    kleora = client(recorder, issuer=SANDBOX_ISSUER)

    with pytest.raises(ApiError) as raised:
        kleora.api()

    assert raised.value.status == 401
    assert raised.value.errors == ()


def test_a_response_that_is_not_a_problem_document_is_still_an_api_error() -> None:
    recorder = Recorder(
        httpx.Response(502, text="<html>Bad Gateway</html>", headers={"X-Request-Id": "req_9"})
    )
    kleora = client(recorder, issuer=SANDBOX_ISSUER)

    with pytest.raises(ApiError) as raised:
        kleora.api()

    assert raised.value.status == 502
    assert raised.value.type == "about:blank"
    assert raised.value.detail == "<html>Bad Gateway</html>"
    assert raised.value.request_id == "req_9"


def test_a_caller_s_own_response_hook_still_sees_the_error_response() -> None:
    seen: list[int] = []
    recorder = Recorder(httpx.Response(403, json={"type": "x", "title": "no", "status": 403}))
    kleora = ManagementClient(
        api_key=TEST_KEY,
        base_url=API_BASE,
        issuer=SANDBOX_ISSUER,
        httpx_args={
            "transport": recorder.transport(),
            "event_hooks": {"response": [lambda response: seen.append(response.status_code)]},
        },
    )

    with pytest.raises(ApiError):
        kleora.api()

    assert seen == [403]


# The async client -------------------------------------------------------


def test_the_async_client_guards_the_same_way() -> None:
    recorder = Recorder(httpx.Response(200, json=me_document(kind="production", issuer=ISSUER)))

    async def run() -> str:
        async with async_client(recorder) as kleora:
            with pytest.raises(EnvironmentMismatch) as raised:
                await kleora.api()
            with pytest.raises(EnvironmentMismatch):
                await kleora.api()
            return str(raised.value)

    message = asyncio.run(run())

    assert "production" in message
    assert len(recorder.requests) == 1


def test_the_async_client_reads_me_once_and_raises_api_errors() -> None:
    recorder = Recorder(
        httpx.Response(200, json=me_document()),
        httpx.Response(200, json=me_document()),
        httpx.Response(404, json={"type": "not-found", "title": "Not found", "status": 404}),
    )

    async def run() -> ApiError:
        async with async_client(recorder, issuer=SANDBOX_ISSUER) as kleora:
            principal = await kleora.me()
            assert principal.principal.kind == "api_key"
            with pytest.raises(ApiError) as raised:
                await kleora.me()
            return raised.value

    error = asyncio.run(run())

    assert error.status == 404
    assert error.type == "not-found"


def test_the_async_client_construction_guard_sends_nothing() -> None:
    recorder = Recorder()

    with pytest.raises(EnvironmentMismatch):
        async_client(recorder, issuer=ISSUER)

    assert recorder.requests == []
