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
from ...models.account_read import AccountRead
from ...models.problem import Problem
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/account",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AccountRead | Problem | None:
    if response.status_code == 200:
        response_200 = AccountRead.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Problem.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Problem.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

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
) -> Response[AccountRead | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[AccountRead | Problem]:
    """The calling principal's account

     The caller's own Account — resolved from the token, never from a path.

    `@requires` has already made `request.target.account` the principal's own
    Account, so a `console_user` who belongs to two Accounts reads each one's
    own row depending on which `tenant=` context authorised the token: never
    another Account's data, and never a 404.

    One of the two operations a suspended Account still gets, so the console can
    say why everything else is 403.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountRead | Problem]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> AccountRead | Problem | None:
    """The calling principal's account

     The caller's own Account — resolved from the token, never from a path.

    `@requires` has already made `request.target.account` the principal's own
    Account, so a `console_user` who belongs to two Accounts reads each one's
    own row depending on which `tenant=` context authorised the token: never
    another Account's data, and never a 404.

    One of the two operations a suspended Account still gets, so the console can
    say why everything else is 403.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountRead | Problem
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[AccountRead | Problem]:
    """The calling principal's account

     The caller's own Account — resolved from the token, never from a path.

    `@requires` has already made `request.target.account` the principal's own
    Account, so a `console_user` who belongs to two Accounts reads each one's
    own row depending on which `tenant=` context authorised the token: never
    another Account's data, and never a 404.

    One of the two operations a suspended Account still gets, so the console can
    say why everything else is 403.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountRead | Problem]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> AccountRead | Problem | None:
    """The calling principal's account

     The caller's own Account — resolved from the token, never from a path.

    `@requires` has already made `request.target.account` the principal's own
    Account, so a `console_user` who belongs to two Accounts reads each one's
    own row depending on which `tenant=` context authorised the token: never
    another Account's data, and never a 404.

    One of the two operations a suspended Account still gets, so the console can
    say why everything else is 403.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountRead | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
