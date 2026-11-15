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
from ...models.delete_identity_provider_kind import DeleteIdentityProviderKind
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    environment_id: str,
    kind: DeleteIdentityProviderKind,
    *,
    force: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["force"] = force

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/environments/{environment_id}/identity-providers/{kind}".format(
            environment_id=quote(str(environment_id), safe=""),
            kind=quote(str(kind), safe=""),
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
    kind: DeleteIdentityProviderKind,
    *,
    client: AuthenticatedClient,
    force: bool | Unset = False,
) -> Response[Any | Problem]:
    """Delete an identity provider

     Remove an identity provider's configuration. The identities it authenticated are kept.

    `409 provider-in-use`, with the number of identities, while any identity of that provider exists
    in the environment; `?force=1` proceeds anyway. People whose only credential is that provider
    can no longer sign in once it is removed.

    Args:
        environment_id (str):
        kind (DeleteIdentityProviderKind):
        force (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        kind=kind,
        force=force,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    kind: DeleteIdentityProviderKind,
    *,
    client: AuthenticatedClient,
    force: bool | Unset = False,
) -> Any | Problem | None:
    """Delete an identity provider

     Remove an identity provider's configuration. The identities it authenticated are kept.

    `409 provider-in-use`, with the number of identities, while any identity of that provider exists
    in the environment; `?force=1` proceeds anyway. People whose only credential is that provider
    can no longer sign in once it is removed.

    Args:
        environment_id (str):
        kind (DeleteIdentityProviderKind):
        force (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Problem
    """

    return sync_detailed(
        environment_id=environment_id,
        kind=kind,
        client=client,
        force=force,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    kind: DeleteIdentityProviderKind,
    *,
    client: AuthenticatedClient,
    force: bool | Unset = False,
) -> Response[Any | Problem]:
    """Delete an identity provider

     Remove an identity provider's configuration. The identities it authenticated are kept.

    `409 provider-in-use`, with the number of identities, while any identity of that provider exists
    in the environment; `?force=1` proceeds anyway. People whose only credential is that provider
    can no longer sign in once it is removed.

    Args:
        environment_id (str):
        kind (DeleteIdentityProviderKind):
        force (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        kind=kind,
        force=force,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    kind: DeleteIdentityProviderKind,
    *,
    client: AuthenticatedClient,
    force: bool | Unset = False,
) -> Any | Problem | None:
    """Delete an identity provider

     Remove an identity provider's configuration. The identities it authenticated are kept.

    `409 provider-in-use`, with the number of identities, while any identity of that provider exists
    in the environment; `?force=1` proceeds anyway. People whose only credential is that provider
    can no longer sign in once it is removed.

    Args:
        environment_id (str):
        kind (DeleteIdentityProviderKind):
        force (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Problem
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            kind=kind,
            client=client,
            force=force,
        )
    ).parsed
