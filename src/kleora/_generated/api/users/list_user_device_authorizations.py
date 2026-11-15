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
from ...models.device_authorization_list import DeviceAuthorizationList
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    environment_id: str,
    user_id: str,
    *,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    json_cursor: None | str | Unset
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/environments/{environment_id}/users/{user_id}/device-authorizations".format(
            environment_id=quote(str(environment_id), safe=""),
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeviceAuthorizationList | Problem | None:
    if response.status_code == 200:
        response_200 = DeviceAuthorizationList.from_dict(response.json())

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
) -> Response[DeviceAuthorizationList | Problem]:
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
) -> Response[DeviceAuthorizationList | Problem]:
    r"""A user's device authorizations

     What this user has approved a device or agent to do as them, newest first.

    device-grant.md §\"Living with the grant afterwards\": \"Every approval creates
    a named authorization the user can see: the client's name, when it was
    approved, when it was last used, and from where.\" A credential that runs
    where the person is not looking is acceptable only because of this list and
    the `DELETE` beside it.

    Ended rows are **not** hidden. Somebody who did not approve a thing has to be
    able to discover that it happened, so an authorization that was revoked or
    that expired stays here saying which — what the list must not do is show one
    of those as live.

    Args:
        environment_id (str):
        user_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeviceAuthorizationList | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        user_id=user_id,
        limit=limit,
        cursor=cursor,
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
) -> DeviceAuthorizationList | Problem | None:
    r"""A user's device authorizations

     What this user has approved a device or agent to do as them, newest first.

    device-grant.md §\"Living with the grant afterwards\": \"Every approval creates
    a named authorization the user can see: the client's name, when it was
    approved, when it was last used, and from where.\" A credential that runs
    where the person is not looking is acceptable only because of this list and
    the `DELETE` beside it.

    Ended rows are **not** hidden. Somebody who did not approve a thing has to be
    able to discover that it happened, so an authorization that was revoked or
    that expired stays here saying which — what the list must not do is show one
    of those as live.

    Args:
        environment_id (str):
        user_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeviceAuthorizationList | Problem
    """

    return sync_detailed(
        environment_id=environment_id,
        user_id=user_id,
        client=client,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
) -> Response[DeviceAuthorizationList | Problem]:
    r"""A user's device authorizations

     What this user has approved a device or agent to do as them, newest first.

    device-grant.md §\"Living with the grant afterwards\": \"Every approval creates
    a named authorization the user can see: the client's name, when it was
    approved, when it was last used, and from where.\" A credential that runs
    where the person is not looking is acceptable only because of this list and
    the `DELETE` beside it.

    Ended rows are **not** hidden. Somebody who did not approve a thing has to be
    able to discover that it happened, so an authorization that was revoked or
    that expired stays here saying which — what the list must not do is show one
    of those as live.

    Args:
        environment_id (str):
        user_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeviceAuthorizationList | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        user_id=user_id,
        limit=limit,
        cursor=cursor,
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
) -> DeviceAuthorizationList | Problem | None:
    r"""A user's device authorizations

     What this user has approved a device or agent to do as them, newest first.

    device-grant.md §\"Living with the grant afterwards\": \"Every approval creates
    a named authorization the user can see: the client's name, when it was
    approved, when it was last used, and from where.\" A credential that runs
    where the person is not looking is acceptable only because of this list and
    the `DELETE` beside it.

    Ended rows are **not** hidden. Somebody who did not approve a thing has to be
    able to discover that it happened, so an authorization that was revoked or
    that expired stays here saying which — what the list must not do is show one
    of those as live.

    Args:
        environment_id (str):
        user_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeviceAuthorizationList | Problem
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            user_id=user_id,
            client=client,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
