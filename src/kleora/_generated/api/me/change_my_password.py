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
    r"""Change the caller's own password

     `POST /me/password` — the current password, a new one, and no body back.

    Reauth-gated like every `/me/mfa` mutation, then throttled, then handed to
    `passwords.change_password`. A wrong `current_password` is `401
    invalid-credentials` — the same answer a blocked or a locked account gets,
    because which of the three it was is not something a caller who does not
    already know should learn here — and a new password the environment's policy
    refuses is the `422 password-policy` / `password-breached` pair every other
    password endpoint answers with.

    Every other session of the caller's is revoked and this one survives, so the
    console tab the change was made in keeps working (users-and-credentials.md
    §\"Password change (user-initiated)\").

    Args:
        body (MePasswordIn): `POST /me/password` — the person's own password change (`Q3-151`).

            Two fields, both required, and the current one is not optional on any path:
            users-and-credentials.md §"Password change (user-initiated)" asks for it, and
            it is what makes this a change rather than an administrator's set
            (`UserPasswordIn` above has no `current_password` precisely because an
            administrator does not know it).

            `extra="forbid"` for the reason that schema gives. Neither value is ever
            echoed: the response is `204` with no body.

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
    r"""Change the caller's own password

     `POST /me/password` — the current password, a new one, and no body back.

    Reauth-gated like every `/me/mfa` mutation, then throttled, then handed to
    `passwords.change_password`. A wrong `current_password` is `401
    invalid-credentials` — the same answer a blocked or a locked account gets,
    because which of the three it was is not something a caller who does not
    already know should learn here — and a new password the environment's policy
    refuses is the `422 password-policy` / `password-breached` pair every other
    password endpoint answers with.

    Every other session of the caller's is revoked and this one survives, so the
    console tab the change was made in keeps working (users-and-credentials.md
    §\"Password change (user-initiated)\").

    Args:
        body (MePasswordIn): `POST /me/password` — the person's own password change (`Q3-151`).

            Two fields, both required, and the current one is not optional on any path:
            users-and-credentials.md §"Password change (user-initiated)" asks for it, and
            it is what makes this a change rather than an administrator's set
            (`UserPasswordIn` above has no `current_password` precisely because an
            administrator does not know it).

            `extra="forbid"` for the reason that schema gives. Neither value is ever
            echoed: the response is `204` with no body.

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
    r"""Change the caller's own password

     `POST /me/password` — the current password, a new one, and no body back.

    Reauth-gated like every `/me/mfa` mutation, then throttled, then handed to
    `passwords.change_password`. A wrong `current_password` is `401
    invalid-credentials` — the same answer a blocked or a locked account gets,
    because which of the three it was is not something a caller who does not
    already know should learn here — and a new password the environment's policy
    refuses is the `422 password-policy` / `password-breached` pair every other
    password endpoint answers with.

    Every other session of the caller's is revoked and this one survives, so the
    console tab the change was made in keeps working (users-and-credentials.md
    §\"Password change (user-initiated)\").

    Args:
        body (MePasswordIn): `POST /me/password` — the person's own password change (`Q3-151`).

            Two fields, both required, and the current one is not optional on any path:
            users-and-credentials.md §"Password change (user-initiated)" asks for it, and
            it is what makes this a change rather than an administrator's set
            (`UserPasswordIn` above has no `current_password` precisely because an
            administrator does not know it).

            `extra="forbid"` for the reason that schema gives. Neither value is ever
            echoed: the response is `204` with no body.

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
    r"""Change the caller's own password

     `POST /me/password` — the current password, a new one, and no body back.

    Reauth-gated like every `/me/mfa` mutation, then throttled, then handed to
    `passwords.change_password`. A wrong `current_password` is `401
    invalid-credentials` — the same answer a blocked or a locked account gets,
    because which of the three it was is not something a caller who does not
    already know should learn here — and a new password the environment's policy
    refuses is the `422 password-policy` / `password-breached` pair every other
    password endpoint answers with.

    Every other session of the caller's is revoked and this one survives, so the
    console tab the change was made in keeps working (users-and-credentials.md
    §\"Password change (user-initiated)\").

    Args:
        body (MePasswordIn): `POST /me/password` — the person's own password change (`Q3-151`).

            Two fields, both required, and the current one is not optional on any path:
            users-and-credentials.md §"Password change (user-initiated)" asks for it, and
            it is what makes this a change rather than an administrator's set
            (`UserPasswordIn` above has no `current_password` precisely because an
            administrator does not know it).

            `extra="forbid"` for the reason that schema gives. Neither value is ever
            echoed: the response is `204` with no body.

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
