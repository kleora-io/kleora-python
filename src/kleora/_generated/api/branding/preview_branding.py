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
    r"""Create a branding preview draft

     A draft in Redis for 600 s, and the URL that renders it.

    Nothing is written to the environment: the console saves by calling `PUT`
    with the same body. An invalid draft is the same 422 a `PUT` of it would be
    and nothing reaches Redis, because validation happens first.

    `no_store` on the answer: the `preview_url` carries a token that reads a
    draft, and a shared cache holding it would hand the next caller somebody
    else's unsaved work.

    **The budget is spent before the draft is parsed.** Validation tokenizes up
    to 8 KiB of customer CSS, and an over-budget caller that still paid for
    that parse would have a cheap way to buy work at thirty-one requests a
    minute. The precedence this fixes is 429-over-422, which is the right way
    round: \"you are sending too many\" is true of a request whether or not its
    body is also wrong, and a client that is being told to slow down does not
    need its body reviewed first. Authorisation still comes first — `@requires`
    is outside this — so a caller with no permission never spends a budget.

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
    r"""Create a branding preview draft

     A draft in Redis for 600 s, and the URL that renders it.

    Nothing is written to the environment: the console saves by calling `PUT`
    with the same body. An invalid draft is the same 422 a `PUT` of it would be
    and nothing reaches Redis, because validation happens first.

    `no_store` on the answer: the `preview_url` carries a token that reads a
    draft, and a shared cache holding it would hand the next caller somebody
    else's unsaved work.

    **The budget is spent before the draft is parsed.** Validation tokenizes up
    to 8 KiB of customer CSS, and an over-budget caller that still paid for
    that parse would have a cheap way to buy work at thirty-one requests a
    minute. The precedence this fixes is 429-over-422, which is the right way
    round: \"you are sending too many\" is true of a request whether or not its
    body is also wrong, and a client that is being told to slow down does not
    need its body reviewed first. Authorisation still comes first — `@requires`
    is outside this — so a caller with no permission never spends a budget.

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
    r"""Create a branding preview draft

     A draft in Redis for 600 s, and the URL that renders it.

    Nothing is written to the environment: the console saves by calling `PUT`
    with the same body. An invalid draft is the same 422 a `PUT` of it would be
    and nothing reaches Redis, because validation happens first.

    `no_store` on the answer: the `preview_url` carries a token that reads a
    draft, and a shared cache holding it would hand the next caller somebody
    else's unsaved work.

    **The budget is spent before the draft is parsed.** Validation tokenizes up
    to 8 KiB of customer CSS, and an over-budget caller that still paid for
    that parse would have a cheap way to buy work at thirty-one requests a
    minute. The precedence this fixes is 429-over-422, which is the right way
    round: \"you are sending too many\" is true of a request whether or not its
    body is also wrong, and a client that is being told to slow down does not
    need its body reviewed first. Authorisation still comes first — `@requires`
    is outside this — so a caller with no permission never spends a budget.

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
    r"""Create a branding preview draft

     A draft in Redis for 600 s, and the URL that renders it.

    Nothing is written to the environment: the console saves by calling `PUT`
    with the same body. An invalid draft is the same 422 a `PUT` of it would be
    and nothing reaches Redis, because validation happens first.

    `no_store` on the answer: the `preview_url` carries a token that reads a
    draft, and a shared cache holding it would hand the next caller somebody
    else's unsaved work.

    **The budget is spent before the draft is parsed.** Validation tokenizes up
    to 8 KiB of customer CSS, and an over-budget caller that still paid for
    that parse would have a cheap way to buy work at thirty-one requests a
    minute. The precedence this fixes is 429-over-422, which is the right way
    round: \"you are sending too many\" is true of a request whether or not its
    body is also wrong, and a client that is being told to slow down does not
    need its body reviewed first. Authorisation still comes first — `@requires`
    is outside this — so a caller with no permission never spends a budget.

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
        BrandingPreviewOut | Problem
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
            body=body,
        )
    ).parsed
