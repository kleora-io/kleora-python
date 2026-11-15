# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.me_enroll_confirm_body import MeEnrollConfirmBody
from ...models.me_recovery_codes_out import MeRecoveryCodesOut
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    *,
    body: MeEnrollConfirmBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/me/mfa/totp/confirm",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MeRecoveryCodesOut | Problem | None:
    if response.status_code == 200:
        response_200 = MeRecoveryCodesOut.from_dict(response.json())

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
) -> Response[MeRecoveryCodesOut | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: MeEnrollConfirmBody,
) -> Response[MeRecoveryCodesOut | Problem]:
    r"""Confirm the caller's own TOTP enrolment

     Verifies `code`, confirms the pending factor, and returns the ten
    recovery codes once — the one place on this surface a secret appears in a
    body, and it appears once (`mfa.md`'s \"shown once\" rule, unrelaxed here).

    Args:
        body (MeEnrollConfirmBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MeRecoveryCodesOut | Problem]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: MeEnrollConfirmBody,
) -> MeRecoveryCodesOut | Problem | None:
    r"""Confirm the caller's own TOTP enrolment

     Verifies `code`, confirms the pending factor, and returns the ten
    recovery codes once — the one place on this surface a secret appears in a
    body, and it appears once (`mfa.md`'s \"shown once\" rule, unrelaxed here).

    Args:
        body (MeEnrollConfirmBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MeRecoveryCodesOut | Problem
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: MeEnrollConfirmBody,
) -> Response[MeRecoveryCodesOut | Problem]:
    r"""Confirm the caller's own TOTP enrolment

     Verifies `code`, confirms the pending factor, and returns the ten
    recovery codes once — the one place on this surface a secret appears in a
    body, and it appears once (`mfa.md`'s \"shown once\" rule, unrelaxed here).

    Args:
        body (MeEnrollConfirmBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MeRecoveryCodesOut | Problem]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: MeEnrollConfirmBody,
) -> MeRecoveryCodesOut | Problem | None:
    r"""Confirm the caller's own TOTP enrolment

     Verifies `code`, confirms the pending factor, and returns the ten
    recovery codes once — the one place on this surface a secret appears in a
    body, and it appears once (`mfa.md`'s \"shown once\" rule, unrelaxed here).

    Args:
        body (MeEnrollConfirmBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MeRecoveryCodesOut | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
