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
from ...models.billing_session_out import BillingSessionOut
from ...models.checkout_in import CheckoutIn
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    *,
    body: CheckoutIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/account/billing/checkout",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BillingSessionOut | Problem | None:
    if response.status_code == 200:
        response_200 = BillingSessionOut.from_dict(response.json())

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
) -> Response[BillingSessionOut | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CheckoutIn,
) -> Response[BillingSessionOut | Problem]:
    """Start Stripe Checkout

     A short-lived Stripe Checkout URL for a named plan.

    Answers `200`: nothing is created until the Checkout is completed. The currency follows
    `billing_country` (or the address on record when none is given, and the default currency
    otherwise), never the caller's language, and is fixed for the life of the subscription. Taxes
    are calculated and tax ids collected during Checkout; every price is net.

    `409 conflict` when the Account already has a live subscription; change it through the billing
    portal instead.

    Args:
        body (CheckoutIn): The body of `POST /api/v1/account/billing/checkout`.

            The plan, the billing interval and the billing country. There is no return URL, currency
            or
            price: the return URL is fixed, and the price and currency follow from the plan and the
            country.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BillingSessionOut | Problem]
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
    body: CheckoutIn,
) -> BillingSessionOut | Problem | None:
    """Start Stripe Checkout

     A short-lived Stripe Checkout URL for a named plan.

    Answers `200`: nothing is created until the Checkout is completed. The currency follows
    `billing_country` (or the address on record when none is given, and the default currency
    otherwise), never the caller's language, and is fixed for the life of the subscription. Taxes
    are calculated and tax ids collected during Checkout; every price is net.

    `409 conflict` when the Account already has a live subscription; change it through the billing
    portal instead.

    Args:
        body (CheckoutIn): The body of `POST /api/v1/account/billing/checkout`.

            The plan, the billing interval and the billing country. There is no return URL, currency
            or
            price: the return URL is fixed, and the price and currency follow from the plan and the
            country.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BillingSessionOut | Problem
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CheckoutIn,
) -> Response[BillingSessionOut | Problem]:
    """Start Stripe Checkout

     A short-lived Stripe Checkout URL for a named plan.

    Answers `200`: nothing is created until the Checkout is completed. The currency follows
    `billing_country` (or the address on record when none is given, and the default currency
    otherwise), never the caller's language, and is fixed for the life of the subscription. Taxes
    are calculated and tax ids collected during Checkout; every price is net.

    `409 conflict` when the Account already has a live subscription; change it through the billing
    portal instead.

    Args:
        body (CheckoutIn): The body of `POST /api/v1/account/billing/checkout`.

            The plan, the billing interval and the billing country. There is no return URL, currency
            or
            price: the return URL is fixed, and the price and currency follow from the plan and the
            country.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BillingSessionOut | Problem]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CheckoutIn,
) -> BillingSessionOut | Problem | None:
    """Start Stripe Checkout

     A short-lived Stripe Checkout URL for a named plan.

    Answers `200`: nothing is created until the Checkout is completed. The currency follows
    `billing_country` (or the address on record when none is given, and the default currency
    otherwise), never the caller's language, and is fixed for the life of the subscription. Taxes
    are calculated and tax ids collected during Checkout; every price is net.

    `409 conflict` when the Account already has a live subscription; change it through the billing
    portal instead.

    Args:
        body (CheckoutIn): The body of `POST /api/v1/account/billing/checkout`.

            The plan, the billing interval and the billing country. There is no return URL, currency
            or
            price: the return URL is fixed, and the price and currency follow from the plan and the
            country.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BillingSessionOut | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
