# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed self-service API document
# (https://id.kleora.eu/account/v1/openapi.json). `kleora.account` wraps this tree; nothing outside the
# package imports it.
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.flow_problem import FlowProblem
from ...models.session_page import SessionPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
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
        "url": "/account/v1/sessions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FlowProblem | SessionPage | None:
    if response.status_code == 200:
        response_200 = SessionPage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = FlowProblem.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FlowProblem.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FlowProblem.from_dict(response.json())

        return response_403

    if response.status_code == 429:
        response_429 = FlowProblem.from_dict(response.json())

        return response_429

    if response.status_code == 503:
        response_503 = FlowProblem.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FlowProblem | SessionPage]:
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
) -> Response[FlowProblem | SessionPage]:
    """The signed-in person's own live sessions

     Newest first, cursor paginated like every other list.

    The cursor is `api.management.pagination`'s and not a second implementation:
    it is a *position* rather than an offset, it is HMAC-tagged so a client cannot
    mint one, and it names its own query so a cursor issued for one listing cannot
    seek in another. A person with two devices will never see the difference; a
    person with two hundred would, and writing a second cursor to find that out
    would be the mistake this codebase keeps a single `paginate` to avoid.

    `ManagementProblem` is caught rather than raised: that module answers an
    unusable cursor with `400 invalid-cursor`, which is the right decision in the
    wrong surface's shape — this surface's problems carry a `code`. The slug is
    the same one, for the reason every shared slug here is shared.
    **`account-portal.md` declares no row for it**; the amendment is drafted in
    `U10-03`'s Log.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlowProblem | SessionPage]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
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
) -> FlowProblem | SessionPage | None:
    """The signed-in person's own live sessions

     Newest first, cursor paginated like every other list.

    The cursor is `api.management.pagination`'s and not a second implementation:
    it is a *position* rather than an offset, it is HMAC-tagged so a client cannot
    mint one, and it names its own query so a cursor issued for one listing cannot
    seek in another. A person with two devices will never see the difference; a
    person with two hundred would, and writing a second cursor to find that out
    would be the mistake this codebase keeps a single `paginate` to avoid.

    `ManagementProblem` is caught rather than raised: that module answers an
    unusable cursor with `400 invalid-cursor`, which is the right decision in the
    wrong surface's shape — this surface's problems carry a `code`. The slug is
    the same one, for the reason every shared slug here is shared.
    **`account-portal.md` declares no row for it**; the amendment is drafted in
    `U10-03`'s Log.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlowProblem | SessionPage
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
) -> Response[FlowProblem | SessionPage]:
    """The signed-in person's own live sessions

     Newest first, cursor paginated like every other list.

    The cursor is `api.management.pagination`'s and not a second implementation:
    it is a *position* rather than an offset, it is HMAC-tagged so a client cannot
    mint one, and it names its own query so a cursor issued for one listing cannot
    seek in another. A person with two devices will never see the difference; a
    person with two hundred would, and writing a second cursor to find that out
    would be the mistake this codebase keeps a single `paginate` to avoid.

    `ManagementProblem` is caught rather than raised: that module answers an
    unusable cursor with `400 invalid-cursor`, which is the right decision in the
    wrong surface's shape — this surface's problems carry a `code`. The slug is
    the same one, for the reason every shared slug here is shared.
    **`account-portal.md` declares no row for it**; the amendment is drafted in
    `U10-03`'s Log.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlowProblem | SessionPage]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: None | str | Unset = UNSET,
) -> FlowProblem | SessionPage | None:
    """The signed-in person's own live sessions

     Newest first, cursor paginated like every other list.

    The cursor is `api.management.pagination`'s and not a second implementation:
    it is a *position* rather than an offset, it is HMAC-tagged so a client cannot
    mint one, and it names its own query so a cursor issued for one listing cannot
    seek in another. A person with two devices will never see the difference; a
    person with two hundred would, and writing a second cursor to find that out
    would be the mistake this codebase keeps a single `paginate` to avoid.

    `ManagementProblem` is caught rather than raised: that module answers an
    unusable cursor with `400 invalid-cursor`, which is the right decision in the
    wrong surface's shape — this surface's problems carry a `code`. The slug is
    the same one, for the reason every shared slug here is shared.
    **`account-portal.md` declares no row for it**; the amendment is drafted in
    `U10-03`'s Log.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlowProblem | SessionPage
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
