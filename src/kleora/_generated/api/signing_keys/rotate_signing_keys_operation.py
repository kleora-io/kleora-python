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
from ...models.signing_key_rotate_in import SigningKeyRotateIn
from ...models.signing_key_rotated import SigningKeyRotated
from ...types import UNSET, Response, Unset


def _get_kwargs(
    environment_id: str,
    *,
    body: None | SigningKeyRotateIn | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/environments/{environment_id}/signing-keys/rotate".format(
            environment_id=quote(str(environment_id), safe=""),
        ),
    }

    if isinstance(body, SigningKeyRotateIn):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | SigningKeyRotated | None:
    if response.status_code == 200:
        response_200 = SigningKeyRotated.from_dict(response.json())

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
) -> Response[Problem | SigningKeyRotated]:
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
    body: None | SigningKeyRotateIn | Unset = UNSET,
) -> Response[Problem | SigningKeyRotated]:
    r"""Rotate the signing keys

     Rotate the environment's signing keys: `next` becomes `active`, the old `active` key is
    retired, and a new `next` key is announced.

    Audited as one `signing_key.rotated` event naming the three key ids. The body is optional;
    `{\"retire_immediately\": true}` is for a key compromise, and deletes the previously active key
    rather than retiring it, so it leaves the JWKS at once and tokens it signed stop verifying as
    caches refresh.

    The response is the keys' state after the rotation, as `GET .../signing-keys` and
    `/.well-known/jwks.json` report it.

    Args:
        environment_id (str):
        body (None | SigningKeyRotateIn | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | SigningKeyRotated]
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
    body: None | SigningKeyRotateIn | Unset = UNSET,
) -> Problem | SigningKeyRotated | None:
    r"""Rotate the signing keys

     Rotate the environment's signing keys: `next` becomes `active`, the old `active` key is
    retired, and a new `next` key is announced.

    Audited as one `signing_key.rotated` event naming the three key ids. The body is optional;
    `{\"retire_immediately\": true}` is for a key compromise, and deletes the previously active key
    rather than retiring it, so it leaves the JWKS at once and tokens it signed stop verifying as
    caches refresh.

    The response is the keys' state after the rotation, as `GET .../signing-keys` and
    `/.well-known/jwks.json` report it.

    Args:
        environment_id (str):
        body (None | SigningKeyRotateIn | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | SigningKeyRotated
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
    body: None | SigningKeyRotateIn | Unset = UNSET,
) -> Response[Problem | SigningKeyRotated]:
    r"""Rotate the signing keys

     Rotate the environment's signing keys: `next` becomes `active`, the old `active` key is
    retired, and a new `next` key is announced.

    Audited as one `signing_key.rotated` event naming the three key ids. The body is optional;
    `{\"retire_immediately\": true}` is for a key compromise, and deletes the previously active key
    rather than retiring it, so it leaves the JWKS at once and tokens it signed stop verifying as
    caches refresh.

    The response is the keys' state after the rotation, as `GET .../signing-keys` and
    `/.well-known/jwks.json` report it.

    Args:
        environment_id (str):
        body (None | SigningKeyRotateIn | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | SigningKeyRotated]
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
    body: None | SigningKeyRotateIn | Unset = UNSET,
) -> Problem | SigningKeyRotated | None:
    r"""Rotate the signing keys

     Rotate the environment's signing keys: `next` becomes `active`, the old `active` key is
    retired, and a new `next` key is announced.

    Audited as one `signing_key.rotated` event naming the three key ids. The body is optional;
    `{\"retire_immediately\": true}` is for a key compromise, and deletes the previously active key
    rather than retiring it, so it leaves the JWKS at once and tokens it signed stop verifying as
    caches refresh.

    The response is the keys' state after the rotation, as `GET .../signing-keys` and
    `/.well-known/jwks.json` report it.

    Args:
        environment_id (str):
        body (None | SigningKeyRotateIn | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | SigningKeyRotated
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
            body=body,
        )
    ).parsed
