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
from ...models.invitation_list import InvitationList
from ...models.list_invitations_status import ListInvitationsStatus
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_id: str,
    *,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    status: ListInvitationsStatus | Unset = ListInvitationsStatus.OPEN,
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

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_q: None | str | Unset
    if isinstance(q, Unset):
        json_q = UNSET
    else:
        json_q = q
    params["q"] = json_q

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tenants/{tenant_id}/invitations".format(
            tenant_id=quote(str(tenant_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InvitationList | Problem | None:
    if response.status_code == 200:
        response_200 = InvitationList.from_dict(response.json())

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
) -> Response[InvitationList | Problem]:
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
    status: ListInvitationsStatus | Unset = ListInvitationsStatus.OPEN,
    q: None | str | Unset = UNSET,
) -> Response[InvitationList | Problem]:
    """List invitations

     The tenant's invitations in one state, newest first.

    `status` defaults to `open`: the invitations still waiting for an answer. `q` is a
    case-insensitive substring of the invited email. A cursor is only valid with the filters it was
    issued for.

    Args:
        tenant_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        status (ListInvitationsStatus | Unset):  Default: ListInvitationsStatus.OPEN.
        q (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvitationList | Problem]
    """

    kwargs = _get_kwargs(
        tenant_id=tenant_id,
        limit=limit,
        cursor=cursor,
        status=status,
        q=q,
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
    status: ListInvitationsStatus | Unset = ListInvitationsStatus.OPEN,
    q: None | str | Unset = UNSET,
) -> InvitationList | Problem | None:
    """List invitations

     The tenant's invitations in one state, newest first.

    `status` defaults to `open`: the invitations still waiting for an answer. `q` is a
    case-insensitive substring of the invited email. A cursor is only valid with the filters it was
    issued for.

    Args:
        tenant_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        status (ListInvitationsStatus | Unset):  Default: ListInvitationsStatus.OPEN.
        q (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvitationList | Problem
    """

    return sync_detailed(
        tenant_id=tenant_id,
        client=client,
        limit=limit,
        cursor=cursor,
        status=status,
        q=q,
    ).parsed


async def asyncio_detailed(
    tenant_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    status: ListInvitationsStatus | Unset = ListInvitationsStatus.OPEN,
    q: None | str | Unset = UNSET,
) -> Response[InvitationList | Problem]:
    """List invitations

     The tenant's invitations in one state, newest first.

    `status` defaults to `open`: the invitations still waiting for an answer. `q` is a
    case-insensitive substring of the invited email. A cursor is only valid with the filters it was
    issued for.

    Args:
        tenant_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        status (ListInvitationsStatus | Unset):  Default: ListInvitationsStatus.OPEN.
        q (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvitationList | Problem]
    """

    kwargs = _get_kwargs(
        tenant_id=tenant_id,
        limit=limit,
        cursor=cursor,
        status=status,
        q=q,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    status: ListInvitationsStatus | Unset = ListInvitationsStatus.OPEN,
    q: None | str | Unset = UNSET,
) -> InvitationList | Problem | None:
    """List invitations

     The tenant's invitations in one state, newest first.

    `status` defaults to `open`: the invitations still waiting for an answer. `q` is a
    case-insensitive substring of the invited email. A cursor is only valid with the filters it was
    issued for.

    Args:
        tenant_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        status (ListInvitationsStatus | Unset):  Default: ListInvitationsStatus.OPEN.
        q (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvitationList | Problem
    """

    return (
        await asyncio_detailed(
            tenant_id=tenant_id,
            client=client,
            limit=limit,
            cursor=cursor,
            status=status,
            q=q,
        )
    ).parsed
