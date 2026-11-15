"""The account portal's URL and the `return_to` shape rules.

The same cases as `@kleora-io/browser`'s and `@kleora-io/node`'s portal tests,
as cross-referenced copies rather than one fixture: the SDKs live in separate
repositories, and no CI runs all three.
"""

from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import parse_qsl, urlsplit

import pytest

from kleora import ACCOUNT_PORTAL_SECTIONS, KleoraError, account_portal_url

ISSUER = "https://acme-sandbox.kleora.eu"
DOCUMENT = Path(__file__).resolve().parents[1] / "openapi" / "account-v1.json"


def test_is_the_issuer_s_account_page_for_the_client() -> None:
    assert account_portal_url(issuer=ISSUER, client_id="cl_1") == (
        "https://acme-sandbox.kleora.eu/account?client_id=cl_1"
    )


def test_opens_at_a_section_and_carries_return_to_encoded() -> None:
    url = account_portal_url(
        issuer=f"{ISSUER}/",
        client_id="cl_1",
        section="security",
        return_to="https://app.example.com/settings?tab=a&b=1",
    )
    split = urlsplit(url)
    assert f"{split.scheme}://{split.netloc}" == ISSUER
    assert split.path == "/account/security"
    assert parse_qsl(split.query) == [
        ("client_id", "cl_1"),
        ("return_to", "https://app.example.com/settings?tab=a&b=1"),
    ]
    assert "return_to=https%3A%2F%2Fapp.example.com%2Fsettings%3Ftab%3Da%26b%3D1" in url


def test_every_declared_section_and_nothing_else() -> None:
    for section in ACCOUNT_PORTAL_SECTIONS:
        path = urlsplit(account_portal_url(issuer=ISSUER, client_id="c", section=section)).path
        assert path == f"/account/{section}"
    with pytest.raises(KleoraError, match="section must be one of"):
        account_portal_url(issuer=ISSUER, client_id="c", section="tenants")  # type: ignore[arg-type]


def test_the_sections_are_the_document_s_portal_section_enum() -> None:
    document = json.loads(DOCUMENT.read_text(encoding="utf-8"))
    declared = document["components"]["schemas"]["PortalSection"]["enum"]
    assert list(ACCOUNT_PORTAL_SECTIONS) == declared


@pytest.mark.parametrize(
    ("return_to", "complaint"),
    [
        ("/settings", "absolute"),
        ("//app.example.com/", "absolute"),
        ("javascript:alert(1)", "absolute"),
        ("https://app.example.com/#top", "fragment"),
        ("https://app.example.com/#", "fragment"),
        ("https://user:pw@app.example.com/", "userinfo"),
        ("https://user@app.example.com/", "userinfo"),
    ],
)
def test_refuses_a_return_to_of_the_wrong_shape(return_to: str, complaint: str) -> None:
    with pytest.raises(KleoraError, match=complaint):
        account_portal_url(issuer=ISSUER, client_id="c", return_to=return_to)


def test_accepts_any_absolute_url_because_membership_is_the_issuer_s() -> None:
    for return_to in ("http://localhost:3000/", "https://app.example.com/a?b=c"):
        assert "return_to=" in account_portal_url(issuer=ISSUER, client_id="c", return_to=return_to)


def test_refuses_an_unusable_issuer_or_an_empty_client_id() -> None:
    with pytest.raises(KleoraError, match="issuer"):
        account_portal_url(issuer="acme.kleora.eu", client_id="c")
    with pytest.raises(KleoraError, match="client_id"):
        account_portal_url(issuer=ISSUER, client_id="")


def test_is_keyword_only() -> None:
    with pytest.raises(TypeError):
        account_portal_url(ISSUER, "c")  # type: ignore[call-arg]
