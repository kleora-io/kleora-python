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
from ...models.webhook_endpoint_list import WebhookEndpointList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    environment_id: str,
    *,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    enabled: bool | None | Unset = UNSET,
    event_type: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    json_cursor: None | str | Unset
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    json_enabled: bool | None | Unset
    if isinstance(enabled, Unset):
        json_enabled = UNSET
    else:
        json_enabled = enabled
    params["enabled"] = json_enabled

    json_event_type: None | str | Unset
    if isinstance(event_type, Unset):
        json_event_type = UNSET
    else:
        json_event_type = event_type
    params["event_type"] = json_event_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/environments/{environment_id}/webhook-endpoints".format(
            environment_id=quote(str(environment_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | WebhookEndpointList | None:
    if response.status_code == 200:
        response_200 = WebhookEndpointList.from_dict(response.json())

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
) -> Response[Problem | WebhookEndpointList]:
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
    enabled: bool | None | Unset = UNSET,
    event_type: None | str | Unset = UNSET,
) -> Response[Problem | WebhookEndpointList]:
    """List webhook endpoints

     The environment's endpoints, newest first.

    `?enabled=` narrows to endpoints in that state, and `?event_type=` to
    endpoints subscribed to that one type — the same `array-contains` lookup
    the model's GIN index exists for. Both are named to `paginate` as well as
    applied, so a cursor issued under one filter cannot be presented against a
    different one and seek at a position that means something else there.

    Args:
        environment_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        enabled (bool | None | Unset):
        event_type (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | WebhookEndpointList]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        limit=limit,
        cursor=cursor,
        enabled=enabled,
        event_type=event_type,
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
    enabled: bool | None | Unset = UNSET,
    event_type: None | str | Unset = UNSET,
) -> Problem | WebhookEndpointList | None:
    """List webhook endpoints

     The environment's endpoints, newest first.

    `?enabled=` narrows to endpoints in that state, and `?event_type=` to
    endpoints subscribed to that one type — the same `array-contains` lookup
    the model's GIN index exists for. Both are named to `paginate` as well as
    applied, so a cursor issued under one filter cannot be presented against a
    different one and seek at a position that means something else there.

    Args:
        environment_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        enabled (bool | None | Unset):
        event_type (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | WebhookEndpointList
    """

    return sync_detailed(
        environment_id=environment_id,
        client=client,
        limit=limit,
        cursor=cursor,
        enabled=enabled,
        event_type=event_type,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    enabled: bool | None | Unset = UNSET,
    event_type: None | str | Unset = UNSET,
) -> Response[Problem | WebhookEndpointList]:
    """List webhook endpoints

     The environment's endpoints, newest first.

    `?enabled=` narrows to endpoints in that state, and `?event_type=` to
    endpoints subscribed to that one type — the same `array-contains` lookup
    the model's GIN index exists for. Both are named to `paginate` as well as
    applied, so a cursor issued under one filter cannot be presented against a
    different one and seek at a position that means something else there.

    Args:
        environment_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        enabled (bool | None | Unset):
        event_type (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | WebhookEndpointList]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        limit=limit,
        cursor=cursor,
        enabled=enabled,
        event_type=event_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    enabled: bool | None | Unset = UNSET,
    event_type: None | str | Unset = UNSET,
) -> Problem | WebhookEndpointList | None:
    """List webhook endpoints

     The environment's endpoints, newest first.

    `?enabled=` narrows to endpoints in that state, and `?event_type=` to
    endpoints subscribed to that one type — the same `array-contains` lookup
    the model's GIN index exists for. Both are named to `paginate` as well as
    applied, so a cursor issued under one filter cannot be presented against a
    different one and seek at a position that means something else there.

    Args:
        environment_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        enabled (bool | None | Unset):
        event_type (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | WebhookEndpointList
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
            limit=limit,
            cursor=cursor,
            enabled=enabled,
            event_type=event_type,
        )
    ).parsed
