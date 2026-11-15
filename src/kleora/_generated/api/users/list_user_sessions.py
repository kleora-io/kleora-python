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
from ...models.session_list import SessionList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    environment_id: str,
    user_id: str,
    *,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    include_expired: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    json_cursor: None | str | Unset
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    params["include_expired"] = include_expired

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/environments/{environment_id}/users/{user_id}/sessions".format(
            environment_id=quote(str(environment_id), safe=""),
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | SessionList | None:
    if response.status_code == 200:
        response_200 = SessionList.from_dict(response.json())

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
) -> Response[Problem | SessionList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    environment_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    include_expired: bool | Unset = False,
) -> Response[Problem | SessionList]:
    """A user's sessions

     The user's browser sessions, newest first; only live ones unless `include_expired` is set.

    A live session is not revoked, has not expired, and has been used within the environment's
    `session_idle_ttl`. A cursor is only valid with the `include_expired` value it was issued for.

    Args:
        environment_id (str):
        user_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        include_expired (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | SessionList]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        user_id=user_id,
        limit=limit,
        cursor=cursor,
        include_expired=include_expired,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    include_expired: bool | Unset = False,
) -> Problem | SessionList | None:
    """A user's sessions

     The user's browser sessions, newest first; only live ones unless `include_expired` is set.

    A live session is not revoked, has not expired, and has been used within the environment's
    `session_idle_ttl`. A cursor is only valid with the `include_expired` value it was issued for.

    Args:
        environment_id (str):
        user_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        include_expired (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | SessionList
    """

    return sync_detailed(
        environment_id=environment_id,
        user_id=user_id,
        client=client,
        limit=limit,
        cursor=cursor,
        include_expired=include_expired,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    include_expired: bool | Unset = False,
) -> Response[Problem | SessionList]:
    """A user's sessions

     The user's browser sessions, newest first; only live ones unless `include_expired` is set.

    A live session is not revoked, has not expired, and has been used within the environment's
    `session_idle_ttl`. A cursor is only valid with the `include_expired` value it was issued for.

    Args:
        environment_id (str):
        user_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        include_expired (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | SessionList]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        user_id=user_id,
        limit=limit,
        cursor=cursor,
        include_expired=include_expired,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    include_expired: bool | Unset = False,
) -> Problem | SessionList | None:
    """A user's sessions

     The user's browser sessions, newest first; only live ones unless `include_expired` is set.

    A live session is not revoked, has not expired, and has been used within the environment's
    `session_idle_ttl`. A cursor is only valid with the `include_expired` value it was issued for.

    Args:
        environment_id (str):
        user_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        include_expired (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | SessionList
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            user_id=user_id,
            client=client,
            limit=limit,
            cursor=cursor,
            include_expired=include_expired,
        )
    ).parsed
