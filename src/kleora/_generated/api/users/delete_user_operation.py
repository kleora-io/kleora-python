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
from ...types import UNSET, Response, Unset


def _get_kwargs(
    environment_id: str,
    user_id: str,
    *,
    erase: bool | Unset = True,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["erase"] = erase

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/environments/{environment_id}/users/{user_id}".format(
            environment_id=quote(str(environment_id), safe=""),
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
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
) -> Response[Any | Problem]:
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
    erase: bool | Unset = True,
) -> Response[Any | Problem]:
    r"""Erase a user

     Always erasure; the row is never removed (users-and-credentials.md).

    `?erase=true` is accepted and has no additional effect: every user has at
    least a `user.created` event, so a \"hard delete when there is no history\"
    branch is unreachable, and `Invitation.invited_by` and `ApiKey.created_by`
    are `PROTECT` references that would make it fail unpredictably.

    Irreversible. The identifying columns are overwritten rather than copied
    aside, the credentials and memberships are deleted, and the audit trail —
    which still names the id — is the only thing left that says the person was
    ever here.

    Refused with 409 `last-owner` while the user is the last active owner of an
    Account's tenant: erasure takes every membership with it, and that one must
    not go.

    Args:
        environment_id (str):
        user_id (str):
        erase (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        user_id=user_id,
        erase=erase,
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
    erase: bool | Unset = True,
) -> Any | Problem | None:
    r"""Erase a user

     Always erasure; the row is never removed (users-and-credentials.md).

    `?erase=true` is accepted and has no additional effect: every user has at
    least a `user.created` event, so a \"hard delete when there is no history\"
    branch is unreachable, and `Invitation.invited_by` and `ApiKey.created_by`
    are `PROTECT` references that would make it fail unpredictably.

    Irreversible. The identifying columns are overwritten rather than copied
    aside, the credentials and memberships are deleted, and the audit trail —
    which still names the id — is the only thing left that says the person was
    ever here.

    Refused with 409 `last-owner` while the user is the last active owner of an
    Account's tenant: erasure takes every membership with it, and that one must
    not go.

    Args:
        environment_id (str):
        user_id (str):
        erase (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Problem
    """

    return sync_detailed(
        environment_id=environment_id,
        user_id=user_id,
        client=client,
        erase=erase,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
    erase: bool | Unset = True,
) -> Response[Any | Problem]:
    r"""Erase a user

     Always erasure; the row is never removed (users-and-credentials.md).

    `?erase=true` is accepted and has no additional effect: every user has at
    least a `user.created` event, so a \"hard delete when there is no history\"
    branch is unreachable, and `Invitation.invited_by` and `ApiKey.created_by`
    are `PROTECT` references that would make it fail unpredictably.

    Irreversible. The identifying columns are overwritten rather than copied
    aside, the credentials and memberships are deleted, and the audit trail —
    which still names the id — is the only thing left that says the person was
    ever here.

    Refused with 409 `last-owner` while the user is the last active owner of an
    Account's tenant: erasure takes every membership with it, and that one must
    not go.

    Args:
        environment_id (str):
        user_id (str):
        erase (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        user_id=user_id,
        erase=erase,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
    erase: bool | Unset = True,
) -> Any | Problem | None:
    r"""Erase a user

     Always erasure; the row is never removed (users-and-credentials.md).

    `?erase=true` is accepted and has no additional effect: every user has at
    least a `user.created` event, so a \"hard delete when there is no history\"
    branch is unreachable, and `Invitation.invited_by` and `ApiKey.created_by`
    are `PROTECT` references that would make it fail unpredictably.

    Irreversible. The identifying columns are overwritten rather than copied
    aside, the credentials and memberships are deleted, and the audit trail —
    which still names the id — is the only thing left that says the person was
    ever here.

    Refused with 409 `last-owner` while the user is the last active owner of an
    Account's tenant: erasure takes every membership with it, and that one must
    not go.

    Args:
        environment_id (str):
        user_id (str):
        erase (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Problem
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            user_id=user_id,
            client=client,
            erase=erase,
        )
    ).parsed
