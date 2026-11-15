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
from ...models.member_in import MemberIn
from ...models.member_out import MemberOut
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    tenant_id: str,
    *,
    body: MemberIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tenants/{tenant_id}/members".format(
            tenant_id=quote(str(tenant_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MemberOut | Problem | None:
    if response.status_code == 201:
        response_201 = MemberOut.from_dict(response.json())

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
) -> Response[MemberOut | Problem]:
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
    body: MemberIn,
) -> Response[MemberOut | Problem]:
    """Add a member

     Link an existing User to this tenant, with the roles the body names.

    Exactly one of `user_id` and `email`; both or neither is 422. The address is
    normalised the way `users-and-credentials.md` normalises one, so the caller
    does not have to know the casing the row was written with — and a user who
    is not in this environment, or is erased, is 404 `user-not-found` rather
    than an invitation this endpoint does not send (that is Phase 3).

    Args:
        tenant_id (str):
        body (MemberIn): `POST /api/v1/tenants/{tenant_id}/members`.

            Exactly one of `user_id` and `email`; both or neither is 422
            (tenants-and-membership.md §"Failure modes"). It is checked by the resource
            rather than declared here because JSON Schema cannot say "exactly one of",
            so a rule expressed only in the document would be one a generated client
            could not enforce and we would still have to make.

            `roles` is a list of Role ids and defaults to none — a member with no roles
            is a member, and `roles: []` is what the token then carries.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemberOut | Problem]
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
    body: MemberIn,
) -> MemberOut | Problem | None:
    """Add a member

     Link an existing User to this tenant, with the roles the body names.

    Exactly one of `user_id` and `email`; both or neither is 422. The address is
    normalised the way `users-and-credentials.md` normalises one, so the caller
    does not have to know the casing the row was written with — and a user who
    is not in this environment, or is erased, is 404 `user-not-found` rather
    than an invitation this endpoint does not send (that is Phase 3).

    Args:
        tenant_id (str):
        body (MemberIn): `POST /api/v1/tenants/{tenant_id}/members`.

            Exactly one of `user_id` and `email`; both or neither is 422
            (tenants-and-membership.md §"Failure modes"). It is checked by the resource
            rather than declared here because JSON Schema cannot say "exactly one of",
            so a rule expressed only in the document would be one a generated client
            could not enforce and we would still have to make.

            `roles` is a list of Role ids and defaults to none — a member with no roles
            is a member, and `roles: []` is what the token then carries.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemberOut | Problem
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
    body: MemberIn,
) -> Response[MemberOut | Problem]:
    """Add a member

     Link an existing User to this tenant, with the roles the body names.

    Exactly one of `user_id` and `email`; both or neither is 422. The address is
    normalised the way `users-and-credentials.md` normalises one, so the caller
    does not have to know the casing the row was written with — and a user who
    is not in this environment, or is erased, is 404 `user-not-found` rather
    than an invitation this endpoint does not send (that is Phase 3).

    Args:
        tenant_id (str):
        body (MemberIn): `POST /api/v1/tenants/{tenant_id}/members`.

            Exactly one of `user_id` and `email`; both or neither is 422
            (tenants-and-membership.md §"Failure modes"). It is checked by the resource
            rather than declared here because JSON Schema cannot say "exactly one of",
            so a rule expressed only in the document would be one a generated client
            could not enforce and we would still have to make.

            `roles` is a list of Role ids and defaults to none — a member with no roles
            is a member, and `roles: []` is what the token then carries.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemberOut | Problem]
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
    body: MemberIn,
) -> MemberOut | Problem | None:
    """Add a member

     Link an existing User to this tenant, with the roles the body names.

    Exactly one of `user_id` and `email`; both or neither is 422. The address is
    normalised the way `users-and-credentials.md` normalises one, so the caller
    does not have to know the casing the row was written with — and a user who
    is not in this environment, or is erased, is 404 `user-not-found` rather
    than an invitation this endpoint does not send (that is Phase 3).

    Args:
        tenant_id (str):
        body (MemberIn): `POST /api/v1/tenants/{tenant_id}/members`.

            Exactly one of `user_id` and `email`; both or neither is 422
            (tenants-and-membership.md §"Failure modes"). It is checked by the resource
            rather than declared here because JSON Schema cannot say "exactly one of",
            so a rule expressed only in the document would be one a generated client
            could not enforce and we would still have to make.

            `roles` is a list of Role ids and defaults to none — a member with no roles
            is a member, and `roles: []` is what the token then carries.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemberOut | Problem
    """

    return (
        await asyncio_detailed(
            tenant_id=tenant_id,
            client=client,
            body=body,
        )
    ).parsed
