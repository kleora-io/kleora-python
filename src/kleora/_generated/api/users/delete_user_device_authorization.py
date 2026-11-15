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
    authorization_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/environments/{environment_id}/users/{user_id}/device-authorizations/{authorization_id}".format(
            environment_id=quote(str(environment_id), safe=""),
            user_id=quote(str(user_id), safe=""),
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
    authorization_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | Problem]:
    r"""Revoke a device authorization

     Revoke it: the Session it opened, and every refresh token of that Session.

    device-grant.md §\"Living with the grant afterwards\": \"Revoking it is one
    action.\" That action is `apps.identity.services.device.revoke`, which is
    `sessions.revoke_session` plus the `device.revoked` event naming the client —
    so this never disagrees with `DELETE …/sessions/{id}` about what a revoked
    Session is. Access tokens already minted run to `exp`
    (sessions-and-tokens.md §\"Revocation semantics\"); what stops immediately is
    the credential's ability to renew itself.

    204, and idempotent: a second call finds the row already dead, writes no
    second event and answers the same. An id that is not this user's — or not a
    UUID — is the 404 a missing row gets, the same way the session routes answer.

    409 `conflict` for the row deleted under the write, which is the same race
    `DELETE …/sessions/{id}` documents: `identity.sessions.prune` and user
    erasure both remove Session rows.

    Args:
        environment_id (str):
        user_id (str):
        authorization_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        user_id=user_id,
        authorization_id=authorization_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    user_id: str,
    authorization_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | Problem | None:
    r"""Revoke a device authorization

     Revoke it: the Session it opened, and every refresh token of that Session.

    device-grant.md §\"Living with the grant afterwards\": \"Revoking it is one
    action.\" That action is `apps.identity.services.device.revoke`, which is
    `sessions.revoke_session` plus the `device.revoked` event naming the client —
    so this never disagrees with `DELETE …/sessions/{id}` about what a revoked
    Session is. Access tokens already minted run to `exp`
    (sessions-and-tokens.md §\"Revocation semantics\"); what stops immediately is
    the credential's ability to renew itself.

    204, and idempotent: a second call finds the row already dead, writes no
    second event and answers the same. An id that is not this user's — or not a
    UUID — is the 404 a missing row gets, the same way the session routes answer.

    409 `conflict` for the row deleted under the write, which is the same race
    `DELETE …/sessions/{id}` documents: `identity.sessions.prune` and user
    erasure both remove Session rows.

    Args:
        environment_id (str):
        user_id (str):
        authorization_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Problem
    """

    return sync_detailed(
        environment_id=environment_id,
        user_id=user_id,
        authorization_id=authorization_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    user_id: str,
    authorization_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | Problem]:
    r"""Revoke a device authorization

     Revoke it: the Session it opened, and every refresh token of that Session.

    device-grant.md §\"Living with the grant afterwards\": \"Revoking it is one
    action.\" That action is `apps.identity.services.device.revoke`, which is
    `sessions.revoke_session` plus the `device.revoked` event naming the client —
    so this never disagrees with `DELETE …/sessions/{id}` about what a revoked
    Session is. Access tokens already minted run to `exp`
    (sessions-and-tokens.md §\"Revocation semantics\"); what stops immediately is
    the credential's ability to renew itself.

    204, and idempotent: a second call finds the row already dead, writes no
    second event and answers the same. An id that is not this user's — or not a
    UUID — is the 404 a missing row gets, the same way the session routes answer.

    409 `conflict` for the row deleted under the write, which is the same race
    `DELETE …/sessions/{id}` documents: `identity.sessions.prune` and user
    erasure both remove Session rows.

    Args:
        environment_id (str):
        user_id (str):
        authorization_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        user_id=user_id,
        authorization_id=authorization_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    user_id: str,
    authorization_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | Problem | None:
    r"""Revoke a device authorization

     Revoke it: the Session it opened, and every refresh token of that Session.

    device-grant.md §\"Living with the grant afterwards\": \"Revoking it is one
    action.\" That action is `apps.identity.services.device.revoke`, which is
    `sessions.revoke_session` plus the `device.revoked` event naming the client —
    so this never disagrees with `DELETE …/sessions/{id}` about what a revoked
    Session is. Access tokens already minted run to `exp`
    (sessions-and-tokens.md §\"Revocation semantics\"); what stops immediately is
    the credential's ability to renew itself.

    204, and idempotent: a second call finds the row already dead, writes no
    second event and answers the same. An id that is not this user's — or not a
    UUID — is the 404 a missing row gets, the same way the session routes answer.

    409 `conflict` for the row deleted under the write, which is the same race
    `DELETE …/sessions/{id}` documents: `identity.sessions.prune` and user
    erasure both remove Session rows.

    Args:
        environment_id (str):
        user_id (str):
        authorization_id (str):

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
            authorization_id=authorization_id,
            client=client,
        )
    ).parsed
