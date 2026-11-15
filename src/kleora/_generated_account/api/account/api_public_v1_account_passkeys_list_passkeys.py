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
from ...models.passkeys_out import PasskeysOut
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/account/v1/passkeys",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FlowProblem | PasskeysOut | None:
    if response.status_code == 200:
        response_200 = PasskeysOut.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = FlowProblem.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FlowProblem.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = FlowProblem.from_dict(response.json())

        return response_404

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
) -> Response[FlowProblem | PasskeysOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[FlowProblem | PasskeysOut]:
    """The signed-in person's own passkeys, and where one can be added

     The credentials, and the hosted URL that can register another.

    `fail_open` like every `GET` on the catch-all row: making a person's security
    list unreachable because Redis is unreachable is a worse outage than serving
    it unbounded for a few minutes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlowProblem | PasskeysOut]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> FlowProblem | PasskeysOut | None:
    """The signed-in person's own passkeys, and where one can be added

     The credentials, and the hosted URL that can register another.

    `fail_open` like every `GET` on the catch-all row: making a person's security
    list unreachable because Redis is unreachable is a worse outage than serving
    it unbounded for a few minutes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlowProblem | PasskeysOut
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[FlowProblem | PasskeysOut]:
    """The signed-in person's own passkeys, and where one can be added

     The credentials, and the hosted URL that can register another.

    `fail_open` like every `GET` on the catch-all row: making a person's security
    list unreachable because Redis is unreachable is a worse outage than serving
    it unbounded for a few minutes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlowProblem | PasskeysOut]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> FlowProblem | PasskeysOut | None:
    """The signed-in person's own passkeys, and where one can be added

     The credentials, and the hosted URL that can register another.

    `fail_open` like every `GET` on the catch-all row: making a person's security
    list unreachable because Redis is unreachable is a worse outage than serving
    it unbounded for a few minutes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlowProblem | PasskeysOut
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
