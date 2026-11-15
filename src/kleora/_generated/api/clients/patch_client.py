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
from ...models.client_out import ClientOut
from ...models.client_patch import ClientPatch
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    environment_id: str,
    client_id: str,
    *,
    body: ClientPatch,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/environments/{environment_id}/clients/{client_id}".format(
            environment_id=quote(str(environment_id), safe=""),
            client_id=quote(str(client_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ClientOut | Problem | None:
    if response.status_code == 200:
        response_200 = ClientOut.from_dict(response.json())

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
) -> Response[ClientOut | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    environment_id: str,
    client_id: str,
    *,
    client: AuthenticatedClient,
    body: ClientPatch,
) -> Response[ClientOut | Problem]:
    r"""Change a client

     A merge patch over the client's own properties. Never a secret.

    Three answers that are the resource's rather than the schema's.
    `{\"is_default\": false}` is 409 `client-default`: an environment always has
    one default, and the way to stop being it is for another client to become
    it. A write the partial unique index refuses is 409 `conflict` rather than a
    500 — the backstop for a swap interleaved with a delete. And a `kind` change
    away from `web` clears the secret, which is 200 with `has_secret: false`.

    Args:
        environment_id (str):
        client_id (str):
        body (ClientPatch): `PATCH /api/v1/environments/{environment_id}/clients/{client_id}`.

            `initiate_login_uri` is the one clearable field: `null` means "this client
            names no landing", and the hosted pages then carry no link at all. The two
            URI arrays are replaced whole by a merge patch, and `[]` is a valid value
            distinct from the `null` neither of them accepts.

            `is_default` is a plain `bool`, which is what makes `{"is_default": null}`
            answer 422 `field-not-nullable` rather than a type error: the field has no
            null state, and a merge patch's `null` would mean the same impossible thing
            `false` does. `false` itself passes the schema and is refused by the
            resource, as 409 `client-default`.

            `client_id`, `client_secret`, `has_secret` and `environment_id` are unknown
            fields rather than immutable ones, because the spec answers them that way:
            the identifier is not a property a caller addresses at all
            (clients.md §"Failure modes").

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClientOut | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        client_id=client_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    client_id: str,
    *,
    client: AuthenticatedClient,
    body: ClientPatch,
) -> ClientOut | Problem | None:
    r"""Change a client

     A merge patch over the client's own properties. Never a secret.

    Three answers that are the resource's rather than the schema's.
    `{\"is_default\": false}` is 409 `client-default`: an environment always has
    one default, and the way to stop being it is for another client to become
    it. A write the partial unique index refuses is 409 `conflict` rather than a
    500 — the backstop for a swap interleaved with a delete. And a `kind` change
    away from `web` clears the secret, which is 200 with `has_secret: false`.

    Args:
        environment_id (str):
        client_id (str):
        body (ClientPatch): `PATCH /api/v1/environments/{environment_id}/clients/{client_id}`.

            `initiate_login_uri` is the one clearable field: `null` means "this client
            names no landing", and the hosted pages then carry no link at all. The two
            URI arrays are replaced whole by a merge patch, and `[]` is a valid value
            distinct from the `null` neither of them accepts.

            `is_default` is a plain `bool`, which is what makes `{"is_default": null}`
            answer 422 `field-not-nullable` rather than a type error: the field has no
            null state, and a merge patch's `null` would mean the same impossible thing
            `false` does. `false` itself passes the schema and is refused by the
            resource, as 409 `client-default`.

            `client_id`, `client_secret`, `has_secret` and `environment_id` are unknown
            fields rather than immutable ones, because the spec answers them that way:
            the identifier is not a property a caller addresses at all
            (clients.md §"Failure modes").

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClientOut | Problem
    """

    return sync_detailed(
        environment_id=environment_id,
        client_id=client_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    client_id: str,
    *,
    client: AuthenticatedClient,
    body: ClientPatch,
) -> Response[ClientOut | Problem]:
    r"""Change a client

     A merge patch over the client's own properties. Never a secret.

    Three answers that are the resource's rather than the schema's.
    `{\"is_default\": false}` is 409 `client-default`: an environment always has
    one default, and the way to stop being it is for another client to become
    it. A write the partial unique index refuses is 409 `conflict` rather than a
    500 — the backstop for a swap interleaved with a delete. And a `kind` change
    away from `web` clears the secret, which is 200 with `has_secret: false`.

    Args:
        environment_id (str):
        client_id (str):
        body (ClientPatch): `PATCH /api/v1/environments/{environment_id}/clients/{client_id}`.

            `initiate_login_uri` is the one clearable field: `null` means "this client
            names no landing", and the hosted pages then carry no link at all. The two
            URI arrays are replaced whole by a merge patch, and `[]` is a valid value
            distinct from the `null` neither of them accepts.

            `is_default` is a plain `bool`, which is what makes `{"is_default": null}`
            answer 422 `field-not-nullable` rather than a type error: the field has no
            null state, and a merge patch's `null` would mean the same impossible thing
            `false` does. `false` itself passes the schema and is refused by the
            resource, as 409 `client-default`.

            `client_id`, `client_secret`, `has_secret` and `environment_id` are unknown
            fields rather than immutable ones, because the spec answers them that way:
            the identifier is not a property a caller addresses at all
            (clients.md §"Failure modes").

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClientOut | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        client_id=client_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    client_id: str,
    *,
    client: AuthenticatedClient,
    body: ClientPatch,
) -> ClientOut | Problem | None:
    r"""Change a client

     A merge patch over the client's own properties. Never a secret.

    Three answers that are the resource's rather than the schema's.
    `{\"is_default\": false}` is 409 `client-default`: an environment always has
    one default, and the way to stop being it is for another client to become
    it. A write the partial unique index refuses is 409 `conflict` rather than a
    500 — the backstop for a swap interleaved with a delete. And a `kind` change
    away from `web` clears the secret, which is 200 with `has_secret: false`.

    Args:
        environment_id (str):
        client_id (str):
        body (ClientPatch): `PATCH /api/v1/environments/{environment_id}/clients/{client_id}`.

            `initiate_login_uri` is the one clearable field: `null` means "this client
            names no landing", and the hosted pages then carry no link at all. The two
            URI arrays are replaced whole by a merge patch, and `[]` is a valid value
            distinct from the `null` neither of them accepts.

            `is_default` is a plain `bool`, which is what makes `{"is_default": null}`
            answer 422 `field-not-nullable` rather than a type error: the field has no
            null state, and a merge patch's `null` would mean the same impossible thing
            `false` does. `false` itself passes the schema and is refused by the
            resource, as 409 `client-default`.

            `client_id`, `client_secret`, `has_secret` and `environment_id` are unknown
            fields rather than immutable ones, because the spec answers them that way:
            the identifier is not a property a caller addresses at all
            (clients.md §"Failure modes").

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClientOut | Problem
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client_id=client_id,
            client=client,
            body=body,
        )
    ).parsed
