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
from ...models.list_tenant_roles_scope_type_0 import ListTenantRolesScopeType0
from ...models.problem import Problem
from ...models.role_list import RoleList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_id: str,
    *,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    q: None | str | Unset = UNSET,
    scope: ListTenantRolesScopeType0 | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    json_cursor: None | str | Unset
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    json_q: None | str | Unset
    if isinstance(q, Unset):
        json_q = UNSET
    else:
        json_q = q
    params["q"] = json_q

    json_scope: None | str | Unset
    if isinstance(scope, Unset):
        json_scope = UNSET
    elif isinstance(scope, ListTenantRolesScopeType0):
        json_scope = scope.value
    else:
        json_scope = scope
    params["scope"] = json_scope

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tenants/{tenant_id}/roles".format(
            tenant_id=quote(str(tenant_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | RoleList | None:
    if response.status_code == 200:
        response_200 = RoleList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Problem.from_dict(response.json())

        return response_400

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
) -> Response[Problem | RoleList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    q: None | str | Unset = UNSET,
    scope: ListTenantRolesScopeType0 | None | Unset = UNSET,
) -> Response[Problem | RoleList]:
    """Roles assignable in a tenant

     Every role assignable in this tenant: the environment's app-scoped roles and the tenant's
    own.

    This is how a tenant member sees app-scoped roles. `q` is a case-insensitive substring of the
    slug or the name.

    Args:
        tenant_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        q (None | str | Unset):
        scope (ListTenantRolesScopeType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | RoleList]
    """

    kwargs = _get_kwargs(
        tenant_id=tenant_id,
        limit=limit,
        cursor=cursor,
        q=q,
        scope=scope,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    q: None | str | Unset = UNSET,
    scope: ListTenantRolesScopeType0 | None | Unset = UNSET,
) -> Problem | RoleList | None:
    """Roles assignable in a tenant

     Every role assignable in this tenant: the environment's app-scoped roles and the tenant's
    own.

    This is how a tenant member sees app-scoped roles. `q` is a case-insensitive substring of the
    slug or the name.

    Args:
        tenant_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        q (None | str | Unset):
        scope (ListTenantRolesScopeType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | RoleList
    """

    return sync_detailed(
        tenant_id=tenant_id,
        client=client,
        limit=limit,
        cursor=cursor,
        q=q,
        scope=scope,
    ).parsed


async def asyncio_detailed(
    tenant_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    q: None | str | Unset = UNSET,
    scope: ListTenantRolesScopeType0 | None | Unset = UNSET,
) -> Response[Problem | RoleList]:
    """Roles assignable in a tenant

     Every role assignable in this tenant: the environment's app-scoped roles and the tenant's
    own.

    This is how a tenant member sees app-scoped roles. `q` is a case-insensitive substring of the
    slug or the name.

    Args:
        tenant_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        q (None | str | Unset):
        scope (ListTenantRolesScopeType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | RoleList]
    """

    kwargs = _get_kwargs(
        tenant_id=tenant_id,
        limit=limit,
        cursor=cursor,
        q=q,
        scope=scope,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    q: None | str | Unset = UNSET,
    scope: ListTenantRolesScopeType0 | None | Unset = UNSET,
) -> Problem | RoleList | None:
    """Roles assignable in a tenant

     Every role assignable in this tenant: the environment's app-scoped roles and the tenant's
    own.

    This is how a tenant member sees app-scoped roles. `q` is a case-insensitive substring of the
    slug or the name.

    Args:
        tenant_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        q (None | str | Unset):
        scope (ListTenantRolesScopeType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | RoleList
    """

    return (
        await asyncio_detailed(
            tenant_id=tenant_id,
            client=client,
            limit=limit,
            cursor=cursor,
            q=q,
            scope=scope,
        )
    ).parsed
