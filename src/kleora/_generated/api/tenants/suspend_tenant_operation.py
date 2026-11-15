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
from ...models.tenant_out import TenantOut
from ...types import Response


def _get_kwargs(
    tenant_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tenants/{tenant_id}/suspend".format(
            tenant_id=quote(str(tenant_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | TenantOut | None:
    if response.status_code == 200:
        response_200 = TenantOut.from_dict(response.json())

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
) -> Response[Problem | TenantOut]:
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
) -> Response[Problem | TenantOut]:
    r"""Suspend a tenant

     Stop the tenant being selected at login. Idempotent, and only the first writes.

    Nothing is revoked: an access token already minted lives out its `exp`
    (ADR 0008), and the next token for a session bound to this tenant carries no
    `tenant` claim (rbac.md §\"Claims at token issuance\"). A tenant an Account is
    linked to, the Kleora Account's own included, is refused (409
    `account-tenant`): suspending it would lock every member out of the Account.

    Args:
        tenant_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | TenantOut]
    """

    kwargs = _get_kwargs(
        tenant_id=tenant_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_id: str,
    *,
    client: AuthenticatedClient,
) -> Problem | TenantOut | None:
    r"""Suspend a tenant

     Stop the tenant being selected at login. Idempotent, and only the first writes.

    Nothing is revoked: an access token already minted lives out its `exp`
    (ADR 0008), and the next token for a session bound to this tenant carries no
    `tenant` claim (rbac.md §\"Claims at token issuance\"). A tenant an Account is
    linked to, the Kleora Account's own included, is refused (409
    `account-tenant`): suspending it would lock every member out of the Account.

    Args:
        tenant_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | TenantOut
    """

    return sync_detailed(
        tenant_id=tenant_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Problem | TenantOut]:
    r"""Suspend a tenant

     Stop the tenant being selected at login. Idempotent, and only the first writes.

    Nothing is revoked: an access token already minted lives out its `exp`
    (ADR 0008), and the next token for a session bound to this tenant carries no
    `tenant` claim (rbac.md §\"Claims at token issuance\"). A tenant an Account is
    linked to, the Kleora Account's own included, is refused (409
    `account-tenant`): suspending it would lock every member out of the Account.

    Args:
        tenant_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | TenantOut]
    """

    kwargs = _get_kwargs(
        tenant_id=tenant_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_id: str,
    *,
    client: AuthenticatedClient,
) -> Problem | TenantOut | None:
    r"""Suspend a tenant

     Stop the tenant being selected at login. Idempotent, and only the first writes.

    Nothing is revoked: an access token already minted lives out its `exp`
    (ADR 0008), and the next token for a session bound to this tenant carries no
    `tenant` claim (rbac.md §\"Claims at token issuance\"). A tenant an Account is
    linked to, the Kleora Account's own included, is refused (409
    `account-tenant`): suspending it would lock every member out of the Account.

    Args:
        tenant_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | TenantOut
    """

    return (
        await asyncio_detailed(
            tenant_id=tenant_id,
            client=client,
        )
    ).parsed
