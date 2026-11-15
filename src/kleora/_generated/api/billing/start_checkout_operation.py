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
    r"""Start Stripe Checkout

     A short-lived Stripe Checkout URL for a named plan.

    `200`, not `201`: nothing of ours was created. The Stripe objects a
    completed Checkout produces reach this codebase through the webhook, which
    is the only writer of the mirror.

    **The currency follows `billing_country`** and never the caller's locale
    (billing.md §\"Currency follows the customer, never the page language\"); the
    country the buyer states wins, the address on their Stripe record answers
    when they state none, and the default currency applies when neither does.
    It is fixed for the life of the subscription, because Stripe will not switch
    a live one's currency.

    Stripe Tax is enabled on the session and tax ids are collected there
    (`apps.billing.services.start_checkout`), so VAT and sales tax are Stripe's
    arithmetic — every Price is net in both currencies. A second Checkout for an
    Account that already has a live subscription is `409 conflict` pointing at
    the Portal — the door half of
    billing.md's \"the second is a no-op, not a second subscription\"; the
    one-to-one mirror is the other half.

    Args:
        body (CheckoutIn): `POST /api/v1/account/billing/checkout`.

            Two closed sets and a country. In particular **no return URL**: one taken
            from the body would be an open redirect with a payment page in front of it,
            so it comes from this deployment's own configuration
            (`apps.billing.services._return_url`), and **no currency and no price**
            either — the caller says where the customer bills from and the server
            decides what that costs. A currency in the body would be a client choosing
            its own price list.

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
    r"""Start Stripe Checkout

     A short-lived Stripe Checkout URL for a named plan.

    `200`, not `201`: nothing of ours was created. The Stripe objects a
    completed Checkout produces reach this codebase through the webhook, which
    is the only writer of the mirror.

    **The currency follows `billing_country`** and never the caller's locale
    (billing.md §\"Currency follows the customer, never the page language\"); the
    country the buyer states wins, the address on their Stripe record answers
    when they state none, and the default currency applies when neither does.
    It is fixed for the life of the subscription, because Stripe will not switch
    a live one's currency.

    Stripe Tax is enabled on the session and tax ids are collected there
    (`apps.billing.services.start_checkout`), so VAT and sales tax are Stripe's
    arithmetic — every Price is net in both currencies. A second Checkout for an
    Account that already has a live subscription is `409 conflict` pointing at
    the Portal — the door half of
    billing.md's \"the second is a no-op, not a second subscription\"; the
    one-to-one mirror is the other half.

    Args:
        body (CheckoutIn): `POST /api/v1/account/billing/checkout`.

            Two closed sets and a country. In particular **no return URL**: one taken
            from the body would be an open redirect with a payment page in front of it,
            so it comes from this deployment's own configuration
            (`apps.billing.services._return_url`), and **no currency and no price**
            either — the caller says where the customer bills from and the server
            decides what that costs. A currency in the body would be a client choosing
            its own price list.

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
    r"""Start Stripe Checkout

     A short-lived Stripe Checkout URL for a named plan.

    `200`, not `201`: nothing of ours was created. The Stripe objects a
    completed Checkout produces reach this codebase through the webhook, which
    is the only writer of the mirror.

    **The currency follows `billing_country`** and never the caller's locale
    (billing.md §\"Currency follows the customer, never the page language\"); the
    country the buyer states wins, the address on their Stripe record answers
    when they state none, and the default currency applies when neither does.
    It is fixed for the life of the subscription, because Stripe will not switch
    a live one's currency.

    Stripe Tax is enabled on the session and tax ids are collected there
    (`apps.billing.services.start_checkout`), so VAT and sales tax are Stripe's
    arithmetic — every Price is net in both currencies. A second Checkout for an
    Account that already has a live subscription is `409 conflict` pointing at
    the Portal — the door half of
    billing.md's \"the second is a no-op, not a second subscription\"; the
    one-to-one mirror is the other half.

    Args:
        body (CheckoutIn): `POST /api/v1/account/billing/checkout`.

            Two closed sets and a country. In particular **no return URL**: one taken
            from the body would be an open redirect with a payment page in front of it,
            so it comes from this deployment's own configuration
            (`apps.billing.services._return_url`), and **no currency and no price**
            either — the caller says where the customer bills from and the server
            decides what that costs. A currency in the body would be a client choosing
            its own price list.

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
    r"""Start Stripe Checkout

     A short-lived Stripe Checkout URL for a named plan.

    `200`, not `201`: nothing of ours was created. The Stripe objects a
    completed Checkout produces reach this codebase through the webhook, which
    is the only writer of the mirror.

    **The currency follows `billing_country`** and never the caller's locale
    (billing.md §\"Currency follows the customer, never the page language\"); the
    country the buyer states wins, the address on their Stripe record answers
    when they state none, and the default currency applies when neither does.
    It is fixed for the life of the subscription, because Stripe will not switch
    a live one's currency.

    Stripe Tax is enabled on the session and tax ids are collected there
    (`apps.billing.services.start_checkout`), so VAT and sales tax are Stripe's
    arithmetic — every Price is net in both currencies. A second Checkout for an
    Account that already has a live subscription is `409 conflict` pointing at
    the Portal — the door half of
    billing.md's \"the second is a no-op, not a second subscription\"; the
    one-to-one mirror is the other half.

    Args:
        body (CheckoutIn): `POST /api/v1/account/billing/checkout`.

            Two closed sets and a country. In particular **no return URL**: one taken
            from the body would be an open redirect with a payment page in front of it,
            so it comes from this deployment's own configuration
            (`apps.billing.services._return_url`), and **no currency and no price**
            either — the caller says where the customer bills from and the server
            decides what that costs. A currency in the body would be a client choosing
            its own price list.

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
