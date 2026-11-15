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
from ...models.client_created import ClientCreated
from ...models.client_in import ClientIn
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    environment_id: str,
    *,
    body: ClientIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/environments/{environment_id}/clients".format(
            environment_id=quote(str(environment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ClientCreated | Problem | None:
    if response.status_code == 201:
        response_201 = ClientCreated.from_dict(response.json())

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
) -> Response[ClientCreated | Problem]:
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
    body: ClientIn,
) -> Response[ClientCreated | Problem]:
    r"""Create a client

     A `spa`, `web` or `native` client, with a `client_id` we mint.

    For `kind: \"web\"` the 201 carries the secret, once, under the shown-once
    rules — `no_store` on the response and nothing that could show it again. A
    replay under the same `Idempotency-Key` returns the stored body including
    the secret, because that is the same response and the store holds it under
    the same guarantees.

    Args:
        environment_id (str):
        body (ClientIn): `POST /api/v1/environments/{environment_id}/clients`.

            `extra="forbid"` is the whole of the "not an input field" rule: `client_id`,
            `client_secret`, `has_secret`, `environment_id` and `is_default` are 422 as
            unknown fields, and `is_default` in particular is settable only by `PATCH`
            and only to `true` — a new client is never silently the one the hosted pages
            fall back to (clients.md §`POST …/clients`).

            The one rule about the arrays that does not depend on the environment is
            here: at most `MAX_URIS` entries each, so the bound reaches the OpenAPI
            document and a generated client refuses the thirty-third before we do.

            The rest of the URI and scope rules are not here: they depend on the *environment*
            (`http://localhost` is a sandbox-only value), which a schema cannot see, so
            the router checks them against the resolved environment and names the array
            index the caller sent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClientCreated | Problem]
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
    body: ClientIn,
) -> ClientCreated | Problem | None:
    r"""Create a client

     A `spa`, `web` or `native` client, with a `client_id` we mint.

    For `kind: \"web\"` the 201 carries the secret, once, under the shown-once
    rules — `no_store` on the response and nothing that could show it again. A
    replay under the same `Idempotency-Key` returns the stored body including
    the secret, because that is the same response and the store holds it under
    the same guarantees.

    Args:
        environment_id (str):
        body (ClientIn): `POST /api/v1/environments/{environment_id}/clients`.

            `extra="forbid"` is the whole of the "not an input field" rule: `client_id`,
            `client_secret`, `has_secret`, `environment_id` and `is_default` are 422 as
            unknown fields, and `is_default` in particular is settable only by `PATCH`
            and only to `true` — a new client is never silently the one the hosted pages
            fall back to (clients.md §`POST …/clients`).

            The one rule about the arrays that does not depend on the environment is
            here: at most `MAX_URIS` entries each, so the bound reaches the OpenAPI
            document and a generated client refuses the thirty-third before we do.

            The rest of the URI and scope rules are not here: they depend on the *environment*
            (`http://localhost` is a sandbox-only value), which a schema cannot see, so
            the router checks them against the resolved environment and names the array
            index the caller sent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClientCreated | Problem
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
    body: ClientIn,
) -> Response[ClientCreated | Problem]:
    r"""Create a client

     A `spa`, `web` or `native` client, with a `client_id` we mint.

    For `kind: \"web\"` the 201 carries the secret, once, under the shown-once
    rules — `no_store` on the response and nothing that could show it again. A
    replay under the same `Idempotency-Key` returns the stored body including
    the secret, because that is the same response and the store holds it under
    the same guarantees.

    Args:
        environment_id (str):
        body (ClientIn): `POST /api/v1/environments/{environment_id}/clients`.

            `extra="forbid"` is the whole of the "not an input field" rule: `client_id`,
            `client_secret`, `has_secret`, `environment_id` and `is_default` are 422 as
            unknown fields, and `is_default` in particular is settable only by `PATCH`
            and only to `true` — a new client is never silently the one the hosted pages
            fall back to (clients.md §`POST …/clients`).

            The one rule about the arrays that does not depend on the environment is
            here: at most `MAX_URIS` entries each, so the bound reaches the OpenAPI
            document and a generated client refuses the thirty-third before we do.

            The rest of the URI and scope rules are not here: they depend on the *environment*
            (`http://localhost` is a sandbox-only value), which a schema cannot see, so
            the router checks them against the resolved environment and names the array
            index the caller sent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClientCreated | Problem]
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
    body: ClientIn,
) -> ClientCreated | Problem | None:
    r"""Create a client

     A `spa`, `web` or `native` client, with a `client_id` we mint.

    For `kind: \"web\"` the 201 carries the secret, once, under the shown-once
    rules — `no_store` on the response and nothing that could show it again. A
    replay under the same `Idempotency-Key` returns the stored body including
    the secret, because that is the same response and the store holds it under
    the same guarantees.

    Args:
        environment_id (str):
        body (ClientIn): `POST /api/v1/environments/{environment_id}/clients`.

            `extra="forbid"` is the whole of the "not an input field" rule: `client_id`,
            `client_secret`, `has_secret`, `environment_id` and `is_default` are 422 as
            unknown fields, and `is_default` in particular is settable only by `PATCH`
            and only to `true` — a new client is never silently the one the hosted pages
            fall back to (clients.md §`POST …/clients`).

            The one rule about the arrays that does not depend on the environment is
            here: at most `MAX_URIS` entries each, so the bound reaches the OpenAPI
            document and a generated client refuses the thirty-third before we do.

            The rest of the URI and scope rules are not here: they depend on the *environment*
            (`http://localhost` is a sandbox-only value), which a schema cannot see, so
            the router checks them against the resolved environment and names the array
            index the caller sent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClientCreated | Problem
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
            body=body,
        )
    ).parsed
