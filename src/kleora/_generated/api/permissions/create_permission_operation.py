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
from ...models.permission_in import PermissionIn
from ...models.permission_out import PermissionOut
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    environment_id: str,
    *,
    body: PermissionIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/environments/{environment_id}/permissions".format(
            environment_id=quote(str(environment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PermissionOut | Problem | None:
    if response.status_code == 201:
        response_201 = PermissionOut.from_dict(response.json())

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
) -> Response[PermissionOut | Problem]:
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
    body: PermissionIn,
) -> Response[PermissionOut | Problem]:
    """Create a permission

     Create a permission.

    A name whose resource part is one of the reserved resources (for example `users:export`) is `422
    reserved-permission`.

    Args:
        environment_id (str):
        body (PermissionIn): The body of `POST /api/v1/environments/{environment_id}/permissions`.

            `is_system` is not an input field. A name in the reserved namespace is `422
            reserved-permission`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PermissionOut | Problem]
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
    body: PermissionIn,
) -> PermissionOut | Problem | None:
    """Create a permission

     Create a permission.

    A name whose resource part is one of the reserved resources (for example `users:export`) is `422
    reserved-permission`.

    Args:
        environment_id (str):
        body (PermissionIn): The body of `POST /api/v1/environments/{environment_id}/permissions`.

            `is_system` is not an input field. A name in the reserved namespace is `422
            reserved-permission`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PermissionOut | Problem
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
    body: PermissionIn,
) -> Response[PermissionOut | Problem]:
    """Create a permission

     Create a permission.

    A name whose resource part is one of the reserved resources (for example `users:export`) is `422
    reserved-permission`.

    Args:
        environment_id (str):
        body (PermissionIn): The body of `POST /api/v1/environments/{environment_id}/permissions`.

            `is_system` is not an input field. A name in the reserved namespace is `422
            reserved-permission`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PermissionOut | Problem]
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
    body: PermissionIn,
) -> PermissionOut | Problem | None:
    """Create a permission

     Create a permission.

    A name whose resource part is one of the reserved resources (for example `users:export`) is `422
    reserved-permission`.

    Args:
        environment_id (str):
        body (PermissionIn): The body of `POST /api/v1/environments/{environment_id}/permissions`.

            `is_system` is not an input field. A name in the reserved namespace is `422
            reserved-permission`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PermissionOut | Problem
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
            body=body,
        )
    ).parsed
