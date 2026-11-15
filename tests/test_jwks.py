"""The cache's TTL, its refetch floor, its stale window and its lock."""

from __future__ import annotations

import asyncio
import threading
import time

import httpx
import pytest
from conftest import ISSUER, Clock, JWKSEndpoint, SigningKey

from kleora import AsyncJWKSCache, JWKSCache, TokenError


def test_the_first_lookup_fetches_and_the_second_does_not(
    jwks: JWKSEndpoint, clock: Clock, key: SigningKey
) -> None:
    cache = JWKSCache(ISSUER, client=jwks.client(), clock=clock)

    assert cache.get_key(key.kid).key_id == key.kid
    assert cache.get_key(key.kid).key_id == key.kid
    assert jwks.fetches == 1


def test_the_url_is_the_issuer_s_well_known_document(jwks: JWKSEndpoint, clock: Clock) -> None:
    cache = JWKSCache(f"{ISSUER}/", client=jwks.client(), clock=clock)

    assert cache.url == f"{ISSUER}/.well-known/jwks.json"


def test_the_document_is_refetched_once_its_ttl_has_passed(
    jwks: JWKSEndpoint, clock: Clock, key: SigningKey
) -> None:
    cache = JWKSCache(ISSUER, client=jwks.client(), clock=clock)
    cache.get_key(key.kid)

    clock.advance(299)
    cache.get_key(key.kid)
    assert jwks.fetches == 1

    clock.advance(2)
    cache.get_key(key.kid)
    assert jwks.fetches == 2


def test_the_ttl_comes_from_the_document_s_cache_control(
    jwks: JWKSEndpoint, clock: Clock, key: SigningKey
) -> None:
    """A `max-age` shorter than the default shortens the cache, not the other way about."""

    jwks.max_age = 120
    cache = JWKSCache(ISSUER, client=jwks.client(), clock=clock)
    cache.get_key(key.kid)

    clock.advance(119)
    cache.get_key(key.kid)
    assert jwks.fetches == 1

    clock.advance(2)
    cache.get_key(key.kid)
    assert jwks.fetches == 2


@pytest.mark.parametrize(("max_age", "ttl"), [(0, 60), (5, 60), (999_999_999, 86_400)])
def test_an_absurd_max_age_is_clamped_into_a_sane_band(
    max_age: int, ttl: int, jwks: JWKSEndpoint, clock: Clock, key: SigningKey
) -> None:
    """`max-age=0` must not mean "fetch per token", nor "five minutes"."""

    jwks.max_age = max_age
    cache = JWKSCache(ISSUER, client=jwks.client(), clock=clock)
    cache.get_key(key.kid)

    clock.advance(ttl - 1)
    cache.get_key(key.kid)
    assert jwks.fetches == 1

    clock.advance(2)
    cache.get_key(key.kid)
    assert jwks.fetches == 2


def test_a_key_that_is_not_an_es256_signing_key_is_not_in_the_map(
    clock: Clock, key: SigningKey
) -> None:
    """The issuer publishes EC / P-256 / sig / ES256 and nothing else."""

    endpoint = JWKSEndpoint(keys=[key])
    endpoint.body = {
        "keys": [
            {"kty": "oct", "kid": "symmetric", "k": "c2VjcmV0", "alg": "HS256"},
            {**key.public_jwk(), "kid": "encryption", "use": "enc"},
            {**key.public_jwk(), "kid": "wrong-curve", "crv": "P-384"},
            key.public_jwk(),
        ]
    }
    cache = JWKSCache(ISSUER, client=endpoint.client(), clock=clock)

    assert cache.get_key(key.kid).key_id == key.kid
    for rejected in ("symmetric", "encryption", "wrong-curve"):
        with pytest.raises(TokenError):
            cache.get_key(rejected)


def test_a_document_without_cache_control_uses_the_configured_ttl(
    jwks: JWKSEndpoint, clock: Clock, key: SigningKey
) -> None:
    jwks.max_age = None
    cache = JWKSCache(ISSUER, ttl=10, client=jwks.client(), clock=clock)
    cache.get_key(key.kid)

    clock.advance(11)
    cache.get_key(key.kid)

    assert jwks.fetches == 2


def test_a_rotated_key_is_found_with_exactly_one_refetch(
    jwks: JWKSEndpoint, clock: Clock, key: SigningKey, rotated: SigningKey
) -> None:
    """Scenario 6: the `kid` the environment now signs with was not in the cache."""

    cache = JWKSCache(ISSUER, client=jwks.client(), clock=clock)
    cache.get_key(key.kid)
    assert jwks.fetches == 1

    jwks.keys = [rotated, key]
    clock.advance(61)

    assert cache.get_key(rotated.kid).key_id == rotated.kid
    assert jwks.fetches == 2


def test_a_second_unknown_kid_inside_the_floor_is_refused_without_a_fetch(
    jwks: JWKSEndpoint, clock: Clock, key: SigningKey
) -> None:
    cache = JWKSCache(ISSUER, client=jwks.client(), clock=clock)
    cache.get_key(key.kid)

    clock.advance(61)
    with pytest.raises(TokenError) as first:
        cache.get_key("kid-nobody-has")
    assert first.value.code == "unknown_kid"
    assert jwks.fetches == 2

    clock.advance(59)
    with pytest.raises(TokenError):
        cache.get_key("kid-nobody-has")
    assert jwks.fetches == 2


def test_a_failing_endpoint_keeps_serving_the_keys_it_has_until_twice_the_ttl(
    jwks: JWKSEndpoint, clock: Clock, key: SigningKey
) -> None:
    cache = JWKSCache(ISSUER, client=jwks.client(), clock=clock)
    cache.get_key(key.kid)
    jwks.status = 503

    clock.advance(301)
    assert cache.get_key(key.kid).key_id == key.kid

    clock.advance(298)
    assert cache.get_key(key.kid).key_id == key.kid


def test_past_twice_the_ttl_a_stale_cache_fails_closed(
    jwks: JWKSEndpoint, clock: Clock, key: SigningKey
) -> None:
    """And fails closed as an *outage*, which is not the token's fault.

    The `kid` asked for is the one the issuer signs with; the only thing wrong is
    that nothing this cache may trust has been fetched for twice the TTL. A
    middleware answers `issuer_unavailable` with a retryable 503; reporting
    `unknown_kid` here would send every caller back to re-authenticate against
    an issuer that is already down.
    """

    cache = JWKSCache(ISSUER, client=jwks.client(), clock=clock)
    cache.get_key(key.kid)
    jwks.status = 503

    clock.advance(601)
    with pytest.raises(TokenError) as raised:
        cache.get_key(key.kid)

    assert raised.value.code == "issuer_unavailable"
    assert "503" in str(raised.value)


def test_inside_the_stale_window_an_unknown_kid_is_still_the_caller_s_fault(
    jwks: JWKSEndpoint, clock: Clock, key: SigningKey
) -> None:
    """The discriminator is the cached set, not the last fetch's outcome.

    A failing endpoint and a `kid` the document never listed are two facts. While
    the document is still usable its contents are the issuer's own answer, so the
    token is the thing that is wrong — `unknown_kid`, and a 401.
    """

    cache = JWKSCache(ISSUER, client=jwks.client(), clock=clock)
    cache.get_key(key.kid)
    jwks.status = 503

    clock.advance(301)
    with pytest.raises(TokenError) as raised:
        cache.get_key("kid-nobody-has")

    assert raised.value.code == "unknown_kid"


def test_an_endpoint_that_never_answers_fails_closed(clock: Clock) -> None:
    """A refused connection with nothing cached is the outage, not a bad token."""

    def refuse(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("nothing is listening", request=request)

    cache = JWKSCache(
        ISSUER, client=httpx.Client(transport=httpx.MockTransport(refuse)), clock=clock
    )

    with pytest.raises(TokenError) as raised:
        cache.get_key("kid-active")

    assert raised.value.code == "issuer_unavailable"
    assert "nothing is listening" in str(raised.value)


def test_a_non_2xx_with_nothing_cached_is_an_outage(
    jwks: JWKSEndpoint, clock: Clock, key: SigningKey
) -> None:
    jwks.status = 503
    cache = JWKSCache(ISSUER, client=jwks.client(), clock=clock)

    with pytest.raises(TokenError) as raised:
        cache.get_key(key.kid)

    assert raised.value.code == "issuer_unavailable"
    assert cache.url in str(raised.value)


def test_a_body_that_is_not_a_jwk_set_with_nothing_cached_is_an_outage(
    jwks: JWKSEndpoint, clock: Clock, key: SigningKey
) -> None:
    jwks.body = {"not": "a key set"}
    cache = JWKSCache(ISSUER, client=jwks.client(), clock=clock)

    with pytest.raises(TokenError) as raised:
        cache.get_key(key.kid)

    assert raised.value.code == "issuer_unavailable"


def test_a_set_with_no_usable_key_is_an_outage_and_keeps_the_keys_held(
    jwks: JWKSEndpoint, clock: Clock, key: SigningKey
) -> None:
    """An issuer that publishes nothing this verifier can use is unavailable.

    `@kleora-io/node` calls the same case "published no usable key" and it
    matters twice over: the empty document must not replace a set that still
    verifies tokens, and once the stale window closes the failure is the
    issuer's, not the token's.
    """

    cache = JWKSCache(ISSUER, client=jwks.client(), clock=clock)
    cache.get_key(key.kid)

    jwks.body = {"keys": []}
    clock.advance(301)
    assert cache.get_key(key.kid).key_id == key.kid
    assert jwks.fetches == 2

    clock.advance(300)
    with pytest.raises(TokenError) as raised:
        cache.get_key(key.kid)

    assert raised.value.code == "issuer_unavailable"
    assert "no usable key" in str(raised.value)


def test_a_response_that_is_not_a_jwk_set_does_not_replace_the_keys(
    jwks: JWKSEndpoint, clock: Clock, key: SigningKey
) -> None:
    cache = JWKSCache(ISSUER, client=jwks.client(), clock=clock)
    cache.get_key(key.kid)

    jwks.body = {"not": "a key set"}
    clock.advance(301)

    assert cache.get_key(key.kid).key_id == key.kid
    assert jwks.fetches == 2


def test_a_member_that_is_not_a_key_is_skipped_and_the_rest_survive(
    clock: Clock, key: SigningKey
) -> None:
    endpoint = JWKSEndpoint(keys=[key])
    endpoint.body = {"keys": [{"kty": "EC", "kid": "broken"}, "not-an-object", key.public_jwk()]}
    cache = JWKSCache(ISSUER, client=endpoint.client(), clock=clock)

    assert cache.get_key(key.kid).key_id == key.kid
    with pytest.raises(TokenError):
        cache.get_key("broken")


def test_concurrent_lookups_make_one_request_between_them(
    jwks: JWKSEndpoint, key: SigningKey
) -> None:
    """The lock covers the fetch, not only the decision to fetch.

    Sixteen threads reach an empty cache at once against an endpoint that sleeps
    long enough for every one of them to arrive. A cache that only guarded its
    dictionary would answer with sixteen requests to the issuer.
    """

    started = threading.Barrier(16)
    jwks.before = lambda: time.sleep(0.05)
    cache = JWKSCache(ISSUER, client=jwks.client(), clock=time.monotonic)
    failures: list[BaseException] = []

    def lookup() -> None:
        try:
            started.wait(timeout=5)
            assert cache.get_key(key.kid).key_id == key.kid
        except BaseException as error:  # noqa: BLE001 - reported below, not swallowed
            failures.append(error)

    threads = [threading.Thread(target=lookup) for _ in range(16)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join(timeout=10)

    assert not failures
    assert jwks.fetches == 1


def test_the_async_cache_follows_the_same_rules(
    jwks: JWKSEndpoint, clock: Clock, key: SigningKey, rotated: SigningKey
) -> None:
    async def run() -> None:
        async with AsyncJWKSCache(ISSUER, client=jwks.async_client(), clock=clock) as cache:
            assert (await cache.get_key(key.kid)).key_id == key.kid
            assert (await cache.get_key(key.kid)).key_id == key.kid
            assert jwks.fetches == 1

            clock.advance(61)
            with pytest.raises(TokenError):
                await cache.get_key(rotated.kid)
            assert jwks.fetches == 2

            clock.advance(1)
            with pytest.raises(TokenError):
                await cache.get_key(rotated.kid)
            assert jwks.fetches == 2

    asyncio.run(run())


def test_the_async_cache_reports_an_outage_with_the_same_code(
    jwks: JWKSEndpoint, clock: Clock, key: SigningKey
) -> None:
    """Both caches run one algorithm, so both split the two failures the same way."""

    async def run() -> None:
        async with AsyncJWKSCache(ISSUER, client=jwks.async_client(), clock=clock) as cache:
            assert (await cache.get_key(key.kid)).key_id == key.kid
            jwks.status = 503

            clock.advance(301)
            with pytest.raises(TokenError) as stale:
                await cache.get_key("kid-nobody-has")
            assert stale.value.code == "unknown_kid"

            clock.advance(300)
            with pytest.raises(TokenError) as gone:
                await cache.get_key(key.kid)
            assert gone.value.code == "issuer_unavailable"

    asyncio.run(run())


def test_concurrent_async_lookups_make_one_request_between_them(
    jwks: JWKSEndpoint, key: SigningKey
) -> None:
    async def run() -> None:
        async with AsyncJWKSCache(ISSUER, client=jwks.async_client()) as cache:
            found = await asyncio.gather(*(cache.get_key(key.kid) for _ in range(16)))
        assert all(jwk.key_id == key.kid for jwk in found)

    asyncio.run(run())

    assert jwks.fetches == 1
