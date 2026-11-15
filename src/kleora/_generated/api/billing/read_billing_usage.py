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
from ...models.billing_usage_out import BillingUsageOut
from ...models.problem import Problem
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/account/billing/usage",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BillingUsageOut | Problem | None:
    if response.status_code == 200:
        response_200 = BillingUsageOut.from_dict(response.json())

        return response_200

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
) -> Response[BillingUsageOut | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[BillingUsageOut | Problem]:
    r"""MAU, App and Tenant usage for the current period

     What this Account has used this calendar month, and against what.

    billing.md §API: \"so a customer can check our arithmetic\". That phrase is
    the whole design of the response — every figure comes with the window it was
    measured over and the allowance it is measured against, because a usage
    number a customer cannot reconcile is a number they will dispute, and one
    that disagrees with their invoice is worse than none at all. It is served
    from the same roll-up the invoice will be built from
    (`apps.billing.metering`), never from a second count of its own.

    **Nothing here refuses anything, and nothing downstream of it may.**
    `over_allowance` is a fact about a number. billing.md §\"Limits, and how they
    are enforced\" is explicit that MAU \"never blocks authentication\" and that
    `free` — which has no card and therefore no overage — is told and keeps
    working: \"Refusing a sign-in because the customer grew is precisely the
    failure this spec is arranged to avoid.\"

    `billing:read`, like `GET /account/billing`: usage is a billing figure, so
    it is behind the billing permission rather than `account:read`. An `admin`
    holds `billing:read` and not `billing:write`, so it reads this and cannot
    reach Checkout or the Portal (rbac.md §Permissions).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BillingUsageOut | Problem]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> BillingUsageOut | Problem | None:
    r"""MAU, App and Tenant usage for the current period

     What this Account has used this calendar month, and against what.

    billing.md §API: \"so a customer can check our arithmetic\". That phrase is
    the whole design of the response — every figure comes with the window it was
    measured over and the allowance it is measured against, because a usage
    number a customer cannot reconcile is a number they will dispute, and one
    that disagrees with their invoice is worse than none at all. It is served
    from the same roll-up the invoice will be built from
    (`apps.billing.metering`), never from a second count of its own.

    **Nothing here refuses anything, and nothing downstream of it may.**
    `over_allowance` is a fact about a number. billing.md §\"Limits, and how they
    are enforced\" is explicit that MAU \"never blocks authentication\" and that
    `free` — which has no card and therefore no overage — is told and keeps
    working: \"Refusing a sign-in because the customer grew is precisely the
    failure this spec is arranged to avoid.\"

    `billing:read`, like `GET /account/billing`: usage is a billing figure, so
    it is behind the billing permission rather than `account:read`. An `admin`
    holds `billing:read` and not `billing:write`, so it reads this and cannot
    reach Checkout or the Portal (rbac.md §Permissions).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BillingUsageOut | Problem
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[BillingUsageOut | Problem]:
    r"""MAU, App and Tenant usage for the current period

     What this Account has used this calendar month, and against what.

    billing.md §API: \"so a customer can check our arithmetic\". That phrase is
    the whole design of the response — every figure comes with the window it was
    measured over and the allowance it is measured against, because a usage
    number a customer cannot reconcile is a number they will dispute, and one
    that disagrees with their invoice is worse than none at all. It is served
    from the same roll-up the invoice will be built from
    (`apps.billing.metering`), never from a second count of its own.

    **Nothing here refuses anything, and nothing downstream of it may.**
    `over_allowance` is a fact about a number. billing.md §\"Limits, and how they
    are enforced\" is explicit that MAU \"never blocks authentication\" and that
    `free` — which has no card and therefore no overage — is told and keeps
    working: \"Refusing a sign-in because the customer grew is precisely the
    failure this spec is arranged to avoid.\"

    `billing:read`, like `GET /account/billing`: usage is a billing figure, so
    it is behind the billing permission rather than `account:read`. An `admin`
    holds `billing:read` and not `billing:write`, so it reads this and cannot
    reach Checkout or the Portal (rbac.md §Permissions).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BillingUsageOut | Problem]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> BillingUsageOut | Problem | None:
    r"""MAU, App and Tenant usage for the current period

     What this Account has used this calendar month, and against what.

    billing.md §API: \"so a customer can check our arithmetic\". That phrase is
    the whole design of the response — every figure comes with the window it was
    measured over and the allowance it is measured against, because a usage
    number a customer cannot reconcile is a number they will dispute, and one
    that disagrees with their invoice is worse than none at all. It is served
    from the same roll-up the invoice will be built from
    (`apps.billing.metering`), never from a second count of its own.

    **Nothing here refuses anything, and nothing downstream of it may.**
    `over_allowance` is a fact about a number. billing.md §\"Limits, and how they
    are enforced\" is explicit that MAU \"never blocks authentication\" and that
    `free` — which has no card and therefore no overage — is told and keeps
    working: \"Refusing a sign-in because the customer grew is precisely the
    failure this spec is arranged to avoid.\"

    `billing:read`, like `GET /account/billing`: usage is a billing figure, so
    it is behind the billing permission rather than `account:read`. An `admin`
    holds `billing:read` and not `billing:write`, so it reads this and cannot
    reach Checkout or the Portal (rbac.md §Permissions).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BillingUsageOut | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
