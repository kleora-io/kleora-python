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
from ...models.branding_in import BrandingIn
from ...models.branding_out import BrandingOut
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    environment_id: str,
    *,
    body: BrandingIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/environments/{environment_id}/branding".format(
            environment_id=quote(str(environment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BrandingOut | Problem | None:
    if response.status_code == 200:
        response_200 = BrandingOut.from_dict(response.json())

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
) -> Response[BrandingOut | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    body: BrandingIn,
) -> Response[BrandingOut | Problem]:
    r"""Replace an environment's branding record

     The whole record, validated and normalised, with the changed keys audited.

    `exclude_unset` is what carries \"unknown keys anywhere are rejected\" past
    the schema and into the validator: a `background` of `{\"kind\": \"solid\"}`
    reaches it as that and not as `solid` plus six nulls, so
    `background.angle` on a solid background is the 422 branding.md asks for
    rather than a null the validator would have to guess about.

    Args:
        environment_id (str):
        body (BrandingIn): `PUT /api/v1/environments/{id}/branding` and `POST …/branding/preview`.

            Every top-level key that existed on 2026-09-18 is required — this is a
            whole-record replacement and branding.md says partial updates are not
            offered — and a key added since may be left out and is stored as its
            default. `extra="forbid"` is what makes an unknown key a 422 rather than a
            value silently dropped on the way to storage.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BrandingOut | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    body: BrandingIn,
) -> BrandingOut | Problem | None:
    r"""Replace an environment's branding record

     The whole record, validated and normalised, with the changed keys audited.

    `exclude_unset` is what carries \"unknown keys anywhere are rejected\" past
    the schema and into the validator: a `background` of `{\"kind\": \"solid\"}`
    reaches it as that and not as `solid` plus six nulls, so
    `background.angle` on a solid background is the 422 branding.md asks for
    rather than a null the validator would have to guess about.

    Args:
        environment_id (str):
        body (BrandingIn): `PUT /api/v1/environments/{id}/branding` and `POST …/branding/preview`.

            Every top-level key that existed on 2026-09-18 is required — this is a
            whole-record replacement and branding.md says partial updates are not
            offered — and a key added since may be left out and is stored as its
            default. `extra="forbid"` is what makes an unknown key a 422 rather than a
            value silently dropped on the way to storage.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BrandingOut | Problem
    """

    return sync_detailed(
        environment_id=environment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    body: BrandingIn,
) -> Response[BrandingOut | Problem]:
    r"""Replace an environment's branding record

     The whole record, validated and normalised, with the changed keys audited.

    `exclude_unset` is what carries \"unknown keys anywhere are rejected\" past
    the schema and into the validator: a `background` of `{\"kind\": \"solid\"}`
    reaches it as that and not as `solid` plus six nulls, so
    `background.angle` on a solid background is the 422 branding.md asks for
    rather than a null the validator would have to guess about.

    Args:
        environment_id (str):
        body (BrandingIn): `PUT /api/v1/environments/{id}/branding` and `POST …/branding/preview`.

            Every top-level key that existed on 2026-09-18 is required — this is a
            whole-record replacement and branding.md says partial updates are not
            offered — and a key added since may be left out and is stored as its
            default. `extra="forbid"` is what makes an unknown key a 422 rather than a
            value silently dropped on the way to storage.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BrandingOut | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    body: BrandingIn,
) -> BrandingOut | Problem | None:
    r"""Replace an environment's branding record

     The whole record, validated and normalised, with the changed keys audited.

    `exclude_unset` is what carries \"unknown keys anywhere are rejected\" past
    the schema and into the validator: a `background` of `{\"kind\": \"solid\"}`
    reaches it as that and not as `solid` plus six nulls, so
    `background.angle` on a solid background is the 422 branding.md asks for
    rather than a null the validator would have to guess about.

    Args:
        environment_id (str):
        body (BrandingIn): `PUT /api/v1/environments/{id}/branding` and `POST …/branding/preview`.

            Every top-level key that existed on 2026-09-18 is required — this is a
            whole-record replacement and branding.md says partial updates are not
            offered — and a key added since may be left out and is stored as its
            default. `extra="forbid"` is what makes an unknown key a 422 rather than a
            value silently dropped on the way to storage.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BrandingOut | Problem
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
            body=body,
        )
    ).parsed
