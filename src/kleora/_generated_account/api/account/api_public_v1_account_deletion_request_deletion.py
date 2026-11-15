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
    r"""Ask for the signed-in person's own account to be deleted

     Schedule this person's erasure for seven days' time, and mail them the undo.

    **No body.** §API's row has none, and there is nothing a caller could usefully
    put in one: there is no user id on this surface, the grace period is ours, and a
    \"reason\" would be free text about a person we are about to erase. The
    re-authentication is the confirmation.

    `202`, not `204` and not `200`: the thing asked for has not happened yet.
    `erase_after` is the moment it will, which is what lets a screen say \"your account
    will be deleted on …\" — §\"What happens, and when\" requires that the delay be
    \"said on the page in plain words\", and a page can only say it if the API does.

    `409 last-owner` through the predicate `DELETE .../users/{id}` already applies
    (ADR 0013): the service asks `guard_erasure`, and this handler only translates.
    The `detail` is deliberately *not* the management surface's
    `LAST_OWNER_ERASURE_DETAIL` — that one is written for an operator erasing somebody
    else (\"give another member 'owner' first\" addressed to a third party) — but the
    slug is byte-identical, which is the half that is contract.

    **An outstanding request answers the same `202` with the same date, and sends
    nothing.** `AlreadyRequested` is not a refusal here, for two reasons: it cannot be
    reached through this surface anyway — the first request revoked every session, so a
    second token is `401 session-revoked` at `AccountAuth` — and §\"Failure modes\" gives
    this route no slug for it, so answering one would mean a problem document nothing
    declares. Idempotent is the honest reading: the state the caller asked for holds,
    and `erase_after` is read off the row rather than recomputed as \"now plus seven
    days\", which would quietly *move* a deadline a person has already been told.

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
    r"""Ask for the signed-in person's own account to be deleted

     Schedule this person's erasure for seven days' time, and mail them the undo.

    **No body.** §API's row has none, and there is nothing a caller could usefully
    put in one: there is no user id on this surface, the grace period is ours, and a
    \"reason\" would be free text about a person we are about to erase. The
    re-authentication is the confirmation.

    `202`, not `204` and not `200`: the thing asked for has not happened yet.
    `erase_after` is the moment it will, which is what lets a screen say \"your account
    will be deleted on …\" — §\"What happens, and when\" requires that the delay be
    \"said on the page in plain words\", and a page can only say it if the API does.

    `409 last-owner` through the predicate `DELETE .../users/{id}` already applies
    (ADR 0013): the service asks `guard_erasure`, and this handler only translates.
    The `detail` is deliberately *not* the management surface's
    `LAST_OWNER_ERASURE_DETAIL` — that one is written for an operator erasing somebody
    else (\"give another member 'owner' first\" addressed to a third party) — but the
    slug is byte-identical, which is the half that is contract.

    **An outstanding request answers the same `202` with the same date, and sends
    nothing.** `AlreadyRequested` is not a refusal here, for two reasons: it cannot be
    reached through this surface anyway — the first request revoked every session, so a
    second token is `401 session-revoked` at `AccountAuth` — and §\"Failure modes\" gives
    this route no slug for it, so answering one would mean a problem document nothing
    declares. Idempotent is the honest reading: the state the caller asked for holds,
    and `erase_after` is read off the row rather than recomputed as \"now plus seven
    days\", which would quietly *move* a deadline a person has already been told.

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
    r"""Ask for the signed-in person's own account to be deleted

     Schedule this person's erasure for seven days' time, and mail them the undo.

    **No body.** §API's row has none, and there is nothing a caller could usefully
    put in one: there is no user id on this surface, the grace period is ours, and a
    \"reason\" would be free text about a person we are about to erase. The
    re-authentication is the confirmation.

    `202`, not `204` and not `200`: the thing asked for has not happened yet.
    `erase_after` is the moment it will, which is what lets a screen say \"your account
    will be deleted on …\" — §\"What happens, and when\" requires that the delay be
    \"said on the page in plain words\", and a page can only say it if the API does.

    `409 last-owner` through the predicate `DELETE .../users/{id}` already applies
    (ADR 0013): the service asks `guard_erasure`, and this handler only translates.
    The `detail` is deliberately *not* the management surface's
    `LAST_OWNER_ERASURE_DETAIL` — that one is written for an operator erasing somebody
    else (\"give another member 'owner' first\" addressed to a third party) — but the
    slug is byte-identical, which is the half that is contract.

    **An outstanding request answers the same `202` with the same date, and sends
    nothing.** `AlreadyRequested` is not a refusal here, for two reasons: it cannot be
    reached through this surface anyway — the first request revoked every session, so a
    second token is `401 session-revoked` at `AccountAuth` — and §\"Failure modes\" gives
    this route no slug for it, so answering one would mean a problem document nothing
    declares. Idempotent is the honest reading: the state the caller asked for holds,
    and `erase_after` is read off the row rather than recomputed as \"now plus seven
    days\", which would quietly *move* a deadline a person has already been told.

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
    r"""Ask for the signed-in person's own account to be deleted

     Schedule this person's erasure for seven days' time, and mail them the undo.

    **No body.** §API's row has none, and there is nothing a caller could usefully
    put in one: there is no user id on this surface, the grace period is ours, and a
    \"reason\" would be free text about a person we are about to erase. The
    re-authentication is the confirmation.

    `202`, not `204` and not `200`: the thing asked for has not happened yet.
    `erase_after` is the moment it will, which is what lets a screen say \"your account
    will be deleted on …\" — §\"What happens, and when\" requires that the delay be
    \"said on the page in plain words\", and a page can only say it if the API does.

    `409 last-owner` through the predicate `DELETE .../users/{id}` already applies
    (ADR 0013): the service asks `guard_erasure`, and this handler only translates.
    The `detail` is deliberately *not* the management surface's
    `LAST_OWNER_ERASURE_DETAIL` — that one is written for an operator erasing somebody
    else (\"give another member 'owner' first\" addressed to a third party) — but the
    slug is byte-identical, which is the half that is contract.

    **An outstanding request answers the same `202` with the same date, and sends
    nothing.** `AlreadyRequested` is not a refusal here, for two reasons: it cannot be
    reached through this surface anyway — the first request revoked every session, so a
    second token is `401 session-revoked` at `AccountAuth` — and §\"Failure modes\" gives
    this route no slug for it, so answering one would mean a problem document nothing
    declares. Idempotent is the honest reading: the state the caller asked for holds,
    and `erase_after` is read off the row rather than recomputed as \"now plus seven
    days\", which would quietly *move* a deadline a person has already been told.

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
