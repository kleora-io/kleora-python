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
from ...models.mfa_out import MfaOut
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/account/v1/mfa",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FlowProblem | MfaOut | None:
    if response.status_code == 200:
        response_200 = MfaOut.from_dict(response.json())

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
) -> Response[FlowProblem | MfaOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[FlowProblem | MfaOut]:
    r"""The signed-in person's own second factors

     Every factor, confirmed or not, and the policy that governs removal.

    `mfa.md` §API: \"Unconfirmed factors included with `confirmed_at: null`. Never
    seeds or hashes.\" `policy` is here because a screen cannot render a Remove
    button honestly without it — under `required` the last factor cannot go, and
    finding that out from a `403` after the click is worse than not offering it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlowProblem | MfaOut]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> FlowProblem | MfaOut | None:
    r"""The signed-in person's own second factors

     Every factor, confirmed or not, and the policy that governs removal.

    `mfa.md` §API: \"Unconfirmed factors included with `confirmed_at: null`. Never
    seeds or hashes.\" `policy` is here because a screen cannot render a Remove
    button honestly without it — under `required` the last factor cannot go, and
    finding that out from a `403` after the click is worse than not offering it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlowProblem | MfaOut
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[FlowProblem | MfaOut]:
    r"""The signed-in person's own second factors

     Every factor, confirmed or not, and the policy that governs removal.

    `mfa.md` §API: \"Unconfirmed factors included with `confirmed_at: null`. Never
    seeds or hashes.\" `policy` is here because a screen cannot render a Remove
    button honestly without it — under `required` the last factor cannot go, and
    finding that out from a `403` after the click is worse than not offering it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlowProblem | MfaOut]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> FlowProblem | MfaOut | None:
    r"""The signed-in person's own second factors

     Every factor, confirmed or not, and the policy that governs removal.

    `mfa.md` §API: \"Unconfirmed factors included with `confirmed_at: null`. Never
    seeds or hashes.\" `policy` is here because a screen cannot render a Remove
    button honestly without it — under `required` the last factor cannot go, and
    finding that out from a `403` after the click is worse than not offering it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlowProblem | MfaOut
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
