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
    r"""Replace an email template

     The whole template, validated by the engine that renders it.

    A `PUT` rather than a merge patch because a subject and the body it belongs
    to are one edit: a message half-written by one request and half by another
    is one nobody composed. The row stops being a default, which is what makes
    `reset` meaningful and what promotion (`environments.md`) keys off.

    Everything email.md §\"Template language\" refuses is a `422` naming the
    construct and the line it sits on — the console renders it in the editor at
    that line — and all of the problems at once, so fixing a template is not one
    round trip per mistake.

    Args:
        environment_id (str):
        kind (str):
        locale (str):
        body (EmailTemplateIn): `PUT …/email-templates/{kind}/{locale}` — the whole resource, at
            once.

            Not a merge patch, which is why it is a plain `Schema`: a subject and the
            body it belongs to are one edit (email.md §API names all three fields
            required), and a template half-written by one request and half by another
            is a message no one composed.

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
    r"""Replace an email template

     The whole template, validated by the engine that renders it.

    A `PUT` rather than a merge patch because a subject and the body it belongs
    to are one edit: a message half-written by one request and half by another
    is one nobody composed. The row stops being a default, which is what makes
    `reset` meaningful and what promotion (`environments.md`) keys off.

    Everything email.md §\"Template language\" refuses is a `422` naming the
    construct and the line it sits on — the console renders it in the editor at
    that line — and all of the problems at once, so fixing a template is not one
    round trip per mistake.

    Args:
        environment_id (str):
        kind (str):
        locale (str):
        body (EmailTemplateIn): `PUT …/email-templates/{kind}/{locale}` — the whole resource, at
            once.

            Not a merge patch, which is why it is a plain `Schema`: a subject and the
            body it belongs to are one edit (email.md §API names all three fields
            required), and a template half-written by one request and half by another
            is a message no one composed.

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
    r"""Replace an email template

     The whole template, validated by the engine that renders it.

    A `PUT` rather than a merge patch because a subject and the body it belongs
    to are one edit: a message half-written by one request and half by another
    is one nobody composed. The row stops being a default, which is what makes
    `reset` meaningful and what promotion (`environments.md`) keys off.

    Everything email.md §\"Template language\" refuses is a `422` naming the
    construct and the line it sits on — the console renders it in the editor at
    that line — and all of the problems at once, so fixing a template is not one
    round trip per mistake.

    Args:
        environment_id (str):
        kind (str):
        locale (str):
        body (EmailTemplateIn): `PUT …/email-templates/{kind}/{locale}` — the whole resource, at
            once.

            Not a merge patch, which is why it is a plain `Schema`: a subject and the
            body it belongs to are one edit (email.md §API names all three fields
            required), and a template half-written by one request and half by another
            is a message no one composed.

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
    r"""Replace an email template

     The whole template, validated by the engine that renders it.

    A `PUT` rather than a merge patch because a subject and the body it belongs
    to are one edit: a message half-written by one request and half by another
    is one nobody composed. The row stops being a default, which is what makes
    `reset` meaningful and what promotion (`environments.md`) keys off.

    Everything email.md §\"Template language\" refuses is a `422` naming the
    construct and the line it sits on — the console renders it in the editor at
    that line — and all of the problems at once, so fixing a template is not one
    round trip per mistake.

    Args:
        environment_id (str):
        kind (str):
        locale (str):
        body (EmailTemplateIn): `PUT …/email-templates/{kind}/{locale}` — the whole resource, at
            once.

            Not a merge patch, which is why it is a plain `Schema`: a subject and the
            body it belongs to are one edit (email.md §API names all three fields
            required), and a template half-written by one request and half by another
            is a message no one composed.

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
