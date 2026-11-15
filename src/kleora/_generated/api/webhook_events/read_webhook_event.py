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
from ...models.webhook_event_detail_out import WebhookEventDetailOut
from ...types import Response


def _get_kwargs(
    environment_id: str,
    webhook_event_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/environments/{environment_id}/webhook-events/{webhook_event_id}".format(
            environment_id=quote(str(environment_id), safe=""),
            webhook_event_id=quote(str(webhook_event_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | WebhookEventDetailOut | None:
    if response.status_code == 200:
        response_200 = WebhookEventDetailOut.from_dict(response.json())

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
) -> Response[Problem | WebhookEventDetailOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    environment_id: str,
    webhook_event_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Problem | WebhookEventDetailOut]:
    r"""A webhook event, with every delivery attempt

     The frozen envelope and every attempt against it, to every endpoint it
    reached, newest first.

    `outcome`/`succeeded_endpoints`/`total_endpoints` are the same worst-
    outcome summary the list computes (`_worst_outcome`, `_endpoint_counts`)
    — over every delivery this event ever made, never narrowed to one
    endpoint, since a detail page has no `?endpoint_id=` to narrow by. The
    `deliveries` array below is unaffected by any of this: it is still every
    attempt, to every endpoint, exactly as stored.

    `payload.data` reads `{}` for an event about a user who has since been
    erased (`apps.webhooks.services.blank_erased_user_events`; webhooks.md
    §\"Retention, and erasure\": the envelope and every delivery outcome survive
    erasure, only `data` is blanked) — this returns the row exactly as stored,
    so there is nothing further to blank here.

    Args:
        environment_id (str):
        webhook_event_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | WebhookEventDetailOut]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        webhook_event_id=webhook_event_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    webhook_event_id: str,
    *,
    client: AuthenticatedClient,
) -> Problem | WebhookEventDetailOut | None:
    r"""A webhook event, with every delivery attempt

     The frozen envelope and every attempt against it, to every endpoint it
    reached, newest first.

    `outcome`/`succeeded_endpoints`/`total_endpoints` are the same worst-
    outcome summary the list computes (`_worst_outcome`, `_endpoint_counts`)
    — over every delivery this event ever made, never narrowed to one
    endpoint, since a detail page has no `?endpoint_id=` to narrow by. The
    `deliveries` array below is unaffected by any of this: it is still every
    attempt, to every endpoint, exactly as stored.

    `payload.data` reads `{}` for an event about a user who has since been
    erased (`apps.webhooks.services.blank_erased_user_events`; webhooks.md
    §\"Retention, and erasure\": the envelope and every delivery outcome survive
    erasure, only `data` is blanked) — this returns the row exactly as stored,
    so there is nothing further to blank here.

    Args:
        environment_id (str):
        webhook_event_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | WebhookEventDetailOut
    """

    return sync_detailed(
        environment_id=environment_id,
        webhook_event_id=webhook_event_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    webhook_event_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Problem | WebhookEventDetailOut]:
    r"""A webhook event, with every delivery attempt

     The frozen envelope and every attempt against it, to every endpoint it
    reached, newest first.

    `outcome`/`succeeded_endpoints`/`total_endpoints` are the same worst-
    outcome summary the list computes (`_worst_outcome`, `_endpoint_counts`)
    — over every delivery this event ever made, never narrowed to one
    endpoint, since a detail page has no `?endpoint_id=` to narrow by. The
    `deliveries` array below is unaffected by any of this: it is still every
    attempt, to every endpoint, exactly as stored.

    `payload.data` reads `{}` for an event about a user who has since been
    erased (`apps.webhooks.services.blank_erased_user_events`; webhooks.md
    §\"Retention, and erasure\": the envelope and every delivery outcome survive
    erasure, only `data` is blanked) — this returns the row exactly as stored,
    so there is nothing further to blank here.

    Args:
        environment_id (str):
        webhook_event_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | WebhookEventDetailOut]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        webhook_event_id=webhook_event_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    webhook_event_id: str,
    *,
    client: AuthenticatedClient,
) -> Problem | WebhookEventDetailOut | None:
    r"""A webhook event, with every delivery attempt

     The frozen envelope and every attempt against it, to every endpoint it
    reached, newest first.

    `outcome`/`succeeded_endpoints`/`total_endpoints` are the same worst-
    outcome summary the list computes (`_worst_outcome`, `_endpoint_counts`)
    — over every delivery this event ever made, never narrowed to one
    endpoint, since a detail page has no `?endpoint_id=` to narrow by. The
    `deliveries` array below is unaffected by any of this: it is still every
    attempt, to every endpoint, exactly as stored.

    `payload.data` reads `{}` for an event about a user who has since been
    erased (`apps.webhooks.services.blank_erased_user_events`; webhooks.md
    §\"Retention, and erasure\": the envelope and every delivery outcome survive
    erasure, only `data` is blanked) — this returns the row exactly as stored,
    so there is nothing further to blank here.

    Args:
        environment_id (str):
        webhook_event_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | WebhookEventDetailOut
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            webhook_event_id=webhook_event_id,
            client=client,
        )
    ).parsed
