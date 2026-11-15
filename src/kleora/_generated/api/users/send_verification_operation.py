# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.sent_out import SentOut
from ...types import Response


def _get_kwargs(
    environment_id: str,
    user_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/environments/{environment_id}/users/{user_id}/send-verification".format(
            environment_id=quote(str(environment_id), safe=""),
            user_id=quote(str(user_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | SentOut | None:
    if response.status_code == 200:
        response_200 = SentOut.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Problem.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = Problem.from_dict(response.json())

        return response_402

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
) -> Response[Problem | SentOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    environment_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Problem | SentOut]:
    r"""Send a verification email

     Mail the `verify_email` link, under the per-user send budget.

    An address that is already verified is a no-op: `{\"sent\": false}`, no
    message, and no slot of the budget spent. users-and-credentials.md wants it
    to \"still report success\", which a 200 is; what it must not do is charge
    somebody's mailbox budget for a message nobody sent, because that is how
    five real sends become four.

    One status and one shape, with `sent` carrying the difference —
    `{\"sent\": true}` means exactly \"one went out\", so a caller can tell the two
    apart without reading `email_verified_at` back, and a generated client has
    a single response type to unwrap. (Ruled in review of P2-10; the spec will
    say so.)

    The budget is `apps.identity.throttles`, and it is **one** budget: this
    endpoint, `…/send-password-reset` and the hosted resend form all spend the
    same windows, because the rule protects somebody's mailbox from us and a
    mailbox does not care which endpoint asked.

    Args:
        environment_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | SentOut]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Problem | SentOut | None:
    r"""Send a verification email

     Mail the `verify_email` link, under the per-user send budget.

    An address that is already verified is a no-op: `{\"sent\": false}`, no
    message, and no slot of the budget spent. users-and-credentials.md wants it
    to \"still report success\", which a 200 is; what it must not do is charge
    somebody's mailbox budget for a message nobody sent, because that is how
    five real sends become four.

    One status and one shape, with `sent` carrying the difference —
    `{\"sent\": true}` means exactly \"one went out\", so a caller can tell the two
    apart without reading `email_verified_at` back, and a generated client has
    a single response type to unwrap. (Ruled in review of P2-10; the spec will
    say so.)

    The budget is `apps.identity.throttles`, and it is **one** budget: this
    endpoint, `…/send-password-reset` and the hosted resend form all spend the
    same windows, because the rule protects somebody's mailbox from us and a
    mailbox does not care which endpoint asked.

    Args:
        environment_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | SentOut
    """

    return sync_detailed(
        environment_id=environment_id,
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Problem | SentOut]:
    r"""Send a verification email

     Mail the `verify_email` link, under the per-user send budget.

    An address that is already verified is a no-op: `{\"sent\": false}`, no
    message, and no slot of the budget spent. users-and-credentials.md wants it
    to \"still report success\", which a 200 is; what it must not do is charge
    somebody's mailbox budget for a message nobody sent, because that is how
    five real sends become four.

    One status and one shape, with `sent` carrying the difference —
    `{\"sent\": true}` means exactly \"one went out\", so a caller can tell the two
    apart without reading `email_verified_at` back, and a generated client has
    a single response type to unwrap. (Ruled in review of P2-10; the spec will
    say so.)

    The budget is `apps.identity.throttles`, and it is **one** budget: this
    endpoint, `…/send-password-reset` and the hosted resend form all spend the
    same windows, because the rule protects somebody's mailbox from us and a
    mailbox does not care which endpoint asked.

    Args:
        environment_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | SentOut]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Problem | SentOut | None:
    r"""Send a verification email

     Mail the `verify_email` link, under the per-user send budget.

    An address that is already verified is a no-op: `{\"sent\": false}`, no
    message, and no slot of the budget spent. users-and-credentials.md wants it
    to \"still report success\", which a 200 is; what it must not do is charge
    somebody's mailbox budget for a message nobody sent, because that is how
    five real sends become four.

    One status and one shape, with `sent` carrying the difference —
    `{\"sent\": true}` means exactly \"one went out\", so a caller can tell the two
    apart without reading `email_verified_at` back, and a generated client has
    a single response type to unwrap. (Ruled in review of P2-10; the spec will
    say so.)

    The budget is `apps.identity.throttles`, and it is **one** budget: this
    endpoint, `…/send-password-reset` and the hosted resend form all spend the
    same windows, because the rule protects somebody's mailbox from us and a
    mailbox does not care which endpoint asked.

    Args:
        environment_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | SentOut
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            user_id=user_id,
            client=client,
        )
    ).parsed
