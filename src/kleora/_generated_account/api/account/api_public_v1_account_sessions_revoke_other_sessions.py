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
from ...models.revoked_out import RevokedOut
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/account/v1/sessions/revoke-others",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FlowProblem | RevokedOut | None:
    if response.status_code == 200:
        response_200 = RevokedOut.from_dict(response.json())

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
) -> Response[FlowProblem | RevokedOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[FlowProblem | RevokedOut]:
    r"""Sign every other device out

     Every live session except this token's, and the count of what went.

    Not sensitive, and not a `revoke-all`: see the module docstring for both. The
    count is what a screen puts in its confirmation — \"3 other devices signed
    out\" — and is the reason this is not a `204`.

    `sessions.revoke_all_for_user` rather than a loop over `_live`, because that
    service is what also emits the `sessions.revoked_all` summary the taxonomy
    defines: \"without it, revoking forty sessions is forty rows and no record of
    the single act that caused them\". It is one transaction, it cascades to the
    refresh families, and `except_session` is exactly this token's own — the
    argument that function already exists to take.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlowProblem | RevokedOut]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> FlowProblem | RevokedOut | None:
    r"""Sign every other device out

     Every live session except this token's, and the count of what went.

    Not sensitive, and not a `revoke-all`: see the module docstring for both. The
    count is what a screen puts in its confirmation — \"3 other devices signed
    out\" — and is the reason this is not a `204`.

    `sessions.revoke_all_for_user` rather than a loop over `_live`, because that
    service is what also emits the `sessions.revoked_all` summary the taxonomy
    defines: \"without it, revoking forty sessions is forty rows and no record of
    the single act that caused them\". It is one transaction, it cascades to the
    refresh families, and `except_session` is exactly this token's own — the
    argument that function already exists to take.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlowProblem | RevokedOut
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[FlowProblem | RevokedOut]:
    r"""Sign every other device out

     Every live session except this token's, and the count of what went.

    Not sensitive, and not a `revoke-all`: see the module docstring for both. The
    count is what a screen puts in its confirmation — \"3 other devices signed
    out\" — and is the reason this is not a `204`.

    `sessions.revoke_all_for_user` rather than a loop over `_live`, because that
    service is what also emits the `sessions.revoked_all` summary the taxonomy
    defines: \"without it, revoking forty sessions is forty rows and no record of
    the single act that caused them\". It is one transaction, it cascades to the
    refresh families, and `except_session` is exactly this token's own — the
    argument that function already exists to take.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlowProblem | RevokedOut]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> FlowProblem | RevokedOut | None:
    r"""Sign every other device out

     Every live session except this token's, and the count of what went.

    Not sensitive, and not a `revoke-all`: see the module docstring for both. The
    count is what a screen puts in its confirmation — \"3 other devices signed
    out\" — and is the reason this is not a `204`.

    `sessions.revoke_all_for_user` rather than a loop over `_live`, because that
    service is what also emits the `sessions.revoked_all` summary the taxonomy
    defines: \"without it, revoking forty sessions is forty rows and no record of
    the single act that caused them\". It is one transaction, it cascades to the
    refresh families, and `except_session` is exactly this token's own — the
    argument that function already exists to take.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlowProblem | RevokedOut
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
