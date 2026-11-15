"""`verify_access_token`, case by case."""

from __future__ import annotations

import asyncio
import time

import jwt
import pytest
from conftest import (
    AUDIENCE,
    CLIENT_ID,
    ISSUER,
    SANDBOX_ISSUER,
    Clock,
    JWKSEndpoint,
    SigningKey,
    access_token,
    id_token,
    raw_token,
)

from kleora import (
    AsyncJWKSCache,
    Claims,
    EnvironmentMismatch,
    JWKSCache,
    TokenError,
    verify_access_token,
    verify_access_token_async,
)


def cache(jwks: JWKSEndpoint, clock: Clock, **kwargs: float) -> JWKSCache:
    return JWKSCache(ISSUER, client=jwks.client(), clock=clock, **kwargs)


def test_a_valid_token_becomes_claims(key: SigningKey, jwks: JWKSEndpoint, clock: Clock) -> None:
    claims = verify_access_token(
        access_token(key), issuer=ISSUER, audience=AUDIENCE, jwks=cache(jwks, clock)
    )

    assert isinstance(claims, Claims)
    assert claims.iss == ISSUER
    assert claims.aud == (CLIENT_ID, AUDIENCE)
    assert claims.client_id == CLIENT_ID
    assert claims.env == "production"
    assert claims.scope == "openid profile email"
    assert claims.tenant_slug == "acme"
    assert claims.roles == ("owner",)
    assert claims.permissions == ("invoices:read", "invoices:write")
    assert claims.permissions_truncated is False
    assert claims.email == "ada@acme.example"
    assert claims.email_verified is True
    assert claims.amr == ("pwd", "otp")
    assert "invoices:read" in claims.permissions


def test_the_audience_must_be_in_aud(key: SigningKey, jwks: JWKSEndpoint, clock: Clock) -> None:
    with pytest.raises(TokenError) as raised:
        verify_access_token(
            access_token(key),
            issuer=ISSUER,
            audience="https://api.other.example",
            jwks=cache(jwks, clock),
        )

    assert raised.value.code == "audience_mismatch"


def test_the_issuer_must_match_exactly(key: SigningKey, jwks: JWKSEndpoint, clock: Clock) -> None:
    with pytest.raises(TokenError) as raised:
        verify_access_token(
            access_token(key, issuer="https://elsewhere.kleora.eu"),
            issuer=ISSUER,
            audience=AUDIENCE,
            jwks=cache(jwks, clock),
        )

    assert raised.value.code == "issuer_mismatch"


def test_a_trailing_slash_on_the_configured_issuer_is_forgiven(
    key: SigningKey, jwks: JWKSEndpoint, clock: Clock
) -> None:
    claims = verify_access_token(
        access_token(key), issuer=f"{ISSUER}/", audience=AUDIENCE, jwks=cache(jwks, clock)
    )

    assert claims.iss == ISSUER


def test_an_expired_token_is_rejected(key: SigningKey, jwks: JWKSEndpoint, clock: Clock) -> None:
    stale = access_token(key, now=int(time.time()) - 3600, lifetime=300)

    with pytest.raises(TokenError) as raised:
        verify_access_token(stale, issuer=ISSUER, audience=AUDIENCE, jwks=cache(jwks, clock))

    assert raised.value.code == "expired"
    assert "60s" in str(raised.value)


def test_expiry_inside_the_clock_tolerance_still_verifies(
    key: SigningKey, jwks: JWKSEndpoint, clock: Clock
) -> None:
    just_expired = access_token(key, now=int(time.time()) - 330, lifetime=300)

    claims = verify_access_token(
        just_expired, issuer=ISSUER, audience=AUDIENCE, jwks=cache(jwks, clock)
    )

    assert claims.client_id == CLIENT_ID


def test_an_iat_beyond_the_tolerance_is_rejected(
    key: SigningKey, jwks: JWKSEndpoint, clock: Clock
) -> None:
    """`malformed`, not `expired`: a retry would bring back the same skew."""

    ahead = access_token(key, now=int(time.time()) + 600)

    with pytest.raises(TokenError) as raised:
        verify_access_token(ahead, issuer=ISSUER, audience=AUDIENCE, jwks=cache(jwks, clock))

    assert raised.value.code == "malformed"
    assert "60s" in str(raised.value)


def test_an_unknown_kid_fails_after_the_refetch(
    jwks: JWKSEndpoint, clock: Clock, rotated: SigningKey
) -> None:
    """The `kid` is not in the document and a refetch does not produce it."""

    token = access_token(rotated)

    with pytest.raises(TokenError) as raised:
        verify_access_token(token, issuer=ISSUER, audience=AUDIENCE, jwks=cache(jwks, clock))

    assert raised.value.code == "unknown_kid"
    assert jwks.fetches == 1


def test_an_unreachable_issuer_is_not_reported_as_a_bad_token(
    jwks: JWKSEndpoint, clock: Clock, key: SigningKey
) -> None:
    """The consequence `issuer_unavailable` exists for: a middleware can answer 503, not 401.

    Nothing is wrong with this token — the issuer signed it with the key it
    publishes — and the JWKS endpoint is down. The verifier passes the cache's
    verdict through unchanged, so an application branching on `code` can tell the
    outage from a credential it should refuse.
    """

    jwks.status = 503

    with pytest.raises(TokenError) as raised:
        verify_access_token(
            access_token(key), issuer=ISSUER, audience=AUDIENCE, jwks=cache(jwks, clock)
        )

    assert raised.value.code == "issuer_unavailable"


def test_an_unknown_kid_inside_the_floor_does_not_fetch_again(
    jwks: JWKSEndpoint, clock: Clock, rotated: SigningKey, key: SigningKey
) -> None:
    keys = cache(jwks, clock)
    verify_access_token(access_token(key), issuer=ISSUER, audience=AUDIENCE, jwks=keys)
    assert jwks.fetches == 1

    clock.advance(90)
    with pytest.raises(TokenError):
        verify_access_token(access_token(rotated), issuer=ISSUER, audience=AUDIENCE, jwks=keys)
    assert jwks.fetches == 2

    clock.advance(30)
    with pytest.raises(TokenError):
        verify_access_token(access_token(rotated), issuer=ISSUER, audience=AUDIENCE, jwks=keys)
    assert jwks.fetches == 2


def test_a_tampered_signature_is_rejected(
    key: SigningKey, jwks: JWKSEndpoint, clock: Clock
) -> None:
    header, payload, signature = access_token(key).split(".")
    # The FIRST character, not the last two: character 0 contributes all six of
    # its bits to byte 0 of the signature, so the decoded bytes always change.
    # The last two characters of an 86-character ES256 signature carry only
    # byte 63 plus slack bits, so several distinct pairs decode to the same
    # byte — a "tampered" token that verifies about 1 time in 256.
    flipped = ("A" if signature[0] != "A" else "B") + signature[1:]

    with pytest.raises(TokenError) as raised:
        verify_access_token(
            f"{header}.{payload}.{flipped}",
            issuer=ISSUER,
            audience=AUDIENCE,
            jwks=cache(jwks, clock),
        )

    assert raised.value.code == "invalid_signature"


def test_a_token_signed_by_another_key_is_rejected(
    jwks: JWKSEndpoint, clock: Clock, key: SigningKey
) -> None:
    impostor = SigningKey.make(key.kid)

    with pytest.raises(TokenError) as raised:
        verify_access_token(
            access_token(impostor), issuer=ISSUER, audience=AUDIENCE, jwks=cache(jwks, clock)
        )

    assert raised.value.code == "invalid_signature"


@pytest.mark.parametrize("token", ["", "not-a-token", "a.b.c"])
def test_an_unreadable_token_is_malformed(token: str, jwks: JWKSEndpoint, clock: Clock) -> None:
    with pytest.raises(TokenError) as raised:
        verify_access_token(token, issuer=ISSUER, audience=AUDIENCE, jwks=cache(jwks, clock))

    assert raised.value.code == "malformed"
    assert jwks.fetches == 0


def test_an_algorithm_other_than_es256_is_refused_before_any_fetch(
    key: SigningKey, jwks: JWKSEndpoint, clock: Clock
) -> None:
    token = jwt.encode({"iss": ISSUER}, "x" * 32, algorithm="HS256", headers={"kid": key.kid})

    with pytest.raises(TokenError) as raised:
        verify_access_token(token, issuer=ISSUER, audience=AUDIENCE, jwks=cache(jwks, clock))

    assert raised.value.code == "malformed"
    assert "ES256" in str(raised.value)
    assert jwks.fetches == 0


def test_a_header_without_a_kid_is_malformed(
    key: SigningKey, jwks: JWKSEndpoint, clock: Clock
) -> None:
    token = raw_token({"alg": "ES256", "typ": "at+jwt"}, {"iss": ISSUER})

    with pytest.raises(TokenError) as raised:
        verify_access_token(token, issuer=ISSUER, audience=AUDIENCE, jwks=cache(jwks, clock))

    assert raised.value.code == "malformed"


def test_an_id_token_is_refused_by_type(key: SigningKey, jwks: JWKSEndpoint, clock: Clock) -> None:
    """The same key, the same signature, every access-token claim — `typ: "JWT"`.

    Without the type check the only thing refusing this would be whichever
    claims an ID token happens to lack, which is an accident rather than a
    check.
    """

    with pytest.raises(TokenError) as raised:
        verify_access_token(
            id_token(key), issuer=ISSUER, audience=AUDIENCE, jwks=cache(jwks, clock)
        )

    assert raised.value.code == "invalid_type"
    assert "at+jwt" in str(raised.value)
    assert jwks.fetches == 0


def test_a_typ_of_jwt_is_refused_before_any_fetch(
    key: SigningKey, jwks: JWKSEndpoint, clock: Clock
) -> None:
    """An otherwise perfect access token relabelled `typ: "JWT"`."""

    with pytest.raises(TokenError) as raised:
        verify_access_token(
            access_token(key, typ="JWT"),
            issuer=ISSUER,
            audience=AUDIENCE,
            jwks=cache(jwks, clock),
        )

    assert raised.value.code == "invalid_type"
    assert "JWT" in str(raised.value)
    assert jwks.fetches == 0


def test_a_header_without_a_typ_is_refused(
    key: SigningKey, jwks: JWKSEndpoint, clock: Clock
) -> None:
    token = raw_token({"alg": "ES256", "kid": key.kid}, {"iss": ISSUER})

    with pytest.raises(TokenError) as raised:
        verify_access_token(token, issuer=ISSUER, audience=AUDIENCE, jwks=cache(jwks, clock))

    assert raised.value.code == "invalid_type"
    assert "no typ" in str(raised.value)
    assert jwks.fetches == 0


@pytest.mark.parametrize("typ", ["at+jwt", "AT+JWT", "application/at+jwt"])
def test_every_spelling_of_the_access_token_type_is_accepted(
    typ: str, key: SigningKey, jwks: JWKSEndpoint, clock: Clock
) -> None:
    """RFC 7515 §4.1.9 lets `typ` drop `application/`; media types are caseless."""

    token = key.sign(
        {
            "iss": ISSUER,
            "sub": "s",
            "aud": [AUDIENCE],
            "iat": int(time.time()),
            "exp": int(time.time()) + 300,
            "jti": "j",
            "client_id": CLIENT_ID,
            "scope": "openid",
            "env": "production",
            "amr": ["pwd"],
        },
        headers={"typ": typ},
    )

    claims = verify_access_token(token, issuer=ISSUER, audience=AUDIENCE, jwks=cache(jwks, clock))

    assert claims.client_id == CLIENT_ID


@pytest.mark.parametrize("claim", ["sub", "jti", "client_id", "scope", "env", "exp", "iat"])
def test_a_missing_required_claim_is_malformed(
    claim: str, key: SigningKey, jwks: JWKSEndpoint, clock: Clock
) -> None:
    token = access_token(key, omit=[claim])

    with pytest.raises(TokenError) as raised:
        verify_access_token(token, issuer=ISSUER, audience=AUDIENCE, jwks=cache(jwks, clock))

    assert raised.value.code == "malformed"


def test_a_session_without_a_tenant_verifies_with_empty_authorisation(
    key: SigningKey, jwks: JWKSEndpoint, clock: Clock
) -> None:
    token = access_token(
        key,
        omit=["tenant", "tenant_slug", "email", "email_verified"],
        roles=[],
        permissions=[],
    )

    claims = verify_access_token(token, issuer=ISSUER, audience=AUDIENCE, jwks=cache(jwks, clock))

    assert claims.tenant is None
    assert claims.tenant_slug is None
    assert claims.roles == ()
    assert claims.permissions == ()
    assert claims.email is None
    assert claims.email_verified is None


def test_truncated_permissions_are_reported(
    key: SigningKey, jwks: JWKSEndpoint, clock: Clock
) -> None:
    token = access_token(key, permissions_truncated=True)

    claims = verify_access_token(token, issuer=ISSUER, audience=AUDIENCE, jwks=cache(jwks, clock))

    assert claims.permissions_truncated is True


def test_a_sandbox_token_on_a_production_issuer_is_an_environment_mismatch(
    key: SigningKey, jwks: JWKSEndpoint, clock: Clock
) -> None:
    token = access_token(key, env="sandbox")

    with pytest.raises(EnvironmentMismatch):
        verify_access_token(token, issuer=ISSUER, audience=AUDIENCE, jwks=cache(jwks, clock))


def test_a_sandbox_issuer_expects_a_sandbox_token(
    key: SigningKey, jwks: JWKSEndpoint, clock: Clock
) -> None:
    keys = JWKSCache(SANDBOX_ISSUER, client=jwks.client(), clock=clock)

    claims = verify_access_token(
        access_token(key, issuer=SANDBOX_ISSUER, env="sandbox"),
        issuer=SANDBOX_ISSUER,
        audience=AUDIENCE,
        jwks=keys,
    )

    assert claims.env == "sandbox"


def test_the_async_verifier_answers_the_same(
    key: SigningKey, jwks: JWKSEndpoint, clock: Clock
) -> None:
    async def run() -> tuple[Claims, str]:
        keys = AsyncJWKSCache(ISSUER, client=jwks.async_client(), clock=clock)
        claims = await verify_access_token_async(
            access_token(key), issuer=ISSUER, audience=AUDIENCE, jwks=keys
        )
        with pytest.raises(TokenError) as raised:
            await verify_access_token_async(
                access_token(key, issuer="https://elsewhere.kleora.eu"),
                issuer=ISSUER,
                audience=AUDIENCE,
                jwks=keys,
            )
        await keys.aclose()
        return claims, raised.value.code

    claims, code = asyncio.run(run())

    assert claims.client_id == CLIENT_ID
    assert code == "issuer_mismatch"
