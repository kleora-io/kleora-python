"""The cases that need a real issuer and a real key.

Opt-in: `pytest -m live`. The unit suite covers the same rules against locally
minted keys and an `httpx.MockTransport`; these prove the wire — that the
document a real issuer publishes is one `JWKSCache` can read, and that a real
`GET /me` is what the environment guard thinks it is.

Configuration comes from these environment variables; none has a default:

| Variable | Meaning |
| --- | --- |
| `KLEORA_TEST_ISSUER` | A sandbox issuer, e.g. `https://acme-sandbox.kleora.eu` |
| `KLEORA_TEST_API_BASE` | The management API origin |
| `KLEORA_TEST_API_KEY` | A `kl_test_` key for that issuer's environment |
| `KLEORA_TEST_PRODUCTION_ISSUER` | The same App's production issuer (optional) |
| `KLEORA_TEST_PRODUCTION_ENVIRONMENT_ID` | An environment outside the key's scope (optional) |
| `KLEORA_TEST_ACCESS_TOKEN`, `KLEORA_TEST_AUDIENCE` | A token to verify (optional) |
| `KLEORA_TEST_SELF_SERVICE_CLIENT_ID` | A Client of that issuer allowing `self_service` |
| `KLEORA_TEST_SELF_SERVICE_REDIRECT_URI` | One of that Client's redirect URIs |
| `KLEORA_TEST_SELF_SERVICE_EMAIL` | A person who can sign in to it |
| `KLEORA_TEST_SELF_SERVICE_PASSWORD` | That person's password |

Every test skips rather than fails when what it needs is absent or the issuer is
not answering: a suite that goes red because nothing is running says nothing
about the code.

**Except where somebody arranged an issuer, where that leniency is the hazard.**
`pytest -m live` *collects* these tests, so a missing environment or an
unreachable issuer is a row of skips and exit 0 — a run that goes green without
having talked to anything. `KLEORA_TEST_REQUIRE_LIVE=1` says the caller arranged
an environment and means it: absence becomes a failure naming the variable or
the URL. Only the two settings marked optional above still skip under it, and
they skip because minting an access token needs a browser login this suite has
no business doing (`@kleora-io/node`'s contract suite does log in).
"""

from __future__ import annotations

import os
from typing import NoReturn
from uuid import UUID

import httpx
import pytest
from hosted_login import sign_in

from kleora import (
    AccountClient,
    ApiError,
    EnvironmentMismatch,
    JWKSCache,
    ManagementClient,
    account_portal_url,
    verify_access_token,
)
from kleora._generated.api.environments import read_environment

pytestmark = pytest.mark.live

# See the module docstring: it turns "there was nothing to talk to" from a skip
# into the failure it is when somebody went to the trouble of arranging one.
REQUIRE_LIVE = os.environ.get("KLEORA_TEST_REQUIRE_LIVE") == "1"


def absent(message: str) -> NoReturn:
    """Skip on a developer's machine; fail where an environment was promised."""
    if REQUIRE_LIVE:
        pytest.fail(message)
    pytest.skip(message)


def setting(name: str, *, optional: bool = False) -> str:
    """The `KLEORA_TEST_{name}` value, or the end of this test.

    `optional` is for the settings that need more than an issuer and a key: those
    skip even under `KLEORA_TEST_REQUIRE_LIVE`, because their absence is the
    arrangement rather than a broken one.
    """
    value = os.environ.get(f"KLEORA_TEST_{name}")
    if not value:
        message = f"KLEORA_TEST_{name} is not set"
        if optional:
            pytest.skip(message)
        absent(message)
    return value


def reachable(url: str) -> None:
    """Skip — or fail, under `KLEORA_TEST_REQUIRE_LIVE` — unless `url` answers."""

    try:
        httpx.get(url, timeout=5.0)
    except httpx.HTTPError as error:
        absent(f"{url} is not answering: {error}")


@pytest.fixture
def issuer() -> str:
    value = setting("ISSUER").rstrip("/")
    reachable(f"{value}/.well-known/jwks.json")
    return value


@pytest.fixture
def kleora(issuer: str) -> ManagementClient:
    base_url = setting("API_BASE")
    reachable(f"{base_url.rstrip('/')}/api/v1/me")
    return ManagementClient(api_key=setting("API_KEY"), base_url=base_url, issuer=issuer)


def test_the_published_jwks_is_one_the_cache_can_read(issuer: str) -> None:
    document = httpx.get(f"{issuer}/.well-known/jwks.json", timeout=5.0).json()
    kids = [key["kid"] for key in document["keys"]]
    assert kids, "the issuer publishes no signing keys"

    cache = JWKSCache(issuer)
    try:
        for kid in kids:
            assert cache.get_key(kid).key_id == kid
    finally:
        cache.close()


def test_me_reports_the_environment_the_key_belongs_to(
    kleora: ManagementClient, issuer: str
) -> None:
    principal = kleora.me()

    assert principal.principal.kind == "api_key"
    environment = kleora.environment
    assert environment is not None
    assert environment.kind == "sandbox"
    assert environment.issuer.rstrip("/") == issuer


def test_a_test_key_with_the_production_issuer_never_reaches_the_wire() -> None:
    production = setting("PRODUCTION_ISSUER")

    with pytest.raises(EnvironmentMismatch):
        ManagementClient(
            api_key=setting("API_KEY"), base_url=setting("API_BASE"), issuer=production
        )


def test_an_environment_outside_the_key_s_scope_is_a_problem(
    kleora: ManagementClient,
) -> None:
    """404, not 403: existence outside a principal's scope is never revealed."""

    other = str(UUID(setting("PRODUCTION_ENVIRONMENT_ID")))

    with pytest.raises(ApiError) as raised:
        read_environment.sync(other, client=kleora.api())

    assert raised.value.status == 404
    assert raised.value.type.endswith("not-found")


def test_a_real_access_token_verifies(issuer: str) -> None:
    token = setting("ACCESS_TOKEN", optional=True)
    audience = setting("AUDIENCE", optional=True)

    claims = verify_access_token(token, issuer=issuer, audience=audience)

    assert claims.iss == issuer
    assert claims.env == "sandbox"
    assert audience in claims.aud


# --- Self-service --------------------------------------------------------------
#
# A credential is proved by using it. The token comes from a real sign-in with
# `self_service` in the scope, exactly as a customer's application obtains one.

SELF_SERVICE_SCOPE = "openid profile email offline_access self_service"


@pytest.fixture
def person(issuer: str) -> dict[str, str]:
    return {
        "issuer": issuer,
        "client_id": setting("SELF_SERVICE_CLIENT_ID"),
        "redirect_uri": setting("SELF_SERVICE_REDIRECT_URI"),
        "email": setting("SELF_SERVICE_EMAIL"),
        "password": setting("SELF_SERVICE_PASSWORD"),
    }


def _sign_in(person: dict[str, str], password: str | None = None) -> str:
    tokens = sign_in(
        issuer=person["issuer"],
        client_id=person["client_id"],
        redirect_uri=person["redirect_uri"],
        email=person["email"],
        password=password or person["password"],
        scope=SELF_SERVICE_SCOPE,
    )
    token = tokens["access_token"]
    assert isinstance(token, str)
    return token


def test_the_self_service_token_verifies_and_carries_the_scope(person: dict[str, str]) -> None:
    claims = verify_access_token(
        _sign_in(person), issuer=person["issuer"], audience=person["client_id"]
    )
    assert "self_service" in claims.scope.split()


def test_account_client_changes_the_password_with_the_person_s_own_token(
    person: dict[str, str],
) -> None:
    with AccountClient(issuer=person["issuer"], access_token=_sign_in(person)) as account:
        profile = account.get_profile()
        assert profile.email == person["email"]
        assert profile.has_password is True

        # Sensitive: refused until the person re-authenticates.
        with pytest.raises(ApiError) as refused:
            account.change_password(current_password=person["password"], new_password="x")
        assert refused.value.type.endswith("/reauth-required")

        account.reauthenticate(person["password"])
        new_password = f"{person['password']}-next"
        account.change_password(current_password=person["password"], new_password=new_password)

        sessions = account.list_sessions()
        assert [row.current for row in sessions.items].count(True) == 1
        portal = account.get_portal()
        assert portal.url == f"{person['issuer']}/account"

    # The password the call set is the one that signs in now.
    assert _sign_in(person, new_password)


def test_the_portal_url_names_a_page_the_issuer_serves(person: dict[str, str]) -> None:
    url = account_portal_url(
        issuer=person["issuer"], client_id=person["client_id"], section="security"
    )
    response = httpx.get(url, timeout=5.0)
    assert response.status_code == 200
    assert "frame-ancestors 'none'" in response.headers["content-security-policy"]
