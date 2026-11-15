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
from ...models.account_in import AccountIn
from ...models.account_out import AccountOut
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    *,
    body: AccountIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/accounts",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AccountOut | Problem | None:
    if response.status_code == 201:
        response_201 = AccountOut.from_dict(response.json())

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
) -> Response[AccountOut | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AccountIn,
) -> Response[AccountOut | Problem]:
    """Create an account

     Create an additional Account for the person holding a console token.

    Only a console user's token may call this; an API key or a tenant member's token is refused. The
    person's email address must be verified, and the number of Accounts a person may hold is
    limited.

    No `Location` header: `/account` always means the Account the token was issued for, and the new
    Account becomes reachable once the console signs in again for it.

    Args:
        body (AccountIn): The body of `POST /api/v1/accounts`.

            `slug` is optional and derived from `name` when absent or `null`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountOut | Problem]
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
    body: AccountIn,
) -> AccountOut | Problem | None:
    """Create an account

     Create an additional Account for the person holding a console token.

    Only a console user's token may call this; an API key or a tenant member's token is refused. The
    person's email address must be verified, and the number of Accounts a person may hold is
    limited.

    No `Location` header: `/account` always means the Account the token was issued for, and the new
    Account becomes reachable once the console signs in again for it.

    Args:
        body (AccountIn): The body of `POST /api/v1/accounts`.

            `slug` is optional and derived from `name` when absent or `null`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountOut | Problem
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AccountIn,
) -> Response[AccountOut | Problem]:
    """Create an account

     Create an additional Account for the person holding a console token.

    Only a console user's token may call this; an API key or a tenant member's token is refused. The
    person's email address must be verified, and the number of Accounts a person may hold is
    limited.

    No `Location` header: `/account` always means the Account the token was issued for, and the new
    Account becomes reachable once the console signs in again for it.

    Args:
        body (AccountIn): The body of `POST /api/v1/accounts`.

            `slug` is optional and derived from `name` when absent or `null`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountOut | Problem]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AccountIn,
) -> AccountOut | Problem | None:
    """Create an account

     Create an additional Account for the person holding a console token.

    Only a console user's token may call this; an API key or a tenant member's token is refused. The
    person's email address must be verified, and the number of Accounts a person may hold is
    limited.

    No `Location` header: `/account` always means the Account the token was issued for, and the new
    Account becomes reachable once the console signs in again for it.

    Args:
        body (AccountIn): The body of `POST /api/v1/accounts`.

            `slug` is optional and derived from `name` when absent or `null`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountOut | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
