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
from ...models.identity_provider_in import IdentityProviderIn
from ...models.identity_provider_out import IdentityProviderOut
from ...models.problem import Problem
from ...models.put_identity_provider_kind import PutIdentityProviderKind
from ...types import Response


def _get_kwargs(
    environment_id: str,
    kind: PutIdentityProviderKind,
    *,
    body: IdentityProviderIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/environments/{environment_id}/identity-providers/{kind}".format(
            environment_id=quote(str(environment_id), safe=""),
            kind=quote(str(kind), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IdentityProviderOut | Problem | None:
    if response.status_code == 200:
        response_200 = IdentityProviderOut.from_dict(response.json())

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
) -> Response[IdentityProviderOut | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    environment_id: str,
    kind: PutIdentityProviderKind,
    *,
    client: AuthenticatedClient,
    body: IdentityProviderIn,
) -> Response[IdentityProviderOut | Problem]:
    """Configure an identity provider

     Create or replace this environment's configuration for `kind`.

    `client_secret` is write-only and **optional: omitting it keeps the stored
    one**. That is not a shortcut, it is the only workable shape — the value is
    never readable, so a client flipping `enabled` cannot send it back, and
    demanding it would make a customer mint a fresh secret at their provider in
    order to turn a button off. Omitted on the *first* write for a kind it is 422
    `validation-error` on `client_secret`. Sent with a value different from the
    stored one it **rotates**: the previous secret keeps completing token
    exchanges for 24 hours, and `identity_provider.secret_rotated` is audited
    beside the `.updated`.

    Args:
        environment_id (str):
        kind (PutIdentityProviderKind):
        body (IdentityProviderIn): `PUT E/identity-providers/{kind}` — create or replace.

            `client_secret` is **optional, and omitting it keeps the stored one.** That is
            the one place this `PUT` is not a literal replacement, and it is deliberate:
            the secret is write-only, so a console flipping `enabled` has never been able
            to read the value it would have to send back, and requiring it would mean
            asking the customer to mint a new secret at their provider in order to turn a
            button off. Omitted on a *first* write it is 422 — a configuration with no
            secret is a button that cannot work. Sent with a different value it rotates,
            and the previous secret keeps working for 24 hours.

            `null` is not the same as absent and is refused by the type: a caller who
            meant "clear the secret" is asking for a configuration that cannot complete a
            sign-in, and `DELETE` is how a provider goes away.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentityProviderOut | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        kind=kind,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    kind: PutIdentityProviderKind,
    *,
    client: AuthenticatedClient,
    body: IdentityProviderIn,
) -> IdentityProviderOut | Problem | None:
    """Configure an identity provider

     Create or replace this environment's configuration for `kind`.

    `client_secret` is write-only and **optional: omitting it keeps the stored
    one**. That is not a shortcut, it is the only workable shape — the value is
    never readable, so a client flipping `enabled` cannot send it back, and
    demanding it would make a customer mint a fresh secret at their provider in
    order to turn a button off. Omitted on the *first* write for a kind it is 422
    `validation-error` on `client_secret`. Sent with a value different from the
    stored one it **rotates**: the previous secret keeps completing token
    exchanges for 24 hours, and `identity_provider.secret_rotated` is audited
    beside the `.updated`.

    Args:
        environment_id (str):
        kind (PutIdentityProviderKind):
        body (IdentityProviderIn): `PUT E/identity-providers/{kind}` — create or replace.

            `client_secret` is **optional, and omitting it keeps the stored one.** That is
            the one place this `PUT` is not a literal replacement, and it is deliberate:
            the secret is write-only, so a console flipping `enabled` has never been able
            to read the value it would have to send back, and requiring it would mean
            asking the customer to mint a new secret at their provider in order to turn a
            button off. Omitted on a *first* write it is 422 — a configuration with no
            secret is a button that cannot work. Sent with a different value it rotates,
            and the previous secret keeps working for 24 hours.

            `null` is not the same as absent and is refused by the type: a caller who
            meant "clear the secret" is asking for a configuration that cannot complete a
            sign-in, and `DELETE` is how a provider goes away.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentityProviderOut | Problem
    """

    return sync_detailed(
        environment_id=environment_id,
        kind=kind,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    kind: PutIdentityProviderKind,
    *,
    client: AuthenticatedClient,
    body: IdentityProviderIn,
) -> Response[IdentityProviderOut | Problem]:
    """Configure an identity provider

     Create or replace this environment's configuration for `kind`.

    `client_secret` is write-only and **optional: omitting it keeps the stored
    one**. That is not a shortcut, it is the only workable shape — the value is
    never readable, so a client flipping `enabled` cannot send it back, and
    demanding it would make a customer mint a fresh secret at their provider in
    order to turn a button off. Omitted on the *first* write for a kind it is 422
    `validation-error` on `client_secret`. Sent with a value different from the
    stored one it **rotates**: the previous secret keeps completing token
    exchanges for 24 hours, and `identity_provider.secret_rotated` is audited
    beside the `.updated`.

    Args:
        environment_id (str):
        kind (PutIdentityProviderKind):
        body (IdentityProviderIn): `PUT E/identity-providers/{kind}` — create or replace.

            `client_secret` is **optional, and omitting it keeps the stored one.** That is
            the one place this `PUT` is not a literal replacement, and it is deliberate:
            the secret is write-only, so a console flipping `enabled` has never been able
            to read the value it would have to send back, and requiring it would mean
            asking the customer to mint a new secret at their provider in order to turn a
            button off. Omitted on a *first* write it is 422 — a configuration with no
            secret is a button that cannot work. Sent with a different value it rotates,
            and the previous secret keeps working for 24 hours.

            `null` is not the same as absent and is refused by the type: a caller who
            meant "clear the secret" is asking for a configuration that cannot complete a
            sign-in, and `DELETE` is how a provider goes away.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentityProviderOut | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        kind=kind,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    kind: PutIdentityProviderKind,
    *,
    client: AuthenticatedClient,
    body: IdentityProviderIn,
) -> IdentityProviderOut | Problem | None:
    """Configure an identity provider

     Create or replace this environment's configuration for `kind`.

    `client_secret` is write-only and **optional: omitting it keeps the stored
    one**. That is not a shortcut, it is the only workable shape — the value is
    never readable, so a client flipping `enabled` cannot send it back, and
    demanding it would make a customer mint a fresh secret at their provider in
    order to turn a button off. Omitted on the *first* write for a kind it is 422
    `validation-error` on `client_secret`. Sent with a value different from the
    stored one it **rotates**: the previous secret keeps completing token
    exchanges for 24 hours, and `identity_provider.secret_rotated` is audited
    beside the `.updated`.

    Args:
        environment_id (str):
        kind (PutIdentityProviderKind):
        body (IdentityProviderIn): `PUT E/identity-providers/{kind}` — create or replace.

            `client_secret` is **optional, and omitting it keeps the stored one.** That is
            the one place this `PUT` is not a literal replacement, and it is deliberate:
            the secret is write-only, so a console flipping `enabled` has never been able
            to read the value it would have to send back, and requiring it would mean
            asking the customer to mint a new secret at their provider in order to turn a
            button off. Omitted on a *first* write it is 422 — a configuration with no
            secret is a button that cannot work. Sent with a different value it rotates,
            and the previous secret keeps working for 24 hours.

            `null` is not the same as absent and is refused by the type: a caller who
            meant "clear the secret" is asking for a configuration that cannot complete a
            sign-in, and `DELETE` is how a provider goes away.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentityProviderOut | Problem
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            kind=kind,
            client=client,
            body=body,
        )
    ).parsed
