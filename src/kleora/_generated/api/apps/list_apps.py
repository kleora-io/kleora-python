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
from ...models.app_list import AppList
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    slug: None | str | Unset = UNSET,
    q: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    json_cursor: None | str | Unset
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    json_slug: None | str | Unset
    if isinstance(slug, Unset):
        json_slug = UNSET
    else:
        json_slug = slug
    params["slug"] = json_slug

    json_q: None | str | Unset
    if isinstance(q, Unset):
        json_q = UNSET
    else:
        json_q = q
    params["q"] = json_q

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/apps",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppList | Problem | None:
    if response.status_code == 200:
        response_200 = AppList.from_dict(response.json())

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
) -> Response[AppList | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    slug: None | str | Unset = UNSET,
    q: None | str | Unset = UNSET,
) -> Response[AppList | Problem]:
    """List apps

     The Account's Apps, oldest first, optionally filtered to one slug or searched.

    `?slug=` is an exact, case-sensitive match — not a prefix and not a search —
    because it exists for one thing: the console resolving the slug in its URL
    to the App the page is about. It is filtered *inside* the Account, so
    another Account's slug returns an empty page rather than a 404: a filter
    that matched nothing, not a row that was hidden (apps.md §`GET /apps`).

    `q` is management-api.md §Conventions' own contract: a case-insensitive
    substring of `name` or `slug`, for the console's Apps table (Q3-59).

    Both filters are named to `paginate` as well as applied, so they are part
    of the cursor's fingerprint and a cursor issued for one cannot be presented
    against the unfiltered listing.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        slug (None | str | Unset):
        q (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppList | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        slug=slug,
        q=q,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    slug: None | str | Unset = UNSET,
    q: None | str | Unset = UNSET,
) -> AppList | Problem | None:
    """List apps

     The Account's Apps, oldest first, optionally filtered to one slug or searched.

    `?slug=` is an exact, case-sensitive match — not a prefix and not a search —
    because it exists for one thing: the console resolving the slug in its URL
    to the App the page is about. It is filtered *inside* the Account, so
    another Account's slug returns an empty page rather than a 404: a filter
    that matched nothing, not a row that was hidden (apps.md §`GET /apps`).

    `q` is management-api.md §Conventions' own contract: a case-insensitive
    substring of `name` or `slug`, for the console's Apps table (Q3-59).

    Both filters are named to `paginate` as well as applied, so they are part
    of the cursor's fingerprint and a cursor issued for one cannot be presented
    against the unfiltered listing.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        slug (None | str | Unset):
        q (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppList | Problem
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        slug=slug,
        q=q,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    slug: None | str | Unset = UNSET,
    q: None | str | Unset = UNSET,
) -> Response[AppList | Problem]:
    """List apps

     The Account's Apps, oldest first, optionally filtered to one slug or searched.

    `?slug=` is an exact, case-sensitive match — not a prefix and not a search —
    because it exists for one thing: the console resolving the slug in its URL
    to the App the page is about. It is filtered *inside* the Account, so
    another Account's slug returns an empty page rather than a 404: a filter
    that matched nothing, not a row that was hidden (apps.md §`GET /apps`).

    `q` is management-api.md §Conventions' own contract: a case-insensitive
    substring of `name` or `slug`, for the console's Apps table (Q3-59).

    Both filters are named to `paginate` as well as applied, so they are part
    of the cursor's fingerprint and a cursor issued for one cannot be presented
    against the unfiltered listing.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        slug (None | str | Unset):
        q (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppList | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        slug=slug,
        q=q,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    slug: None | str | Unset = UNSET,
    q: None | str | Unset = UNSET,
) -> AppList | Problem | None:
    """List apps

     The Account's Apps, oldest first, optionally filtered to one slug or searched.

    `?slug=` is an exact, case-sensitive match — not a prefix and not a search —
    because it exists for one thing: the console resolving the slug in its URL
    to the App the page is about. It is filtered *inside* the Account, so
    another Account's slug returns an empty page rather than a 404: a filter
    that matched nothing, not a row that was hidden (apps.md §`GET /apps`).

    `q` is management-api.md §Conventions' own contract: a case-insensitive
    substring of `name` or `slug`, for the console's Apps table (Q3-59).

    Both filters are named to `paginate` as well as applied, so they are part
    of the cursor's fingerprint and a cursor issued for one cannot be presented
    against the unfiltered listing.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        slug (None | str | Unset):
        q (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppList | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            slug=slug,
            q=q,
        )
    ).parsed
