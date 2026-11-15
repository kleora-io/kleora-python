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

     Create an API key. Its prefix follows the environment's kind.

    The `201` carries the full key, once, and is never cached. Repeating the request with the same
    `Idempotency-Key` returns the same response, key included; without one, a second request creates
    a second key.

    - A scope that is not allowed: `422 invalid-scope`, naming each.
    - An environment that already has 100 keys that are not revoked: `422 limit-exceeded`.
    - An `expires_at` less than 60 seconds ahead: `422 validation-error` on that field.

    Args:
        environment_id (str):
        body (ApiKeyIn): The body of `POST /api/v1/environments/{environment_id}/api-keys`.

            `prefix`, `key`, `key_hash`, `status`, `environment_id` and `created_by` are refused as
            unknown
            fields. The prefix follows the environment's kind, so a `kl_test_` key can never be used
            in
            production. A scope that is not allowed for an API key is `422 invalid-scope`.

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

     Create an API key. Its prefix follows the environment's kind.

    The `201` carries the full key, once, and is never cached. Repeating the request with the same
    `Idempotency-Key` returns the same response, key included; without one, a second request creates
    a second key.

    - A scope that is not allowed: `422 invalid-scope`, naming each.
    - An environment that already has 100 keys that are not revoked: `422 limit-exceeded`.
    - An `expires_at` less than 60 seconds ahead: `422 validation-error` on that field.

    Args:
        environment_id (str):
        body (ApiKeyIn): The body of `POST /api/v1/environments/{environment_id}/api-keys`.

            `prefix`, `key`, `key_hash`, `status`, `environment_id` and `created_by` are refused as
            unknown
            fields. The prefix follows the environment's kind, so a `kl_test_` key can never be used
            in
            production. A scope that is not allowed for an API key is `422 invalid-scope`.

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

     Create an API key. Its prefix follows the environment's kind.

    The `201` carries the full key, once, and is never cached. Repeating the request with the same
    `Idempotency-Key` returns the same response, key included; without one, a second request creates
    a second key.

    - A scope that is not allowed: `422 invalid-scope`, naming each.
    - An environment that already has 100 keys that are not revoked: `422 limit-exceeded`.
    - An `expires_at` less than 60 seconds ahead: `422 validation-error` on that field.

    Args:
        environment_id (str):
        body (ApiKeyIn): The body of `POST /api/v1/environments/{environment_id}/api-keys`.

            `prefix`, `key`, `key_hash`, `status`, `environment_id` and `created_by` are refused as
            unknown
            fields. The prefix follows the environment's kind, so a `kl_test_` key can never be used
            in
            production. A scope that is not allowed for an API key is `422 invalid-scope`.

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

     Create an API key. Its prefix follows the environment's kind.

    The `201` carries the full key, once, and is never cached. Repeating the request with the same
    `Idempotency-Key` returns the same response, key included; without one, a second request creates
    a second key.

    - A scope that is not allowed: `422 invalid-scope`, naming each.
    - An environment that already has 100 keys that are not revoked: `422 limit-exceeded`.
    - An `expires_at` less than 60 seconds ahead: `422 validation-error` on that field.

    Args:
        environment_id (str):
        body (ApiKeyIn): The body of `POST /api/v1/environments/{environment_id}/api-keys`.

            `prefix`, `key`, `key_hash`, `status`, `environment_id` and `created_by` are refused as
            unknown
            fields. The prefix follows the environment's kind, so a `kl_test_` key can never be used
            in
            production. A scope that is not allowed for an API key is `422 invalid-scope`.

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
