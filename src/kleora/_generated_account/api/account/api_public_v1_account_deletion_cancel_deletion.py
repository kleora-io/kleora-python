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
from ...models.deletion_cancel_in import DeletionCancelIn
from ...models.flow_problem import FlowProblem
from ...types import Response


def _get_kwargs(
    *,
    body: DeletionCancelIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/account/v1/deletion",
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
) -> Response[Any | FlowProblem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DeletionCancelIn,
) -> Response[Any | FlowProblem]:
    r"""Cancel a deletion request with the token from the emailed link

     Spend the mailed token and put the account back.

    **The one route on this surface with no bearer token**, and the reason is
    structural rather than a convenience: the request that produced this token revoked
    every session of the person it belongs to, so there is no session to present. A
    route here that demanded one would make the cancellation link useless, and a
    cancellation link that does not work is a seven-day grace period that is not an
    undo.

    It is on this surface rather than on `/flow/*` \"so that the deletion resource has
    one home\" (§\"What happens, and when\"), and it is keyed by IP because there is no
    `sid` to key on — 30 a minute, \"the shared 30-per-IP-per-minute token row every
    other token endpoint takes\".

    The Environment comes from the host rather than from the credential, which is the
    one thing this handler does differently from every other on the surface:
    `HostResolutionMiddleware` has already resolved it, and it is what scopes the
    token lookup (ADR 0005). A token of another Environment is `400 invalid-token`
    for free, because `users.consume` never sees it.

    `204` for a token that was spent and for a row with nothing outstanding alike:
    the state the caller asked for is the state that holds. A second click on the same
    link is `400 invalid-token`, because the first one spent it — one answer for
    unknown, spent and expired, which §\"Failure modes\" asks for in as many words.

    Args:
        body (DeletionCancelIn): `DELETE /deletion` with `{token}` — the one anonymous body on
            this surface.

            The person holds no session by construction: the request that produced this token
            revoked every one of them. So the mailed token is the whole credential, and
            `TOKEN_MAX_LENGTH` is the same non-committal ceiling `EmailConfirmIn.token`
            carries, for the same reason — one `400 invalid-token` for every way a token can
            be wrong, and a length bound would make a second answer out of one of them.

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
    client: AuthenticatedClient | Client,
    body: DeletionCancelIn,
) -> Any | FlowProblem | None:
    r"""Cancel a deletion request with the token from the emailed link

     Spend the mailed token and put the account back.

    **The one route on this surface with no bearer token**, and the reason is
    structural rather than a convenience: the request that produced this token revoked
    every session of the person it belongs to, so there is no session to present. A
    route here that demanded one would make the cancellation link useless, and a
    cancellation link that does not work is a seven-day grace period that is not an
    undo.

    It is on this surface rather than on `/flow/*` \"so that the deletion resource has
    one home\" (§\"What happens, and when\"), and it is keyed by IP because there is no
    `sid` to key on — 30 a minute, \"the shared 30-per-IP-per-minute token row every
    other token endpoint takes\".

    The Environment comes from the host rather than from the credential, which is the
    one thing this handler does differently from every other on the surface:
    `HostResolutionMiddleware` has already resolved it, and it is what scopes the
    token lookup (ADR 0005). A token of another Environment is `400 invalid-token`
    for free, because `users.consume` never sees it.

    `204` for a token that was spent and for a row with nothing outstanding alike:
    the state the caller asked for is the state that holds. A second click on the same
    link is `400 invalid-token`, because the first one spent it — one answer for
    unknown, spent and expired, which §\"Failure modes\" asks for in as many words.

    Args:
        body (DeletionCancelIn): `DELETE /deletion` with `{token}` — the one anonymous body on
            this surface.

            The person holds no session by construction: the request that produced this token
            revoked every one of them. So the mailed token is the whole credential, and
            `TOKEN_MAX_LENGTH` is the same non-committal ceiling `EmailConfirmIn.token`
            carries, for the same reason — one `400 invalid-token` for every way a token can
            be wrong, and a length bound would make a second answer out of one of them.

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
    client: AuthenticatedClient | Client,
    body: DeletionCancelIn,
) -> Response[Any | FlowProblem]:
    r"""Cancel a deletion request with the token from the emailed link

     Spend the mailed token and put the account back.

    **The one route on this surface with no bearer token**, and the reason is
    structural rather than a convenience: the request that produced this token revoked
    every session of the person it belongs to, so there is no session to present. A
    route here that demanded one would make the cancellation link useless, and a
    cancellation link that does not work is a seven-day grace period that is not an
    undo.

    It is on this surface rather than on `/flow/*` \"so that the deletion resource has
    one home\" (§\"What happens, and when\"), and it is keyed by IP because there is no
    `sid` to key on — 30 a minute, \"the shared 30-per-IP-per-minute token row every
    other token endpoint takes\".

    The Environment comes from the host rather than from the credential, which is the
    one thing this handler does differently from every other on the surface:
    `HostResolutionMiddleware` has already resolved it, and it is what scopes the
    token lookup (ADR 0005). A token of another Environment is `400 invalid-token`
    for free, because `users.consume` never sees it.

    `204` for a token that was spent and for a row with nothing outstanding alike:
    the state the caller asked for is the state that holds. A second click on the same
    link is `400 invalid-token`, because the first one spent it — one answer for
    unknown, spent and expired, which §\"Failure modes\" asks for in as many words.

    Args:
        body (DeletionCancelIn): `DELETE /deletion` with `{token}` — the one anonymous body on
            this surface.

            The person holds no session by construction: the request that produced this token
            revoked every one of them. So the mailed token is the whole credential, and
            `TOKEN_MAX_LENGTH` is the same non-committal ceiling `EmailConfirmIn.token`
            carries, for the same reason — one `400 invalid-token` for every way a token can
            be wrong, and a length bound would make a second answer out of one of them.

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
    client: AuthenticatedClient | Client,
    body: DeletionCancelIn,
) -> Any | FlowProblem | None:
    r"""Cancel a deletion request with the token from the emailed link

     Spend the mailed token and put the account back.

    **The one route on this surface with no bearer token**, and the reason is
    structural rather than a convenience: the request that produced this token revoked
    every session of the person it belongs to, so there is no session to present. A
    route here that demanded one would make the cancellation link useless, and a
    cancellation link that does not work is a seven-day grace period that is not an
    undo.

    It is on this surface rather than on `/flow/*` \"so that the deletion resource has
    one home\" (§\"What happens, and when\"), and it is keyed by IP because there is no
    `sid` to key on — 30 a minute, \"the shared 30-per-IP-per-minute token row every
    other token endpoint takes\".

    The Environment comes from the host rather than from the credential, which is the
    one thing this handler does differently from every other on the surface:
    `HostResolutionMiddleware` has already resolved it, and it is what scopes the
    token lookup (ADR 0005). A token of another Environment is `400 invalid-token`
    for free, because `users.consume` never sees it.

    `204` for a token that was spent and for a row with nothing outstanding alike:
    the state the caller asked for is the state that holds. A second click on the same
    link is `400 invalid-token`, because the first one spent it — one answer for
    unknown, spent and expired, which §\"Failure modes\" asks for in as many words.

    Args:
        body (DeletionCancelIn): `DELETE /deletion` with `{token}` — the one anonymous body on
            this surface.

            The person holds no session by construction: the request that produced this token
            revoked every one of them. So the mailed token is the whole credential, and
            `TOKEN_MAX_LENGTH` is the same non-committal ceiling `EmailConfirmIn.token`
            carries, for the same reason — one `400 invalid-token` for every way a token can
            be wrong, and a length bound would make a second answer out of one of them.

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
