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
from ...models.branding_preview_out import BrandingPreviewOut
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    environment_id: str,
    *,
    body: BrandingIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/environments/{environment_id}/branding/preview".format(
            environment_id=quote(str(environment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BrandingPreviewOut | Problem | None:
    if response.status_code == 201:
        response_201 = BrandingPreviewOut.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = Problem.from_dict(response.json())

        return response_401

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

    if response.status_code == 503:
        response_503 = Problem.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BrandingPreviewOut | Problem]:
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
) -> Response[BrandingPreviewOut | Problem]:
    """Create a branding preview draft

     Store a draft branding record for 600 seconds, and return a URL that renders it.

    Nothing is saved to the environment; to save the draft, `PUT` the same body. An invalid draft is
    the same `422` a `PUT` of it would be. The response is never cached, since `preview_url` grants
    access to the draft.

    The rate limit is checked before the draft is validated, so a rate-limited request is `429` even
    when its body is also invalid.

    Args:
        environment_id (str):
        body (BrandingIn): The body of `PUT /api/v1/environments/{environment_id}/branding` and
            `POST
            .../branding/preview`: the whole branding record.

            Partial updates are not offered. A few recently added keys may be left out, and are stored
            as
            their defaults. Unknown keys are `422`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BrandingPreviewOut | Problem]
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
) -> BrandingPreviewOut | Problem | None:
    """Create a branding preview draft

     Store a draft branding record for 600 seconds, and return a URL that renders it.

    Nothing is saved to the environment; to save the draft, `PUT` the same body. An invalid draft is
    the same `422` a `PUT` of it would be. The response is never cached, since `preview_url` grants
    access to the draft.

    The rate limit is checked before the draft is validated, so a rate-limited request is `429` even
    when its body is also invalid.

    Args:
        environment_id (str):
        body (BrandingIn): The body of `PUT /api/v1/environments/{environment_id}/branding` and
            `POST
            .../branding/preview`: the whole branding record.

            Partial updates are not offered. A few recently added keys may be left out, and are stored
            as
            their defaults. Unknown keys are `422`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BrandingPreviewOut | Problem
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
) -> Response[BrandingPreviewOut | Problem]:
    """Create a branding preview draft

     Store a draft branding record for 600 seconds, and return a URL that renders it.

    Nothing is saved to the environment; to save the draft, `PUT` the same body. An invalid draft is
    the same `422` a `PUT` of it would be. The response is never cached, since `preview_url` grants
    access to the draft.

    The rate limit is checked before the draft is validated, so a rate-limited request is `429` even
    when its body is also invalid.

    Args:
        environment_id (str):
        body (BrandingIn): The body of `PUT /api/v1/environments/{environment_id}/branding` and
            `POST
            .../branding/preview`: the whole branding record.

            Partial updates are not offered. A few recently added keys may be left out, and are stored
            as
            their defaults. Unknown keys are `422`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BrandingPreviewOut | Problem]
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
) -> BrandingPreviewOut | Problem | None:
    """Create a branding preview draft

     Store a draft branding record for 600 seconds, and return a URL that renders it.

    Nothing is saved to the environment; to save the draft, `PUT` the same body. An invalid draft is
    the same `422` a `PUT` of it would be. The response is never cached, since `preview_url` grants
    access to the draft.

    The rate limit is checked before the draft is validated, so a rate-limited request is `429` even
    when its body is also invalid.

    Args:
        environment_id (str):
        body (BrandingIn): The body of `PUT /api/v1/environments/{environment_id}/branding` and
            `POST
            .../branding/preview`: the whole branding record.

            Partial updates are not offered. A few recently added keys may be left out, and are stored
            as
            their defaults. Unknown keys are `422`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BrandingPreviewOut | Problem
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
            body=body,
        )
    ).parsed
