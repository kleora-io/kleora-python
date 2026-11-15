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
from ...models.user_export import UserExport
from ...types import Response


def _get_kwargs(
    environment_id: str,
    user_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/environments/{environment_id}/users/{user_id}/export".format(
            environment_id=quote(str(environment_id), safe=""),
            user_id=quote(str(user_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | UserExport | None:
    if response.status_code == 200:
        response_200 = UserExport.from_dict(response.json())

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
) -> Response[Problem | UserExport]:
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
) -> Response[Problem | UserExport]:
    """Export a user

     Everything Kleora holds about one user, as one document.

    The user record, identities without their secrets, MFA factors without their seeds, memberships,
    sessions, and the audit events where the user is actor or target, newest first. The audit events
    are capped, and `audit_events_truncated` says when the cap applied. The response is never
    cached.

    Args:
        environment_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UserExport]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        user_id=user_id,
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
) -> Problem | UserExport | None:
    """Export a user

     Everything Kleora holds about one user, as one document.

    The user record, identities without their secrets, MFA factors without their seeds, memberships,
    sessions, and the audit events where the user is actor or target, newest first. The audit events
    are capped, and `audit_events_truncated` says when the cap applied. The response is never
    cached.

    Args:
        environment_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UserExport
    """

    return sync_detailed(
        environment_id=environment_id,
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Problem | UserExport]:
    """Export a user

     Everything Kleora holds about one user, as one document.

    The user record, identities without their secrets, MFA factors without their seeds, memberships,
    sessions, and the audit events where the user is actor or target, newest first. The audit events
    are capped, and `audit_events_truncated` says when the cap applied. The response is never
    cached.

    Args:
        environment_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UserExport]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Problem | UserExport | None:
    """Export a user

     Everything Kleora holds about one user, as one document.

    The user record, identities without their secrets, MFA factors without their seeds, memberships,
    sessions, and the audit events where the user is actor or target, newest first. The audit events
    are capped, and `audit_events_truncated` says when the cap applied. The response is never
    cached.

    Args:
        environment_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UserExport
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            user_id=user_id,
            client=client,
        )
    ).parsed
