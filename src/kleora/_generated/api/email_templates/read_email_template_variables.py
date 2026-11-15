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
from ...models.email_variables import EmailVariables
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    environment_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/environments/{environment_id}/email-templates/variables".format(
            environment_id=quote(str(environment_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EmailVariables | Problem | None:
    if response.status_code == 200:
        response_200 = EmailVariables.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Problem.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Problem.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

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
) -> Response[EmailVariables | Problem]:
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
) -> Response[EmailVariables | Problem]:
    """The variables an email template may use

     email.md §Variables, machine-readable, for the editor to render.

    A singleton document rather than a list: there is nothing to seek and
    nothing to page, and an `items`/`next_cursor` envelope around a description
    of a table would be pagination with no pagination in it (management-api.md
    §OpenAPI).

    Environment-scoped because two of the samples are the environment's own —
    `app_name` is its App's name and `link` is built on its issuer — and served
    from `apps.email.engine`'s own table, the one the validator walks and the
    renderer binds, so the console never holds a second copy of the spec's
    table. Samples are the `all` set, written in the environment's default
    locale: the editor shows what a variable stands for, and `POST …/render`
    is where the two sample sets are chosen between.

    Args:
        environment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailVariables | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    *,
    client: AuthenticatedClient,
) -> EmailVariables | Problem | None:
    """The variables an email template may use

     email.md §Variables, machine-readable, for the editor to render.

    A singleton document rather than a list: there is nothing to seek and
    nothing to page, and an `items`/`next_cursor` envelope around a description
    of a table would be pagination with no pagination in it (management-api.md
    §OpenAPI).

    Environment-scoped because two of the samples are the environment's own —
    `app_name` is its App's name and `link` is built on its issuer — and served
    from `apps.email.engine`'s own table, the one the validator walks and the
    renderer binds, so the console never holds a second copy of the spec's
    table. Samples are the `all` set, written in the environment's default
    locale: the editor shows what a variable stands for, and `POST …/render`
    is where the two sample sets are chosen between.

    Args:
        environment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmailVariables | Problem
    """

    return sync_detailed(
        environment_id=environment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[EmailVariables | Problem]:
    """The variables an email template may use

     email.md §Variables, machine-readable, for the editor to render.

    A singleton document rather than a list: there is nothing to seek and
    nothing to page, and an `items`/`next_cursor` envelope around a description
    of a table would be pagination with no pagination in it (management-api.md
    §OpenAPI).

    Environment-scoped because two of the samples are the environment's own —
    `app_name` is its App's name and `link` is built on its issuer — and served
    from `apps.email.engine`'s own table, the one the validator walks and the
    renderer binds, so the console never holds a second copy of the spec's
    table. Samples are the `all` set, written in the environment's default
    locale: the editor shows what a variable stands for, and `POST …/render`
    is where the two sample sets are chosen between.

    Args:
        environment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailVariables | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    *,
    client: AuthenticatedClient,
) -> EmailVariables | Problem | None:
    """The variables an email template may use

     email.md §Variables, machine-readable, for the editor to render.

    A singleton document rather than a list: there is nothing to seek and
    nothing to page, and an `items`/`next_cursor` envelope around a description
    of a table would be pagination with no pagination in it (management-api.md
    §OpenAPI).

    Environment-scoped because two of the samples are the environment's own —
    `app_name` is its App's name and `link` is built on its issuer — and served
    from `apps.email.engine`'s own table, the one the validator walks and the
    renderer binds, so the console never holds a second copy of the spec's
    table. Samples are the `all` set, written in the environment's default
    locale: the editor shows what a variable stands for, and `POST …/render`
    is where the two sample sets are chosen between.

    Args:
        environment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmailVariables | Problem
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
        )
    ).parsed
