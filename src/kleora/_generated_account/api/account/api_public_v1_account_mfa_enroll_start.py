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
from ...models.enroll_start_out import EnrollStartOut
from ...models.flow_problem import FlowProblem
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/account/v1/mfa/enroll/start",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EnrollStartOut | FlowProblem | None:
    if response.status_code == 200:
        response_200 = EnrollStartOut.from_dict(response.json())

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
) -> Response[EnrollStartOut | FlowProblem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[EnrollStartOut | FlowProblem]:
    r"""Begin TOTP enrolment

     Seed a factor (or reuse the pending one) and return the secret once.

    Sensitive, and §\"The operations\" marks the whole write column so. The reason
    is not procedural, and `api.public.v1.flow.mfa` argues it at length: a caller
    holding only a session — a stolen token, XSS — could otherwise plant a factor
    of *their own* on an account with none, which under `optional` policy starts
    challenging the legitimate owner at every login for a code only the attacker
    holds, with no self-service way back (removal is gated too) short of an
    administrative reset.

    `409 mfa-already-enrolled` because \"at most one confirmed TOTP factor\"
    (`mfa.md` §TOTP): without it a signed-in caller could re-enrol and silently
    replace a confirmed factor outside the gated remove flow.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnrollStartOut | FlowProblem]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> EnrollStartOut | FlowProblem | None:
    r"""Begin TOTP enrolment

     Seed a factor (or reuse the pending one) and return the secret once.

    Sensitive, and §\"The operations\" marks the whole write column so. The reason
    is not procedural, and `api.public.v1.flow.mfa` argues it at length: a caller
    holding only a session — a stolen token, XSS — could otherwise plant a factor
    of *their own* on an account with none, which under `optional` policy starts
    challenging the legitimate owner at every login for a code only the attacker
    holds, with no self-service way back (removal is gated too) short of an
    administrative reset.

    `409 mfa-already-enrolled` because \"at most one confirmed TOTP factor\"
    (`mfa.md` §TOTP): without it a signed-in caller could re-enrol and silently
    replace a confirmed factor outside the gated remove flow.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnrollStartOut | FlowProblem
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[EnrollStartOut | FlowProblem]:
    r"""Begin TOTP enrolment

     Seed a factor (or reuse the pending one) and return the secret once.

    Sensitive, and §\"The operations\" marks the whole write column so. The reason
    is not procedural, and `api.public.v1.flow.mfa` argues it at length: a caller
    holding only a session — a stolen token, XSS — could otherwise plant a factor
    of *their own* on an account with none, which under `optional` policy starts
    challenging the legitimate owner at every login for a code only the attacker
    holds, with no self-service way back (removal is gated too) short of an
    administrative reset.

    `409 mfa-already-enrolled` because \"at most one confirmed TOTP factor\"
    (`mfa.md` §TOTP): without it a signed-in caller could re-enrol and silently
    replace a confirmed factor outside the gated remove flow.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnrollStartOut | FlowProblem]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> EnrollStartOut | FlowProblem | None:
    r"""Begin TOTP enrolment

     Seed a factor (or reuse the pending one) and return the secret once.

    Sensitive, and §\"The operations\" marks the whole write column so. The reason
    is not procedural, and `api.public.v1.flow.mfa` argues it at length: a caller
    holding only a session — a stolen token, XSS — could otherwise plant a factor
    of *their own* on an account with none, which under `optional` policy starts
    challenging the legitimate owner at every login for a code only the attacker
    holds, with no self-service way back (removal is gated too) short of an
    administrative reset.

    `409 mfa-already-enrolled` because \"at most one confirmed TOTP factor\"
    (`mfa.md` §TOTP): without it a signed-in caller could re-enrol and silently
    replace a confirmed factor outside the gated remove flow.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnrollStartOut | FlowProblem
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
