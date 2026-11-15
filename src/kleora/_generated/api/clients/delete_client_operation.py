# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    environment_id: str,
    client_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/environments/{environment_id}/clients/{client_id}".format(
            environment_id=quote(str(environment_id), safe=""),
            client_id=quote(str(client_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Problem | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    environment_id: str,
    client_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | Problem]:
    """Delete a client

     Delete an OAuth client, with its authorization codes, pending authorization requests and
    refresh tokens.

    Browser sessions are not affected, since they are shared by the environment's clients; tokens
    issued through this client can no longer be refreshed. `409 client-default` for the
    environment's default client.

    Args:
        environment_id (str):
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        client_id=client_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    client_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | Problem | None:
    """Delete a client

     Delete an OAuth client, with its authorization codes, pending authorization requests and
    refresh tokens.

    Browser sessions are not affected, since they are shared by the environment's clients; tokens
    issued through this client can no longer be refreshed. `409 client-default` for the
    environment's default client.

    Args:
        environment_id (str):
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Problem
    """

    return sync_detailed(
        environment_id=environment_id,
        client_id=client_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    client_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | Problem]:
    """Delete a client

     Delete an OAuth client, with its authorization codes, pending authorization requests and
    refresh tokens.

    Browser sessions are not affected, since they are shared by the environment's clients; tokens
    issued through this client can no longer be refreshed. `409 client-default` for the
    environment's default client.

    Args:
        environment_id (str):
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        client_id=client_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    client_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | Problem | None:
    """Delete a client

     Delete an OAuth client, with its authorization codes, pending authorization requests and
    refresh tokens.

    Browser sessions are not affected, since they are shared by the environment's clients; tokens
    issued through this client can no longer be refreshed. `409 client-default` for the
    environment's default client.

    Args:
        environment_id (str):
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Problem
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client_id=client_id,
            client=client,
        )
    ).parsed
