"""`AccountClient` against an `httpx.MockTransport`.

`tests/test_contract.py` runs it against a live issuer, with a real
`self_service` token.
"""

# One row per operation reads as a table only when a row is one line.
# ruff: noqa: E501

from __future__ import annotations

import inspect
import json
import re
from collections.abc import Callable
from pathlib import Path
from typing import Any

import httpx
import pytest

from kleora import AccountClient, ApiError, KleoraError
from kleora import account as account_module

ISSUER = "https://acme.kleora.eu"
DOCUMENT = Path(__file__).resolve().parents[1] / "openapi" / "account-v1.json"

PROFILE = {
    "id": "0b8f2a5e-4c1d-4e8a-9b7f-2d6c1e0a9f31",
    "email": "a@example.test",
    "email_verified": True,
    "name": "Ada",
    "locale": None,
    "picture_url": None,
    "has_password": True,
    "mfa_enrolled": False,
    "created_at": "2026-09-29T10:00:00Z",
}


class Recorder:
    """Records every request and answers each with `answer`."""

    def __init__(self, answer: Callable[[httpx.Request], httpx.Response]) -> None:
        self.answer = answer
        self.requests: list[httpx.Request] = []

    def handle(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        return self.answer(request)


def client(recorder: Recorder) -> AccountClient:
    return AccountClient(
        issuer=f"{ISSUER}/",
        access_token="tok",
        httpx_args={"transport": httpx.MockTransport(recorder.handle)},
    )


def schema_example(request: httpx.Request) -> httpx.Response:
    """A body shaped for whichever route was called — enough to parse."""

    path = request.url.path.removeprefix("/account/v1")
    bodies: dict[tuple[str, str], Any] = {
        ("GET", "/profile"): PROFILE,
        ("PATCH", "/profile"): PROFILE,
        ("GET", "/email"): {
            "email": "a@example.test",
            "email_verified": True,
            "change_pending": False,
        },
        ("POST", "/email"): {"sent": True},
        ("POST", "/email/resend"): {"sent": False},
        ("GET", "/password"): {"has_password": True, "min_length": 12, "breach_check": True},
        ("GET", "/reauth"): {
            "has_password": True,
            "reauth_providers": [],
            "passkey_available": False,
            "reauthenticated_until": None,
        },
        ("GET", "/sessions"): {"items": [], "next_cursor": None},
        ("POST", "/sessions/revoke-others"): {"revoked": 2},
        ("GET", "/mfa"): {"factors": [], "policy": "optional"},
        ("POST", "/mfa/enroll/start"): {"secret": "S", "otpauth_uri": "otpauth://totp/x"},
        ("POST", "/mfa/enroll/confirm"): {"recovery_codes": ["a"]},
        ("POST", "/mfa/recovery/regenerate"): {"recovery_codes": ["b"]},
        ("GET", "/passkeys"): {"passkeys": [], "portal_url": f"{ISSUER}/account/security"},
        ("GET", "/identities"): {"identities": [], "providers": [], "has_password": True},
        ("GET", "/settings"): {"settings": []},
        ("PUT", "/settings/theme"): {
            "key": "theme",
            "type": "string",
            "label": "Theme",
            "value": "dark",
            "constraints": {},
        },
        ("GET", "/portal"): {"url": f"{ISSUER}/account", "sections": ["profile"]},
        ("POST", "/deletion"): {"erase_after": "2026-10-06T10:00:00Z"},
    }
    body = bodies.get((request.method, path))
    if body is None:
        return httpx.Response(204)
    status = 202 if (request.method, path) in {("POST", "/email"), ("POST", "/deletion")} else 200
    return httpx.Response(status, json=body)


OPERATIONS: list[tuple[str, Callable[[AccountClient], object], str, str, Any]] = [
    ("get_profile", lambda c: c.get_profile(), "GET", "/profile", None),
    ("update_profile", lambda c: c.update_profile({"name": "Ada"}), "PATCH", "/profile", {"name": "Ada"}),
    ("get_email", lambda c: c.get_email(), "GET", "/email", None),
    ("request_email_change", lambda c: c.request_email_change("n@example.test"), "POST", "/email", {"email": "n@example.test"}),
    ("confirm_email_change", lambda c: c.confirm_email_change("t"), "POST", "/email/confirm", {"token": "t"}),
    ("resend_verification_email", lambda c: c.resend_verification_email(), "POST", "/email/resend", None),
    ("get_password_policy", lambda c: c.get_password_policy(), "GET", "/password", None),
    ("change_password", lambda c: c.change_password(current_password="o", new_password="n"), "POST", "/password", {"current_password": "o", "new_password": "n"}),
    ("get_reauthentication", lambda c: c.get_reauthentication(), "GET", "/reauth", None),
    ("reauthenticate", lambda c: c.reauthenticate("pw"), "POST", "/reauth", {"password": "pw"}),
    ("list_sessions", lambda c: c.list_sessions(limit=5, cursor="x"), "GET", "/sessions", None),
    ("revoke_session", lambda c: c.revoke_session("s1"), "DELETE", "/sessions/s1", None),
    ("revoke_other_sessions", lambda c: c.revoke_other_sessions(), "POST", "/sessions/revoke-others", None),
    ("list_mfa_factors", lambda c: c.list_mfa_factors(), "GET", "/mfa", None),
    ("start_totp_enrollment", lambda c: c.start_totp_enrollment(), "POST", "/mfa/enroll/start", None),
    ("confirm_totp_enrollment", lambda c: c.confirm_totp_enrollment("123456"), "POST", "/mfa/enroll/confirm", {"code": "123456"}),
    ("remove_mfa_factor", lambda c: c.remove_mfa_factor("f1"), "DELETE", "/mfa/f1", None),
    ("regenerate_recovery_codes", lambda c: c.regenerate_recovery_codes(), "POST", "/mfa/recovery/regenerate", None),
    ("list_passkeys", lambda c: c.list_passkeys(), "GET", "/passkeys", None),
    ("remove_passkey", lambda c: c.remove_passkey("p1"), "DELETE", "/passkeys/p1", None),
    ("list_identities", lambda c: c.list_identities(), "GET", "/identities", None),
    ("unlink_identity", lambda c: c.unlink_identity("i1"), "DELETE", "/identities/i1", None),
    ("list_settings", lambda c: c.list_settings(), "GET", "/settings", None),
    ("set_setting", lambda c: c.set_setting("theme", "dark"), "PUT", "/settings/theme", {"value": "dark"}),
    ("reset_setting", lambda c: c.reset_setting("theme"), "DELETE", "/settings/theme", None),
    ("get_portal", lambda c: c.get_portal(), "GET", "/portal", None),
    ("request_deletion", lambda c: c.request_deletion(), "POST", "/deletion", None),
    ("cancel_deletion", lambda c: c.cancel_deletion("mailed"), "DELETE", "/deletion", {"token": "mailed"}),
]  # fmt: skip


@pytest.mark.parametrize(("name", "run", "method", "path", "body"), OPERATIONS)
def test_each_operation_reaches_its_route(
    name: str, run: Callable[[AccountClient], object], method: str, path: str, body: Any
) -> None:
    recorder = Recorder(schema_example)
    run(client(recorder))

    request = recorder.requests[0]
    assert request.method == method
    assert request.url.path == f"/account/v1{path}"
    assert (json.loads(request.content) if request.content else None) == body
    assert request.headers["user-agent"].startswith("kleora-python/")
    if name == "cancel_deletion":
        assert "authorization" not in request.headers
    else:
        assert request.headers["authorization"] == "Bearer tok"


def test_list_sessions_pages() -> None:
    recorder = Recorder(schema_example)
    client(recorder).list_sessions(limit=5, cursor="x")
    assert dict(recorder.requests[0].url.params) == {"limit": "5", "cursor": "x"}


def test_covers_every_operation_the_document_declares() -> None:
    document = json.loads(DOCUMENT.read_text(encoding="utf-8"))
    declared = {
        f"{method.upper()} {path.removeprefix('/account/v1')}"
        for path, methods in document["paths"].items()
        for method in methods
    }
    names = {
        "/sessions/s1": "/sessions/{session_id}",
        "/mfa/f1": "/mfa/{factor_id}",
        "/passkeys/p1": "/passkeys/{factor_id}",
        "/identities/i1": "/identities/{identity_id}",
        "/settings/theme": "/settings/{key}",
    }
    reached = {f"{method} {names.get(path, path)}" for _, _, method, path, _ in OPERATIONS}
    assert reached == declared


SENSITIVE_NOTE = "**Sensitive.**"
ROUTE = re.compile(r"`(GET|POST|PUT|PATCH|DELETE) (/[^`]*)`")


def _placeholders(path: str) -> str:
    return re.sub(r"\{[^}]*\}", "{}", path)


def test_marks_sensitive_exactly_the_operations_the_document_marks() -> None:
    """The `**Sensitive.**` notes against `x-kleora-sensitive`.

    No generator carries the extension into this package, so the notes are
    hand-written prose and this is the one thing holding them to the committed
    document. A method whose docstring opens with a backticked route is one
    operation, and the note is its claim.
    """

    document = json.loads(DOCUMENT.read_text(encoding="utf-8"))
    declared = {
        f"{method.upper()} {_placeholders(path.removeprefix('/account/v1'))}": operation.get(
            "x-kleora-sensitive"
        )
        for path, methods in document["paths"].items()
        for method, operation in methods.items()
    }
    claimed: dict[str, bool] = {}
    for member in vars(AccountClient).values():
        doc = inspect.getdoc(member) or ""
        route = ROUTE.match(doc)
        if route is not None:
            claimed[f"{route[1]} {_placeholders(route[2])}"] = SENSITIVE_NOTE in doc
    assert claimed == declared
    # A note that drifted off its method's docstring would be counted by nobody.
    source = inspect.getsource(account_module)
    assert source.count(SENSITIVE_NOTE) == sum(claimed.values())


def test_returns_the_generated_models() -> None:
    profile = client(Recorder(schema_example)).get_profile()
    assert profile.email == "a@example.test"
    assert profile.has_password is True


def test_a_refusal_is_an_api_error_carrying_the_problem_type() -> None:
    def refuse(_: httpx.Request) -> httpx.Response:
        return httpx.Response(
            401,
            json={
                "type": "https://kleora.io/problems/reauth-required",
                "title": "Re-authentication required",
                "status": 401,
                "code": "reauth_required",
            },
            headers={"content-type": "application/problem+json"},
        )

    with pytest.raises(ApiError) as caught:
        client(Recorder(refuse)).change_password(new_password="x")
    assert caught.value.type == "https://kleora.io/problems/reauth-required"
    assert caught.value.status == 401


def test_update_profile_refuses_a_member_the_api_does_not_take() -> None:
    with pytest.raises(KleoraError, match="email"):
        client(Recorder(schema_example)).update_profile({"email": "x@example.test"})


def test_refuses_an_unusable_configuration() -> None:
    with pytest.raises(KleoraError, match="issuer"):
        AccountClient(issuer="acme.kleora.eu", access_token="t")
    with pytest.raises(KleoraError, match="access_token"):
        AccountClient(issuer=ISSUER, access_token="")


def test_never_shows_the_token() -> None:
    account = AccountClient(issuer=ISSUER, access_token="secret-token")
    assert "secret-token" not in repr(account)
    assert "secret-token" not in repr(account.api())


def test_is_a_context_manager() -> None:
    with AccountClient(issuer=ISSUER, access_token="t") as account:
        assert account.base_url == f"{ISSUER}/account/v1"
