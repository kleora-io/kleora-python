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
from ...models.list_tenants_status_type_0 import ListTenantsStatusType0
from ...models.problem import Problem
from ...models.tenant_list import TenantList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    environment_id: str,
    *,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    q: None | str | Unset = UNSET,
    status: ListTenantsStatusType0 | None | Unset = UNSET,
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

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    elif isinstance(status, ListTenantsStatusType0):
        json_status = status.value
    else:
        json_status = status
    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/environments/{environment_id}/tenants".format(
            environment_id=quote(str(environment_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | TenantList | None:
    if response.status_code == 200:
        response_200 = TenantList.from_dict(response.json())

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
) -> Response[Problem | TenantList]:
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
    status: ListTenantsStatusType0 | None | Unset = UNSET,
) -> Response[Problem | TenantList]:
    r"""List tenants

     The environment's tenants, newest first, filtered by `q` and `status`.

    In `single` mode the default tenant is **excluded**: it is hidden there, it
    is never a selection step, and a console page listing it would offer a row
    the product says does not exist (tenants-and-membership.md §\"Tenant modes\").
    That exclusion is not a caller's filter and so is not in the cursor's
    fingerprint — the environment already is, through the resolved path.

    `q` is a case-insensitive substring of the name or the slug
    (management-api.md §Conventions \"Search\"; Q3-59). Both filters are named
    to `paginate` as well as applied, so a cursor issued for `?status=suspended`
    cannot be presented against the unfiltered listing and seek at a position
    that means something else there.

    Args:
        environment_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        q (None | str | Unset):
        status (ListTenantsStatusType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | TenantList]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        limit=limit,
        cursor=cursor,
        q=q,
        status=status,
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
    status: ListTenantsStatusType0 | None | Unset = UNSET,
) -> Problem | TenantList | None:
    r"""List tenants

     The environment's tenants, newest first, filtered by `q` and `status`.

    In `single` mode the default tenant is **excluded**: it is hidden there, it
    is never a selection step, and a console page listing it would offer a row
    the product says does not exist (tenants-and-membership.md §\"Tenant modes\").
    That exclusion is not a caller's filter and so is not in the cursor's
    fingerprint — the environment already is, through the resolved path.

    `q` is a case-insensitive substring of the name or the slug
    (management-api.md §Conventions \"Search\"; Q3-59). Both filters are named
    to `paginate` as well as applied, so a cursor issued for `?status=suspended`
    cannot be presented against the unfiltered listing and seek at a position
    that means something else there.

    Args:
        environment_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        q (None | str | Unset):
        status (ListTenantsStatusType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | TenantList
    """

    return sync_detailed(
        environment_id=environment_id,
        client=client,
        limit=limit,
        cursor=cursor,
        q=q,
        status=status,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    q: None | str | Unset = UNSET,
    status: ListTenantsStatusType0 | None | Unset = UNSET,
) -> Response[Problem | TenantList]:
    r"""List tenants

     The environment's tenants, newest first, filtered by `q` and `status`.

    In `single` mode the default tenant is **excluded**: it is hidden there, it
    is never a selection step, and a console page listing it would offer a row
    the product says does not exist (tenants-and-membership.md §\"Tenant modes\").
    That exclusion is not a caller's filter and so is not in the cursor's
    fingerprint — the environment already is, through the resolved path.

    `q` is a case-insensitive substring of the name or the slug
    (management-api.md §Conventions \"Search\"; Q3-59). Both filters are named
    to `paginate` as well as applied, so a cursor issued for `?status=suspended`
    cannot be presented against the unfiltered listing and seek at a position
    that means something else there.

    Args:
        environment_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        q (None | str | Unset):
        status (ListTenantsStatusType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | TenantList]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        limit=limit,
        cursor=cursor,
        q=q,
        status=status,
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
    status: ListTenantsStatusType0 | None | Unset = UNSET,
) -> Problem | TenantList | None:
    r"""List tenants

     The environment's tenants, newest first, filtered by `q` and `status`.

    In `single` mode the default tenant is **excluded**: it is hidden there, it
    is never a selection step, and a console page listing it would offer a row
    the product says does not exist (tenants-and-membership.md §\"Tenant modes\").
    That exclusion is not a caller's filter and so is not in the cursor's
    fingerprint — the environment already is, through the resolved path.

    `q` is a case-insensitive substring of the name or the slug
    (management-api.md §Conventions \"Search\"; Q3-59). Both filters are named
    to `paginate` as well as applied, so a cursor issued for `?status=suspended`
    cannot be presented against the unfiltered listing and seek at a position
    that means something else there.

    Args:
        environment_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        q (None | str | Unset):
        status (ListTenantsStatusType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | TenantList
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
            limit=limit,
            cursor=cursor,
            q=q,
            status=status,
        )
    ).parsed
