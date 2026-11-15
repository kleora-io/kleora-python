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
from ...models.email_out import EmailOut
from ...models.flow_problem import FlowProblem
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/account/v1/email",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EmailOut | FlowProblem | None:
    if response.status_code == 200:
        response_200 = EmailOut.from_dict(response.json())

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
) -> Response[EmailOut | FlowProblem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[EmailOut | FlowProblem]:
    r"""The signed-in person's own address, and whether a change is outstanding

     `{email, email_verified, change_pending}`.

    `change_pending` is read from the existence of an unspent `change_email`
    `ActionToken` — §\"Changing an email address\": \"there is exactly one place the
    pending address is written and no second place for it to be wrong\".

    **It never names the pending address**, only that there is one. The address is on
    the token and the token was mailed to it; a `GET` that echoed it would hand a
    stolen session the one fact a person could otherwise notice from the mail in their
    own inbox, and §API asks for a bool.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailOut | FlowProblem]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> EmailOut | FlowProblem | None:
    r"""The signed-in person's own address, and whether a change is outstanding

     `{email, email_verified, change_pending}`.

    `change_pending` is read from the existence of an unspent `change_email`
    `ActionToken` — §\"Changing an email address\": \"there is exactly one place the
    pending address is written and no second place for it to be wrong\".

    **It never names the pending address**, only that there is one. The address is on
    the token and the token was mailed to it; a `GET` that echoed it would hand a
    stolen session the one fact a person could otherwise notice from the mail in their
    own inbox, and §API asks for a bool.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmailOut | FlowProblem
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[EmailOut | FlowProblem]:
    r"""The signed-in person's own address, and whether a change is outstanding

     `{email, email_verified, change_pending}`.

    `change_pending` is read from the existence of an unspent `change_email`
    `ActionToken` — §\"Changing an email address\": \"there is exactly one place the
    pending address is written and no second place for it to be wrong\".

    **It never names the pending address**, only that there is one. The address is on
    the token and the token was mailed to it; a `GET` that echoed it would hand a
    stolen session the one fact a person could otherwise notice from the mail in their
    own inbox, and §API asks for a bool.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailOut | FlowProblem]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> EmailOut | FlowProblem | None:
    r"""The signed-in person's own address, and whether a change is outstanding

     `{email, email_verified, change_pending}`.

    `change_pending` is read from the existence of an unspent `change_email`
    `ActionToken` — §\"Changing an email address\": \"there is exactly one place the
    pending address is written and no second place for it to be wrong\".

    **It never names the pending address**, only that there is one. The address is on
    the token and the token was mailed to it; a `GET` that echoed it would hand a
    stolen session the one fact a person could otherwise notice from the mail in their
    own inbox, and §API asks for a bool.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmailOut | FlowProblem
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
