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
from ...models.member_out import MemberOut
from ...models.member_patch import MemberPatch
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    tenant_id: str,
    member_id: str,
    *,
    body: MemberPatch,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/tenants/{tenant_id}/members/{member_id}".format(
            tenant_id=quote(str(tenant_id), safe=""),
            member_id=quote(str(member_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MemberOut | Problem | None:
    if response.status_code == 200:
        response_200 = MemberOut.from_dict(response.json())

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
) -> Response[MemberOut | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_id: str,
    member_id: str,
    *,
    client: AuthenticatedClient,
    body: MemberPatch,
) -> Response[MemberOut | Problem]:
    """Change a member

     Replace the role set, change the status, or both.

    `roles` replaces the whole set and emits `member.roles_changed` with `from`
    and `to` as slugs; a status move emits `member.suspended` or
    `member.unsuspended`. Either can break the Account tenant's `owner`
    invariant, and both are refused with 409 `last-owner` when they would.

    Args:
        tenant_id (str):
        member_id (str):
        body (MemberPatch): `PATCH /api/v1/tenants/{tenant_id}/members/{member_id}`.

            `roles` replaces the whole set — there is no add-one or remove-one
            operation on this surface — and `[]` is a valid value distinct from the
            `null` it does not accept. `user`, `tenant_id` and the timestamps are
            unknown fields: a membership is not moved from one user or tenant to
            another, it is removed and another is added.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemberOut | Problem]
    """

    kwargs = _get_kwargs(
        tenant_id=tenant_id,
        member_id=member_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_id: str,
    member_id: str,
    *,
    client: AuthenticatedClient,
    body: MemberPatch,
) -> MemberOut | Problem | None:
    """Change a member

     Replace the role set, change the status, or both.

    `roles` replaces the whole set and emits `member.roles_changed` with `from`
    and `to` as slugs; a status move emits `member.suspended` or
    `member.unsuspended`. Either can break the Account tenant's `owner`
    invariant, and both are refused with 409 `last-owner` when they would.

    Args:
        tenant_id (str):
        member_id (str):
        body (MemberPatch): `PATCH /api/v1/tenants/{tenant_id}/members/{member_id}`.

            `roles` replaces the whole set — there is no add-one or remove-one
            operation on this surface — and `[]` is a valid value distinct from the
            `null` it does not accept. `user`, `tenant_id` and the timestamps are
            unknown fields: a membership is not moved from one user or tenant to
            another, it is removed and another is added.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemberOut | Problem
    """

    return sync_detailed(
        tenant_id=tenant_id,
        member_id=member_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tenant_id: str,
    member_id: str,
    *,
    client: AuthenticatedClient,
    body: MemberPatch,
) -> Response[MemberOut | Problem]:
    """Change a member

     Replace the role set, change the status, or both.

    `roles` replaces the whole set and emits `member.roles_changed` with `from`
    and `to` as slugs; a status move emits `member.suspended` or
    `member.unsuspended`. Either can break the Account tenant's `owner`
    invariant, and both are refused with 409 `last-owner` when they would.

    Args:
        tenant_id (str):
        member_id (str):
        body (MemberPatch): `PATCH /api/v1/tenants/{tenant_id}/members/{member_id}`.

            `roles` replaces the whole set — there is no add-one or remove-one
            operation on this surface — and `[]` is a valid value distinct from the
            `null` it does not accept. `user`, `tenant_id` and the timestamps are
            unknown fields: a membership is not moved from one user or tenant to
            another, it is removed and another is added.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemberOut | Problem]
    """

    kwargs = _get_kwargs(
        tenant_id=tenant_id,
        member_id=member_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_id: str,
    member_id: str,
    *,
    client: AuthenticatedClient,
    body: MemberPatch,
) -> MemberOut | Problem | None:
    """Change a member

     Replace the role set, change the status, or both.

    `roles` replaces the whole set and emits `member.roles_changed` with `from`
    and `to` as slugs; a status move emits `member.suspended` or
    `member.unsuspended`. Either can break the Account tenant's `owner`
    invariant, and both are refused with 409 `last-owner` when they would.

    Args:
        tenant_id (str):
        member_id (str):
        body (MemberPatch): `PATCH /api/v1/tenants/{tenant_id}/members/{member_id}`.

            `roles` replaces the whole set — there is no add-one or remove-one
            operation on this surface — and `[]` is a valid value distinct from the
            `null` it does not accept. `user`, `tenant_id` and the timestamps are
            unknown fields: a membership is not moved from one user or tenant to
            another, it is removed and another is added.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemberOut | Problem
    """

    return (
        await asyncio_detailed(
            tenant_id=tenant_id,
            member_id=member_id,
            client=client,
            body=body,
        )
    ).parsed
