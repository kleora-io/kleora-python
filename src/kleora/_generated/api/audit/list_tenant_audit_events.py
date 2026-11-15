# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audit_event_list import AuditEventList
from ...models.list_tenant_audit_events_format import ListTenantAuditEventsFormat
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_id: str,
    *,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    action: list[str] | None | Unset = UNSET,
    actor_id: None | Unset | UUID = UNSET,
    target_id: None | Unset | UUID = UNSET,
    from_: datetime.datetime | None | Unset = UNSET,
    to: datetime.datetime | None | Unset = UNSET,
    format_: ListTenantAuditEventsFormat | Unset = ListTenantAuditEventsFormat.JSON,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    json_cursor: None | str | Unset
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    json_action: list[str] | None | Unset
    if isinstance(action, Unset):
        json_action = UNSET
    elif isinstance(action, list):
        json_action = action

    else:
        json_action = action
    params["action"] = json_action

    json_actor_id: None | str | Unset
    if isinstance(actor_id, Unset):
        json_actor_id = UNSET
    elif isinstance(actor_id, UUID):
        json_actor_id = str(actor_id)
    else:
        json_actor_id = actor_id
    params["actor_id"] = json_actor_id

    json_target_id: None | str | Unset
    if isinstance(target_id, Unset):
        json_target_id = UNSET
    elif isinstance(target_id, UUID):
        json_target_id = str(target_id)
    else:
        json_target_id = target_id
    params["target_id"] = json_target_id

    json_from_: None | str | Unset
    if isinstance(from_, Unset):
        json_from_ = UNSET
    elif isinstance(from_, datetime.datetime):
        json_from_ = from_.isoformat()
    else:
        json_from_ = from_
    params["from"] = json_from_

    json_to: None | str | Unset
    if isinstance(to, Unset):
        json_to = UNSET
    elif isinstance(to, datetime.datetime):
        json_to = to.isoformat()
    else:
        json_to = to
    params["to"] = json_to

    json_format_: str | Unset = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tenants/{tenant_id}/audit-events".format(
            tenant_id=quote(str(tenant_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AuditEventList | Problem | None:
    if response.status_code == 200:
        response_200 = AuditEventList.from_dict(response.json())

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
) -> Response[AuditEventList | Problem]:
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
    action: list[str] | None | Unset = UNSET,
    actor_id: None | Unset | UUID = UNSET,
    target_id: None | Unset | UUID = UNSET,
    from_: datetime.datetime | None | Unset = UNSET,
    to: datetime.datetime | None | Unset = UNSET,
    format_: ListTenantAuditEventsFormat | Unset = ListTenantAuditEventsFormat.JSON,
) -> Response[AuditEventList | Problem]:
    """A tenant's audit events

     Every event recorded against this tenant — the `tenant_member`'s endpoint.

    It takes no `tenant_id` filter because the path already is one, and no
    `environment_id` one because a Tenant belongs to exactly one environment.
    Another tenant's id is 404 by containment, whether or not the row exists.

    Args:
        tenant_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        action (list[str] | None | Unset):
        actor_id (None | Unset | UUID):
        target_id (None | Unset | UUID):
        from_ (datetime.datetime | None | Unset):
        to (datetime.datetime | None | Unset):
        format_ (ListTenantAuditEventsFormat | Unset):  Default: ListTenantAuditEventsFormat.JSON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditEventList | Problem]
    """

    kwargs = _get_kwargs(
        tenant_id=tenant_id,
        limit=limit,
        cursor=cursor,
        action=action,
        actor_id=actor_id,
        target_id=target_id,
        from_=from_,
        to=to,
        format_=format_,
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
    action: list[str] | None | Unset = UNSET,
    actor_id: None | Unset | UUID = UNSET,
    target_id: None | Unset | UUID = UNSET,
    from_: datetime.datetime | None | Unset = UNSET,
    to: datetime.datetime | None | Unset = UNSET,
    format_: ListTenantAuditEventsFormat | Unset = ListTenantAuditEventsFormat.JSON,
) -> AuditEventList | Problem | None:
    """A tenant's audit events

     Every event recorded against this tenant — the `tenant_member`'s endpoint.

    It takes no `tenant_id` filter because the path already is one, and no
    `environment_id` one because a Tenant belongs to exactly one environment.
    Another tenant's id is 404 by containment, whether or not the row exists.

    Args:
        tenant_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        action (list[str] | None | Unset):
        actor_id (None | Unset | UUID):
        target_id (None | Unset | UUID):
        from_ (datetime.datetime | None | Unset):
        to (datetime.datetime | None | Unset):
        format_ (ListTenantAuditEventsFormat | Unset):  Default: ListTenantAuditEventsFormat.JSON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditEventList | Problem
    """

    return sync_detailed(
        tenant_id=tenant_id,
        client=client,
        limit=limit,
        cursor=cursor,
        action=action,
        actor_id=actor_id,
        target_id=target_id,
        from_=from_,
        to=to,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    tenant_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    action: list[str] | None | Unset = UNSET,
    actor_id: None | Unset | UUID = UNSET,
    target_id: None | Unset | UUID = UNSET,
    from_: datetime.datetime | None | Unset = UNSET,
    to: datetime.datetime | None | Unset = UNSET,
    format_: ListTenantAuditEventsFormat | Unset = ListTenantAuditEventsFormat.JSON,
) -> Response[AuditEventList | Problem]:
    """A tenant's audit events

     Every event recorded against this tenant — the `tenant_member`'s endpoint.

    It takes no `tenant_id` filter because the path already is one, and no
    `environment_id` one because a Tenant belongs to exactly one environment.
    Another tenant's id is 404 by containment, whether or not the row exists.

    Args:
        tenant_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        action (list[str] | None | Unset):
        actor_id (None | Unset | UUID):
        target_id (None | Unset | UUID):
        from_ (datetime.datetime | None | Unset):
        to (datetime.datetime | None | Unset):
        format_ (ListTenantAuditEventsFormat | Unset):  Default: ListTenantAuditEventsFormat.JSON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditEventList | Problem]
    """

    kwargs = _get_kwargs(
        tenant_id=tenant_id,
        limit=limit,
        cursor=cursor,
        action=action,
        actor_id=actor_id,
        target_id=target_id,
        from_=from_,
        to=to,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    action: list[str] | None | Unset = UNSET,
    actor_id: None | Unset | UUID = UNSET,
    target_id: None | Unset | UUID = UNSET,
    from_: datetime.datetime | None | Unset = UNSET,
    to: datetime.datetime | None | Unset = UNSET,
    format_: ListTenantAuditEventsFormat | Unset = ListTenantAuditEventsFormat.JSON,
) -> AuditEventList | Problem | None:
    """A tenant's audit events

     Every event recorded against this tenant — the `tenant_member`'s endpoint.

    It takes no `tenant_id` filter because the path already is one, and no
    `environment_id` one because a Tenant belongs to exactly one environment.
    Another tenant's id is 404 by containment, whether or not the row exists.

    Args:
        tenant_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        action (list[str] | None | Unset):
        actor_id (None | Unset | UUID):
        target_id (None | Unset | UUID):
        from_ (datetime.datetime | None | Unset):
        to (datetime.datetime | None | Unset):
        format_ (ListTenantAuditEventsFormat | Unset):  Default: ListTenantAuditEventsFormat.JSON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditEventList | Problem
    """

    return (
        await asyncio_detailed(
            tenant_id=tenant_id,
            client=client,
            limit=limit,
            cursor=cursor,
            action=action,
            actor_id=actor_id,
            target_id=target_id,
            from_=from_,
            to=to,
            format_=format_,
        )
    ).parsed
