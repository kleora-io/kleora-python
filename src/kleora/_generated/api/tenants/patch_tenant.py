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
from ...models.tenant_patch import TenantPatch
from ...types import Response


def _get_kwargs(
    tenant_id: str,
    *,
    body: TenantPatch,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/tenants/{tenant_id}".format(
            tenant_id=quote(str(tenant_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: TenantPatch,
) -> Response[Problem | TenantOut]:
    r"""Change a tenant

     `name`, `slug` and `metadata`; the last replaced whole.

    The default tenant's `slug` is 422 with `code: \"immutable\"` — it is the
    string `single` mode hides the tenant under and the one every other tenant
    is blocked from claiming (tenants-and-membership.md §Tenants). So is the
    `slug` of a tenant an Account is linked to: it is the Account's slug, which
    cannot change either (platform-bootstrap.md).

    Args:
        tenant_id (str):
        body (TenantPatch): `PATCH /api/v1/tenants/{tenant_id}` — `name`, `slug` and `metadata`.

            `metadata` is replaced whole, which is what a merge patch does with an
            object unless a spec says it merges, and no spec says this one does.

            `is_default`, `status`, `member_count` and `environment_id` are unknown
            fields on purpose: the first is what the environment's own tenant is, the
            second moves through `suspend`/`unsuspend`, and the last two are
            projections rather than properties. The default tenant's `slug` is refused
            by the resource rather than by the schema — 422 with `code: "immutable"` —
            because which tenant it is is a row this schema cannot see.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | TenantOut]
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
    body: TenantPatch,
) -> Problem | TenantOut | None:
    r"""Change a tenant

     `name`, `slug` and `metadata`; the last replaced whole.

    The default tenant's `slug` is 422 with `code: \"immutable\"` — it is the
    string `single` mode hides the tenant under and the one every other tenant
    is blocked from claiming (tenants-and-membership.md §Tenants). So is the
    `slug` of a tenant an Account is linked to: it is the Account's slug, which
    cannot change either (platform-bootstrap.md).

    Args:
        tenant_id (str):
        body (TenantPatch): `PATCH /api/v1/tenants/{tenant_id}` — `name`, `slug` and `metadata`.

            `metadata` is replaced whole, which is what a merge patch does with an
            object unless a spec says it merges, and no spec says this one does.

            `is_default`, `status`, `member_count` and `environment_id` are unknown
            fields on purpose: the first is what the environment's own tenant is, the
            second moves through `suspend`/`unsuspend`, and the last two are
            projections rather than properties. The default tenant's `slug` is refused
            by the resource rather than by the schema — 422 with `code: "immutable"` —
            because which tenant it is is a row this schema cannot see.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | TenantOut
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
    body: TenantPatch,
) -> Response[Problem | TenantOut]:
    r"""Change a tenant

     `name`, `slug` and `metadata`; the last replaced whole.

    The default tenant's `slug` is 422 with `code: \"immutable\"` — it is the
    string `single` mode hides the tenant under and the one every other tenant
    is blocked from claiming (tenants-and-membership.md §Tenants). So is the
    `slug` of a tenant an Account is linked to: it is the Account's slug, which
    cannot change either (platform-bootstrap.md).

    Args:
        tenant_id (str):
        body (TenantPatch): `PATCH /api/v1/tenants/{tenant_id}` — `name`, `slug` and `metadata`.

            `metadata` is replaced whole, which is what a merge patch does with an
            object unless a spec says it merges, and no spec says this one does.

            `is_default`, `status`, `member_count` and `environment_id` are unknown
            fields on purpose: the first is what the environment's own tenant is, the
            second moves through `suspend`/`unsuspend`, and the last two are
            projections rather than properties. The default tenant's `slug` is refused
            by the resource rather than by the schema — 422 with `code: "immutable"` —
            because which tenant it is is a row this schema cannot see.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | TenantOut]
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
    body: TenantPatch,
) -> Problem | TenantOut | None:
    r"""Change a tenant

     `name`, `slug` and `metadata`; the last replaced whole.

    The default tenant's `slug` is 422 with `code: \"immutable\"` — it is the
    string `single` mode hides the tenant under and the one every other tenant
    is blocked from claiming (tenants-and-membership.md §Tenants). So is the
    `slug` of a tenant an Account is linked to: it is the Account's slug, which
    cannot change either (platform-bootstrap.md).

    Args:
        tenant_id (str):
        body (TenantPatch): `PATCH /api/v1/tenants/{tenant_id}` — `name`, `slug` and `metadata`.

            `metadata` is replaced whole, which is what a merge patch does with an
            object unless a spec says it merges, and no spec says this one does.

            `is_default`, `status`, `member_count` and `environment_id` are unknown
            fields on purpose: the first is what the environment's own tenant is, the
            second moves through `suspend`/`unsuspend`, and the last two are
            projections rather than properties. The default tenant's `slug` is refused
            by the resource rather than by the schema — 422 with `code: "immutable"` —
            because which tenant it is is a row this schema cannot see.

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
            body=body,
        )
    ).parsed
