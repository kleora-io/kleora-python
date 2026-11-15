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
from ...models.identity_in import IdentityIn
from ...models.identity_out import IdentityOut
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    environment_id: str,
    user_id: str,
    *,
    body: IdentityIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/environments/{environment_id}/users/{user_id}/identities".format(
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
) -> IdentityOut | Problem | None:
    if response.status_code == 200:
        response_200 = IdentityOut.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = IdentityOut.from_dict(response.json())

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
) -> Response[IdentityOut | Problem]:
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
    body: IdentityIn,
) -> Response[IdentityOut | Problem]:
    """Link a provider account to a user

     Link an external provider account to this user, by the provider's subject identifier.

    `provider_subject` is the provider's own permanent id for the person, never an email address.

    - `201` with a `Location` header when the link is new.
    - `200` when that subject is already linked to this user, with no second audit event.
    - `409 provider-already-linked` when the subject is linked to another user of this environment.
      It is never moved; merge the two users instead.

    The link records no provider email or verification status; they are filled in at the person's
    next sign-in through that provider.

    Args:
        environment_id (str):
        user_id (str):
        body (IdentityIn): The body of `POST .../users/{user_id}/identities`: an external provider
            account to link, by
            subject.

            `provider_subject` is the provider's own permanent id for the person (Google's `sub`,
            GitHub's
            numeric `id`, Microsoft's `oid`, Facebook's app-scoped `id`), never an email address. Any
            other
            field, such as a provider email, token or secret, is refused as unknown.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentityOut | Problem]
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
    body: IdentityIn,
) -> IdentityOut | Problem | None:
    """Link a provider account to a user

     Link an external provider account to this user, by the provider's subject identifier.

    `provider_subject` is the provider's own permanent id for the person, never an email address.

    - `201` with a `Location` header when the link is new.
    - `200` when that subject is already linked to this user, with no second audit event.
    - `409 provider-already-linked` when the subject is linked to another user of this environment.
      It is never moved; merge the two users instead.

    The link records no provider email or verification status; they are filled in at the person's
    next sign-in through that provider.

    Args:
        environment_id (str):
        user_id (str):
        body (IdentityIn): The body of `POST .../users/{user_id}/identities`: an external provider
            account to link, by
            subject.

            `provider_subject` is the provider's own permanent id for the person (Google's `sub`,
            GitHub's
            numeric `id`, Microsoft's `oid`, Facebook's app-scoped `id`), never an email address. Any
            other
            field, such as a provider email, token or secret, is refused as unknown.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentityOut | Problem
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
    body: IdentityIn,
) -> Response[IdentityOut | Problem]:
    """Link a provider account to a user

     Link an external provider account to this user, by the provider's subject identifier.

    `provider_subject` is the provider's own permanent id for the person, never an email address.

    - `201` with a `Location` header when the link is new.
    - `200` when that subject is already linked to this user, with no second audit event.
    - `409 provider-already-linked` when the subject is linked to another user of this environment.
      It is never moved; merge the two users instead.

    The link records no provider email or verification status; they are filled in at the person's
    next sign-in through that provider.

    Args:
        environment_id (str):
        user_id (str):
        body (IdentityIn): The body of `POST .../users/{user_id}/identities`: an external provider
            account to link, by
            subject.

            `provider_subject` is the provider's own permanent id for the person (Google's `sub`,
            GitHub's
            numeric `id`, Microsoft's `oid`, Facebook's app-scoped `id`), never an email address. Any
            other
            field, such as a provider email, token or secret, is refused as unknown.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentityOut | Problem]
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
    body: IdentityIn,
) -> IdentityOut | Problem | None:
    """Link a provider account to a user

     Link an external provider account to this user, by the provider's subject identifier.

    `provider_subject` is the provider's own permanent id for the person, never an email address.

    - `201` with a `Location` header when the link is new.
    - `200` when that subject is already linked to this user, with no second audit event.
    - `409 provider-already-linked` when the subject is linked to another user of this environment.
      It is never moved; merge the two users instead.

    The link records no provider email or verification status; they are filled in at the person's
    next sign-in through that provider.

    Args:
        environment_id (str):
        user_id (str):
        body (IdentityIn): The body of `POST .../users/{user_id}/identities`: an external provider
            account to link, by
            subject.

            `provider_subject` is the provider's own permanent id for the person (Google's `sub`,
            GitHub's
            numeric `id`, Microsoft's `oid`, Facebook's app-scoped `id`), never an email address. Any
            other
            field, such as a provider email, token or secret, is refused as unknown.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentityOut | Problem
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            user_id=user_id,
            client=client,
            body=body,
        )
    ).parsed
