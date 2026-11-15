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
from ...models.identity_provider_out import IdentityProviderOut
from ...models.problem import Problem
from ...models.read_identity_provider_kind import ReadIdentityProviderKind
from ...types import Response


def _get_kwargs(
    environment_id: str,
    kind: ReadIdentityProviderKind,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/environments/{environment_id}/identity-providers/{kind}".format(
            environment_id=quote(str(environment_id), safe=""),
            kind=quote(str(kind), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IdentityProviderOut | Problem | None:
    if response.status_code == 200:
        response_200 = IdentityProviderOut.from_dict(response.json())

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
) -> Response[IdentityProviderOut | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    environment_id: str,
    kind: ReadIdentityProviderKind,
    *,
    client: AuthenticatedClient,
) -> Response[IdentityProviderOut | Problem]:
    """An identity provider

     One identity provider's configuration. The client secret is never returned.

    `404` when this environment has not configured that kind. `client_secret_set` and
    `client_secret_updated_at` say whether a secret is stored and when it last changed.

    Args:
        environment_id (str):
        kind (ReadIdentityProviderKind):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentityProviderOut | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        kind=kind,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    kind: ReadIdentityProviderKind,
    *,
    client: AuthenticatedClient,
) -> IdentityProviderOut | Problem | None:
    """An identity provider

     One identity provider's configuration. The client secret is never returned.

    `404` when this environment has not configured that kind. `client_secret_set` and
    `client_secret_updated_at` say whether a secret is stored and when it last changed.

    Args:
        environment_id (str):
        kind (ReadIdentityProviderKind):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentityProviderOut | Problem
    """

    return sync_detailed(
        environment_id=environment_id,
        kind=kind,
        client=client,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    kind: ReadIdentityProviderKind,
    *,
    client: AuthenticatedClient,
) -> Response[IdentityProviderOut | Problem]:
    """An identity provider

     One identity provider's configuration. The client secret is never returned.

    `404` when this environment has not configured that kind. `client_secret_set` and
    `client_secret_updated_at` say whether a secret is stored and when it last changed.

    Args:
        environment_id (str):
        kind (ReadIdentityProviderKind):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentityProviderOut | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        kind=kind,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    kind: ReadIdentityProviderKind,
    *,
    client: AuthenticatedClient,
) -> IdentityProviderOut | Problem | None:
    """An identity provider

     One identity provider's configuration. The client secret is never returned.

    `404` when this environment has not configured that kind. `client_secret_set` and
    `client_secret_updated_at` say whether a secret is stored and when it last changed.

    Args:
        environment_id (str):
        kind (ReadIdentityProviderKind):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentityProviderOut | Problem
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            kind=kind,
            client=client,
        )
    ).parsed
