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
from ...models.webhook_endpoint_created import WebhookEndpointCreated
from ...models.webhook_endpoint_in import WebhookEndpointIn
from ...types import Response


def _get_kwargs(
    environment_id: str,
    *,
    body: WebhookEndpointIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/environments/{environment_id}/webhook-endpoints".format(
            environment_id=quote(str(environment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | WebhookEndpointCreated | None:
    if response.status_code == 201:
        response_201 = WebhookEndpointCreated.from_dict(response.json())

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
) -> Response[Problem | WebhookEndpointCreated]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    body: WebhookEndpointIn,
) -> Response[Problem | WebhookEndpointCreated]:
    """Create a webhook endpoint

     An endpoint subscribed to `event_types` — empty by default, never a wildcard.

    The `201` carries the full secret, once, under the shown-once rules —
    `no_store` on the response and nothing that could show it again. A URL
    that is not `https://`, does not resolve, or resolves to a private or
    reserved address is 422 `webhook-url-rejected`, naming why
    (webhooks.md §SSRF). An `event_types` entry outside the published
    catalogue is 422 `invalid-event-type`, naming every offending one. And an
    Environment already holding as many endpoints as the App's plan allows is
    422 `limit-exceeded` naming the number (billing.md §Plans) — a *creation*
    refusal only: endpoints already registered keep delivering after a
    downgrade, exactly as tenants over the limit keep serving.

    Args:
        environment_id (str):
        body (WebhookEndpointIn): `POST /api/v1/environments/{environment_id}/webhook-endpoints`.

            `event_types` defaults to empty — webhooks.md §"Volume, and why
            subscription is explicit": "a new endpoint starts subscribed to nothing".
            There is no "all events" value this field accepts; every entry is checked
            against `apps.webhooks.catalogue.EVENT_TYPES` by the resource, which
            answers 422 `invalid-event-type` rather than `validation-error` for one
            that is not — a slug this schema cannot produce, the same reason
            `ApiKeyIn.scopes`'s catalogue check is not here either.

            `extra="forbid"`: `id`, `secret`, `enabled`, `disabled_at`,
            `disabled_reason`, `environment_id` are 422 as unknown fields. A new
            endpoint is always `enabled: true`; there is no way to create one disabled.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | WebhookEndpointCreated]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    body: WebhookEndpointIn,
) -> Problem | WebhookEndpointCreated | None:
    """Create a webhook endpoint

     An endpoint subscribed to `event_types` — empty by default, never a wildcard.

    The `201` carries the full secret, once, under the shown-once rules —
    `no_store` on the response and nothing that could show it again. A URL
    that is not `https://`, does not resolve, or resolves to a private or
    reserved address is 422 `webhook-url-rejected`, naming why
    (webhooks.md §SSRF). An `event_types` entry outside the published
    catalogue is 422 `invalid-event-type`, naming every offending one. And an
    Environment already holding as many endpoints as the App's plan allows is
    422 `limit-exceeded` naming the number (billing.md §Plans) — a *creation*
    refusal only: endpoints already registered keep delivering after a
    downgrade, exactly as tenants over the limit keep serving.

    Args:
        environment_id (str):
        body (WebhookEndpointIn): `POST /api/v1/environments/{environment_id}/webhook-endpoints`.

            `event_types` defaults to empty — webhooks.md §"Volume, and why
            subscription is explicit": "a new endpoint starts subscribed to nothing".
            There is no "all events" value this field accepts; every entry is checked
            against `apps.webhooks.catalogue.EVENT_TYPES` by the resource, which
            answers 422 `invalid-event-type` rather than `validation-error` for one
            that is not — a slug this schema cannot produce, the same reason
            `ApiKeyIn.scopes`'s catalogue check is not here either.

            `extra="forbid"`: `id`, `secret`, `enabled`, `disabled_at`,
            `disabled_reason`, `environment_id` are 422 as unknown fields. A new
            endpoint is always `enabled: true`; there is no way to create one disabled.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | WebhookEndpointCreated
    """

    return sync_detailed(
        environment_id=environment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    body: WebhookEndpointIn,
) -> Response[Problem | WebhookEndpointCreated]:
    """Create a webhook endpoint

     An endpoint subscribed to `event_types` — empty by default, never a wildcard.

    The `201` carries the full secret, once, under the shown-once rules —
    `no_store` on the response and nothing that could show it again. A URL
    that is not `https://`, does not resolve, or resolves to a private or
    reserved address is 422 `webhook-url-rejected`, naming why
    (webhooks.md §SSRF). An `event_types` entry outside the published
    catalogue is 422 `invalid-event-type`, naming every offending one. And an
    Environment already holding as many endpoints as the App's plan allows is
    422 `limit-exceeded` naming the number (billing.md §Plans) — a *creation*
    refusal only: endpoints already registered keep delivering after a
    downgrade, exactly as tenants over the limit keep serving.

    Args:
        environment_id (str):
        body (WebhookEndpointIn): `POST /api/v1/environments/{environment_id}/webhook-endpoints`.

            `event_types` defaults to empty — webhooks.md §"Volume, and why
            subscription is explicit": "a new endpoint starts subscribed to nothing".
            There is no "all events" value this field accepts; every entry is checked
            against `apps.webhooks.catalogue.EVENT_TYPES` by the resource, which
            answers 422 `invalid-event-type` rather than `validation-error` for one
            that is not — a slug this schema cannot produce, the same reason
            `ApiKeyIn.scopes`'s catalogue check is not here either.

            `extra="forbid"`: `id`, `secret`, `enabled`, `disabled_at`,
            `disabled_reason`, `environment_id` are 422 as unknown fields. A new
            endpoint is always `enabled: true`; there is no way to create one disabled.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | WebhookEndpointCreated]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    body: WebhookEndpointIn,
) -> Problem | WebhookEndpointCreated | None:
    """Create a webhook endpoint

     An endpoint subscribed to `event_types` — empty by default, never a wildcard.

    The `201` carries the full secret, once, under the shown-once rules —
    `no_store` on the response and nothing that could show it again. A URL
    that is not `https://`, does not resolve, or resolves to a private or
    reserved address is 422 `webhook-url-rejected`, naming why
    (webhooks.md §SSRF). An `event_types` entry outside the published
    catalogue is 422 `invalid-event-type`, naming every offending one. And an
    Environment already holding as many endpoints as the App's plan allows is
    422 `limit-exceeded` naming the number (billing.md §Plans) — a *creation*
    refusal only: endpoints already registered keep delivering after a
    downgrade, exactly as tenants over the limit keep serving.

    Args:
        environment_id (str):
        body (WebhookEndpointIn): `POST /api/v1/environments/{environment_id}/webhook-endpoints`.

            `event_types` defaults to empty — webhooks.md §"Volume, and why
            subscription is explicit": "a new endpoint starts subscribed to nothing".
            There is no "all events" value this field accepts; every entry is checked
            against `apps.webhooks.catalogue.EVENT_TYPES` by the resource, which
            answers 422 `invalid-event-type` rather than `validation-error` for one
            that is not — a slug this schema cannot produce, the same reason
            `ApiKeyIn.scopes`'s catalogue check is not here either.

            `extra="forbid"`: `id`, `secret`, `enabled`, `disabled_at`,
            `disabled_reason`, `environment_id` are 422 as unknown fields. A new
            endpoint is always `enabled: true`; there is no way to create one disabled.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | WebhookEndpointCreated
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
            body=body,
        )
    ).parsed
