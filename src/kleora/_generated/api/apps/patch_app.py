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
from ...models.app_out import AppOut
from ...models.app_patch import AppPatch
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    app_id: str,
    *,
    body: AppPatch,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/apps/{app_id}".format(
            app_id=quote(str(app_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppOut | Problem | None:
    if response.status_code == 200:
        response_200 = AppOut.from_dict(response.json())

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
) -> Response[AppOut | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient,
    body: AppPatch,
) -> Response[AppOut | Problem]:
    """Rename an app

     Rename it. The slug is not a property that can move; the schema says so.

    Args:
        app_id (str):
        body (AppPatch): `PATCH /api/v1/apps/{app_id}` — `name`, and nothing else.

            `slug` is not a field of this schema, so it cannot be written; it is named
            in `immutable_fields` so that sending it is answered as what it is rather
            than as a typo. Both of the App's issuers are derived from it and every
            token minted so far claims one of them as `iss`, so a rename would silently
            invalidate deployed integrations (apps.md §"The slug is the issuer").

            `is_platform`, `account_id` and `environments` are unknown fields on
            purpose: the first two are ours and the third is a projection, not a
            property, and `extra="forbid"` says so.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppOut | Problem]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    *,
    client: AuthenticatedClient,
    body: AppPatch,
) -> AppOut | Problem | None:
    """Rename an app

     Rename it. The slug is not a property that can move; the schema says so.

    Args:
        app_id (str):
        body (AppPatch): `PATCH /api/v1/apps/{app_id}` — `name`, and nothing else.

            `slug` is not a field of this schema, so it cannot be written; it is named
            in `immutable_fields` so that sending it is answered as what it is rather
            than as a typo. Both of the App's issuers are derived from it and every
            token minted so far claims one of them as `iss`, so a rename would silently
            invalidate deployed integrations (apps.md §"The slug is the issuer").

            `is_platform`, `account_id` and `environments` are unknown fields on
            purpose: the first two are ours and the third is a projection, not a
            property, and `extra="forbid"` says so.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppOut | Problem
    """

    return sync_detailed(
        app_id=app_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient,
    body: AppPatch,
) -> Response[AppOut | Problem]:
    """Rename an app

     Rename it. The slug is not a property that can move; the schema says so.

    Args:
        app_id (str):
        body (AppPatch): `PATCH /api/v1/apps/{app_id}` — `name`, and nothing else.

            `slug` is not a field of this schema, so it cannot be written; it is named
            in `immutable_fields` so that sending it is answered as what it is rather
            than as a typo. Both of the App's issuers are derived from it and every
            token minted so far claims one of them as `iss`, so a rename would silently
            invalidate deployed integrations (apps.md §"The slug is the issuer").

            `is_platform`, `account_id` and `environments` are unknown fields on
            purpose: the first two are ours and the third is a projection, not a
            property, and `extra="forbid"` says so.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppOut | Problem]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    *,
    client: AuthenticatedClient,
    body: AppPatch,
) -> AppOut | Problem | None:
    """Rename an app

     Rename it. The slug is not a property that can move; the schema says so.

    Args:
        app_id (str):
        body (AppPatch): `PATCH /api/v1/apps/{app_id}` — `name`, and nothing else.

            `slug` is not a field of this schema, so it cannot be written; it is named
            in `immutable_fields` so that sending it is answered as what it is rather
            than as a typo. Both of the App's issuers are derived from it and every
            token minted so far claims one of them as `iss`, so a rename would silently
            invalidate deployed integrations (apps.md §"The slug is the issuer").

            `is_platform`, `account_id` and `environments` are unknown fields on
            purpose: the first two are ours and the third is a projection, not a
            property, and `extra="forbid"` says so.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppOut | Problem
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            client=client,
            body=body,
        )
    ).parsed
