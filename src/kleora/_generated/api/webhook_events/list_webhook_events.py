# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_webhook_events_outcome_type_0 import ListWebhookEventsOutcomeType0
from ...models.problem import Problem
from ...models.webhook_event_list import WebhookEventList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    environment_id: str,
    *,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    event_type: None | str | Unset = UNSET,
    endpoint_id: None | Unset | UUID = UNSET,
    outcome: ListWebhookEventsOutcomeType0 | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    json_cursor: None | str | Unset
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    json_event_type: None | str | Unset
    if isinstance(event_type, Unset):
        json_event_type = UNSET
    else:
        json_event_type = event_type
    params["event_type"] = json_event_type

    json_endpoint_id: None | str | Unset
    if isinstance(endpoint_id, Unset):
        json_endpoint_id = UNSET
    elif isinstance(endpoint_id, UUID):
        json_endpoint_id = str(endpoint_id)
    else:
        json_endpoint_id = endpoint_id
    params["endpoint_id"] = json_endpoint_id

    json_outcome: None | str | Unset
    if isinstance(outcome, Unset):
        json_outcome = UNSET
    elif isinstance(outcome, ListWebhookEventsOutcomeType0):
        json_outcome = outcome.value
    else:
        json_outcome = outcome
    params["outcome"] = json_outcome

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/environments/{environment_id}/webhook-events".format(
            environment_id=quote(str(environment_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | WebhookEventList | None:
    if response.status_code == 200:
        response_200 = WebhookEventList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Problem.from_dict(response.json())

        return response_400

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
) -> Response[Problem | WebhookEventList]:
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
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    event_type: None | str | Unset = UNSET,
    endpoint_id: None | Unset | UUID = UNSET,
    outcome: ListWebhookEventsOutcomeType0 | None | Unset = UNSET,
) -> Response[Problem | WebhookEventList]:
    """List webhook events

     The environment's webhook events, newest first: across every endpoint, or one endpoint's
    delivery log with `?endpoint_id=`.

    Each event's `outcome` is the worst outcome among the endpoints it was delivered to, so a later
    success does not hide a failure; `succeeded_endpoints` and `total_endpoints` give the counts.

    The `outcome` filter, by contrast, matches an event if any of its deliveries had that outcome,
    so an event that failed for one endpoint and succeeded for another is returned by both
    `?outcome=failed` and `?outcome=succeeded`. A cursor is only valid with the filters it was
    issued for.

    Args:
        environment_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        event_type (None | str | Unset):
        endpoint_id (None | Unset | UUID):
        outcome (ListWebhookEventsOutcomeType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | WebhookEventList]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        limit=limit,
        cursor=cursor,
        event_type=event_type,
        endpoint_id=endpoint_id,
        outcome=outcome,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    event_type: None | str | Unset = UNSET,
    endpoint_id: None | Unset | UUID = UNSET,
    outcome: ListWebhookEventsOutcomeType0 | None | Unset = UNSET,
) -> Problem | WebhookEventList | None:
    """List webhook events

     The environment's webhook events, newest first: across every endpoint, or one endpoint's
    delivery log with `?endpoint_id=`.

    Each event's `outcome` is the worst outcome among the endpoints it was delivered to, so a later
    success does not hide a failure; `succeeded_endpoints` and `total_endpoints` give the counts.

    The `outcome` filter, by contrast, matches an event if any of its deliveries had that outcome,
    so an event that failed for one endpoint and succeeded for another is returned by both
    `?outcome=failed` and `?outcome=succeeded`. A cursor is only valid with the filters it was
    issued for.

    Args:
        environment_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        event_type (None | str | Unset):
        endpoint_id (None | Unset | UUID):
        outcome (ListWebhookEventsOutcomeType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | WebhookEventList
    """

    return sync_detailed(
        environment_id=environment_id,
        client=client,
        limit=limit,
        cursor=cursor,
        event_type=event_type,
        endpoint_id=endpoint_id,
        outcome=outcome,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    event_type: None | str | Unset = UNSET,
    endpoint_id: None | Unset | UUID = UNSET,
    outcome: ListWebhookEventsOutcomeType0 | None | Unset = UNSET,
) -> Response[Problem | WebhookEventList]:
    """List webhook events

     The environment's webhook events, newest first: across every endpoint, or one endpoint's
    delivery log with `?endpoint_id=`.

    Each event's `outcome` is the worst outcome among the endpoints it was delivered to, so a later
    success does not hide a failure; `succeeded_endpoints` and `total_endpoints` give the counts.

    The `outcome` filter, by contrast, matches an event if any of its deliveries had that outcome,
    so an event that failed for one endpoint and succeeded for another is returned by both
    `?outcome=failed` and `?outcome=succeeded`. A cursor is only valid with the filters it was
    issued for.

    Args:
        environment_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        event_type (None | str | Unset):
        endpoint_id (None | Unset | UUID):
        outcome (ListWebhookEventsOutcomeType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | WebhookEventList]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        limit=limit,
        cursor=cursor,
        event_type=event_type,
        endpoint_id=endpoint_id,
        outcome=outcome,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    event_type: None | str | Unset = UNSET,
    endpoint_id: None | Unset | UUID = UNSET,
    outcome: ListWebhookEventsOutcomeType0 | None | Unset = UNSET,
) -> Problem | WebhookEventList | None:
    """List webhook events

     The environment's webhook events, newest first: across every endpoint, or one endpoint's
    delivery log with `?endpoint_id=`.

    Each event's `outcome` is the worst outcome among the endpoints it was delivered to, so a later
    success does not hide a failure; `succeeded_endpoints` and `total_endpoints` give the counts.

    The `outcome` filter, by contrast, matches an event if any of its deliveries had that outcome,
    so an event that failed for one endpoint and succeeded for another is returned by both
    `?outcome=failed` and `?outcome=succeeded`. A cursor is only valid with the filters it was
    issued for.

    Args:
        environment_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        event_type (None | str | Unset):
        endpoint_id (None | Unset | UUID):
        outcome (ListWebhookEventsOutcomeType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | WebhookEventList
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
            limit=limit,
            cursor=cursor,
            event_type=event_type,
            endpoint_id=endpoint_id,
            outcome=outcome,
        )
    ).parsed
