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
from ...models.flow_problem import FlowProblem
from ...models.password_in import PasswordIn
from ...types import Response


def _get_kwargs(
    *,
    body: PasswordIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/account/v1/password",
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

    if response.status_code == 401:
        response_401 = FlowProblem.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FlowProblem.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = FlowProblem.from_dict(response.json())

        return response_422

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
    body: PasswordIn,
) -> Response[Any | FlowProblem]:
    r"""Change the signed-in person's own password

     Change the person's password, or set one if they have none.

    Requires a recent re-authentication. What happens depends on whether the person already has a
    password, never on what the caller sent:

    - **They have one:** `current_password` is verified. A wrong or missing one is `401
      invalid-credentials`. Every other session is revoked; this one keeps working.
    - **They have none:** no `current_password` is needed. Every session is revoked, including this
      one.

    A new password the policy refuses is `422 password-policy` or `422 password-breached`, with
    `errors[].field = \"password\"`.

    Args:
        body (PasswordIn): The body of `POST /password`.

            `current_password` is required when the person has a password, and omitted when they have
            none;
            a missing or wrong one is `401 invalid-credentials`. Length is checked by the
            environment's
            password policy, which answers `422 password-policy` with `errors[].field = "password"`.

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
    body: PasswordIn,
) -> Any | FlowProblem | None:
    r"""Change the signed-in person's own password

     Change the person's password, or set one if they have none.

    Requires a recent re-authentication. What happens depends on whether the person already has a
    password, never on what the caller sent:

    - **They have one:** `current_password` is verified. A wrong or missing one is `401
      invalid-credentials`. Every other session is revoked; this one keeps working.
    - **They have none:** no `current_password` is needed. Every session is revoked, including this
      one.

    A new password the policy refuses is `422 password-policy` or `422 password-breached`, with
    `errors[].field = \"password\"`.

    Args:
        body (PasswordIn): The body of `POST /password`.

            `current_password` is required when the person has a password, and omitted when they have
            none;
            a missing or wrong one is `401 invalid-credentials`. Length is checked by the
            environment's
            password policy, which answers `422 password-policy` with `errors[].field = "password"`.

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
    body: PasswordIn,
) -> Response[Any | FlowProblem]:
    r"""Change the signed-in person's own password

     Change the person's password, or set one if they have none.

    Requires a recent re-authentication. What happens depends on whether the person already has a
    password, never on what the caller sent:

    - **They have one:** `current_password` is verified. A wrong or missing one is `401
      invalid-credentials`. Every other session is revoked; this one keeps working.
    - **They have none:** no `current_password` is needed. Every session is revoked, including this
      one.

    A new password the policy refuses is `422 password-policy` or `422 password-breached`, with
    `errors[].field = \"password\"`.

    Args:
        body (PasswordIn): The body of `POST /password`.

            `current_password` is required when the person has a password, and omitted when they have
            none;
            a missing or wrong one is `401 invalid-credentials`. Length is checked by the
            environment's
            password policy, which answers `422 password-policy` with `errors[].field = "password"`.

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
    body: PasswordIn,
) -> Any | FlowProblem | None:
    r"""Change the signed-in person's own password

     Change the person's password, or set one if they have none.

    Requires a recent re-authentication. What happens depends on whether the person already has a
    password, never on what the caller sent:

    - **They have one:** `current_password` is verified. A wrong or missing one is `401
      invalid-credentials`. Every other session is revoked; this one keeps working.
    - **They have none:** no `current_password` is needed. Every session is revoked, including this
      one.

    A new password the policy refuses is `422 password-policy` or `422 password-breached`, with
    `errors[].field = \"password\"`.

    Args:
        body (PasswordIn): The body of `POST /password`.

            `current_password` is required when the person has a password, and omitted when they have
            none;
            a missing or wrong one is `401 invalid-credentials`. Length is checked by the
            environment's
            password policy, which answers `422 password-policy` with `errors[].field = "password"`.

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
