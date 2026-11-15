# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_key_created import ApiKeyCreated
from ...models.api_key_in import ApiKeyIn
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    environment_id: str,
    *,
    body: ApiKeyIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/environments/{environment_id}/api-keys".format(
            environment_id=quote(str(environment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiKeyCreated | Problem | None:
    if response.status_code == 201:
        response_201 = ApiKeyCreated.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = Problem.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = Problem.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = Problem.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = Problem.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = Problem.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiKeyCreated | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    body: ApiKeyIn,
) -> Response[ApiKeyCreated | Problem]:
    """Create an API key

     A key for this environment, with a prefix that follows the environment.

    The 201 carries the full key, once, under the shown-once rules — `no_store`
    on the response and nothing that could show it again. A replay under the
    same `Idempotency-Key` returns the stored body including the key, because
    that is the same response and the store holds it under the same guarantees;
    a second `POST` without one mints a second key, which is what a second
    creation means.

    Three refusals are the resource's rather than the schema's: a scope outside
    the allowed set is 422 `invalid-scope` naming every offending entry, an
    environment already holding 100 non-revoked keys is 422 `limit-exceeded`,
    and an `expires_at` less than 60 s ahead is 422 `validation-error` on that
    field.

    Args:
        environment_id (str):
        body (ApiKeyIn): `POST /api/v1/environments/{environment_id}/api-keys`.

            `extra="forbid"` is the whole of the "not an input field" rule: `prefix`,
            `key`, `key_hash`, `status`, `environment_id` and `created_by` are 422 as
            unknown fields. The prefix in particular is never a caller's choice — it
            follows the environment's kind, which is what makes a `kl_test_` key
            structurally unable to reach production (api-keys.md §Format).

            The scope rules are not here. They are the resource's — the allowed set is
            the reserved permission table minus the account-level half — and they
            answer 422 `invalid-scope` rather than `validation-error`, which is a slug
            a schema cannot produce.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKeyCreated | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    body: ApiKeyIn,
) -> ApiKeyCreated | Problem | None:
    """Create an API key

     A key for this environment, with a prefix that follows the environment.

    The 201 carries the full key, once, under the shown-once rules — `no_store`
    on the response and nothing that could show it again. A replay under the
    same `Idempotency-Key` returns the stored body including the key, because
    that is the same response and the store holds it under the same guarantees;
    a second `POST` without one mints a second key, which is what a second
    creation means.

    Three refusals are the resource's rather than the schema's: a scope outside
    the allowed set is 422 `invalid-scope` naming every offending entry, an
    environment already holding 100 non-revoked keys is 422 `limit-exceeded`,
    and an `expires_at` less than 60 s ahead is 422 `validation-error` on that
    field.

    Args:
        environment_id (str):
        body (ApiKeyIn): `POST /api/v1/environments/{environment_id}/api-keys`.

            `extra="forbid"` is the whole of the "not an input field" rule: `prefix`,
            `key`, `key_hash`, `status`, `environment_id` and `created_by` are 422 as
            unknown fields. The prefix in particular is never a caller's choice — it
            follows the environment's kind, which is what makes a `kl_test_` key
            structurally unable to reach production (api-keys.md §Format).

            The scope rules are not here. They are the resource's — the allowed set is
            the reserved permission table minus the account-level half — and they
            answer 422 `invalid-scope` rather than `validation-error`, which is a slug
            a schema cannot produce.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKeyCreated | Problem
    """

    return sync_detailed(
        environment_id=environment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    body: ApiKeyIn,
) -> Response[ApiKeyCreated | Problem]:
    """Create an API key

     A key for this environment, with a prefix that follows the environment.

    The 201 carries the full key, once, under the shown-once rules — `no_store`
    on the response and nothing that could show it again. A replay under the
    same `Idempotency-Key` returns the stored body including the key, because
    that is the same response and the store holds it under the same guarantees;
    a second `POST` without one mints a second key, which is what a second
    creation means.

    Three refusals are the resource's rather than the schema's: a scope outside
    the allowed set is 422 `invalid-scope` naming every offending entry, an
    environment already holding 100 non-revoked keys is 422 `limit-exceeded`,
    and an `expires_at` less than 60 s ahead is 422 `validation-error` on that
    field.

    Args:
        environment_id (str):
        body (ApiKeyIn): `POST /api/v1/environments/{environment_id}/api-keys`.

            `extra="forbid"` is the whole of the "not an input field" rule: `prefix`,
            `key`, `key_hash`, `status`, `environment_id` and `created_by` are 422 as
            unknown fields. The prefix in particular is never a caller's choice — it
            follows the environment's kind, which is what makes a `kl_test_` key
            structurally unable to reach production (api-keys.md §Format).

            The scope rules are not here. They are the resource's — the allowed set is
            the reserved permission table minus the account-level half — and they
            answer 422 `invalid-scope` rather than `validation-error`, which is a slug
            a schema cannot produce.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKeyCreated | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    body: ApiKeyIn,
) -> ApiKeyCreated | Problem | None:
    """Create an API key

     A key for this environment, with a prefix that follows the environment.

    The 201 carries the full key, once, under the shown-once rules — `no_store`
    on the response and nothing that could show it again. A replay under the
    same `Idempotency-Key` returns the stored body including the key, because
    that is the same response and the store holds it under the same guarantees;
    a second `POST` without one mints a second key, which is what a second
    creation means.

    Three refusals are the resource's rather than the schema's: a scope outside
    the allowed set is 422 `invalid-scope` naming every offending entry, an
    environment already holding 100 non-revoked keys is 422 `limit-exceeded`,
    and an `expires_at` less than 60 s ahead is 422 `validation-error` on that
    field.

    Args:
        environment_id (str):
        body (ApiKeyIn): `POST /api/v1/environments/{environment_id}/api-keys`.

            `extra="forbid"` is the whole of the "not an input field" rule: `prefix`,
            `key`, `key_hash`, `status`, `environment_id` and `created_by` are 422 as
            unknown fields. The prefix in particular is never a caller's choice — it
            follows the environment's kind, which is what makes a `kl_test_` key
            structurally unable to reach production (api-keys.md §Format).

            The scope rules are not here. They are the resource's — the allowed set is
            the reserved permission table minus the account-level half — and they
            answer 422 `invalid-scope` rather than `validation-error`, which is a slug
            a schema cannot produce.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKeyCreated | Problem
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
            body=body,
        )
    ).parsed
