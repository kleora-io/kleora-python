# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed self-service API document
# (https://id.kleora.eu/account/v1/openapi.json). `kleora.account` wraps this tree; nothing outside the
# package imports it.
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.flow_problem import FlowProblem
from ...models.portal_out import PortalOut
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/account/v1/portal",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FlowProblem | PortalOut | None:
    if response.status_code == 200:
        response_200 = PortalOut.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = FlowProblem.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FlowProblem.from_dict(response.json())

        return response_403

    if response.status_code == 429:
        response_429 = FlowProblem.from_dict(response.json())

        return response_429

    if response.status_code == 503:
        response_503 = FlowProblem.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FlowProblem | PortalOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[FlowProblem | PortalOut]:
    """Where the hosted account portal is, and which sections it offers

     The hosted account portal's entry URL, and the sections this environment offers.

    `danger` (account deletion) is listed only when the environment allows people to delete their
    own account. The list is for rendering links; the `/deletion` operations answer `404` whenever
    deletion is not offered, whatever a client shows.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlowProblem | PortalOut]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> FlowProblem | PortalOut | None:
    """Where the hosted account portal is, and which sections it offers

     The hosted account portal's entry URL, and the sections this environment offers.

    `danger` (account deletion) is listed only when the environment allows people to delete their
    own account. The list is for rendering links; the `/deletion` operations answer `404` whenever
    deletion is not offered, whatever a client shows.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlowProblem | PortalOut
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[FlowProblem | PortalOut]:
    """Where the hosted account portal is, and which sections it offers

     The hosted account portal's entry URL, and the sections this environment offers.

    `danger` (account deletion) is listed only when the environment allows people to delete their
    own account. The list is for rendering links; the `/deletion` operations answer `404` whenever
    deletion is not offered, whatever a client shows.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlowProblem | PortalOut]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> FlowProblem | PortalOut | None:
    """Where the hosted account portal is, and which sections it offers

     The hosted account portal's entry URL, and the sections this environment offers.

    `danger` (account deletion) is listed only when the environment allows people to delete their
    own account. The list is for rendering links; the `/deletion` operations answer `404` whenever
    deletion is not offered, whatever a client shows.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlowProblem | PortalOut
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
