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
    r"""Confirm a new email address with the token from the emailed link

     Step 2 of two: spend the mailed token and move the address.

    The operation §API omits; the row is drafted in `U10-05`'s Log and three things
    about it are decisions rather than defaults:

    * **Authenticated.** §API's note under the table calls `DELETE /deletion` \"the one
      route on this surface that takes no bearer token\", and one is one. It also means
      an attacker who can read the new mailbox but holds no token cannot move the
      address — the mailbox and the session are two credentials and this step wants
      both.
    * **Not sensitive.** §\"Failure modes\" gives this route `invalid-token` and
      `email-taken` and no `reauth-required`, and step 1 already took a
      re-authentication. A second password prompt in front of clicking a link we
      ourselves mailed would teach people to type their password at prompts that did
      not need it.
    * **The token must be the caller's own**, and a token that is somebody else's is
      `400 invalid-token` rather than a `403` — one document for every way a token
      cannot be spent, so a caller holding a guessed one learns nothing from which
      reason refused it.

    Args:
        body (EmailConfirmIn): `POST /email/confirm` with `{token}` — the row drafted in
            `U10-05`'s Log.

            The operation §API omits: §"Changing an email address" step 2 requires a route
            the mailed token is `POST`ed to ("only the `POST` spends it, so a mail scanner
            cannot") and §"Failure modes" declares its two refusals, but the table has no row.

            No `max_length` bound below the column's: a token is 32 random bytes as URL-safe
            base64 and the only thing that matters about a wrong one is that it is wrong, so
            a length refusal would answer `422` where §"Failure modes" says `400
            invalid-token` — one answer for unknown, spent and expired, and a bound would
            make a fourth.

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
    r"""Confirm a new email address with the token from the emailed link

     Step 2 of two: spend the mailed token and move the address.

    The operation §API omits; the row is drafted in `U10-05`'s Log and three things
    about it are decisions rather than defaults:

    * **Authenticated.** §API's note under the table calls `DELETE /deletion` \"the one
      route on this surface that takes no bearer token\", and one is one. It also means
      an attacker who can read the new mailbox but holds no token cannot move the
      address — the mailbox and the session are two credentials and this step wants
      both.
    * **Not sensitive.** §\"Failure modes\" gives this route `invalid-token` and
      `email-taken` and no `reauth-required`, and step 1 already took a
      re-authentication. A second password prompt in front of clicking a link we
      ourselves mailed would teach people to type their password at prompts that did
      not need it.
    * **The token must be the caller's own**, and a token that is somebody else's is
      `400 invalid-token` rather than a `403` — one document for every way a token
      cannot be spent, so a caller holding a guessed one learns nothing from which
      reason refused it.

    Args:
        body (EmailConfirmIn): `POST /email/confirm` with `{token}` — the row drafted in
            `U10-05`'s Log.

            The operation §API omits: §"Changing an email address" step 2 requires a route
            the mailed token is `POST`ed to ("only the `POST` spends it, so a mail scanner
            cannot") and §"Failure modes" declares its two refusals, but the table has no row.

            No `max_length` bound below the column's: a token is 32 random bytes as URL-safe
            base64 and the only thing that matters about a wrong one is that it is wrong, so
            a length refusal would answer `422` where §"Failure modes" says `400
            invalid-token` — one answer for unknown, spent and expired, and a bound would
            make a fourth.

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
    r"""Confirm a new email address with the token from the emailed link

     Step 2 of two: spend the mailed token and move the address.

    The operation §API omits; the row is drafted in `U10-05`'s Log and three things
    about it are decisions rather than defaults:

    * **Authenticated.** §API's note under the table calls `DELETE /deletion` \"the one
      route on this surface that takes no bearer token\", and one is one. It also means
      an attacker who can read the new mailbox but holds no token cannot move the
      address — the mailbox and the session are two credentials and this step wants
      both.
    * **Not sensitive.** §\"Failure modes\" gives this route `invalid-token` and
      `email-taken` and no `reauth-required`, and step 1 already took a
      re-authentication. A second password prompt in front of clicking a link we
      ourselves mailed would teach people to type their password at prompts that did
      not need it.
    * **The token must be the caller's own**, and a token that is somebody else's is
      `400 invalid-token` rather than a `403` — one document for every way a token
      cannot be spent, so a caller holding a guessed one learns nothing from which
      reason refused it.

    Args:
        body (EmailConfirmIn): `POST /email/confirm` with `{token}` — the row drafted in
            `U10-05`'s Log.

            The operation §API omits: §"Changing an email address" step 2 requires a route
            the mailed token is `POST`ed to ("only the `POST` spends it, so a mail scanner
            cannot") and §"Failure modes" declares its two refusals, but the table has no row.

            No `max_length` bound below the column's: a token is 32 random bytes as URL-safe
            base64 and the only thing that matters about a wrong one is that it is wrong, so
            a length refusal would answer `422` where §"Failure modes" says `400
            invalid-token` — one answer for unknown, spent and expired, and a bound would
            make a fourth.

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
    r"""Confirm a new email address with the token from the emailed link

     Step 2 of two: spend the mailed token and move the address.

    The operation §API omits; the row is drafted in `U10-05`'s Log and three things
    about it are decisions rather than defaults:

    * **Authenticated.** §API's note under the table calls `DELETE /deletion` \"the one
      route on this surface that takes no bearer token\", and one is one. It also means
      an attacker who can read the new mailbox but holds no token cannot move the
      address — the mailbox and the session are two credentials and this step wants
      both.
    * **Not sensitive.** §\"Failure modes\" gives this route `invalid-token` and
      `email-taken` and no `reauth-required`, and step 1 already took a
      re-authentication. A second password prompt in front of clicking a link we
      ourselves mailed would teach people to type their password at prompts that did
      not need it.
    * **The token must be the caller's own**, and a token that is somebody else's is
      `400 invalid-token` rather than a `403` — one document for every way a token
      cannot be spent, so a caller holding a guessed one learns nothing from which
      reason refused it.

    Args:
        body (EmailConfirmIn): `POST /email/confirm` with `{token}` — the row drafted in
            `U10-05`'s Log.

            The operation §API omits: §"Changing an email address" step 2 requires a route
            the mailed token is `POST`ed to ("only the `POST` spends it, so a mail scanner
            cannot") and §"Failure modes" declares its two refusals, but the table has no row.

            No `max_length` bound below the column's: a token is 32 random bytes as URL-safe
            base64 and the only thing that matters about a wrong one is that it is wrong, so
            a length refusal would answer `422` where §"Failure modes" says `400
            invalid-token` — one answer for unknown, spent and expired, and a bound would
            make a fourth.

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
