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
from ...models.invitation_out import InvitationOut
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    tenant_id: str,
    invitation_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tenants/{tenant_id}/invitations/{invitation_id}/resend".format(
            tenant_id=quote(str(tenant_id), safe=""),
            invitation_id=quote(str(invitation_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InvitationOut | Problem | None:
    if response.status_code == 200:
        response_200 = InvitationOut.from_dict(response.json())

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
) -> Response[InvitationOut | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_id: str,
    invitation_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[InvitationOut | Problem]:
    """Re-send an invitation

     A new token, a fresh seven days, and another mail.

    The previous link stops working the moment this returns: the row holds one
    token hash and this overwrites it. That is the point of re-sending rather
    than sending twice — an invitation that had two live links would be two
    invitations, and revoking it would only take one of them away.

    Throttled per invitation, one a minute and five an hour
    (`apps.tenancy.throttles`), because the budget protects the mailbox of
    somebody who is not our user and cannot ask us to stop.

    Args:
        tenant_id (str):
        invitation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvitationOut | Problem]
    """

    kwargs = _get_kwargs(
        tenant_id=tenant_id,
        invitation_id=invitation_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_id: str,
    invitation_id: str,
    *,
    client: AuthenticatedClient,
) -> InvitationOut | Problem | None:
    """Re-send an invitation

     A new token, a fresh seven days, and another mail.

    The previous link stops working the moment this returns: the row holds one
    token hash and this overwrites it. That is the point of re-sending rather
    than sending twice — an invitation that had two live links would be two
    invitations, and revoking it would only take one of them away.

    Throttled per invitation, one a minute and five an hour
    (`apps.tenancy.throttles`), because the budget protects the mailbox of
    somebody who is not our user and cannot ask us to stop.

    Args:
        tenant_id (str):
        invitation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvitationOut | Problem
    """

    return sync_detailed(
        tenant_id=tenant_id,
        invitation_id=invitation_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_id: str,
    invitation_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[InvitationOut | Problem]:
    """Re-send an invitation

     A new token, a fresh seven days, and another mail.

    The previous link stops working the moment this returns: the row holds one
    token hash and this overwrites it. That is the point of re-sending rather
    than sending twice — an invitation that had two live links would be two
    invitations, and revoking it would only take one of them away.

    Throttled per invitation, one a minute and five an hour
    (`apps.tenancy.throttles`), because the budget protects the mailbox of
    somebody who is not our user and cannot ask us to stop.

    Args:
        tenant_id (str):
        invitation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvitationOut | Problem]
    """

    kwargs = _get_kwargs(
        tenant_id=tenant_id,
        invitation_id=invitation_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_id: str,
    invitation_id: str,
    *,
    client: AuthenticatedClient,
) -> InvitationOut | Problem | None:
    """Re-send an invitation

     A new token, a fresh seven days, and another mail.

    The previous link stops working the moment this returns: the row holds one
    token hash and this overwrites it. That is the point of re-sending rather
    than sending twice — an invitation that had two live links would be two
    invitations, and revoking it would only take one of them away.

    Throttled per invitation, one a minute and five an hour
    (`apps.tenancy.throttles`), because the budget protects the mailbox of
    somebody who is not our user and cannot ask us to stop.

    Args:
        tenant_id (str):
        invitation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvitationOut | Problem
    """

    return (
        await asyncio_detailed(
            tenant_id=tenant_id,
            invitation_id=invitation_id,
            client=client,
        )
    ).parsed
