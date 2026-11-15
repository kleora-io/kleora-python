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
from ...types import UNSET, Response, Unset


def _get_kwargs(
    environment_id: str,
    *,
    event_types: list[str] | None | Unset = UNSET,
    after: None | str | Unset = UNSET,
    last_event_id: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(last_event_id, Unset):
        headers["Last-Event-ID"] = last_event_id

    params: dict[str, Any] = {}

    json_event_types: list[str] | None | Unset
    if isinstance(event_types, Unset):
        json_event_types = UNSET
    elif isinstance(event_types, list):
        json_event_types = event_types

    else:
        json_event_types = event_types
    params["event_types"] = json_event_types

    json_after: None | str | Unset
    if isinstance(after, Unset):
        json_after = UNSET
    else:
        json_after = after
    params["after"] = json_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/environments/{environment_id}/webhook-events/stream".format(
            environment_id=quote(str(environment_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | str | None:
    if response.status_code == 200:
        response_200 = response.text
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
) -> Response[Problem | str]:
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
    event_types: list[str] | None | Unset = UNSET,
    after: None | str | Unset = UNSET,
    last_event_id: None | str | Unset = UNSET,
) -> Response[Problem | str]:
    """Tail an environment's webhook events

     A live `text/event-stream` of this environment's webhook events as they are recorded, used by
    `kleora webhooks forward`.

    Each message is the same envelope a delivery carries, with the event id as the SSE `id`; a
    comment is sent every fifteen seconds to keep the connection alive. `event_types` is repeatable
    and narrows the stream; without it, every event type is included.

    To resume without losing events, pass the last event received as `after=<event id>` or in the
    `Last-Event-ID` header; either `evt_…` or the bare UUID is accepted. An id this environment does
    not hold, for example one past the retention window, is `400 invalid-cursor`.

    Unlike the rest of this API, the response is a stream rather than JSON, so generated clients
    cannot consume it. Requires `webhooks:read`. The number of concurrent streams per credential is
    limited (`429 too-many-streams`), and a stream closes after a maximum lifetime, after which the
    client reconnects with its last event id. Starting and stopping a stream is audited.

    Args:
        environment_id (str):
        event_types (list[str] | None | Unset):
        after (None | str | Unset):
        last_event_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | str]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        event_types=event_types,
        after=after,
        last_event_id=last_event_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    event_types: list[str] | None | Unset = UNSET,
    after: None | str | Unset = UNSET,
    last_event_id: None | str | Unset = UNSET,
) -> Problem | str | None:
    """Tail an environment's webhook events

     A live `text/event-stream` of this environment's webhook events as they are recorded, used by
    `kleora webhooks forward`.

    Each message is the same envelope a delivery carries, with the event id as the SSE `id`; a
    comment is sent every fifteen seconds to keep the connection alive. `event_types` is repeatable
    and narrows the stream; without it, every event type is included.

    To resume without losing events, pass the last event received as `after=<event id>` or in the
    `Last-Event-ID` header; either `evt_…` or the bare UUID is accepted. An id this environment does
    not hold, for example one past the retention window, is `400 invalid-cursor`.

    Unlike the rest of this API, the response is a stream rather than JSON, so generated clients
    cannot consume it. Requires `webhooks:read`. The number of concurrent streams per credential is
    limited (`429 too-many-streams`), and a stream closes after a maximum lifetime, after which the
    client reconnects with its last event id. Starting and stopping a stream is audited.

    Args:
        environment_id (str):
        event_types (list[str] | None | Unset):
        after (None | str | Unset):
        last_event_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | str
    """

    return sync_detailed(
        environment_id=environment_id,
        client=client,
        event_types=event_types,
        after=after,
        last_event_id=last_event_id,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    event_types: list[str] | None | Unset = UNSET,
    after: None | str | Unset = UNSET,
    last_event_id: None | str | Unset = UNSET,
) -> Response[Problem | str]:
    """Tail an environment's webhook events

     A live `text/event-stream` of this environment's webhook events as they are recorded, used by
    `kleora webhooks forward`.

    Each message is the same envelope a delivery carries, with the event id as the SSE `id`; a
    comment is sent every fifteen seconds to keep the connection alive. `event_types` is repeatable
    and narrows the stream; without it, every event type is included.

    To resume without losing events, pass the last event received as `after=<event id>` or in the
    `Last-Event-ID` header; either `evt_…` or the bare UUID is accepted. An id this environment does
    not hold, for example one past the retention window, is `400 invalid-cursor`.

    Unlike the rest of this API, the response is a stream rather than JSON, so generated clients
    cannot consume it. Requires `webhooks:read`. The number of concurrent streams per credential is
    limited (`429 too-many-streams`), and a stream closes after a maximum lifetime, after which the
    client reconnects with its last event id. Starting and stopping a stream is audited.

    Args:
        environment_id (str):
        event_types (list[str] | None | Unset):
        after (None | str | Unset):
        last_event_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | str]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        event_types=event_types,
        after=after,
        last_event_id=last_event_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    event_types: list[str] | None | Unset = UNSET,
    after: None | str | Unset = UNSET,
    last_event_id: None | str | Unset = UNSET,
) -> Problem | str | None:
    """Tail an environment's webhook events

     A live `text/event-stream` of this environment's webhook events as they are recorded, used by
    `kleora webhooks forward`.

    Each message is the same envelope a delivery carries, with the event id as the SSE `id`; a
    comment is sent every fifteen seconds to keep the connection alive. `event_types` is repeatable
    and narrows the stream; without it, every event type is included.

    To resume without losing events, pass the last event received as `after=<event id>` or in the
    `Last-Event-ID` header; either `evt_…` or the bare UUID is accepted. An id this environment does
    not hold, for example one past the retention window, is `400 invalid-cursor`.

    Unlike the rest of this API, the response is a stream rather than JSON, so generated clients
    cannot consume it. Requires `webhooks:read`. The number of concurrent streams per credential is
    limited (`429 too-many-streams`), and a stream closes after a maximum lifetime, after which the
    client reconnects with its last event id. Starting and stopping a stream is audited.

    Args:
        environment_id (str):
        event_types (list[str] | None | Unset):
        after (None | str | Unset):
        last_event_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | str
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
            event_types=event_types,
            after=after,
            last_event_id=last_event_id,
        )
    ).parsed
