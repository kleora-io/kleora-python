# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account_patch import AccountPatch
from ...models.account_read import AccountRead
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    *,
    body: AccountPatch,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/account",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AccountRead | Problem | None:
    if response.status_code == 200:
        response_200 = AccountRead.from_dict(response.json())

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
) -> Response[AccountRead | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AccountPatch,
) -> Response[AccountRead | Problem]:
    """Rename the account

     Rename it. `slug`, `plan`, `status` and `tenant_id` are not.

    Not `allow_suspended`: reading an Account while it is suspended is how the
    console explains the suspension, writing to it is not.

    Args:
        body (AccountPatch): `PATCH /api/v1/account` — one property, and one refusal worth
            explaining.

            `slug` is not a field of this schema, so it cannot be written; it is named
            in `immutable_fields` so that sending it is answered as what it is rather
            than as an unknown key. It is also the Account's tenant slug and the value
            `tenant=` carries when the console re-authorises, so renaming it would
            invalidate every bookmarked switch URL and every token in flight
            (platform-bootstrap.md §"The Account resource").

            `plan`, `status` and `tenant_id` are unknown fields on purpose:
            they are not properties a caller has any business addressing, and
            `extra="forbid"` says so.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountRead | Problem]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: AccountPatch,
) -> AccountRead | Problem | None:
    """Rename the account

     Rename it. `slug`, `plan`, `status` and `tenant_id` are not.

    Not `allow_suspended`: reading an Account while it is suspended is how the
    console explains the suspension, writing to it is not.

    Args:
        body (AccountPatch): `PATCH /api/v1/account` — one property, and one refusal worth
            explaining.

            `slug` is not a field of this schema, so it cannot be written; it is named
            in `immutable_fields` so that sending it is answered as what it is rather
            than as an unknown key. It is also the Account's tenant slug and the value
            `tenant=` carries when the console re-authorises, so renaming it would
            invalidate every bookmarked switch URL and every token in flight
            (platform-bootstrap.md §"The Account resource").

            `plan`, `status` and `tenant_id` are unknown fields on purpose:
            they are not properties a caller has any business addressing, and
            `extra="forbid"` says so.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountRead | Problem
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AccountPatch,
) -> Response[AccountRead | Problem]:
    """Rename the account

     Rename it. `slug`, `plan`, `status` and `tenant_id` are not.

    Not `allow_suspended`: reading an Account while it is suspended is how the
    console explains the suspension, writing to it is not.

    Args:
        body (AccountPatch): `PATCH /api/v1/account` — one property, and one refusal worth
            explaining.

            `slug` is not a field of this schema, so it cannot be written; it is named
            in `immutable_fields` so that sending it is answered as what it is rather
            than as an unknown key. It is also the Account's tenant slug and the value
            `tenant=` carries when the console re-authorises, so renaming it would
            invalidate every bookmarked switch URL and every token in flight
            (platform-bootstrap.md §"The Account resource").

            `plan`, `status` and `tenant_id` are unknown fields on purpose:
            they are not properties a caller has any business addressing, and
            `extra="forbid"` says so.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountRead | Problem]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AccountPatch,
) -> AccountRead | Problem | None:
    """Rename the account

     Rename it. `slug`, `plan`, `status` and `tenant_id` are not.

    Not `allow_suspended`: reading an Account while it is suspended is how the
    console explains the suspension, writing to it is not.

    Args:
        body (AccountPatch): `PATCH /api/v1/account` — one property, and one refusal worth
            explaining.

            `slug` is not a field of this schema, so it cannot be written; it is named
            in `immutable_fields` so that sending it is answered as what it is rather
            than as an unknown key. It is also the Account's tenant slug and the value
            `tenant=` carries when the console re-authorises, so renaming it would
            invalidate every bookmarked switch URL and every token in flight
            (platform-bootstrap.md §"The Account resource").

            `plan`, `status` and `tenant_id` are unknown fields on purpose:
            they are not properties a caller has any business addressing, and
            `extra="forbid"` says so.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountRead | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
