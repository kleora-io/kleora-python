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
from ...models.user_in import UserIn
from ...models.user_out import UserOut
from ...types import Response


def _get_kwargs(
    environment_id: str,
    *,
    body: UserIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/environments/{environment_id}/users".format(
            environment_id=quote(str(environment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | UserOut | None:
    if response.status_code == 201:
        response_201 = UserOut.from_dict(response.json())

        return response_201

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
    *,
    client: AuthenticatedClient,
    body: UserIn,
) -> Response[Problem | UserOut]:
    r"""Create a user

     A user an administrator made, rather than one who signed up.

    The difference from `/signup` is the one `security-baseline.md` §\"No
    enumeration\" draws: this surface is not the hosted one, the caller already
    holds `users:write` over the environment, and an address that is taken is
    answered as 409 `email-taken` rather than as a page that looks like a
    success.

    `password` is optional — omitted, the user has no password identity until a
    reset creates one, and `has_password` says so. It is never echoed: the 201
    is the User resource and nothing else.

    Args:
        environment_id (str):
        body (UserIn): `POST /api/v1/environments/{environment_id}/users`.

            `extra="forbid"` is the whole of the "not an input field" rule: `id`,
            `status`, `has_password`, `email_verified_at`, `last_login_at` and
            `locked_until` are 422 as unknown fields. `email_verified` and
            `send_verification` are *instructions* rather than properties — the first
            resolves into `email_verified_at`, the second sends a message — which is
            why neither appears in `UserOut`.

            `password` is optional and, when given, never echoed anywhere: it is not a
            field of any response shape, and the audit event for the creation carries
            only whether the breach check ran.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UserOut]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    body: UserIn,
) -> Problem | UserOut | None:
    r"""Create a user

     A user an administrator made, rather than one who signed up.

    The difference from `/signup` is the one `security-baseline.md` §\"No
    enumeration\" draws: this surface is not the hosted one, the caller already
    holds `users:write` over the environment, and an address that is taken is
    answered as 409 `email-taken` rather than as a page that looks like a
    success.

    `password` is optional — omitted, the user has no password identity until a
    reset creates one, and `has_password` says so. It is never echoed: the 201
    is the User resource and nothing else.

    Args:
        environment_id (str):
        body (UserIn): `POST /api/v1/environments/{environment_id}/users`.

            `extra="forbid"` is the whole of the "not an input field" rule: `id`,
            `status`, `has_password`, `email_verified_at`, `last_login_at` and
            `locked_until` are 422 as unknown fields. `email_verified` and
            `send_verification` are *instructions* rather than properties — the first
            resolves into `email_verified_at`, the second sends a message — which is
            why neither appears in `UserOut`.

            `password` is optional and, when given, never echoed anywhere: it is not a
            field of any response shape, and the audit event for the creation carries
            only whether the breach check ran.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UserOut
    """

    return sync_detailed(
        environment_id=environment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    body: UserIn,
) -> Response[Problem | UserOut]:
    r"""Create a user

     A user an administrator made, rather than one who signed up.

    The difference from `/signup` is the one `security-baseline.md` §\"No
    enumeration\" draws: this surface is not the hosted one, the caller already
    holds `users:write` over the environment, and an address that is taken is
    answered as 409 `email-taken` rather than as a page that looks like a
    success.

    `password` is optional — omitted, the user has no password identity until a
    reset creates one, and `has_password` says so. It is never echoed: the 201
    is the User resource and nothing else.

    Args:
        environment_id (str):
        body (UserIn): `POST /api/v1/environments/{environment_id}/users`.

            `extra="forbid"` is the whole of the "not an input field" rule: `id`,
            `status`, `has_password`, `email_verified_at`, `last_login_at` and
            `locked_until` are 422 as unknown fields. `email_verified` and
            `send_verification` are *instructions* rather than properties — the first
            resolves into `email_verified_at`, the second sends a message — which is
            why neither appears in `UserOut`.

            `password` is optional and, when given, never echoed anywhere: it is not a
            field of any response shape, and the audit event for the creation carries
            only whether the breach check ran.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UserOut]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    body: UserIn,
) -> Problem | UserOut | None:
    r"""Create a user

     A user an administrator made, rather than one who signed up.

    The difference from `/signup` is the one `security-baseline.md` §\"No
    enumeration\" draws: this surface is not the hosted one, the caller already
    holds `users:write` over the environment, and an address that is taken is
    answered as 409 `email-taken` rather than as a page that looks like a
    success.

    `password` is optional — omitted, the user has no password identity until a
    reset creates one, and `has_password` says so. It is never echoed: the 201
    is the User resource and nothing else.

    Args:
        environment_id (str):
        body (UserIn): `POST /api/v1/environments/{environment_id}/users`.

            `extra="forbid"` is the whole of the "not an input field" rule: `id`,
            `status`, `has_password`, `email_verified_at`, `last_login_at` and
            `locked_until` are 422 as unknown fields. `email_verified` and
            `send_verification` are *instructions* rather than properties — the first
            resolves into `email_verified_at`, the second sends a message — which is
            why neither appears in `UserOut`.

            `password` is optional and, when given, never echoed anywhere: it is not a
            field of any response shape, and the audit event for the creation carries
            only whether the breach check ran.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UserOut
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
            body=body,
        )
    ).parsed
