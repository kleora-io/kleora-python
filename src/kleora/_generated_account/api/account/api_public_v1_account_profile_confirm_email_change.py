# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed self-service API document
# (https://id.kleora.eu/account/v1/openapi.json). `kleora.account` wraps this tree; nothing outside the
# package imports it.
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.email_confirm_in import EmailConfirmIn
from ...models.flow_problem import FlowProblem
from ...types import Response


def _get_kwargs(
    *,
    body: EmailConfirmIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/account/v1/email/confirm",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | FlowProblem | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = FlowProblem.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FlowProblem.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FlowProblem.from_dict(response.json())

        return response_403

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
) -> Response[Any | FlowProblem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: EmailConfirmIn,
) -> Response[Any | FlowProblem]:
    """Confirm a new email address with the token from the emailed link

     Step 2 of changing the email address: spend the emailed token and move the address.

    Requires the person's bearer token as well as the emailed token, but no further
    re-authentication. A token that is unknown, already used, expired or issued to somebody else is
    `400 invalid-token`. `409 email-taken` when the new address has since been registered in this
    environment.

    Args:
        body (EmailConfirmIn): The body of `POST /email/confirm`: the token from the confirmation
            link.

            Only the `POST` spends the token, so a mail scanner that follows the link cannot. A token
            that
            is unknown, already used or expired is `400 invalid-token`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FlowProblem]
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
    body: EmailConfirmIn,
) -> Any | FlowProblem | None:
    """Confirm a new email address with the token from the emailed link

     Step 2 of changing the email address: spend the emailed token and move the address.

    Requires the person's bearer token as well as the emailed token, but no further
    re-authentication. A token that is unknown, already used, expired or issued to somebody else is
    `400 invalid-token`. `409 email-taken` when the new address has since been registered in this
    environment.

    Args:
        body (EmailConfirmIn): The body of `POST /email/confirm`: the token from the confirmation
            link.

            Only the `POST` spends the token, so a mail scanner that follows the link cannot. A token
            that
            is unknown, already used or expired is `400 invalid-token`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FlowProblem
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: EmailConfirmIn,
) -> Response[Any | FlowProblem]:
    """Confirm a new email address with the token from the emailed link

     Step 2 of changing the email address: spend the emailed token and move the address.

    Requires the person's bearer token as well as the emailed token, but no further
    re-authentication. A token that is unknown, already used, expired or issued to somebody else is
    `400 invalid-token`. `409 email-taken` when the new address has since been registered in this
    environment.

    Args:
        body (EmailConfirmIn): The body of `POST /email/confirm`: the token from the confirmation
            link.

            Only the `POST` spends the token, so a mail scanner that follows the link cannot. A token
            that
            is unknown, already used or expired is `400 invalid-token`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FlowProblem]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: EmailConfirmIn,
) -> Any | FlowProblem | None:
    """Confirm a new email address with the token from the emailed link

     Step 2 of changing the email address: spend the emailed token and move the address.

    Requires the person's bearer token as well as the emailed token, but no further
    re-authentication. A token that is unknown, already used, expired or issued to somebody else is
    `400 invalid-token`. `409 email-taken` when the new address has since been registered in this
    environment.

    Args:
        body (EmailConfirmIn): The body of `POST /email/confirm`: the token from the confirmation
            link.

            Only the `POST` spends the token, so a mail scanner that follows the link cannot. A token
            that
            is unknown, already used or expired is `400 invalid-token`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FlowProblem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
