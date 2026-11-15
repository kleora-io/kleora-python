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
from ...models.password_policy_out import PasswordPolicyOut
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/account/v1/password",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FlowProblem | PasswordPolicyOut | None:
    if response.status_code == 200:
        response_200 = PasswordPolicyOut.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = FlowProblem.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FlowProblem.from_dict(response.json())

        return response_403

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
) -> Response[FlowProblem | PasswordPolicyOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[FlowProblem | PasswordPolicyOut]:
    """Whether the signed-in person has a password, and the rules for a new one

     What a password form needs before anything is typed: whether the person has a password, the
    minimum length, and whether new passwords are checked against known breaches.

    All three come from the environment's settings. `has_password` decides whether to ask for the
    current password.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlowProblem | PasswordPolicyOut]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> FlowProblem | PasswordPolicyOut | None:
    """Whether the signed-in person has a password, and the rules for a new one

     What a password form needs before anything is typed: whether the person has a password, the
    minimum length, and whether new passwords are checked against known breaches.

    All three come from the environment's settings. `has_password` decides whether to ask for the
    current password.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlowProblem | PasswordPolicyOut
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[FlowProblem | PasswordPolicyOut]:
    """Whether the signed-in person has a password, and the rules for a new one

     What a password form needs before anything is typed: whether the person has a password, the
    minimum length, and whether new passwords are checked against known breaches.

    All three come from the environment's settings. `has_password` decides whether to ask for the
    current password.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlowProblem | PasswordPolicyOut]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> FlowProblem | PasswordPolicyOut | None:
    """Whether the signed-in person has a password, and the rules for a new one

     What a password form needs before anything is typed: whether the person has a password, the
    minimum length, and whether new passwords are checked against known breaches.

    All three come from the environment's settings. `has_password` decides whether to ask for the
    current password.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlowProblem | PasswordPolicyOut
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
