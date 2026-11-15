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
from ...models.account_in import AccountIn
from ...models.account_out import AccountOut
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    *,
    body: AccountIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/accounts",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AccountOut | Problem | None:
    if response.status_code == 201:
        response_201 = AccountOut.from_dict(response.json())

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
) -> Response[AccountOut | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AccountIn,
) -> Response[AccountOut | Problem]:
    r"""Create an account

     An additional Account for the person already holding a console token.

    `scope=\"none\"` because it *creates* the Account a scope would be resolved
    against: there is no target and nothing to contain. The restriction that
    matters here is a different one — only a `console_user` may call it, since
    an `api_key` or a `tenant_member` creating an Account would be a credential
    minting authority outside the environment it was issued for — and it is
    declared as `kinds`, not written below (ADR 0009).

    The two rules that could be mistaken for the endpoint's are the service's:
    `create_account` requires a verified address and refuses an eleventh
    Account, so the hosted \"create your workspace\" form cannot hold to one set
    of rules while this holds to another.

    No `Location`: there is no URL that names this Account. `/account` is
    whichever Account the *token* resolves to, and this one becomes reachable
    only after the console re-authorises with `tenant={slug}`.

    Args:
        body (AccountIn): `POST /api/v1/accounts`.

            `slug` is optional and derived from `name` when it is absent
            (platform-bootstrap.md §"Deriving a slug from a name"). Absent and `null`
            mean the same thing here, which they may on a creation: there is no stored
            value for `null` to be different from.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountOut | Problem]
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
    body: AccountIn,
) -> AccountOut | Problem | None:
    r"""Create an account

     An additional Account for the person already holding a console token.

    `scope=\"none\"` because it *creates* the Account a scope would be resolved
    against: there is no target and nothing to contain. The restriction that
    matters here is a different one — only a `console_user` may call it, since
    an `api_key` or a `tenant_member` creating an Account would be a credential
    minting authority outside the environment it was issued for — and it is
    declared as `kinds`, not written below (ADR 0009).

    The two rules that could be mistaken for the endpoint's are the service's:
    `create_account` requires a verified address and refuses an eleventh
    Account, so the hosted \"create your workspace\" form cannot hold to one set
    of rules while this holds to another.

    No `Location`: there is no URL that names this Account. `/account` is
    whichever Account the *token* resolves to, and this one becomes reachable
    only after the console re-authorises with `tenant={slug}`.

    Args:
        body (AccountIn): `POST /api/v1/accounts`.

            `slug` is optional and derived from `name` when it is absent
            (platform-bootstrap.md §"Deriving a slug from a name"). Absent and `null`
            mean the same thing here, which they may on a creation: there is no stored
            value for `null` to be different from.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountOut | Problem
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AccountIn,
) -> Response[AccountOut | Problem]:
    r"""Create an account

     An additional Account for the person already holding a console token.

    `scope=\"none\"` because it *creates* the Account a scope would be resolved
    against: there is no target and nothing to contain. The restriction that
    matters here is a different one — only a `console_user` may call it, since
    an `api_key` or a `tenant_member` creating an Account would be a credential
    minting authority outside the environment it was issued for — and it is
    declared as `kinds`, not written below (ADR 0009).

    The two rules that could be mistaken for the endpoint's are the service's:
    `create_account` requires a verified address and refuses an eleventh
    Account, so the hosted \"create your workspace\" form cannot hold to one set
    of rules while this holds to another.

    No `Location`: there is no URL that names this Account. `/account` is
    whichever Account the *token* resolves to, and this one becomes reachable
    only after the console re-authorises with `tenant={slug}`.

    Args:
        body (AccountIn): `POST /api/v1/accounts`.

            `slug` is optional and derived from `name` when it is absent
            (platform-bootstrap.md §"Deriving a slug from a name"). Absent and `null`
            mean the same thing here, which they may on a creation: there is no stored
            value for `null` to be different from.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountOut | Problem]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AccountIn,
) -> AccountOut | Problem | None:
    r"""Create an account

     An additional Account for the person already holding a console token.

    `scope=\"none\"` because it *creates* the Account a scope would be resolved
    against: there is no target and nothing to contain. The restriction that
    matters here is a different one — only a `console_user` may call it, since
    an `api_key` or a `tenant_member` creating an Account would be a credential
    minting authority outside the environment it was issued for — and it is
    declared as `kinds`, not written below (ADR 0009).

    The two rules that could be mistaken for the endpoint's are the service's:
    `create_account` requires a verified address and refuses an eleventh
    Account, so the hosted \"create your workspace\" form cannot hold to one set
    of rules while this holds to another.

    No `Location`: there is no URL that names this Account. `/account` is
    whichever Account the *token* resolves to, and this one becomes reachable
    only after the console re-authorises with `tenant={slug}`.

    Args:
        body (AccountIn): `POST /api/v1/accounts`.

            `slug` is optional and derived from `name` when it is absent
            (platform-bootstrap.md §"Deriving a slug from a name"). Absent and `null`
            mean the same thing here, which they may on a creation: there is no stored
            value for `null` to be different from.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountOut | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
