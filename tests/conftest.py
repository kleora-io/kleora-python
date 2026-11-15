"""Locally minted keys and tokens, and a JWKS endpoint that counts its fetches.

Everything the unit suite verifies is verified against keys made here, so the
whole of it runs with no server, no network and no clock to wait on: the caches
take an injected monotonic clock and the HTTP goes through `httpx.MockTransport`.
The live half of the suite is `test_contract.py`, behind the `live` marker.
"""

from __future__ import annotations

import base64
import json
import time
import uuid
from collections.abc import Callable, Iterator, Sequence
from dataclasses import dataclass, field
from typing import Any

import httpx
import jwt
import pytest
from cryptography.hazmat.primitives.asymmetric import ec
from jwt.algorithms import ECAlgorithm

ISSUER = "https://acme.kleora.eu"
SANDBOX_ISSUER = "https://acme-sandbox.kleora.eu"
AUDIENCE = "https://api.acme.example"
CLIENT_ID = "8f1c9d5e-0b3a-4d1e-9a2b-6c7d8e9f0a1b"
API_BASE = "https://api.kleora.io"

TEST_KEY = "kl_test_" + "K" * 40
LIVE_KEY = "kl_live_" + "L" * 40


@dataclass
class SigningKey:
    """One ES256 key pair, as an environment's signing key.

    `kid` is a random 16-byte base64url string on the server; any unique string
    does here.
    """

    kid: str
    private: ec.EllipticCurvePrivateKey

    @classmethod
    def make(cls, kid: str) -> SigningKey:
        return cls(kid=kid, private=ec.generate_private_key(ec.SECP256R1()))

    def public_jwk(self) -> dict[str, Any]:
        jwk: dict[str, Any] = dict(ECAlgorithm.to_jwk(self.private.public_key(), as_dict=True))
        jwk.update({"kid": self.kid, "use": "sig", "alg": "ES256"})
        return jwk

    def sign(
        self,
        payload: dict[str, Any],
        *,
        algorithm: str = "ES256",
        headers: dict[str, Any] | None = None,
    ) -> str:
        header: dict[str, Any] = {"kid": self.kid, "typ": "at+jwt"}
        header.update(headers or {})
        return jwt.encode(payload, self.private, algorithm=algorithm, headers=header)


def access_token(
    key: SigningKey,
    *,
    issuer: str = ISSUER,
    audience: str | list[str] | None = None,
    lifetime: int = 300,
    now: int | None = None,
    typ: str = "at+jwt",
    omit: Sequence[str] = (),
    **overrides: Any,
) -> str:
    """A token shaped like the access token an issuer mints."""

    issued = int(time.time()) if now is None else now
    payload: dict[str, Any] = {
        "iss": issuer,
        "sub": str(uuid.uuid4()),
        "aud": [CLIENT_ID, AUDIENCE] if audience is None else audience,
        "iat": issued,
        "exp": issued + lifetime,
        "jti": str(uuid.uuid4()),
        "client_id": CLIENT_ID,
        "scope": "openid profile email",
        "env": "production",
        "tenant": str(uuid.uuid4()),
        "tenant_slug": "acme",
        "roles": ["owner"],
        "permissions": ["invoices:read", "invoices:write"],
        "email": "ada@acme.example",
        "email_verified": True,
        "amr": ["pwd", "otp"],
    }
    payload.update(overrides)
    for name in omit:
        payload.pop(name, None)
    return key.sign(payload, headers={"typ": typ})


def id_token(key: SigningKey, *, issuer: str = ISSUER, **overrides: Any) -> str:
    """An ID token: the same header, the same key, `typ: "JWT"`.

    The substitution an access-token verifier has to refuse by type rather
    than by luck of the claim shape, so this one deliberately carries every
    claim the access token carries.
    """

    issued = int(time.time())
    payload: dict[str, Any] = {
        "iss": issuer,
        "sub": str(uuid.uuid4()),
        "aud": [CLIENT_ID, AUDIENCE],
        "iat": issued,
        "exp": issued + 300,
        "jti": str(uuid.uuid4()),
        "client_id": CLIENT_ID,
        "scope": "openid profile email",
        "env": "production",
        "roles": [],
        "permissions": [],
        "amr": ["pwd"],
    }
    payload.update(overrides)
    return key.sign(payload, headers={"typ": "JWT"})


def raw_token(header: dict[str, Any], payload: dict[str, Any]) -> str:
    """A syntactically valid JWS with a header PyJWT would refuse to write.

    `jwt.encode` validates `kid` and `alg` as it writes, so a token whose header
    is *missing* a `kid` — the shape the verifier has to refuse — has to be built
    by hand.
    """

    def segment(value: dict[str, Any]) -> str:
        return base64.urlsafe_b64encode(json.dumps(value).encode()).decode().rstrip("=")

    return f"{segment(header)}.{segment(payload)}.{'A' * 86}"


class Clock:
    """A monotonic clock the test moves by hand."""

    def __init__(self, start: float = 1_000.0) -> None:
        self.now = start

    def __call__(self) -> float:
        return self.now

    def advance(self, seconds: float) -> None:
        self.now += seconds


@dataclass
class JWKSEndpoint:
    """`/.well-known/jwks.json` for one issuer, counting every request it answers."""

    keys: list[SigningKey] = field(default_factory=list)
    max_age: int | None = 300
    status: int = 200
    fetches: int = 0
    before: Callable[[], None] | None = None
    body: dict[str, Any] | None = None
    """Answered instead of the JWK Set, for the documents that are not one."""

    def document(self) -> dict[str, Any]:
        if self.body is not None:
            return self.body
        return {"keys": [key.public_jwk() for key in self.keys]}

    def handle(self, request: httpx.Request) -> httpx.Response:
        self.fetches += 1
        if self.before is not None:
            self.before()
        if self.status != 200:
            return httpx.Response(self.status, json={"title": "no"})
        headers = {} if self.max_age is None else {"Cache-Control": f"max-age={self.max_age}"}
        return httpx.Response(200, json=self.document(), headers=headers)

    def client(self) -> httpx.Client:
        return httpx.Client(transport=httpx.MockTransport(self.handle))

    def async_client(self) -> httpx.AsyncClient:
        return httpx.AsyncClient(transport=httpx.MockTransport(self.handle))


@pytest.fixture
def key() -> SigningKey:
    return SigningKey.make("kid-active")


@pytest.fixture
def rotated() -> SigningKey:
    return SigningKey.make("kid-next")


@pytest.fixture
def clock() -> Clock:
    return Clock()


@pytest.fixture
def jwks(key: SigningKey) -> Iterator[JWKSEndpoint]:
    yield JWKSEndpoint(keys=[key])
