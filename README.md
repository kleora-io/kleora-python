# `kleora`

The Kleora Python SDK: access-token verification, a JWKS cache, and clients
for the management API and the end-user self-service API.

Python ≥ 3.12. Kleora's documentation, including how to create an App,
register a Client and issue an API key, is at https://kleora.io/en/docs.

## Install

```bash
pip install kleora
# or
uv add kleora
```

```python
from kleora import ManagementClient, verify_access_token

claims = verify_access_token(token, issuer=ISSUER, audience="https://api.acme.example")
if "invoices:read" not in claims.permissions:
    raise PermissionError

with ManagementClient(api_key=API_KEY, issuer=ISSUER) as kleora:
    principal = kleora.me()
```

## Verification

`verify_access_token(token, *, issuer, audience, jwks=None, clock_tolerance=60)`
returns a frozen `Claims` after seven checks: the header's `alg` (`ES256`) and
`typ` (`at+jwt`); the key resolved by `kid` from the issuer's JWKS; the
signature; `iss`, compared with the configured issuer as an exact string; `aud`,
which must contain the configured `audience`; and `exp` and `iat`, with
`clock_tolerance` seconds of allowed skew either way. (The eighth check, that a
sandbox issuer is not paired with a production credential, happens at
construction rather than here.) It is local: the only request it can make is
for the issuer's JWKS document, so our availability is never in front of a
customer's API. `verify_access_token_async` is the same over `AsyncJWKSCache`.

The header is checked before the JWKS is consulted: `alg` must be `ES256` and
`typ` must be `at+jwt` (RFC 9068 §2.1; `application/at+jwt` is the same media
type and is accepted, case-insensitively). The type check is what refuses an ID
token, which the environment signs with the same key and the same `alg` and
which differs from an access token only there.

Failures are `TokenError`, whose `code` is one of `expired`,
`invalid_signature`, `invalid_type`, `issuer_mismatch`, `audience_mismatch`,
`unknown_kid`, `issuer_unavailable` or `malformed` — the same set
`@kleora-io/node` raises, so an application that branches on one branches on
the other unchanged. `issuer_unavailable` is the one that is **not** a verdict on
the token: the key set could not be read at all, so a middleware answers it with
a retryable `503` where every other code is a `401`. A token whose
`env` claim disagrees with the issuer's classification raises
`EnvironmentMismatch`, the same error a `kl_test_` key against a production
issuer gets, so a middleware should catch `KleoraError` rather than
`TokenError` alone.

`JWKSCache(issuer, ttl=300, min_refresh_interval=60)` holds one issuer's keys.
The document is good for its `Cache-Control` max-age; an unknown `kid` triggers
one refetch and never more often than the floor; a failed fetch keeps serving
the keys already held until twice the TTL, then fails closed with
`issuer_unavailable` — while the set it holds is still usable a missing `kid` is
`unknown_kid`, because the document was read and does not list it. It is
thread-safe — the lock covers the fetch, so concurrent misses make one request
between them — and `AsyncJWKSCache` is the same algorithm on an event loop.
`verify_access_token` shares one cache per issuer per process when it is not
given one.

## The management API

`ManagementClient` and `AsyncManagementClient` **wrap** the generated client,
they do not restate it. `kleora.api()` returns the guarded generated
`AuthenticatedClient`; every operation under `kleora._generated.api` takes
it:

```python
from kleora._generated.api.apps import list_apps

apps = list_apps.sync(client=kleora.api())
```

The wrapper adds what a generator cannot know:

- **the credential.** Accepted through the constructor only — never read from
  the environment behind the caller's back — never logged, and rendered in
  `repr` as its literal prefix (`kl_test_…`) and nothing more.
- **the environment guard.** With `issuer` given, a `kl_test_` key
  against a production issuer raises `EnvironmentMismatch` at construction,
  before a socket is opened. Without it, the first call fetches `GET /me` and
  compares the key's kind — and the configured issuer, when there is one —
  against what the environment reports. The verdict, refusal included, is then
  answered locally, so a misconfigured key is sent exactly once.
- **the error shape.** Every non-2xx becomes `ApiError` carrying the RFC 9457
  problem: `type`, `status`, `title`, `detail`, `errors`, `instance`,
  `request_id`.

`base_url` is the API origin; a value that already ends in `/api/v1` is
accepted too. `httpx_args` reaches `httpx.Client` unchanged for a proxy, a
transport or a client certificate. Every request carries
`User-Agent: kleora-python/{version}`.

`api()` always returns the same client, and therefore one connection pool for
the life of the `ManagementClient`; `close()` (or leaving its `with` block)
closes it. To set `X-Request-Id` on a call, scope it:

```python
with kleora.request_id("req_01J…"):
    list_apps.sync(client=kleora.api())
```

`me(request_id=…)` is the same thing for the one call it makes. The label
belongs to the block and to the context that entered it, so it can neither
outlive the call nor reach one made concurrently beside it — and nothing is
invented when the caller supplies nothing, because the server generates the id
in that case.

## The account portal and the self-service API

**Both work only for a Client that lists `self_service` in its
`allowed_scopes`** (that list is the consent). For any other Client
the portal opens and says that managing the account there is not offered, and no
token carrying the scope can be issued.

```python
from kleora import AccountClient, account_portal_url

# A link a server renders: a pure function, keyword-only, no request.
href = account_portal_url(issuer=ISSUER, client_id=CLIENT_ID, return_to="https://app.example.com/")

# The person's own token — the bearer their request arrived with — not an API key.
with AccountClient(issuer=ISSUER, access_token=bearer) as account:
    profile = account.get_profile()
```

`return_to` must be an absolute `http`/`https` URL with no fragment and no
userinfo (`KleoraError` otherwise); the portal shows it as its "back" link only
when it equals one of the Client's `post_logout_redirect_uris`. Link the portal
as a new tab, never a frame. `AccountClient` has one method per `/account/v1/*`
operation, wrapping `kleora._generated_account`; sensitive ones raise `ApiError`
`…/reauth-required` until `reauthenticate(password)` has run in the last five
minutes.

## Development

```bash
uv sync
uv run pytest            # the unit suite: no server, no network, no waiting
uv run ruff check . && uv run ruff format --check .
uv run mypy              # strict, over the generated trees as well
uv build                 # the sdist and the wheel, into dist/
```

The unit suite mints its own ES256 keys and answers its own JWKS and API
requests through `httpx.MockTransport`, and the caches take an injected clock,
so every TTL and floor is asserted without a `sleep`.

### The generated client

`uv run python scripts/generate_client.py` writes two committed copies of the
OpenAPI documents Kleora serves and two client trees generated from them by
`openapi-python-client`. Never edit any of them by hand.

| Document | Committed copy | Tree |
| --- | --- | --- |
| https://api.kleora.io/api/v1/openapi.json (`MANAGEMENT_OPENAPI_URL` overrides it) | `openapi/management-v1.json` | `src/kleora/_generated/` |
| https://id.kleora.eu/account/v1/openapi.json (`ACCOUNT_OPENAPI_URL` overrides it) | `openapi/account-v1.json` | `src/kleora/_generated_account/` |

The copies are written with their keys sorted, so they change only when the API
does. The unit tests read `openapi/account-v1.json`, so they hold the
hand-written self-service wrappers to the document without needing the network.
The script also applies four declared, counted patches to each tree's
`client.py` — two `mypy` suppressions for an upstream `httpx` signature, and
`repr=False` on the bearer token and on the header dictionary it is copied into,
so no `repr`, f-string or traceback prints a credential.

CI regenerates all four and fails when they differ from what is committed, so a
change to the deployed API shows up as a red check: run the script, adjust
`kleora.management` or `kleora.account` if an operation moved, and commit the
result.

### Contract tests

`tests/test_contract.py` provisions nothing: it proves the wire against a live
Kleora environment — that the JWKS document a real issuer publishes is one
`JWKSCache` can read, that a real `GET /me` is what the environment guard
thinks it is, and that a real `self_service` token works with `AccountClient`.
The tests are marked `live` and deselected by default. **They do not run in
CI**: they need a live environment and credentials this repository does not
hold. Run them yourself with:

```bash
KLEORA_TEST_ISSUER=<a sandbox issuer, e.g. https://acme-sandbox.kleora.eu> \
KLEORA_TEST_API_BASE=<the management API origin> \
KLEORA_TEST_API_KEY=<a kl_test_ key for that environment> \
KLEORA_TEST_SELF_SERVICE_CLIENT_ID=<a Client allowing self_service> \
KLEORA_TEST_SELF_SERVICE_REDIRECT_URI=<one of its redirect URIs> \
KLEORA_TEST_SELF_SERVICE_EMAIL=<a person who can sign in to it> \
KLEORA_TEST_SELF_SERVICE_PASSWORD=<their password> \
uv run pytest -m live
```

`tests/test_contract.py`'s docstring lists the optional variables too. A test
whose variables are absent, or whose issuer is not answering, skips; set
`KLEORA_TEST_REQUIRE_LIVE=1` to make that a failure instead.

### Releasing

Bump `version` in `pyproject.toml` on `main`, then run the **Release** workflow
(`.github/workflows/release.yml`) by hand. A maintainer approves the `pypi`
environment, and the workflow runs the unit suite, builds the sdist and the
wheel from the committed lockfile and publishes them to PyPI by trusted
publishing. No token is stored anywhere. PyPI refuses a version that already
exists.

## Licence

[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0) —
the full, unmodified text ships inside this package, so it travels with
whatever you install. Apache-2.0 rather than a shorter permissive licence
because of the explicit patent grant in §3, which is the term a legal review of
a vendor SDK asks about.

**There is no `NOTICE` file**, here or in any other Kleora package, and that
is deliberate. Apache-2.0 §4(d) turns a `NOTICE` into an obligation that
propagates: every downstream redistributor of a work that has one must
reproduce its contents. Kleora is the sole copyright holder of the code in
these packages, so there is nothing to attribute, and a `NOTICE` would place a
requirement on you in exchange for nothing. Third-party dependencies keep their
own licences and their own notices; this package redistributes none of them —
its manifest names them and your installer fetches them.

Apache-2.0 covers what you install and compile into your own product: the
browser, Node, Nuxt and Python SDKs. It does **not** cover the rest of
Kleora — the hosted service, the API servers, the management console and the
hosted authentication pages are proprietary.
