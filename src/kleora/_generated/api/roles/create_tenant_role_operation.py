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
from ...models.role_in import RoleIn
from ...models.role_out import RoleOut
from ...types import Response


def _get_kwargs(
    tenant_id: str,
    *,
    body: RoleIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tenants/{tenant_id}/roles".format(
            tenant_id=quote(str(tenant_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | RoleOut | None:
    if response.status_code == 201:
        response_201 = RoleOut.from_dict(response.json())

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
) -> Response[Problem | RoleOut]:
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
    body: RoleIn,
) -> Response[Problem | RoleOut]:
    r"""Create a tenant-scoped role

     A role this tenant defines for itself, assignable only to its own Members.

    The other half of the resource `POST E/roles` writes, and the reason a role
    carries a `scope` at all: this one is deleted with the tenant, cannot be
    assigned in another tenant of the environment (422 `role-not-assignable`
    there), and is the only kind a `tenant_member` may create — under the
    escalation guard, which refuses a permission the caller does not itself
    hold (403 `privilege-escalation`, rbac.md §\"Escalation guard for tenant
    members\").

    The slug is unique across scopes and across the whole environment, so an
    app-scoped role's slug is 409 `role-slug-conflict` here and this slug is a
    409 for a later `POST E/roles` — while another tenant of the same
    environment may define it freely, because a Member sees exactly one of the
    two (rbac.md §Roles).

    Args:
        tenant_id (str):
        body (RoleIn): `POST E/roles` and `POST T/roles` — one body for both scopes.

            `tenant_id` is not an input field: a role's scope is decided by the endpoint
            it was created at and never changes (rbac.md §Roles). The environment path
            writes the app-scoped role, assignable in every tenant; the tenant path
            writes the one that tenant keeps to itself.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | RoleOut]
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
    body: RoleIn,
) -> Problem | RoleOut | None:
    r"""Create a tenant-scoped role

     A role this tenant defines for itself, assignable only to its own Members.

    The other half of the resource `POST E/roles` writes, and the reason a role
    carries a `scope` at all: this one is deleted with the tenant, cannot be
    assigned in another tenant of the environment (422 `role-not-assignable`
    there), and is the only kind a `tenant_member` may create — under the
    escalation guard, which refuses a permission the caller does not itself
    hold (403 `privilege-escalation`, rbac.md §\"Escalation guard for tenant
    members\").

    The slug is unique across scopes and across the whole environment, so an
    app-scoped role's slug is 409 `role-slug-conflict` here and this slug is a
    409 for a later `POST E/roles` — while another tenant of the same
    environment may define it freely, because a Member sees exactly one of the
    two (rbac.md §Roles).

    Args:
        tenant_id (str):
        body (RoleIn): `POST E/roles` and `POST T/roles` — one body for both scopes.

            `tenant_id` is not an input field: a role's scope is decided by the endpoint
            it was created at and never changes (rbac.md §Roles). The environment path
            writes the app-scoped role, assignable in every tenant; the tenant path
            writes the one that tenant keeps to itself.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | RoleOut
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
    body: RoleIn,
) -> Response[Problem | RoleOut]:
    r"""Create a tenant-scoped role

     A role this tenant defines for itself, assignable only to its own Members.

    The other half of the resource `POST E/roles` writes, and the reason a role
    carries a `scope` at all: this one is deleted with the tenant, cannot be
    assigned in another tenant of the environment (422 `role-not-assignable`
    there), and is the only kind a `tenant_member` may create — under the
    escalation guard, which refuses a permission the caller does not itself
    hold (403 `privilege-escalation`, rbac.md §\"Escalation guard for tenant
    members\").

    The slug is unique across scopes and across the whole environment, so an
    app-scoped role's slug is 409 `role-slug-conflict` here and this slug is a
    409 for a later `POST E/roles` — while another tenant of the same
    environment may define it freely, because a Member sees exactly one of the
    two (rbac.md §Roles).

    Args:
        tenant_id (str):
        body (RoleIn): `POST E/roles` and `POST T/roles` — one body for both scopes.

            `tenant_id` is not an input field: a role's scope is decided by the endpoint
            it was created at and never changes (rbac.md §Roles). The environment path
            writes the app-scoped role, assignable in every tenant; the tenant path
            writes the one that tenant keeps to itself.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | RoleOut]
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
    body: RoleIn,
) -> Problem | RoleOut | None:
    r"""Create a tenant-scoped role

     A role this tenant defines for itself, assignable only to its own Members.

    The other half of the resource `POST E/roles` writes, and the reason a role
    carries a `scope` at all: this one is deleted with the tenant, cannot be
    assigned in another tenant of the environment (422 `role-not-assignable`
    there), and is the only kind a `tenant_member` may create — under the
    escalation guard, which refuses a permission the caller does not itself
    hold (403 `privilege-escalation`, rbac.md §\"Escalation guard for tenant
    members\").

    The slug is unique across scopes and across the whole environment, so an
    app-scoped role's slug is 409 `role-slug-conflict` here and this slug is a
    409 for a later `POST E/roles` — while another tenant of the same
    environment may define it freely, because a Member sees exactly one of the
    two (rbac.md §Roles).

    Args:
        tenant_id (str):
        body (RoleIn): `POST E/roles` and `POST T/roles` — one body for both scopes.

            `tenant_id` is not an input field: a role's scope is decided by the endpoint
            it was created at and never changes (rbac.md §Roles). The environment path
            writes the app-scoped role, assignable in every tenant; the tenant path
            writes the one that tenant keeps to itself.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | RoleOut
    """

    return (
        await asyncio_detailed(
            tenant_id=tenant_id,
            client=client,
            body=body,
        )
    ).parsed
