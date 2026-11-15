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
    factor_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/me/mfa/{factor_id}".format(
            factor_id=quote(str(factor_id), safe=""),
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
    factor_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | Problem]:
    r"""Remove one of the caller's own factors

     One route for either kind — `management-api.md` §\"/me/mfa\": \"Remove
    one, under the same rules self-service follows\" — dispatching to
    `apps.identity.services.webauthn.remove_credential` for a passkey and to
    `apps.identity.services.mfa.remove_factors` (which removes TOTP and the
    shared recovery set together) for anything else, each behind its own kind's
    removal-refusal rule.

    Args:
        factor_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Problem]
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
) -> Any | Problem | None:
    r"""Remove one of the caller's own factors

     One route for either kind — `management-api.md` §\"/me/mfa\": \"Remove
    one, under the same rules self-service follows\" — dispatching to
    `apps.identity.services.webauthn.remove_credential` for a passkey and to
    `apps.identity.services.mfa.remove_factors` (which removes TOTP and the
    shared recovery set together) for anything else, each behind its own kind's
    removal-refusal rule.

    Args:
        factor_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Problem
    """

    return sync_detailed(
        factor_id=factor_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    factor_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | Problem]:
    r"""Remove one of the caller's own factors

     One route for either kind — `management-api.md` §\"/me/mfa\": \"Remove
    one, under the same rules self-service follows\" — dispatching to
    `apps.identity.services.webauthn.remove_credential` for a passkey and to
    `apps.identity.services.mfa.remove_factors` (which removes TOTP and the
    shared recovery set together) for anything else, each behind its own kind's
    removal-refusal rule.

    Args:
        factor_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Problem]
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
) -> Any | Problem | None:
    r"""Remove one of the caller's own factors

     One route for either kind — `management-api.md` §\"/me/mfa\": \"Remove
    one, under the same rules self-service follows\" — dispatching to
    `apps.identity.services.webauthn.remove_credential` for a passkey and to
    `apps.identity.services.mfa.remove_factors` (which removes TOTP and the
    shared recovery set together) for anything else, each behind its own kind's
    removal-refusal rule.

    Args:
        factor_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Problem
    """

    return (
        await asyncio_detailed(
            factor_id=factor_id,
            client=client,
        )
    ).parsed
