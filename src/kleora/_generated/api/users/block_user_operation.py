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
from ...models.user_block_in import UserBlockIn
from ...models.user_out import UserOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    environment_id: str,
    user_id: str,
    *,
    body: None | Unset | UserBlockIn = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/environments/{environment_id}/users/{user_id}/block".format(
            environment_id=quote(str(environment_id), safe=""),
            user_id=quote(str(user_id), safe=""),
        ),
    }

    if isinstance(body, UserBlockIn):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | UserOut | None:
    if response.status_code == 200:
        response_200 = UserOut.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Problem.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = Problem.from_dict(response.json())

        return response_402

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
) -> Response[Problem | UserOut]:
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
    body: None | Unset | UserBlockIn = UNSET,
) -> Response[Problem | UserOut]:
    """Block a user

     Block the user from signing in, and end everything already signed in.

    In one transaction: the status changes, and every live session and its refresh tokens are
    revoked. A blocked user's next sign-in is refused exactly as a wrong password is, and a refresh
    answers `invalid_grant`.

    The body is optional and carries one field, `reason`: a note of up to 200 characters, stored
    with the block and included in the `user.blocked` event's `data.reason`.

    Idempotent: blocking a blocked user answers `200` with no second event, and does not overwrite
    the reason first recorded. To change it, unblock and block again.

    Args:
        environment_id (str):
        user_id (str):
        body (None | Unset | UserBlockIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UserOut]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        user_id=user_id,
        body=body,
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
    body: None | Unset | UserBlockIn = UNSET,
) -> Problem | UserOut | None:
    """Block a user

     Block the user from signing in, and end everything already signed in.

    In one transaction: the status changes, and every live session and its refresh tokens are
    revoked. A blocked user's next sign-in is refused exactly as a wrong password is, and a refresh
    answers `invalid_grant`.

    The body is optional and carries one field, `reason`: a note of up to 200 characters, stored
    with the block and included in the `user.blocked` event's `data.reason`.

    Idempotent: blocking a blocked user answers `200` with no second event, and does not overwrite
    the reason first recorded. To change it, unblock and block again.

    Args:
        environment_id (str):
        user_id (str):
        body (None | Unset | UserBlockIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UserOut
    """

    return sync_detailed(
        environment_id=environment_id,
        user_id=user_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: None | Unset | UserBlockIn = UNSET,
) -> Response[Problem | UserOut]:
    """Block a user

     Block the user from signing in, and end everything already signed in.

    In one transaction: the status changes, and every live session and its refresh tokens are
    revoked. A blocked user's next sign-in is refused exactly as a wrong password is, and a refresh
    answers `invalid_grant`.

    The body is optional and carries one field, `reason`: a note of up to 200 characters, stored
    with the block and included in the `user.blocked` event's `data.reason`.

    Idempotent: blocking a blocked user answers `200` with no second event, and does not overwrite
    the reason first recorded. To change it, unblock and block again.

    Args:
        environment_id (str):
        user_id (str):
        body (None | Unset | UserBlockIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UserOut]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        user_id=user_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: None | Unset | UserBlockIn = UNSET,
) -> Problem | UserOut | None:
    """Block a user

     Block the user from signing in, and end everything already signed in.

    In one transaction: the status changes, and every live session and its refresh tokens are
    revoked. A blocked user's next sign-in is refused exactly as a wrong password is, and a refresh
    answers `invalid_grant`.

    The body is optional and carries one field, `reason`: a note of up to 200 characters, stored
    with the block and included in the `user.blocked` event's `data.reason`.

    Idempotent: blocking a blocked user answers `200` with no second event, and does not overwrite
    the reason first recorded. To change it, unblock and block again.

    Args:
        environment_id (str):
        user_id (str):
        body (None | Unset | UserBlockIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UserOut
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            user_id=user_id,
            client=client,
            body=body,
        )
    ).parsed
