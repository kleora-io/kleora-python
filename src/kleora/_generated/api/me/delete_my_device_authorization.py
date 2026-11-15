# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    authorization_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/me/device-authorizations/{authorization_id}".format(
            authorization_id=quote(str(authorization_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Problem | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = Problem.from_dict(response.json())

        return response_401

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
) -> Response[Any | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    authorization_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | Problem]:
    r"""Revoke one of the caller's own device authorizations

     Revoke it, exactly as the administrative route does. 204, idempotent.

    `allow_unpaid`, like every other self-service write on this surface: a
    dunning block must not stand between somebody and revoking a credential of
    their own (billing.md §\"When payment fails\" gates what costs money, and this
    ends something rather than starting it).

    `reason` is `logout` rather than `admin` — the person who authorised the
    thing is the one ending it (`sessions.Reason`, audit-log.md §Taxonomy).

    Args:
        authorization_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Problem]
    """

    kwargs = _get_kwargs(
        authorization_id=authorization_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    authorization_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | Problem | None:
    r"""Revoke one of the caller's own device authorizations

     Revoke it, exactly as the administrative route does. 204, idempotent.

    `allow_unpaid`, like every other self-service write on this surface: a
    dunning block must not stand between somebody and revoking a credential of
    their own (billing.md §\"When payment fails\" gates what costs money, and this
    ends something rather than starting it).

    `reason` is `logout` rather than `admin` — the person who authorised the
    thing is the one ending it (`sessions.Reason`, audit-log.md §Taxonomy).

    Args:
        authorization_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Problem
    """

    return sync_detailed(
        authorization_id=authorization_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    authorization_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | Problem]:
    r"""Revoke one of the caller's own device authorizations

     Revoke it, exactly as the administrative route does. 204, idempotent.

    `allow_unpaid`, like every other self-service write on this surface: a
    dunning block must not stand between somebody and revoking a credential of
    their own (billing.md §\"When payment fails\" gates what costs money, and this
    ends something rather than starting it).

    `reason` is `logout` rather than `admin` — the person who authorised the
    thing is the one ending it (`sessions.Reason`, audit-log.md §Taxonomy).

    Args:
        authorization_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Problem]
    """

    kwargs = _get_kwargs(
        authorization_id=authorization_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    authorization_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | Problem | None:
    r"""Revoke one of the caller's own device authorizations

     Revoke it, exactly as the administrative route does. 204, idempotent.

    `allow_unpaid`, like every other self-service write on this surface: a
    dunning block must not stand between somebody and revoking a credential of
    their own (billing.md §\"When payment fails\" gates what costs money, and this
    ends something rather than starting it).

    `reason` is `logout` rather than `admin` — the person who authorised the
    thing is the one ending it (`sessions.Reason`, audit-log.md §Taxonomy).

    Args:
        authorization_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Problem
    """

    return (
        await asyncio_detailed(
            authorization_id=authorization_id,
            client=client,
        )
    ).parsed
