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
from ...models.deletion_out import DeletionOut
from ...models.flow_problem import FlowProblem
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/account/v1/deletion",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeletionOut | FlowProblem | None:
    if response.status_code == 202:
        response_202 = DeletionOut.from_dict(response.json())

        return response_202

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
) -> Response[DeletionOut | FlowProblem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[DeletionOut | FlowProblem]:
    """Ask for the signed-in person's own account to be deleted

     Schedule the deletion of the signed-in person's account in seven days, and email them a link
    that cancels it.

    Takes no body; the re-authentication is the confirmation. Answers `202` because the account has
    not been deleted yet: `erase_after` is the moment it will be, so a screen can tell the person
    when.

    Every session of the person is revoked. If a deletion is already scheduled, the answer is the
    same `202` with the same `erase_after`, and nothing is sent. `409 last-owner` when the person is
    the last active owner of a tenant that must always have one.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeletionOut | FlowProblem]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> DeletionOut | FlowProblem | None:
    """Ask for the signed-in person's own account to be deleted

     Schedule the deletion of the signed-in person's account in seven days, and email them a link
    that cancels it.

    Takes no body; the re-authentication is the confirmation. Answers `202` because the account has
    not been deleted yet: `erase_after` is the moment it will be, so a screen can tell the person
    when.

    Every session of the person is revoked. If a deletion is already scheduled, the answer is the
    same `202` with the same `erase_after`, and nothing is sent. `409 last-owner` when the person is
    the last active owner of a tenant that must always have one.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeletionOut | FlowProblem
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[DeletionOut | FlowProblem]:
    """Ask for the signed-in person's own account to be deleted

     Schedule the deletion of the signed-in person's account in seven days, and email them a link
    that cancels it.

    Takes no body; the re-authentication is the confirmation. Answers `202` because the account has
    not been deleted yet: `erase_after` is the moment it will be, so a screen can tell the person
    when.

    Every session of the person is revoked. If a deletion is already scheduled, the answer is the
    same `202` with the same `erase_after`, and nothing is sent. `409 last-owner` when the person is
    the last active owner of a tenant that must always have one.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeletionOut | FlowProblem]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> DeletionOut | FlowProblem | None:
    """Ask for the signed-in person's own account to be deleted

     Schedule the deletion of the signed-in person's account in seven days, and email them a link
    that cancels it.

    Takes no body; the re-authentication is the confirmation. Answers `202` because the account has
    not been deleted yet: `erase_after` is the moment it will be, so a screen can tell the person
    when.

    Every session of the person is revoked. If a deletion is already scheduled, the answer is the
    same `202` with the same `erase_after`, and nothing is sent. `409 last-owner` when the person is
    the last active owner of a tenant that must always have one.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeletionOut | FlowProblem
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
