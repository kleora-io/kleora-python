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
from ...models.api_key_list import ApiKeyList
from ...models.list_api_keys_status_type_0 import ListApiKeysStatusType0
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    environment_id: str,
    *,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    status: ListApiKeysStatusType0 | None | Unset = UNSET,
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

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    elif isinstance(status, ListApiKeysStatusType0):
        json_status = status.value
    else:
        json_status = status
    params["status"] = json_status

    json_q: None | str | Unset
    if isinstance(q, Unset):
        json_q = UNSET
    else:
        json_q = q
    params["q"] = json_q

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/environments/{environment_id}/api-keys".format(
            environment_id=quote(str(environment_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiKeyList | Problem | None:
    if response.status_code == 200:
        response_200 = ApiKeyList.from_dict(response.json())

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
) -> Response[ApiKeyList | Problem]:
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
    status: ListApiKeysStatusType0 | None | Unset = UNSET,
    q: None | str | Unset = UNSET,
) -> Response[ApiKeyList | Problem]:
    r"""List API keys

     The environment's keys, newest first, optionally filtered by `status` or searched.

    Newest first because that is the order the console reads them in: the key
    somebody just made is the one they are looking for, and a key list is a
    thing people scroll rather than page through. It is the second descending
    listing in the surface, after audit events.

    `status` is derived rather than stored, so the filter is three predicates
    over `revoked_at` and `expires_at` rather than an equality — and the clock
    is read once for the whole page, so a key cannot be `active` in the filter
    and `expired` in the body of the same response.

    `q` is a case-insensitive substring of `name` — the credential itself is
    never a searchable field, only ever shown once (management-api.md
    §Conventions \"Search\"; Q3-59).

    Every filter is named to `paginate` as well as applied, so it is part of
    the cursor's fingerprint: a cursor issued for `?status=revoked` cannot be
    presented against the unfiltered listing and seek at a position that means
    something else there.

    Args:
        environment_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        status (ListApiKeysStatusType0 | None | Unset):
        q (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKeyList | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        limit=limit,
        cursor=cursor,
        status=status,
        q=q,
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
    status: ListApiKeysStatusType0 | None | Unset = UNSET,
    q: None | str | Unset = UNSET,
) -> ApiKeyList | Problem | None:
    r"""List API keys

     The environment's keys, newest first, optionally filtered by `status` or searched.

    Newest first because that is the order the console reads them in: the key
    somebody just made is the one they are looking for, and a key list is a
    thing people scroll rather than page through. It is the second descending
    listing in the surface, after audit events.

    `status` is derived rather than stored, so the filter is three predicates
    over `revoked_at` and `expires_at` rather than an equality — and the clock
    is read once for the whole page, so a key cannot be `active` in the filter
    and `expired` in the body of the same response.

    `q` is a case-insensitive substring of `name` — the credential itself is
    never a searchable field, only ever shown once (management-api.md
    §Conventions \"Search\"; Q3-59).

    Every filter is named to `paginate` as well as applied, so it is part of
    the cursor's fingerprint: a cursor issued for `?status=revoked` cannot be
    presented against the unfiltered listing and seek at a position that means
    something else there.

    Args:
        environment_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        status (ListApiKeysStatusType0 | None | Unset):
        q (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKeyList | Problem
    """

    return sync_detailed(
        environment_id=environment_id,
        client=client,
        limit=limit,
        cursor=cursor,
        status=status,
        q=q,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    status: ListApiKeysStatusType0 | None | Unset = UNSET,
    q: None | str | Unset = UNSET,
) -> Response[ApiKeyList | Problem]:
    r"""List API keys

     The environment's keys, newest first, optionally filtered by `status` or searched.

    Newest first because that is the order the console reads them in: the key
    somebody just made is the one they are looking for, and a key list is a
    thing people scroll rather than page through. It is the second descending
    listing in the surface, after audit events.

    `status` is derived rather than stored, so the filter is three predicates
    over `revoked_at` and `expires_at` rather than an equality — and the clock
    is read once for the whole page, so a key cannot be `active` in the filter
    and `expired` in the body of the same response.

    `q` is a case-insensitive substring of `name` — the credential itself is
    never a searchable field, only ever shown once (management-api.md
    §Conventions \"Search\"; Q3-59).

    Every filter is named to `paginate` as well as applied, so it is part of
    the cursor's fingerprint: a cursor issued for `?status=revoked` cannot be
    presented against the unfiltered listing and seek at a position that means
    something else there.

    Args:
        environment_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        status (ListApiKeysStatusType0 | None | Unset):
        q (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKeyList | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        limit=limit,
        cursor=cursor,
        status=status,
        q=q,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
    status: ListApiKeysStatusType0 | None | Unset = UNSET,
    q: None | str | Unset = UNSET,
) -> ApiKeyList | Problem | None:
    r"""List API keys

     The environment's keys, newest first, optionally filtered by `status` or searched.

    Newest first because that is the order the console reads them in: the key
    somebody just made is the one they are looking for, and a key list is a
    thing people scroll rather than page through. It is the second descending
    listing in the surface, after audit events.

    `status` is derived rather than stored, so the filter is three predicates
    over `revoked_at` and `expires_at` rather than an equality — and the clock
    is read once for the whole page, so a key cannot be `active` in the filter
    and `expired` in the body of the same response.

    `q` is a case-insensitive substring of `name` — the credential itself is
    never a searchable field, only ever shown once (management-api.md
    §Conventions \"Search\"; Q3-59).

    Every filter is named to `paginate` as well as applied, so it is part of
    the cursor's fingerprint: a cursor issued for `?status=revoked` cannot be
    presented against the unfiltered listing and seek at a position that means
    something else there.

    Args:
        environment_id (str):
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):
        status (ListApiKeysStatusType0 | None | Unset):
        q (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKeyList | Problem
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
            limit=limit,
            cursor=cursor,
            status=status,
            q=q,
        )
    ).parsed
