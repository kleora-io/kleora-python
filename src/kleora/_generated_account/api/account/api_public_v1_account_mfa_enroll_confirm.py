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
from ...models.enroll_confirm_in import EnrollConfirmIn
from ...models.flow_problem import FlowProblem
from ...models.recovery_codes_out import RecoveryCodesOut
from ...types import Response


def _get_kwargs(
    *,
    body: EnrollConfirmIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/account/v1/mfa/enroll/confirm",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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

    if response.status_code == 409:
        response_409 = FlowProblem.from_dict(response.json())

        return response_409

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
    body: EnrollConfirmIn,
) -> Response[FlowProblem | RecoveryCodesOut]:
    """Confirm TOTP enrolment, and receive the recovery codes once

     Verify a TOTP code, confirm the factor, and return the ten recovery codes, once.

    The codes cannot be read back later. A wrong code is `401 invalid-code`, the same answer as for
    a locked account. Confirming does not change the current session's authentication methods
    (`amr`); the next sign-in asks for the factor.

    Args:
        body (EnrollConfirmIn): The six digits. No `req`: this surface has no login chain to be
            bound to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlowProblem | RecoveryCodesOut]
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
    body: EnrollConfirmIn,
) -> FlowProblem | RecoveryCodesOut | None:
    """Confirm TOTP enrolment, and receive the recovery codes once

     Verify a TOTP code, confirm the factor, and return the ten recovery codes, once.

    The codes cannot be read back later. A wrong code is `401 invalid-code`, the same answer as for
    a locked account. Confirming does not change the current session's authentication methods
    (`amr`); the next sign-in asks for the factor.

    Args:
        body (EnrollConfirmIn): The six digits. No `req`: this surface has no login chain to be
            bound to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlowProblem | RecoveryCodesOut
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: EnrollConfirmIn,
) -> Response[FlowProblem | RecoveryCodesOut]:
    """Confirm TOTP enrolment, and receive the recovery codes once

     Verify a TOTP code, confirm the factor, and return the ten recovery codes, once.

    The codes cannot be read back later. A wrong code is `401 invalid-code`, the same answer as for
    a locked account. Confirming does not change the current session's authentication methods
    (`amr`); the next sign-in asks for the factor.

    Args:
        body (EnrollConfirmIn): The six digits. No `req`: this surface has no login chain to be
            bound to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlowProblem | RecoveryCodesOut]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: EnrollConfirmIn,
) -> FlowProblem | RecoveryCodesOut | None:
    """Confirm TOTP enrolment, and receive the recovery codes once

     Verify a TOTP code, confirm the factor, and return the ten recovery codes, once.

    The codes cannot be read back later. A wrong code is `401 invalid-code`, the same answer as for
    a locked account. Confirming does not change the current session's authentication methods
    (`amr`); the next sign-in asks for the factor.

    Args:
        body (EnrollConfirmIn): The six digits. No `req`: this surface has no login chain to be
            bound to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlowProblem | RecoveryCodesOut
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
