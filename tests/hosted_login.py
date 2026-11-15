"""Enough of the hosted sign-in to obtain a real access token.

`AccountClient` is proved by *using* a `self_service` token, and the only way
to get one is the way a person gets one:
`/oauth/authorize` → the hosted pages → back to `redirect_uri` → `/oauth/token`.
This is `@kleora-io/node`'s `test/contract/hosted-login.ts` in Python: the hosted
pages are a static single-page app that reads `req` off its own URL and calls `/flow/*`
with JSON, so this is that browser minus the rendering. The flow API's
same-origin rule is satisfied the way a browser satisfies it — JSON and an
`Origin` equal to the issuer's on every write.
"""

from __future__ import annotations

import base64
import hashlib
import secrets
from typing import Any
from urllib.parse import parse_qs, urlencode, urljoin, urlsplit

import httpx

MAX_HOPS = 25


class HostedLoginError(Exception):
    """The walk did not end at the redirect URI with a code."""


def _b64url(value: bytes) -> str:
    return base64.urlsafe_b64encode(value).rstrip(b"=").decode()


def sign_in(
    *,
    issuer: str,
    client_id: str,
    redirect_uri: str,
    email: str,
    password: str,
    scope: str,
) -> dict[str, Any]:
    """Sign `email` in and redeem the code; the token endpoint's JSON answer."""

    verifier = _b64url(secrets.token_bytes(32))
    challenge = _b64url(hashlib.sha256(verifier.encode()).digest())
    query = urlencode(
        {
            "response_type": "code",
            "client_id": client_id,
            "redirect_uri": redirect_uri,
            "scope": scope,
            "state": _b64url(secrets.token_bytes(16)),
            "nonce": _b64url(secrets.token_bytes(16)),
            "code_challenge": challenge,
            "code_challenge_method": "S256",
        }
    )
    with httpx.Client(timeout=10.0, follow_redirects=False) as browser:
        code = _walk(browser, f"{issuer}/oauth/authorize?{query}", redirect_uri, email, password)
        response = browser.post(
            f"{issuer}/oauth/token",
            data={
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": redirect_uri,
                "client_id": client_id,
                "code_verifier": verifier,
            },
        )
    body: dict[str, Any] = response.json()
    if response.status_code != 200:
        raise HostedLoginError(f"/oauth/token answered {response.status_code}: {body}")
    return body


def _walk(browser: httpx.Client, url: str, redirect_uri: str, email: str, password: str) -> str:
    target = urlsplit(redirect_uri)
    current = url
    for _ in range(MAX_HOPS):
        here = urlsplit(current)
        if (here.scheme, here.netloc, here.path) == (target.scheme, target.netloc, target.path):
            params = parse_qs(here.query)
            if "code" not in params:
                raise HostedLoginError(f"the flow returned to {current} without a code")
            return params["code"][0]

        response = browser.get(current)
        if response.is_redirect:
            current = urljoin(current, response.headers["location"])
            continue
        if response.status_code != 200:
            raise HostedLoginError(f"{current} answered {response.status_code}")
        current = _act(browser, here.scheme + "://" + here.netloc, here, email, password)
    raise HostedLoginError(f"the hosted login did not finish in {MAX_HOPS} hops")


def _act(browser: httpx.Client, origin: str, here: Any, email: str, password: str) -> str:
    """What the SPA route does, and where it sends the browser next."""

    req = parse_qs(here.query).get("req", [None])[0]
    if req is None:
        raise HostedLoginError(f"{here.path} carries no req for this helper to continue")
    if here.path.endswith("/login"):
        envelope = _call(
            browser, origin, "/flow/login", {"req": req, "email": email, "password": password}
        )
    elif here.path.endswith("/select-tenant"):
        listed = browser.get(f"{origin}/flow/tenants", params={"req": req}).json()
        tenant = listed["tenants"][0]["id"]
        envelope = _call(browser, origin, "/flow/select-tenant", {"req": req, "tenant": tenant})
    else:
        raise HostedLoginError(f"unexpected hosted route: {here.path}")
    target = envelope.get("redirect_to")
    if not isinstance(target, str):
        raise HostedLoginError(f"the flow answered {envelope.get('step')!r} with nowhere to go")
    return urljoin(f"{origin}{here.path}", target)


def _call(browser: httpx.Client, origin: str, path: str, payload: dict[str, str]) -> dict[str, Any]:
    response = browser.post(f"{origin}{path}", json=payload, headers={"Origin": origin})
    body: dict[str, Any] = response.json()
    if response.status_code != 200:
        raise HostedLoginError(f"POST {path} answered {response.status_code}: {body}")
    return body
