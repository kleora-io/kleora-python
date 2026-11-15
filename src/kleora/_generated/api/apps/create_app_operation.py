# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_in import AppIn
from ...models.app_out import AppOut
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    *,
    body: AppIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/apps",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppOut | Problem | None:
    if response.status_code == 201:
        response_201 = AppOut.from_dict(response.json())

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
) -> Response[AppOut | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AppIn,
) -> Response[AppOut | Problem]:
    """Create an app

     Create an App with its production and sandbox environments and their default contents.

    Either everything is created or nothing is. Accepts an `Idempotency-Key` header, which is
    recommended given how much one call provisions.

    Args:
        body (AppIn): The body of `POST /api/v1/apps`.

            `slug` is optional and derived from `name` when absent or `null`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppOut | Problem]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: AppIn,
) -> AppOut | Problem | None:
    """Create an app

     Create an App with its production and sandbox environments and their default contents.

    Either everything is created or nothing is. Accepts an `Idempotency-Key` header, which is
    recommended given how much one call provisions.

    Args:
        body (AppIn): The body of `POST /api/v1/apps`.

            `slug` is optional and derived from `name` when absent or `null`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppOut | Problem
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AppIn,
) -> Response[AppOut | Problem]:
    """Create an app

     Create an App with its production and sandbox environments and their default contents.

    Either everything is created or nothing is. Accepts an `Idempotency-Key` header, which is
    recommended given how much one call provisions.

    Args:
        body (AppIn): The body of `POST /api/v1/apps`.

            `slug` is optional and derived from `name` when absent or `null`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppOut | Problem]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AppIn,
) -> AppOut | Problem | None:
    """Create an app

     Create an App with its production and sandbox environments and their default contents.

    Either everything is created or nothing is. Accepts an `Idempotency-Key` header, which is
    recommended given how much one call provisions.

    Args:
        body (AppIn): The body of `POST /api/v1/apps`.

            `slug` is optional and derived from `name` when absent or `null`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppOut | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
