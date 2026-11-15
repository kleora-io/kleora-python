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
from ...models.role_out import RoleOut
from ...types import Response


def _get_kwargs(
    role_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/roles/{role_id}".format(
            role_id=quote(str(role_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | RoleOut | None:
    if response.status_code == 200:
        response_200 = RoleOut.from_dict(response.json())

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
) -> Response[Problem | RoleOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    role_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Problem | RoleOut]:
    """A role

     One role, at the scope level the role itself decides (rbac.md §API).

    A `tenant_member` reads its own tenant's roles here and nothing else: an
    app-scoped role, another tenant's role and any permission are all rows of
    its environment, so they are 403 `insufficient-scope` rather than 404, and
    `GET T/roles` stays the listing that shows it the app-scoped ones.

    Args:
        role_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | RoleOut]
    """

    kwargs = _get_kwargs(
        role_id=role_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    role_id: str,
    *,
    client: AuthenticatedClient,
) -> Problem | RoleOut | None:
    """A role

     One role, at the scope level the role itself decides (rbac.md §API).

    A `tenant_member` reads its own tenant's roles here and nothing else: an
    app-scoped role, another tenant's role and any permission are all rows of
    its environment, so they are 403 `insufficient-scope` rather than 404, and
    `GET T/roles` stays the listing that shows it the app-scoped ones.

    Args:
        role_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | RoleOut
    """

    return sync_detailed(
        role_id=role_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    role_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Problem | RoleOut]:
    """A role

     One role, at the scope level the role itself decides (rbac.md §API).

    A `tenant_member` reads its own tenant's roles here and nothing else: an
    app-scoped role, another tenant's role and any permission are all rows of
    its environment, so they are 403 `insufficient-scope` rather than 404, and
    `GET T/roles` stays the listing that shows it the app-scoped ones.

    Args:
        role_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | RoleOut]
    """

    kwargs = _get_kwargs(
        role_id=role_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    role_id: str,
    *,
    client: AuthenticatedClient,
) -> Problem | RoleOut | None:
    """A role

     One role, at the scope level the role itself decides (rbac.md §API).

    A `tenant_member` reads its own tenant's roles here and nothing else: an
    app-scoped role, another tenant's role and any permission are all rows of
    its environment, so they are 403 `insufficient-scope` rather than 404, and
    `GET T/roles` stays the listing that shows it the app-scoped ones.

    Args:
        role_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | RoleOut
    """

    return (
        await asyncio_detailed(
            role_id=role_id,
            client=client,
        )
    ).parsed
