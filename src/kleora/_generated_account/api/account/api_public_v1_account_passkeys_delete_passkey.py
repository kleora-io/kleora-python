# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed self-service API document
# (https://id.kleora.eu/account/v1/openapi.json). `kleora.account` wraps this tree; nothing outside the
# package imports it.
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.flow_problem import FlowProblem
from ...types import Response


def _get_kwargs(
    factor_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/account/v1/passkeys/{factor_id}".format(
            factor_id=quote(str(factor_id), safe=""),
        ),
    }

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
) -> Response[Any | FlowProblem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    factor_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | FlowProblem]:
    r"""Remove one of the signed-in person's own passkeys

     Two refusals, from `passkeys.md`'s two rules — and this surface separates them.

    `passkeys.md` §\"Multiple credentials, and removing them\" has two rules:
    refused unconditionally when removing it would leave the person **no way to
    sign in at all**, and refused under `mfa_policy: required` when it is their
    last *second factor* of any kind. `webauthn.removal_refused` answers both with
    one bool, which is all `DELETE /flow/passkeys/{id}` needs — that surface
    answers `403 mfa-required` either way.

    **§API asks this surface for two answers**: `409 last-credential` and
    `403 mfa-required`, and §\"Failure modes\" gives them separate rows with
    separate closed sets. That is right for an API a customer programs against:
    \"you would have no way in\" and \"this environment insists on a second factor\"
    call for different screens, and a client that saw one slug for both would have
    to guess which it was.

    So the split asks `identities.ways_to_sign_in` — the *same* predicate
    `removal_refused` asks for its first rule, with the same
    `excluding_passkey` — and only then asks `removal_refused` for what is left,
    which can then only be the policy rule. One rule, one predicate, two slugs:
    nothing here re-derives what a way in is, which is exactly the mistake `S9-08`
    found when the passkey rule knew about passwords and passkeys and nothing
    about provider identities.

    Args:
        factor_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FlowProblem]
    """

    kwargs = _get_kwargs(
        factor_id=factor_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    factor_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | FlowProblem | None:
    r"""Remove one of the signed-in person's own passkeys

     Two refusals, from `passkeys.md`'s two rules — and this surface separates them.

    `passkeys.md` §\"Multiple credentials, and removing them\" has two rules:
    refused unconditionally when removing it would leave the person **no way to
    sign in at all**, and refused under `mfa_policy: required` when it is their
    last *second factor* of any kind. `webauthn.removal_refused` answers both with
    one bool, which is all `DELETE /flow/passkeys/{id}` needs — that surface
    answers `403 mfa-required` either way.

    **§API asks this surface for two answers**: `409 last-credential` and
    `403 mfa-required`, and §\"Failure modes\" gives them separate rows with
    separate closed sets. That is right for an API a customer programs against:
    \"you would have no way in\" and \"this environment insists on a second factor\"
    call for different screens, and a client that saw one slug for both would have
    to guess which it was.

    So the split asks `identities.ways_to_sign_in` — the *same* predicate
    `removal_refused` asks for its first rule, with the same
    `excluding_passkey` — and only then asks `removal_refused` for what is left,
    which can then only be the policy rule. One rule, one predicate, two slugs:
    nothing here re-derives what a way in is, which is exactly the mistake `S9-08`
    found when the passkey rule knew about passwords and passkeys and nothing
    about provider identities.

    Args:
        factor_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FlowProblem
    """

    return sync_detailed(
        factor_id=factor_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    factor_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | FlowProblem]:
    r"""Remove one of the signed-in person's own passkeys

     Two refusals, from `passkeys.md`'s two rules — and this surface separates them.

    `passkeys.md` §\"Multiple credentials, and removing them\" has two rules:
    refused unconditionally when removing it would leave the person **no way to
    sign in at all**, and refused under `mfa_policy: required` when it is their
    last *second factor* of any kind. `webauthn.removal_refused` answers both with
    one bool, which is all `DELETE /flow/passkeys/{id}` needs — that surface
    answers `403 mfa-required` either way.

    **§API asks this surface for two answers**: `409 last-credential` and
    `403 mfa-required`, and §\"Failure modes\" gives them separate rows with
    separate closed sets. That is right for an API a customer programs against:
    \"you would have no way in\" and \"this environment insists on a second factor\"
    call for different screens, and a client that saw one slug for both would have
    to guess which it was.

    So the split asks `identities.ways_to_sign_in` — the *same* predicate
    `removal_refused` asks for its first rule, with the same
    `excluding_passkey` — and only then asks `removal_refused` for what is left,
    which can then only be the policy rule. One rule, one predicate, two slugs:
    nothing here re-derives what a way in is, which is exactly the mistake `S9-08`
    found when the passkey rule knew about passwords and passkeys and nothing
    about provider identities.

    Args:
        factor_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FlowProblem]
    """

    kwargs = _get_kwargs(
        factor_id=factor_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    factor_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | FlowProblem | None:
    r"""Remove one of the signed-in person's own passkeys

     Two refusals, from `passkeys.md`'s two rules — and this surface separates them.

    `passkeys.md` §\"Multiple credentials, and removing them\" has two rules:
    refused unconditionally when removing it would leave the person **no way to
    sign in at all**, and refused under `mfa_policy: required` when it is their
    last *second factor* of any kind. `webauthn.removal_refused` answers both with
    one bool, which is all `DELETE /flow/passkeys/{id}` needs — that surface
    answers `403 mfa-required` either way.

    **§API asks this surface for two answers**: `409 last-credential` and
    `403 mfa-required`, and §\"Failure modes\" gives them separate rows with
    separate closed sets. That is right for an API a customer programs against:
    \"you would have no way in\" and \"this environment insists on a second factor\"
    call for different screens, and a client that saw one slug for both would have
    to guess which it was.

    So the split asks `identities.ways_to_sign_in` — the *same* predicate
    `removal_refused` asks for its first rule, with the same
    `excluding_passkey` — and only then asks `removal_refused` for what is left,
    which can then only be the policy rule. One rule, one predicate, two slugs:
    nothing here re-derives what a way in is, which is exactly the mistake `S9-08`
    found when the passkey rule knew about passwords and passkeys and nothing
    about provider identities.

    Args:
        factor_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FlowProblem
    """

    return (
        await asyncio_detailed(
            factor_id=factor_id,
            client=client,
        )
    ).parsed
