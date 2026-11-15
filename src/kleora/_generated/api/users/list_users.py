# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from http import HTTPStatus
from typing import Any, Literal
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_users_mfa_type_0 import ListUsersMfaType0
from ...models.list_users_status_type_0 import ListUsersStatusType0
from ...models.problem import Problem
from ...models.user_list import UserList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    environment_id: str,
    *,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    email: None | str | Unset = UNSET,
    q: None | str | Unset = UNSET,
    status: ListUsersStatusType0 | None | Unset = UNSET,
    tenant_id: None | Unset | UUID = UNSET,
    mfa: ListUsersMfaType0 | None | Unset = UNSET,
    session: Literal["active"] | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    json_cursor: None | str | Unset
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    json_email: None | str | Unset
    if isinstance(email, Unset):
        json_email = UNSET
    else:
        json_email = email
    params["email"] = json_email

    json_q: None | str | Unset
    if isinstance(q, Unset):
        json_q = UNSET
    else:
        json_q = q
    params["q"] = json_q

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    elif isinstance(status, ListUsersStatusType0):
        json_status = status.value
    else:
        json_status = status
    params["status"] = json_status

    json_tenant_id: None | str | Unset
    if isinstance(tenant_id, Unset):
        json_tenant_id = UNSET
    elif isinstance(tenant_id, UUID):
        json_tenant_id = str(tenant_id)
    else:
        json_tenant_id = tenant_id
    params["tenant_id"] = json_tenant_id

    json_mfa: None | str | Unset
    if isinstance(mfa, Unset):
        json_mfa = UNSET
    elif isinstance(mfa, ListUsersMfaType0):
        json_mfa = mfa.value
    else:
        json_mfa = mfa
    params["mfa"] = json_mfa

    json_session: Literal["active"] | None | Unset
    if isinstance(session, Unset):
        json_session = UNSET
    else:
        json_session = session
    params["session"] = json_session

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/environments/{environment_id}/users".format(
            environment_id=quote(str(environment_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | UserList | None:
    if response.status_code == 200:
        response_200 = UserList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Problem.from_dict(response.json())

        return response_400

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
) -> Response[Problem | UserList]:
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
    email: None | str | Unset = UNSET,
    q: None | str | Unset = UNSET,
    status: ListUsersStatusType0 | None | Unset = UNSET,
    tenant_id: None | Unset | UUID = UNSET,
    mfa: ListUsersMfaType0 | None | Unset = UNSET,
    session: Literal["active"] | None | Unset = UNSET,
) -> Response[Problem | UserList]:
    """List users

     The environment's users, newest first, narrowed by up to six filters.

    Erased users are excluded unless `status=erased` asks for them.

    `session=active` selects users holding at least one live session. It counts users, not sessions,
    so it can differ from the overview's count of active sessions.

    A cursor is only valid with the filters it was issued for, and a tenant member's cursor only
    within its own tenant.

    Args:
        environment_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        email (None | str | Unset):
        q (None | str | Unset):
        status (ListUsersStatusType0 | None | Unset):
        tenant_id (None | Unset | UUID):
        mfa (ListUsersMfaType0 | None | Unset):
        session (Literal['active'] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UserList]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        limit=limit,
        cursor=cursor,
        email=email,
        q=q,
        status=status,
        tenant_id=tenant_id,
        mfa=mfa,
        session=session,
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
    email: None | str | Unset = UNSET,
    q: None | str | Unset = UNSET,
    status: ListUsersStatusType0 | None | Unset = UNSET,
    tenant_id: None | Unset | UUID = UNSET,
    mfa: ListUsersMfaType0 | None | Unset = UNSET,
    session: Literal["active"] | None | Unset = UNSET,
) -> Problem | UserList | None:
    """List users

     The environment's users, newest first, narrowed by up to six filters.

    Erased users are excluded unless `status=erased` asks for them.

    `session=active` selects users holding at least one live session. It counts users, not sessions,
    so it can differ from the overview's count of active sessions.

    A cursor is only valid with the filters it was issued for, and a tenant member's cursor only
    within its own tenant.

    Args:
        environment_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        email (None | str | Unset):
        q (None | str | Unset):
        status (ListUsersStatusType0 | None | Unset):
        tenant_id (None | Unset | UUID):
        mfa (ListUsersMfaType0 | None | Unset):
        session (Literal['active'] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UserList
    """

    return sync_detailed(
        environment_id=environment_id,
        client=client,
        limit=limit,
        cursor=cursor,
        email=email,
        q=q,
        status=status,
        tenant_id=tenant_id,
        mfa=mfa,
        session=session,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    email: None | str | Unset = UNSET,
    q: None | str | Unset = UNSET,
    status: ListUsersStatusType0 | None | Unset = UNSET,
    tenant_id: None | Unset | UUID = UNSET,
    mfa: ListUsersMfaType0 | None | Unset = UNSET,
    session: Literal["active"] | None | Unset = UNSET,
) -> Response[Problem | UserList]:
    """List users

     The environment's users, newest first, narrowed by up to six filters.

    Erased users are excluded unless `status=erased` asks for them.

    `session=active` selects users holding at least one live session. It counts users, not sessions,
    so it can differ from the overview's count of active sessions.

    A cursor is only valid with the filters it was issued for, and a tenant member's cursor only
    within its own tenant.

    Args:
        environment_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        email (None | str | Unset):
        q (None | str | Unset):
        status (ListUsersStatusType0 | None | Unset):
        tenant_id (None | Unset | UUID):
        mfa (ListUsersMfaType0 | None | Unset):
        session (Literal['active'] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UserList]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        limit=limit,
        cursor=cursor,
        email=email,
        q=q,
        status=status,
        tenant_id=tenant_id,
        mfa=mfa,
        session=session,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    email: None | str | Unset = UNSET,
    q: None | str | Unset = UNSET,
    status: ListUsersStatusType0 | None | Unset = UNSET,
    tenant_id: None | Unset | UUID = UNSET,
    mfa: ListUsersMfaType0 | None | Unset = UNSET,
    session: Literal["active"] | None | Unset = UNSET,
) -> Problem | UserList | None:
    """List users

     The environment's users, newest first, narrowed by up to six filters.

    Erased users are excluded unless `status=erased` asks for them.

    `session=active` selects users holding at least one live session. It counts users, not sessions,
    so it can differ from the overview's count of active sessions.

    A cursor is only valid with the filters it was issued for, and a tenant member's cursor only
    within its own tenant.

    Args:
        environment_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        email (None | str | Unset):
        q (None | str | Unset):
        status (ListUsersStatusType0 | None | Unset):
        tenant_id (None | Unset | UUID):
        mfa (ListUsersMfaType0 | None | Unset):
        session (Literal['active'] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UserList
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
            limit=limit,
            cursor=cursor,
            email=email,
            q=q,
            status=status,
            tenant_id=tenant_id,
            mfa=mfa,
            session=session,
        )
    ).parsed
