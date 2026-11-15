# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.me_passkey_options_out import MePasskeyOptionsOut
from ...models.problem import Problem
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/me/passkeys/register/start",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MePasskeyOptionsOut | Problem | None:
    if response.status_code == 200:
        response_200 = MePasskeyOptionsOut.from_dict(response.json())

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
) -> Response[MePasskeyOptionsOut | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[MePasskeyOptionsOut | Problem]:
    r"""Begin registering one of the caller's own passkeys

     `402` on a plan without passkeys — mfa.md §\"What a plan gates\" names
    this route beside `/flow/passkeys/register/start`.

    `allow_unpaid=True` and a 402 are not in tension: the annotation exempts
    this route from billing.md's day-15 **write block**, which exists to
    collect a debt and must never reach somebody's second factor, while this
    refusal is the plan not carrying passkeys at all. TOTP and recovery codes
    on this surface stay reachable in every billing state and on every plan,
    which is the promise that made the exemption necessary in the first place.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MePasskeyOptionsOut | Problem]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> MePasskeyOptionsOut | Problem | None:
    r"""Begin registering one of the caller's own passkeys

     `402` on a plan without passkeys — mfa.md §\"What a plan gates\" names
    this route beside `/flow/passkeys/register/start`.

    `allow_unpaid=True` and a 402 are not in tension: the annotation exempts
    this route from billing.md's day-15 **write block**, which exists to
    collect a debt and must never reach somebody's second factor, while this
    refusal is the plan not carrying passkeys at all. TOTP and recovery codes
    on this surface stay reachable in every billing state and on every plan,
    which is the promise that made the exemption necessary in the first place.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MePasskeyOptionsOut | Problem
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[MePasskeyOptionsOut | Problem]:
    r"""Begin registering one of the caller's own passkeys

     `402` on a plan without passkeys — mfa.md §\"What a plan gates\" names
    this route beside `/flow/passkeys/register/start`.

    `allow_unpaid=True` and a 402 are not in tension: the annotation exempts
    this route from billing.md's day-15 **write block**, which exists to
    collect a debt and must never reach somebody's second factor, while this
    refusal is the plan not carrying passkeys at all. TOTP and recovery codes
    on this surface stay reachable in every billing state and on every plan,
    which is the promise that made the exemption necessary in the first place.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MePasskeyOptionsOut | Problem]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> MePasskeyOptionsOut | Problem | None:
    r"""Begin registering one of the caller's own passkeys

     `402` on a plan without passkeys — mfa.md §\"What a plan gates\" names
    this route beside `/flow/passkeys/register/start`.

    `allow_unpaid=True` and a 402 are not in tension: the annotation exempts
    this route from billing.md's day-15 **write block**, which exists to
    collect a debt and must never reach somebody's second factor, while this
    refusal is the plan not carrying passkeys at all. TOTP and recovery codes
    on this surface stay reachable in every billing state and on every plan,
    which is the promise that made the exemption necessary in the first place.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MePasskeyOptionsOut | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
