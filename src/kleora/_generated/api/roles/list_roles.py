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
from ...models.role_list import RoleList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    environment_id: str,
    *,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    q: None | str | Unset = UNSET,
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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/environments/{environment_id}/roles".format(
            environment_id=quote(str(environment_id), safe=""),
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
    environment_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    q: None | str | Unset = UNSET,
) -> Response[Problem | RoleList]:
    r"""List app-scoped roles

     The environment's **app-scoped** roles by slug (rbac.md §API).

    Tenant-scoped roles are listed under the tenant that defines them, at
    `GET T/roles`, because that is the only place they are assignable.

    `q` is a case-insensitive substring of the slug or the name
    (management-api.md §Conventions \"Search\"; Q3-59).

    Args:
        environment_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        q (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | RoleList]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        limit=limit,
        cursor=cursor,
        q=q,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    q: None | str | Unset = UNSET,
) -> Problem | RoleList | None:
    r"""List app-scoped roles

     The environment's **app-scoped** roles by slug (rbac.md §API).

    Tenant-scoped roles are listed under the tenant that defines them, at
    `GET T/roles`, because that is the only place they are assignable.

    `q` is a case-insensitive substring of the slug or the name
    (management-api.md §Conventions \"Search\"; Q3-59).

    Args:
        environment_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        q (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | RoleList
    """

    return sync_detailed(
        environment_id=environment_id,
        client=client,
        limit=limit,
        cursor=cursor,
        q=q,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    q: None | str | Unset = UNSET,
) -> Response[Problem | RoleList]:
    r"""List app-scoped roles

     The environment's **app-scoped** roles by slug (rbac.md §API).

    Tenant-scoped roles are listed under the tenant that defines them, at
    `GET T/roles`, because that is the only place they are assignable.

    `q` is a case-insensitive substring of the slug or the name
    (management-api.md §Conventions \"Search\"; Q3-59).

    Args:
        environment_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        q (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | RoleList]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        limit=limit,
        cursor=cursor,
        q=q,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    q: None | str | Unset = UNSET,
) -> Problem | RoleList | None:
    r"""List app-scoped roles

     The environment's **app-scoped** roles by slug (rbac.md §API).

    Tenant-scoped roles are listed under the tenant that defines them, at
    `GET T/roles`, because that is the only place they are assignable.

    `q` is a case-insensitive substring of the slug or the name
    (management-api.md §Conventions \"Search\"; Q3-59).

    Args:
        environment_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        q (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | RoleList
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
            limit=limit,
            cursor=cursor,
            q=q,
        )
    ).parsed
