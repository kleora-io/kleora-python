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
from ...models.permission_out import PermissionOut
from ...models.permission_patch import PermissionPatch
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    permission_id: str,
    *,
    body: PermissionPatch,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/permissions/{permission_id}".format(
            permission_id=quote(str(permission_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PermissionOut | Problem | None:
    if response.status_code == 200:
        response_200 = PermissionOut.from_dict(response.json())

        return response_200

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
    permission_id: str,
    *,
    client: AuthenticatedClient,
    body: PermissionPatch,
) -> Response[PermissionOut | Problem]:
    """Describe a permission

     Update a permission's description. This is also the one change allowed on a reserved
    permission.

    Args:
        permission_id (str):
        body (PermissionPatch): The body of `PATCH /api/v1/permissions/{permission_id}`: the
            description, and nothing else.

            `name` cannot be changed: sending it is refused as immutable.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PermissionOut | Problem]
    """

    kwargs = _get_kwargs(
        permission_id=permission_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    permission_id: str,
    *,
    client: AuthenticatedClient,
    body: PermissionPatch,
) -> PermissionOut | Problem | None:
    """Describe a permission

     Update a permission's description. This is also the one change allowed on a reserved
    permission.

    Args:
        permission_id (str):
        body (PermissionPatch): The body of `PATCH /api/v1/permissions/{permission_id}`: the
            description, and nothing else.

            `name` cannot be changed: sending it is refused as immutable.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PermissionOut | Problem
    """

    return sync_detailed(
        permission_id=permission_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    permission_id: str,
    *,
    client: AuthenticatedClient,
    body: PermissionPatch,
) -> Response[PermissionOut | Problem]:
    """Describe a permission

     Update a permission's description. This is also the one change allowed on a reserved
    permission.

    Args:
        permission_id (str):
        body (PermissionPatch): The body of `PATCH /api/v1/permissions/{permission_id}`: the
            description, and nothing else.

            `name` cannot be changed: sending it is refused as immutable.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PermissionOut | Problem]
    """

    kwargs = _get_kwargs(
        permission_id=permission_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    permission_id: str,
    *,
    client: AuthenticatedClient,
    body: PermissionPatch,
) -> PermissionOut | Problem | None:
    """Describe a permission

     Update a permission's description. This is also the one change allowed on a reserved
    permission.

    Args:
        permission_id (str):
        body (PermissionPatch): The body of `PATCH /api/v1/permissions/{permission_id}`: the
            description, and nothing else.

            `name` cannot be changed: sending it is refused as immutable.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PermissionOut | Problem
    """

    return (
        await asyncio_detailed(
            permission_id=permission_id,
            client=client,
            body=body,
        )
    ).parsed
