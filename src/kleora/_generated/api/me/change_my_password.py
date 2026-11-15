# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.me_password_in import MePasswordIn
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    *,
    body: MePasswordIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/me/password",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    *,
    client: AuthenticatedClient,
    body: MePasswordIn,
) -> Response[Any | Problem]:
    """Change the caller's own password

     Change your own password. Requires the current password, and a recent re-authentication.

    A wrong `current_password` is `401 invalid-credentials`, the same answer a blocked or locked
    account gets. A new password the environment's policy refuses is `422 password-policy` or `422
    password-breached`.

    Every other session of yours is revoked; this one keeps working.

    Args:
        body (MePasswordIn): The body of `POST /me/password`: the current password and the new
            one. Both are required.

            Neither is ever returned; the response is `204` with no body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Problem]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: MePasswordIn,
) -> Any | Problem | None:
    """Change the caller's own password

     Change your own password. Requires the current password, and a recent re-authentication.

    A wrong `current_password` is `401 invalid-credentials`, the same answer a blocked or locked
    account gets. A new password the environment's policy refuses is `422 password-policy` or `422
    password-breached`.

    Every other session of yours is revoked; this one keeps working.

    Args:
        body (MePasswordIn): The body of `POST /me/password`: the current password and the new
            one. Both are required.

            Neither is ever returned; the response is `204` with no body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Problem
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: MePasswordIn,
) -> Response[Any | Problem]:
    """Change the caller's own password

     Change your own password. Requires the current password, and a recent re-authentication.

    A wrong `current_password` is `401 invalid-credentials`, the same answer a blocked or locked
    account gets. A new password the environment's policy refuses is `422 password-policy` or `422
    password-breached`.

    Every other session of yours is revoked; this one keeps working.

    Args:
        body (MePasswordIn): The body of `POST /me/password`: the current password and the new
            one. Both are required.

            Neither is ever returned; the response is `204` with no body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Problem]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: MePasswordIn,
) -> Any | Problem | None:
    """Change the caller's own password

     Change your own password. Requires the current password, and a recent re-authentication.

    A wrong `current_password` is `401 invalid-credentials`, the same answer a blocked or locked
    account gets. A new password the environment's policy refuses is `422 password-policy` or `422
    password-breached`.

    Every other session of yours is revoked; this one keeps working.

    Args:
        body (MePasswordIn): The body of `POST /me/password`: the current password and the new
            one. Both are required.

            Neither is ever returned; the response is `204` with no body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
