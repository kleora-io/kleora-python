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
from ...models.email_template_render_in import EmailTemplateRenderIn
from ...models.email_template_rendered import EmailTemplateRendered
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    environment_id: str,
    kind: str,
    locale: str,
    *,
    body: EmailTemplateRenderIn | None | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/environments/{environment_id}/email-templates/{kind}/{locale}/render".format(
            environment_id=quote(str(environment_id), safe=""),
            kind=quote(str(kind), safe=""),
            locale=quote(str(locale), safe=""),
        ),
    }

    if isinstance(body, EmailTemplateRenderIn):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EmailTemplateRendered | Problem | None:
    if response.status_code == 200:
        response_200 = EmailTemplateRendered.from_dict(response.json())

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
) -> Response[EmailTemplateRendered | Problem]:
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
    body: EmailTemplateRenderIn | None | Unset = UNSET,
) -> Response[EmailTemplateRendered | Problem]:
    """Render an email template with sample values

     The stored row — or a draft — rendered with the sample values. Nothing is sent.

    `email_templates:read` alone, so a `viewer` keeps a working preview of a
    template they may not edit. Nothing is written and no message is enqueued:
    this is `apps.email.engine.render_source`, the same function a send goes
    through, with the sample context in place of a recipient's.

    A field present in the body replaces that column for this render only, so a
    console that has edited the HTML previews it against the saved subject
    without echoing back what it did not touch. The draft is validated exactly
    as a write would validate it — the preview of an invalid template is the
    `422` that explains why it cannot be saved — and validation renders *every*
    sample set, so which one this request asked for cannot make the preview and
    the validator disagree.

    Args:
        environment_id (str):
        kind (str):
        locale (str):
        body (EmailTemplateRenderIn | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailTemplateRendered | Problem]
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
    body: EmailTemplateRenderIn | None | Unset = UNSET,
) -> EmailTemplateRendered | Problem | None:
    """Render an email template with sample values

     The stored row — or a draft — rendered with the sample values. Nothing is sent.

    `email_templates:read` alone, so a `viewer` keeps a working preview of a
    template they may not edit. Nothing is written and no message is enqueued:
    this is `apps.email.engine.render_source`, the same function a send goes
    through, with the sample context in place of a recipient's.

    A field present in the body replaces that column for this render only, so a
    console that has edited the HTML previews it against the saved subject
    without echoing back what it did not touch. The draft is validated exactly
    as a write would validate it — the preview of an invalid template is the
    `422` that explains why it cannot be saved — and validation renders *every*
    sample set, so which one this request asked for cannot make the preview and
    the validator disagree.

    Args:
        environment_id (str):
        kind (str):
        locale (str):
        body (EmailTemplateRenderIn | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmailTemplateRendered | Problem
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
    body: EmailTemplateRenderIn | None | Unset = UNSET,
) -> Response[EmailTemplateRendered | Problem]:
    """Render an email template with sample values

     The stored row — or a draft — rendered with the sample values. Nothing is sent.

    `email_templates:read` alone, so a `viewer` keeps a working preview of a
    template they may not edit. Nothing is written and no message is enqueued:
    this is `apps.email.engine.render_source`, the same function a send goes
    through, with the sample context in place of a recipient's.

    A field present in the body replaces that column for this render only, so a
    console that has edited the HTML previews it against the saved subject
    without echoing back what it did not touch. The draft is validated exactly
    as a write would validate it — the preview of an invalid template is the
    `422` that explains why it cannot be saved — and validation renders *every*
    sample set, so which one this request asked for cannot make the preview and
    the validator disagree.

    Args:
        environment_id (str):
        kind (str):
        locale (str):
        body (EmailTemplateRenderIn | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailTemplateRendered | Problem]
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
    body: EmailTemplateRenderIn | None | Unset = UNSET,
) -> EmailTemplateRendered | Problem | None:
    """Render an email template with sample values

     The stored row — or a draft — rendered with the sample values. Nothing is sent.

    `email_templates:read` alone, so a `viewer` keeps a working preview of a
    template they may not edit. Nothing is written and no message is enqueued:
    this is `apps.email.engine.render_source`, the same function a send goes
    through, with the sample context in place of a recipient's.

    A field present in the body replaces that column for this render only, so a
    console that has edited the HTML previews it against the saved subject
    without echoing back what it did not touch. The draft is validated exactly
    as a write would validate it — the preview of an invalid template is the
    `422` that explains why it cannot be saved — and validation renders *every*
    sample set, so which one this request asked for cannot make the preview and
    the validator disagree.

    Args:
        environment_id (str):
        kind (str):
        locale (str):
        body (EmailTemplateRenderIn | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmailTemplateRendered | Problem
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
