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
from ...models.user_out import UserOut
from ...models.user_patch import UserPatch
from ...types import Response


def _get_kwargs(
    environment_id: str,
    user_id: str,
    *,
    body: UserPatch,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/environments/{environment_id}/users/{user_id}".format(
            environment_id=quote(str(environment_id), safe=""),
            user_id=quote(str(user_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

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
    body: UserPatch,
) -> Response[Problem | UserOut]:
    r"""Change a user

     A merge patch over the user's own profile. Never a password, never a status.

    An `email` change is the one that does more than it says: the address has to
    be free in this environment, `email_verified_at` goes back to null, and a
    fresh verification link is mailed — all three suppressed by
    `email_verified: true` in the same patch, which is how an administrator says
    \"I know this address is theirs\".

    Args:
        environment_id (str):
        user_id (str):
        body (UserPatch): `PATCH /api/v1/environments/{environment_id}/users/{user_id}`.

            `picture_url` and `locale` are the clearable fields: `null` means "no
            picture" and "no preference", and both are values a caller can go back to.
            `email`, `name` and `metadata` are not — an address is what identifies the
            row, a name has `""` for "none", and `metadata` has `{}`.

            `email_verified` is an instruction, not a property: `true` stamps
            `email_verified_at` and suppresses the verification mail an address change
            would otherwise send, `false` clears it. `password` is deliberately absent —
            setting one is `POST …/users/{user_id}/password`, which revokes every
            session and mails the person, and folding that into a patch would make an
            account takeover look like a profile edit.

            `status` is named in `immutable_fields` rather than left off, because it is
            plainly a property of the resource and the way to change it is
            `POST …/block` or `…/unblock`.

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
    body: UserPatch,
) -> Problem | UserOut | None:
    r"""Change a user

     A merge patch over the user's own profile. Never a password, never a status.

    An `email` change is the one that does more than it says: the address has to
    be free in this environment, `email_verified_at` goes back to null, and a
    fresh verification link is mailed — all three suppressed by
    `email_verified: true` in the same patch, which is how an administrator says
    \"I know this address is theirs\".

    Args:
        environment_id (str):
        user_id (str):
        body (UserPatch): `PATCH /api/v1/environments/{environment_id}/users/{user_id}`.

            `picture_url` and `locale` are the clearable fields: `null` means "no
            picture" and "no preference", and both are values a caller can go back to.
            `email`, `name` and `metadata` are not — an address is what identifies the
            row, a name has `""` for "none", and `metadata` has `{}`.

            `email_verified` is an instruction, not a property: `true` stamps
            `email_verified_at` and suppresses the verification mail an address change
            would otherwise send, `false` clears it. `password` is deliberately absent —
            setting one is `POST …/users/{user_id}/password`, which revokes every
            session and mails the person, and folding that into a patch would make an
            account takeover look like a profile edit.

            `status` is named in `immutable_fields` rather than left off, because it is
            plainly a property of the resource and the way to change it is
            `POST …/block` or `…/unblock`.

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
    body: UserPatch,
) -> Response[Problem | UserOut]:
    r"""Change a user

     A merge patch over the user's own profile. Never a password, never a status.

    An `email` change is the one that does more than it says: the address has to
    be free in this environment, `email_verified_at` goes back to null, and a
    fresh verification link is mailed — all three suppressed by
    `email_verified: true` in the same patch, which is how an administrator says
    \"I know this address is theirs\".

    Args:
        environment_id (str):
        user_id (str):
        body (UserPatch): `PATCH /api/v1/environments/{environment_id}/users/{user_id}`.

            `picture_url` and `locale` are the clearable fields: `null` means "no
            picture" and "no preference", and both are values a caller can go back to.
            `email`, `name` and `metadata` are not — an address is what identifies the
            row, a name has `""` for "none", and `metadata` has `{}`.

            `email_verified` is an instruction, not a property: `true` stamps
            `email_verified_at` and suppresses the verification mail an address change
            would otherwise send, `false` clears it. `password` is deliberately absent —
            setting one is `POST …/users/{user_id}/password`, which revokes every
            session and mails the person, and folding that into a patch would make an
            account takeover look like a profile edit.

            `status` is named in `immutable_fields` rather than left off, because it is
            plainly a property of the resource and the way to change it is
            `POST …/block` or `…/unblock`.

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
    body: UserPatch,
) -> Problem | UserOut | None:
    r"""Change a user

     A merge patch over the user's own profile. Never a password, never a status.

    An `email` change is the one that does more than it says: the address has to
    be free in this environment, `email_verified_at` goes back to null, and a
    fresh verification link is mailed — all three suppressed by
    `email_verified: true` in the same patch, which is how an administrator says
    \"I know this address is theirs\".

    Args:
        environment_id (str):
        user_id (str):
        body (UserPatch): `PATCH /api/v1/environments/{environment_id}/users/{user_id}`.

            `picture_url` and `locale` are the clearable fields: `null` means "no
            picture" and "no preference", and both are values a caller can go back to.
            `email`, `name` and `metadata` are not — an address is what identifies the
            row, a name has `""` for "none", and `metadata` has `{}`.

            `email_verified` is an instruction, not a property: `true` stamps
            `email_verified_at` and suppresses the verification mail an address change
            would otherwise send, `false` clears it. `password` is deliberately absent —
            setting one is `POST …/users/{user_id}/password`, which revokes every
            session and mails the person, and folding that into a patch would make an
            account takeover look like a profile edit.

            `status` is named in `immutable_fields` rather than left off, because it is
            plainly a property of the resource and the way to change it is
            `POST …/block` or `…/unblock`.

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
