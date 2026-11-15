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
from ...models.problem import Problem
from ...models.tenant_in import TenantIn
from ...models.tenant_out import TenantOut
from ...types import Response


def _get_kwargs(
    environment_id: str,
    *,
    body: TenantIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/environments/{environment_id}/tenants".format(
            environment_id=quote(str(environment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | TenantOut | None:
    if response.status_code == 201:
        response_201 = TenantOut.from_dict(response.json())

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
) -> Response[Problem | TenantOut]:
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
    body: TenantIn,
) -> Response[Problem | TenantOut]:
    """Create a tenant

     Create a tenant with no members.

    - In `single` tenant mode: `409 tenant-mode-single`.
    - The slugs `default` and `kleora` are reserved: `409 slug-reserved`.
    - A slug another tenant holds: `409 slug-taken`.

    Args:
        environment_id (str):
        body (TenantIn): The body of `POST /api/v1/environments/{environment_id}/tenants`.

            `slug` is required: it is the value of the `tenant` authorization parameter.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | TenantOut]
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
    body: TenantIn,
) -> Problem | TenantOut | None:
    """Create a tenant

     Create a tenant with no members.

    - In `single` tenant mode: `409 tenant-mode-single`.
    - The slugs `default` and `kleora` are reserved: `409 slug-reserved`.
    - A slug another tenant holds: `409 slug-taken`.

    Args:
        environment_id (str):
        body (TenantIn): The body of `POST /api/v1/environments/{environment_id}/tenants`.

            `slug` is required: it is the value of the `tenant` authorization parameter.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | TenantOut
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
    body: TenantIn,
) -> Response[Problem | TenantOut]:
    """Create a tenant

     Create a tenant with no members.

    - In `single` tenant mode: `409 tenant-mode-single`.
    - The slugs `default` and `kleora` are reserved: `409 slug-reserved`.
    - A slug another tenant holds: `409 slug-taken`.

    Args:
        environment_id (str):
        body (TenantIn): The body of `POST /api/v1/environments/{environment_id}/tenants`.

            `slug` is required: it is the value of the `tenant` authorization parameter.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | TenantOut]
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
    body: TenantIn,
) -> Problem | TenantOut | None:
    """Create a tenant

     Create a tenant with no members.

    - In `single` tenant mode: `409 tenant-mode-single`.
    - The slugs `default` and `kleora` are reserved: `409 slug-reserved`.
    - A slug another tenant holds: `409 slug-taken`.

    Args:
        environment_id (str):
        body (TenantIn): The body of `POST /api/v1/environments/{environment_id}/tenants`.

            `slug` is required: it is the value of the `tenant` authorization parameter.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | TenantOut
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
            body=body,
        )
    ).parsed
