# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed self-service API document
# (https://id.kleora.eu/account/v1/openapi.json). `kleora.account` wraps this tree; nothing outside the
# package imports it.
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.flow_problem import FlowProblem
from ...models.recovery_codes_out import RecoveryCodesOut
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/account/v1/mfa/recovery/regenerate",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FlowProblem | RecoveryCodesOut | None:
    if response.status_code == 200:
        response_200 = RecoveryCodesOut.from_dict(response.json())

        return response_200

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
) -> Response[FlowProblem | RecoveryCodesOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[FlowProblem | RecoveryCodesOut]:
    """Replace the signed-in person's own recovery-code set

     Replace the person's recovery codes with ten new ones, returned once.

    Requires a recent re-authentication. `404` when the person holds no confirmed second factor (a
    TOTP factor or a passkey), since recovery codes only back one up.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlowProblem | RecoveryCodesOut]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> FlowProblem | RecoveryCodesOut | None:
    """Replace the signed-in person's own recovery-code set

     Replace the person's recovery codes with ten new ones, returned once.

    Requires a recent re-authentication. `404` when the person holds no confirmed second factor (a
    TOTP factor or a passkey), since recovery codes only back one up.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlowProblem | RecoveryCodesOut
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[FlowProblem | RecoveryCodesOut]:
    """Replace the signed-in person's own recovery-code set

     Replace the person's recovery codes with ten new ones, returned once.

    Requires a recent re-authentication. `404` when the person holds no confirmed second factor (a
    TOTP factor or a passkey), since recovery codes only back one up.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlowProblem | RecoveryCodesOut]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> FlowProblem | RecoveryCodesOut | None:
    """Replace the signed-in person's own recovery-code set

     Replace the person's recovery codes with ten new ones, returned once.

    Requires a recent re-authentication. `404` when the person holds no confirmed second factor (a
    TOTP factor or a passkey), since recovery codes only back one up.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlowProblem | RecoveryCodesOut
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
