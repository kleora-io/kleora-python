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
from ...models.invitation_in import InvitationIn
from ...models.invitation_out import InvitationOut
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    tenant_id: str,
    *,
    body: InvitationIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tenants/{tenant_id}/invitations".format(
            tenant_id=quote(str(tenant_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InvitationOut | Problem | None:
    if response.status_code == 201:
        response_201 = InvitationOut.from_dict(response.json())

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
) -> Response[InvitationOut | Problem]:
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
    body: InvitationIn,
) -> Response[InvitationOut | Problem]:
    """Invite an address

     Create an invitation and email the link. The token is not returned.

    The roles are validated as `POST /tenants/{tenant_id}/members` validates them: a tenant member
    may only offer roles within its own permissions, and `owner` in an Account's tenant may only be
    offered by a member who holds it.

    With an `Idempotency-Key`, a repeated request returns the stored `201` and sends no second
    email.

    Args:
        tenant_id (str):
        body (InvitationIn): The body of `POST /api/v1/tenants/{tenant_id}/invitations`.

            `email` is validated by the same rules as a user's address. `roles` is a list of role ids,
            validated as `POST /tenants/{tenant_id}/members` validates them, and empty by default.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvitationOut | Problem]
    """

    kwargs = _get_kwargs(
        tenant_id=tenant_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_id: str,
    *,
    client: AuthenticatedClient,
    body: InvitationIn,
) -> InvitationOut | Problem | None:
    """Invite an address

     Create an invitation and email the link. The token is not returned.

    The roles are validated as `POST /tenants/{tenant_id}/members` validates them: a tenant member
    may only offer roles within its own permissions, and `owner` in an Account's tenant may only be
    offered by a member who holds it.

    With an `Idempotency-Key`, a repeated request returns the stored `201` and sends no second
    email.

    Args:
        tenant_id (str):
        body (InvitationIn): The body of `POST /api/v1/tenants/{tenant_id}/invitations`.

            `email` is validated by the same rules as a user's address. `roles` is a list of role ids,
            validated as `POST /tenants/{tenant_id}/members` validates them, and empty by default.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvitationOut | Problem
    """

    return sync_detailed(
        tenant_id=tenant_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tenant_id: str,
    *,
    client: AuthenticatedClient,
    body: InvitationIn,
) -> Response[InvitationOut | Problem]:
    """Invite an address

     Create an invitation and email the link. The token is not returned.

    The roles are validated as `POST /tenants/{tenant_id}/members` validates them: a tenant member
    may only offer roles within its own permissions, and `owner` in an Account's tenant may only be
    offered by a member who holds it.

    With an `Idempotency-Key`, a repeated request returns the stored `201` and sends no second
    email.

    Args:
        tenant_id (str):
        body (InvitationIn): The body of `POST /api/v1/tenants/{tenant_id}/invitations`.

            `email` is validated by the same rules as a user's address. `roles` is a list of role ids,
            validated as `POST /tenants/{tenant_id}/members` validates them, and empty by default.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvitationOut | Problem]
    """

    kwargs = _get_kwargs(
        tenant_id=tenant_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_id: str,
    *,
    client: AuthenticatedClient,
    body: InvitationIn,
) -> InvitationOut | Problem | None:
    """Invite an address

     Create an invitation and email the link. The token is not returned.

    The roles are validated as `POST /tenants/{tenant_id}/members` validates them: a tenant member
    may only offer roles within its own permissions, and `owner` in an Account's tenant may only be
    offered by a member who holds it.

    With an `Idempotency-Key`, a repeated request returns the stored `201` and sends no second
    email.

    Args:
        tenant_id (str):
        body (InvitationIn): The body of `POST /api/v1/tenants/{tenant_id}/invitations`.

            `email` is validated by the same rules as a user's address. `roles` is a list of role ids,
            validated as `POST /tenants/{tenant_id}/members` validates them, and empty by default.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvitationOut | Problem
    """

    return (
        await asyncio_detailed(
            tenant_id=tenant_id,
            client=client,
            body=body,
        )
    ).parsed
