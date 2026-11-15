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
from ...models.api_key_out import ApiKeyOut
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    environment_id: str,
    api_key_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/environments/{environment_id}/api-keys/{api_key_id}/revoke".format(
            environment_id=quote(str(environment_id), safe=""),
            api_key_id=quote(str(api_key_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiKeyOut | Problem | None:
    if response.status_code == 200:
        response_200 = ApiKeyOut.from_dict(response.json())

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
) -> Response[ApiKeyOut | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    environment_id: str,
    api_key_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiKeyOut | Problem]:
    """Revoke an API key

     Stop the key authenticating, keeping the row. Idempotent.

    The very next request with that key is 401, and revoking an already revoked
    key answers 200 with the same row rather than a conflict: the end state the
    caller asked for is the end state. Only the first one writes the event.

    404 when a `DELETE` commits between this operation's own lookup and the
    service's — the row is gone, and 200 with a `status` read off an instance
    that no longer has a row behind it would be a worse answer than the one the
    second `DELETE` gets.

    Args:
        environment_id (str):
        api_key_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKeyOut | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        api_key_id=api_key_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    api_key_id: str,
    *,
    client: AuthenticatedClient,
) -> ApiKeyOut | Problem | None:
    """Revoke an API key

     Stop the key authenticating, keeping the row. Idempotent.

    The very next request with that key is 401, and revoking an already revoked
    key answers 200 with the same row rather than a conflict: the end state the
    caller asked for is the end state. Only the first one writes the event.

    404 when a `DELETE` commits between this operation's own lookup and the
    service's — the row is gone, and 200 with a `status` read off an instance
    that no longer has a row behind it would be a worse answer than the one the
    second `DELETE` gets.

    Args:
        environment_id (str):
        api_key_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKeyOut | Problem
    """

    return sync_detailed(
        environment_id=environment_id,
        api_key_id=api_key_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    api_key_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiKeyOut | Problem]:
    """Revoke an API key

     Stop the key authenticating, keeping the row. Idempotent.

    The very next request with that key is 401, and revoking an already revoked
    key answers 200 with the same row rather than a conflict: the end state the
    caller asked for is the end state. Only the first one writes the event.

    404 when a `DELETE` commits between this operation's own lookup and the
    service's — the row is gone, and 200 with a `status` read off an instance
    that no longer has a row behind it would be a worse answer than the one the
    second `DELETE` gets.

    Args:
        environment_id (str):
        api_key_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKeyOut | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        api_key_id=api_key_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    api_key_id: str,
    *,
    client: AuthenticatedClient,
) -> ApiKeyOut | Problem | None:
    """Revoke an API key

     Stop the key authenticating, keeping the row. Idempotent.

    The very next request with that key is 401, and revoking an already revoked
    key answers 200 with the same row rather than a conflict: the end state the
    caller asked for is the end state. Only the first one writes the event.

    404 when a `DELETE` commits between this operation's own lookup and the
    service's — the row is gone, and 200 with a `status` read off an instance
    that no longer has a row behind it would be a worse answer than the one the
    second `DELETE` gets.

    Args:
        environment_id (str):
        api_key_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKeyOut | Problem
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            api_key_id=api_key_id,
            client=client,
        )
    ).parsed
