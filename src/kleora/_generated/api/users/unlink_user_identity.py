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
    environment_id: str,
    user_id: str,
    identity_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/environments/{environment_id}/users/{user_id}/identities/{identity_id}".format(
            environment_id=quote(str(environment_id), safe=""),
            user_id=quote(str(user_id), safe=""),
            identity_id=quote(str(identity_id), safe=""),
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
    identity_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | Problem]:
    """Unlink a provider account

     Remove one linked provider account. **Never the user's last way in.**

    409 `last-credential` when, after the removal, the user would hold neither a
    password, nor another linked provider, nor a confirmed passkey. A passkey
    counts because it can start a sign-in; an authenticator app does **not** —
    a second factor cannot begin one, so a user left holding only that is locked
    out of their own account with a working authenticator in their hand. The
    remedy the refusal names is to set a password first, the same wording an
    administrative password set uses.

    **The sessions that provider opened are ended, and no others.** Somebody
    tidying up a link they no longer use is not signed out of everything; somebody
    removing a link because that provider account was compromised has every
    session it authenticated cut off. A session's `amr` is what tells those two
    apart, which is why it records the provider rather than a generic value.

    Refused with 409 `last-credential` before anything is written, so nothing about
    the user changes on the refusal.

    Args:
        environment_id (str):
        user_id (str):
        identity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        user_id=user_id,
        identity_id=identity_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    user_id: str,
    identity_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | Problem | None:
    """Unlink a provider account

     Remove one linked provider account. **Never the user's last way in.**

    409 `last-credential` when, after the removal, the user would hold neither a
    password, nor another linked provider, nor a confirmed passkey. A passkey
    counts because it can start a sign-in; an authenticator app does **not** —
    a second factor cannot begin one, so a user left holding only that is locked
    out of their own account with a working authenticator in their hand. The
    remedy the refusal names is to set a password first, the same wording an
    administrative password set uses.

    **The sessions that provider opened are ended, and no others.** Somebody
    tidying up a link they no longer use is not signed out of everything; somebody
    removing a link because that provider account was compromised has every
    session it authenticated cut off. A session's `amr` is what tells those two
    apart, which is why it records the provider rather than a generic value.

    Refused with 409 `last-credential` before anything is written, so nothing about
    the user changes on the refusal.

    Args:
        environment_id (str):
        user_id (str):
        identity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Problem
    """

    return sync_detailed(
        environment_id=environment_id,
        user_id=user_id,
        identity_id=identity_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    user_id: str,
    identity_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | Problem]:
    """Unlink a provider account

     Remove one linked provider account. **Never the user's last way in.**

    409 `last-credential` when, after the removal, the user would hold neither a
    password, nor another linked provider, nor a confirmed passkey. A passkey
    counts because it can start a sign-in; an authenticator app does **not** —
    a second factor cannot begin one, so a user left holding only that is locked
    out of their own account with a working authenticator in their hand. The
    remedy the refusal names is to set a password first, the same wording an
    administrative password set uses.

    **The sessions that provider opened are ended, and no others.** Somebody
    tidying up a link they no longer use is not signed out of everything; somebody
    removing a link because that provider account was compromised has every
    session it authenticated cut off. A session's `amr` is what tells those two
    apart, which is why it records the provider rather than a generic value.

    Refused with 409 `last-credential` before anything is written, so nothing about
    the user changes on the refusal.

    Args:
        environment_id (str):
        user_id (str):
        identity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        user_id=user_id,
        identity_id=identity_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    user_id: str,
    identity_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | Problem | None:
    """Unlink a provider account

     Remove one linked provider account. **Never the user's last way in.**

    409 `last-credential` when, after the removal, the user would hold neither a
    password, nor another linked provider, nor a confirmed passkey. A passkey
    counts because it can start a sign-in; an authenticator app does **not** —
    a second factor cannot begin one, so a user left holding only that is locked
    out of their own account with a working authenticator in their hand. The
    remedy the refusal names is to set a password first, the same wording an
    administrative password set uses.

    **The sessions that provider opened are ended, and no others.** Somebody
    tidying up a link they no longer use is not signed out of everything; somebody
    removing a link because that provider account was compromised has every
    session it authenticated cut off. A session's `amr` is what tells those two
    apart, which is why it records the provider rather than a generic value.

    Refused with 409 `last-credential` before anything is written, so nothing about
    the user changes on the refusal.

    Args:
        environment_id (str):
        user_id (str):
        identity_id (str):

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
            identity_id=identity_id,
            client=client,
        )
    ).parsed
