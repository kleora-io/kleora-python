"""The sandbox guard's one rule.

A host is sandbox when its **first** DNS label ends in `-sandbox`. The table below
is the contract, and it is the whole point of this module: the two TypeScript
packages carry the same hosts and the same verdicts, so a fourth opinion about
what a sandbox host looks like fails here or there rather than in a customer's
deployment.
"""

from __future__ import annotations

import pytest

from kleora import KleoraError, ManagementClient
from kleora._environments import classify_api_key, classify_host, classify_issuer

# Keys minted before the product's rename reached the prefix. The API
# honours none of them, so the SDK must not read one as either environment.
RETIRED_KEY_PREFIXES = ("pa_live_", "pa_test_")
BODY = "4Kd9sQx2abcdefghijklmnopqrstuvwxyz01234567"

# The classification table, one rule for every SDK.
#
# **The same hosts and the same verdicts appear in `@kleora-io/browser`'s
# `test/environment.test.ts` and in `@kleora-io/node`'s `test/package.test.ts`.**
# Three implementations that agree only by coincidence is the defect this table
# exists to prevent, so a row added here belongs in the other two as well.
CLASSIFICATION = [
    ("acme.kleora.eu", "production", "a production issuer"),
    ("acme-sandbox.kleora.eu", "sandbox", "a sandbox issuer"),
    # The shape sandbox issuers used to have. Minted nowhere now,
    # and no edge serves it: reading it as sandbox would only widen the guard.
    ("acme.sandbox.kleora.eu", "production", "the retired two-label shape"),
    # A Kleora under a base domain carrying the suffix mints this *production*
    # issuer; the rule reads the first label only, so the base never reaches it.
    ("acme.corp-sandbox.internal", "production", "a base domain that carries the suffix"),
    # The host that retired the substring test, in its base-domain form: a substring test for
    # `.sandbox.` reads it as sandbox and would pair a `kl_test_` key with it.
    ("acme.corp.sandbox.internal", "production", "a base domain that carries the label"),
    ("my-sandbox-app.kleora.eu", "production", "the word inside a slug, not at its end"),
    ("my-sandbox-app-sandbox.kleora.eu", "sandbox", "that slug's sandbox side"),
    # `sandbox` is a reserved App slug, and the suffix needs a slug before it.
    ("sandbox.kleora.eu", "production", "the bare word"),
    ("-sandbox.kleora.eu", "production", "the suffix with nothing before it"),
    ("id-sandbox.localhost:8100", "sandbox", "development, with a port"),
    ("id.localhost:8100", "production", "development, with a port"),
    ("ACME-SANDBOX.kleora.eu", "sandbox", "DNS labels are case-insensitive"),
    ("app.example.com", "production", "a customer host announces nothing"),
    ("app-sandbox.example.com", "sandbox", "a customer host that does announce it"),
    ("localhost", "production", "a single label that is not a sandbox"),
]


@pytest.mark.parametrize(("host", "kind", "why"), CLASSIFICATION)
def test_classify_host(host: str, kind: str, why: str) -> None:
    assert classify_host(host) == kind, why


@pytest.mark.parametrize(("host", "kind", "why"), CLASSIFICATION)
def test_classify_issuer_agrees_over_a_url(host: str, kind: str, why: str) -> None:
    """The same verdicts through the entry point the SDK actually calls."""

    assert classify_issuer(f"https://{host}") == kind, why
    assert classify_issuer(f"https://{host}/") == kind, why


def test_an_issuer_with_no_host_is_refused() -> None:
    with pytest.raises(KleoraError, match="names no host"):
        classify_issuer("https:///oauth")


@pytest.mark.parametrize(
    ("key", "kind"), [(f"kl_live_{BODY}", "production"), (f"kl_test_{BODY}", "sandbox")]
)
def test_each_key_prefix_reads_as_its_environment(key: str, kind: str) -> None:
    assert classify_api_key(key) == kind


@pytest.mark.parametrize("prefix", RETIRED_KEY_PREFIXES)
def test_a_key_carrying_the_retired_prefix_is_refused(prefix: str) -> None:
    with pytest.raises(KleoraError, match="neither 'kl_live_' nor 'kl_test_'"):
        classify_api_key(prefix + BODY)
    with pytest.raises(KleoraError):
        ManagementClient(api_key=prefix + BODY)
