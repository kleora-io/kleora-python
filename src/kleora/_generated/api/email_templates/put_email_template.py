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
from ...models.email_template_in import EmailTemplateIn
from ...models.email_template_out import EmailTemplateOut
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    environment_id: str,
    kind: str,
    locale: str,
    *,
    body: EmailTemplateIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/environments/{environment_id}/email-templates/{kind}/{locale}".format(
            environment_id=quote(str(environment_id), safe=""),
            kind=quote(str(kind), safe=""),
            locale=quote(str(locale), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EmailTemplateOut | Problem | None:
    if response.status_code == 200:
        response_200 = EmailTemplateOut.from_dict(response.json())

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
) -> Response[EmailTemplateOut | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    environment_id: str,
    kind: str,
    locale: str,
    *,
    client: AuthenticatedClient,
    body: EmailTemplateIn,
) -> Response[EmailTemplateOut | Problem]:
    """Replace an email template

     Replace an email template: subject and body together.

    The template stops being the default, so `reset` restores the shipped version. Everything the
    template language does not allow is a `422` naming each problem and the line it is on, all at
    once.

    Args:
        environment_id (str):
        kind (str):
        locale (str):
        body (EmailTemplateIn): The body of `PUT .../email-templates/{kind}/{locale}`: the whole
            template. Every field is
            required.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailTemplateOut | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        kind=kind,
        locale=locale,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    kind: str,
    locale: str,
    *,
    client: AuthenticatedClient,
    body: EmailTemplateIn,
) -> EmailTemplateOut | Problem | None:
    """Replace an email template

     Replace an email template: subject and body together.

    The template stops being the default, so `reset` restores the shipped version. Everything the
    template language does not allow is a `422` naming each problem and the line it is on, all at
    once.

    Args:
        environment_id (str):
        kind (str):
        locale (str):
        body (EmailTemplateIn): The body of `PUT .../email-templates/{kind}/{locale}`: the whole
            template. Every field is
            required.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmailTemplateOut | Problem
    """

    return sync_detailed(
        environment_id=environment_id,
        kind=kind,
        locale=locale,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    kind: str,
    locale: str,
    *,
    client: AuthenticatedClient,
    body: EmailTemplateIn,
) -> Response[EmailTemplateOut | Problem]:
    """Replace an email template

     Replace an email template: subject and body together.

    The template stops being the default, so `reset` restores the shipped version. Everything the
    template language does not allow is a `422` naming each problem and the line it is on, all at
    once.

    Args:
        environment_id (str):
        kind (str):
        locale (str):
        body (EmailTemplateIn): The body of `PUT .../email-templates/{kind}/{locale}`: the whole
            template. Every field is
            required.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailTemplateOut | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        kind=kind,
        locale=locale,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    kind: str,
    locale: str,
    *,
    client: AuthenticatedClient,
    body: EmailTemplateIn,
) -> EmailTemplateOut | Problem | None:
    """Replace an email template

     Replace an email template: subject and body together.

    The template stops being the default, so `reset` restores the shipped version. Everything the
    template language does not allow is a `422` naming each problem and the line it is on, all at
    once.

    Args:
        environment_id (str):
        kind (str):
        locale (str):
        body (EmailTemplateIn): The body of `PUT .../email-templates/{kind}/{locale}`: the whole
            template. Every field is
            required.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmailTemplateOut | Problem
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            kind=kind,
            locale=locale,
            client=client,
            body=body,
        )
    ).parsed
