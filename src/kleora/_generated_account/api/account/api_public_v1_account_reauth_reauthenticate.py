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
from ...models.reauth_in import ReauthIn
from ...types import Response


def _get_kwargs(
    *,
    body: ReauthIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/account/v1/reauth",
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
    body: ReauthIn,
) -> Response[Any | FlowProblem]:
    r"""Re-prove the signed-in person's own password

     Verify the password against this session's own user, and mark the session.

    **`sensitive=False`, and it has to be**: this is the operation that satisfies
    the gate, so gating it would be a cycle with no way in. That is not a
    weakening — it takes a password, which is a stronger proof than the mark it
    writes.

    A wrong password is `401 invalid-credentials`, indistinguishable from every
    other credential refusal on this surface, and **counts toward the same
    progressive lockout** a wrong password anywhere else does — because the check
    goes through `authenticate_password` rather than through a hash comparison.
    §\"Rate limits\" says so in as many words: \"A failed re-authentication and a
    wrong `current_password` both count toward progressive lockout\".

    Nothing about the session is disturbed. `amr` is unchanged and no new session
    is opened: `reauth.mark` writes a property *next to* the session, which is the
    whole of what `mfa.md` §Self-service asks for and the reason a person who has
    just re-authenticated is not suddenly treated as having passed a second factor.

    Args:
        body (ReauthIn): A password and nothing else (§Re-authentication).

            A passkey assertion cannot be accepted here — `rp_id` is the issuer host and a
            ceremony on the customer's origin is refused by the browser — and a provider
            round trip cannot, because it is a navigation. Both remain available on the
            hosted `/account/reauth`, which accepts all three; the asymmetry is the
            browser's and `GET /reauth` is how a caller finds out which it has.

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
    body: ReauthIn,
) -> Any | FlowProblem | None:
    r"""Re-prove the signed-in person's own password

     Verify the password against this session's own user, and mark the session.

    **`sensitive=False`, and it has to be**: this is the operation that satisfies
    the gate, so gating it would be a cycle with no way in. That is not a
    weakening — it takes a password, which is a stronger proof than the mark it
    writes.

    A wrong password is `401 invalid-credentials`, indistinguishable from every
    other credential refusal on this surface, and **counts toward the same
    progressive lockout** a wrong password anywhere else does — because the check
    goes through `authenticate_password` rather than through a hash comparison.
    §\"Rate limits\" says so in as many words: \"A failed re-authentication and a
    wrong `current_password` both count toward progressive lockout\".

    Nothing about the session is disturbed. `amr` is unchanged and no new session
    is opened: `reauth.mark` writes a property *next to* the session, which is the
    whole of what `mfa.md` §Self-service asks for and the reason a person who has
    just re-authenticated is not suddenly treated as having passed a second factor.

    Args:
        body (ReauthIn): A password and nothing else (§Re-authentication).

            A passkey assertion cannot be accepted here — `rp_id` is the issuer host and a
            ceremony on the customer's origin is refused by the browser — and a provider
            round trip cannot, because it is a navigation. Both remain available on the
            hosted `/account/reauth`, which accepts all three; the asymmetry is the
            browser's and `GET /reauth` is how a caller finds out which it has.

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
    body: ReauthIn,
) -> Response[Any | FlowProblem]:
    r"""Re-prove the signed-in person's own password

     Verify the password against this session's own user, and mark the session.

    **`sensitive=False`, and it has to be**: this is the operation that satisfies
    the gate, so gating it would be a cycle with no way in. That is not a
    weakening — it takes a password, which is a stronger proof than the mark it
    writes.

    A wrong password is `401 invalid-credentials`, indistinguishable from every
    other credential refusal on this surface, and **counts toward the same
    progressive lockout** a wrong password anywhere else does — because the check
    goes through `authenticate_password` rather than through a hash comparison.
    §\"Rate limits\" says so in as many words: \"A failed re-authentication and a
    wrong `current_password` both count toward progressive lockout\".

    Nothing about the session is disturbed. `amr` is unchanged and no new session
    is opened: `reauth.mark` writes a property *next to* the session, which is the
    whole of what `mfa.md` §Self-service asks for and the reason a person who has
    just re-authenticated is not suddenly treated as having passed a second factor.

    Args:
        body (ReauthIn): A password and nothing else (§Re-authentication).

            A passkey assertion cannot be accepted here — `rp_id` is the issuer host and a
            ceremony on the customer's origin is refused by the browser — and a provider
            round trip cannot, because it is a navigation. Both remain available on the
            hosted `/account/reauth`, which accepts all three; the asymmetry is the
            browser's and `GET /reauth` is how a caller finds out which it has.

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
    body: ReauthIn,
) -> Any | FlowProblem | None:
    r"""Re-prove the signed-in person's own password

     Verify the password against this session's own user, and mark the session.

    **`sensitive=False`, and it has to be**: this is the operation that satisfies
    the gate, so gating it would be a cycle with no way in. That is not a
    weakening — it takes a password, which is a stronger proof than the mark it
    writes.

    A wrong password is `401 invalid-credentials`, indistinguishable from every
    other credential refusal on this surface, and **counts toward the same
    progressive lockout** a wrong password anywhere else does — because the check
    goes through `authenticate_password` rather than through a hash comparison.
    §\"Rate limits\" says so in as many words: \"A failed re-authentication and a
    wrong `current_password` both count toward progressive lockout\".

    Nothing about the session is disturbed. `amr` is unchanged and no new session
    is opened: `reauth.mark` writes a property *next to* the session, which is the
    whole of what `mfa.md` §Self-service asks for and the reason a person who has
    just re-authenticated is not suddenly treated as having passed a second factor.

    Args:
        body (ReauthIn): A password and nothing else (§Re-authentication).

            A passkey assertion cannot be accepted here — `rp_id` is the issuer host and a
            ceremony on the customer's origin is refused by the browser — and a provider
            round trip cannot, because it is a navigation. Both remain available on the
            hosted `/account/reauth`, which accepts all three; the asymmetry is the
            browser's and `GET /reauth` is how a caller finds out which it has.

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
