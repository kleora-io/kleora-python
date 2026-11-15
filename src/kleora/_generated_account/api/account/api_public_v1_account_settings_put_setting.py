# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed self-service API document
# (https://id.kleora.eu/account/v1/openapi.json). `kleora.account` wraps this tree; nothing outside the
# package imports it.
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.flow_problem import FlowProblem
from ...models.setting_in import SettingIn
from ...models.user_setting_document import UserSettingDocument
from ...types import Response


def _get_kwargs(
    key: str,
    *,
    body: SettingIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/account/v1/settings/{key}".format(
            key=quote(str(key), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FlowProblem | UserSettingDocument | None:
    if response.status_code == 200:
        response_200 = UserSettingDocument.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = FlowProblem.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FlowProblem.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = FlowProblem.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = FlowProblem.from_dict(response.json())

        return response_422

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
) -> Response[FlowProblem | UserSettingDocument]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    key: str,
    *,
    client: AuthenticatedClient,
    body: SettingIn,
) -> Response[FlowProblem | UserSettingDocument]:
    """Write one of the signed-in person's own settings

     One value, validated against the definition by the shared validator.

    `404 setting-not-found` for a key this environment does not define *and* for a
    `hidden` one — byte-identical but for `instance` and `request_id`, so probing
    writes cannot enumerate hidden keys. `403 setting-not-editable` for
    `user_visible`: readable in the listing, operator-writable only. `422` names
    `value` for anything the constraints refuse —
    `apps.settings.validation.validate_value` is the one validator every writer
    takes (`P5-02`), non-finite numbers included.

    Args:
        key (str):
        body (SettingIn): One value, of whatever shape the definition's constraints allow.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlowProblem | UserSettingDocument]
    """

    kwargs = _get_kwargs(
        key=key,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    key: str,
    *,
    client: AuthenticatedClient,
    body: SettingIn,
) -> FlowProblem | UserSettingDocument | None:
    """Write one of the signed-in person's own settings

     One value, validated against the definition by the shared validator.

    `404 setting-not-found` for a key this environment does not define *and* for a
    `hidden` one — byte-identical but for `instance` and `request_id`, so probing
    writes cannot enumerate hidden keys. `403 setting-not-editable` for
    `user_visible`: readable in the listing, operator-writable only. `422` names
    `value` for anything the constraints refuse —
    `apps.settings.validation.validate_value` is the one validator every writer
    takes (`P5-02`), non-finite numbers included.

    Args:
        key (str):
        body (SettingIn): One value, of whatever shape the definition's constraints allow.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlowProblem | UserSettingDocument
    """

    return sync_detailed(
        key=key,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    key: str,
    *,
    client: AuthenticatedClient,
    body: SettingIn,
) -> Response[FlowProblem | UserSettingDocument]:
    """Write one of the signed-in person's own settings

     One value, validated against the definition by the shared validator.

    `404 setting-not-found` for a key this environment does not define *and* for a
    `hidden` one — byte-identical but for `instance` and `request_id`, so probing
    writes cannot enumerate hidden keys. `403 setting-not-editable` for
    `user_visible`: readable in the listing, operator-writable only. `422` names
    `value` for anything the constraints refuse —
    `apps.settings.validation.validate_value` is the one validator every writer
    takes (`P5-02`), non-finite numbers included.

    Args:
        key (str):
        body (SettingIn): One value, of whatever shape the definition's constraints allow.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlowProblem | UserSettingDocument]
    """

    kwargs = _get_kwargs(
        key=key,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    key: str,
    *,
    client: AuthenticatedClient,
    body: SettingIn,
) -> FlowProblem | UserSettingDocument | None:
    """Write one of the signed-in person's own settings

     One value, validated against the definition by the shared validator.

    `404 setting-not-found` for a key this environment does not define *and* for a
    `hidden` one — byte-identical but for `instance` and `request_id`, so probing
    writes cannot enumerate hidden keys. `403 setting-not-editable` for
    `user_visible`: readable in the listing, operator-writable only. `422` names
    `value` for anything the constraints refuse —
    `apps.settings.validation.validate_value` is the one validator every writer
    takes (`P5-02`), non-finite numbers included.

    Args:
        key (str):
        body (SettingIn): One value, of whatever shape the definition's constraints allow.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlowProblem | UserSettingDocument
    """

    return (
        await asyncio_detailed(
            key=key,
            client=client,
            body=body,
        )
    ).parsed
