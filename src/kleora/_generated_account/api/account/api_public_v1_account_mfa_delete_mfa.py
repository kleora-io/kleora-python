# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed self-service API document
# (https://id.kleora.eu/account/v1/openapi.json). `kleora.account` wraps this tree; nothing outside the
# package imports it.
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.flow_problem import FlowProblem
from ...types import Response


def _get_kwargs(
    factor_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/account/v1/mfa/{factor_id}".format(
            factor_id=quote(str(factor_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | FlowProblem | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = FlowProblem.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FlowProblem.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = FlowProblem.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = FlowProblem.from_dict(response.json())

        return response_429

    if response.status_code == 503:
        response_503 = FlowProblem.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | FlowProblem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    factor_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | FlowProblem]:
    """Remove the signed-in person's own second factor

     Remove one of the person's MFA factors.

    `403 mfa-required` for the last factor when the environment requires MFA. `404` for a malformed
    id and for another person's factor alike. Removing a TOTP factor also removes the recovery
    codes, and the other way round.

    Args:
        factor_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FlowProblem]
    """

    kwargs = _get_kwargs(
        factor_id=factor_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    factor_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | FlowProblem | None:
    """Remove the signed-in person's own second factor

     Remove one of the person's MFA factors.

    `403 mfa-required` for the last factor when the environment requires MFA. `404` for a malformed
    id and for another person's factor alike. Removing a TOTP factor also removes the recovery
    codes, and the other way round.

    Args:
        factor_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FlowProblem
    """

    return sync_detailed(
        factor_id=factor_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    factor_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | FlowProblem]:
    """Remove the signed-in person's own second factor

     Remove one of the person's MFA factors.

    `403 mfa-required` for the last factor when the environment requires MFA. `404` for a malformed
    id and for another person's factor alike. Removing a TOTP factor also removes the recovery
    codes, and the other way round.

    Args:
        factor_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FlowProblem]
    """

    kwargs = _get_kwargs(
        factor_id=factor_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    factor_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | FlowProblem | None:
    """Remove the signed-in person's own second factor

     Remove one of the person's MFA factors.

    `403 mfa-required` for the last factor when the environment requires MFA. `404` for a malformed
    id and for another person's factor alike. Removing a TOTP factor also removes the recovery
    codes, and the other way round.

    Args:
        factor_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FlowProblem
    """

    return (
        await asyncio_detailed(
            factor_id=factor_id,
            client=client,
        )
    ).parsed
