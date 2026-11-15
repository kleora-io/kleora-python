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
from ...models.reauth_out import ReauthOut
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/account/v1/reauth",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FlowProblem | ReauthOut | None:
    if response.status_code == 200:
        response_200 = ReauthOut.from_dict(response.json())

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
) -> Response[FlowProblem | ReauthOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[FlowProblem | ReauthOut]:
    r"""What the signed-in person can re-authenticate with

     `{has_password, reauth_providers[], passkey_available, reauthenticated_until}`.

    The same three facts `GET /flow/identities` already carries for the same
    reason, from the same two services — `identities.has_password` and
    `reauth_buttons`, which is the **intersection** of the providers this person
    holds and the providers this Environment still offers. A kind the person holds
    but the Environment has since disabled is left out, because a control that can
    only produce a refusal is worse than no control (`S9-12`).

    `passkey_available` is \"this person holds a confirmed passkey\", which is a
    fact about them and not about what this API can accept — a customer's screen
    uses it to decide whether linking to the hosted `/account/reauth` is worth
    offering, since that page accepts an assertion and this endpoint cannot.

    `reauthenticated_until` is `null` when there is no live mark, so a screen can
    skip the gate it does not need rather than discovering that from a `401`
    after somebody has filled a form in.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlowProblem | ReauthOut]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> FlowProblem | ReauthOut | None:
    r"""What the signed-in person can re-authenticate with

     `{has_password, reauth_providers[], passkey_available, reauthenticated_until}`.

    The same three facts `GET /flow/identities` already carries for the same
    reason, from the same two services — `identities.has_password` and
    `reauth_buttons`, which is the **intersection** of the providers this person
    holds and the providers this Environment still offers. A kind the person holds
    but the Environment has since disabled is left out, because a control that can
    only produce a refusal is worse than no control (`S9-12`).

    `passkey_available` is \"this person holds a confirmed passkey\", which is a
    fact about them and not about what this API can accept — a customer's screen
    uses it to decide whether linking to the hosted `/account/reauth` is worth
    offering, since that page accepts an assertion and this endpoint cannot.

    `reauthenticated_until` is `null` when there is no live mark, so a screen can
    skip the gate it does not need rather than discovering that from a `401`
    after somebody has filled a form in.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlowProblem | ReauthOut
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[FlowProblem | ReauthOut]:
    r"""What the signed-in person can re-authenticate with

     `{has_password, reauth_providers[], passkey_available, reauthenticated_until}`.

    The same three facts `GET /flow/identities` already carries for the same
    reason, from the same two services — `identities.has_password` and
    `reauth_buttons`, which is the **intersection** of the providers this person
    holds and the providers this Environment still offers. A kind the person holds
    but the Environment has since disabled is left out, because a control that can
    only produce a refusal is worse than no control (`S9-12`).

    `passkey_available` is \"this person holds a confirmed passkey\", which is a
    fact about them and not about what this API can accept — a customer's screen
    uses it to decide whether linking to the hosted `/account/reauth` is worth
    offering, since that page accepts an assertion and this endpoint cannot.

    `reauthenticated_until` is `null` when there is no live mark, so a screen can
    skip the gate it does not need rather than discovering that from a `401`
    after somebody has filled a form in.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlowProblem | ReauthOut]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> FlowProblem | ReauthOut | None:
    r"""What the signed-in person can re-authenticate with

     `{has_password, reauth_providers[], passkey_available, reauthenticated_until}`.

    The same three facts `GET /flow/identities` already carries for the same
    reason, from the same two services — `identities.has_password` and
    `reauth_buttons`, which is the **intersection** of the providers this person
    holds and the providers this Environment still offers. A kind the person holds
    but the Environment has since disabled is left out, because a control that can
    only produce a refusal is worse than no control (`S9-12`).

    `passkey_available` is \"this person holds a confirmed passkey\", which is a
    fact about them and not about what this API can accept — a customer's screen
    uses it to decide whether linking to the hosted `/account/reauth` is worth
    offering, since that page accepts an assertion and this endpoint cannot.

    `reauthenticated_until` is `null` when there is no live mark, so a screen can
    skip the gate it does not need rather than discovering that from a `401`
    after somebody has filled a form in.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlowProblem | ReauthOut
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
