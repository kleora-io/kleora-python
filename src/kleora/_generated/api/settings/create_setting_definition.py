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
from ...models.problem import Problem
from ...models.setting_definition_in import SettingDefinitionIn
from ...models.setting_definition_out import SettingDefinitionOut
from ...types import Response


def _get_kwargs(
    environment_id: str,
    *,
    body: SettingDefinitionIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/environments/{environment_id}/settings/definitions".format(
            environment_id=quote(str(environment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | SettingDefinitionOut | None:
    if response.status_code == 201:
        response_201 = SettingDefinitionOut.from_dict(response.json())

        return response_201

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
) -> Response[Problem | SettingDefinitionOut]:
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
    body: SettingDefinitionIn,
) -> Response[Problem | SettingDefinitionOut]:
    """Create a setting definition

     A new definition. `key` and `type` are fixed here, forever.

    Constraints that do not fit the type, or a default that does not satisfy
    them, are 422 `validation-error` naming the field; a key the environment
    already defines is 409 `setting-exists`; the 51st definition is 422
    `limit-exceeded` (user-settings.md §Model, §Limits).

    Args:
        environment_id (str):
        body (SettingDefinitionIn): `POST …/settings/definitions`.

            `key` and `type` are set here and never again (user-settings.md §Model).
            `constraints` may be omitted where the type needs none — a boolean always,
            a string or number falling back to its defaults — but an enum without
            `choices` is a 422, from the same validator every other write runs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | SettingDefinitionOut]
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
    body: SettingDefinitionIn,
) -> Problem | SettingDefinitionOut | None:
    """Create a setting definition

     A new definition. `key` and `type` are fixed here, forever.

    Constraints that do not fit the type, or a default that does not satisfy
    them, are 422 `validation-error` naming the field; a key the environment
    already defines is 409 `setting-exists`; the 51st definition is 422
    `limit-exceeded` (user-settings.md §Model, §Limits).

    Args:
        environment_id (str):
        body (SettingDefinitionIn): `POST …/settings/definitions`.

            `key` and `type` are set here and never again (user-settings.md §Model).
            `constraints` may be omitted where the type needs none — a boolean always,
            a string or number falling back to its defaults — but an enum without
            `choices` is a 422, from the same validator every other write runs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | SettingDefinitionOut
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
    body: SettingDefinitionIn,
) -> Response[Problem | SettingDefinitionOut]:
    """Create a setting definition

     A new definition. `key` and `type` are fixed here, forever.

    Constraints that do not fit the type, or a default that does not satisfy
    them, are 422 `validation-error` naming the field; a key the environment
    already defines is 409 `setting-exists`; the 51st definition is 422
    `limit-exceeded` (user-settings.md §Model, §Limits).

    Args:
        environment_id (str):
        body (SettingDefinitionIn): `POST …/settings/definitions`.

            `key` and `type` are set here and never again (user-settings.md §Model).
            `constraints` may be omitted where the type needs none — a boolean always,
            a string or number falling back to its defaults — but an enum without
            `choices` is a 422, from the same validator every other write runs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | SettingDefinitionOut]
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
    body: SettingDefinitionIn,
) -> Problem | SettingDefinitionOut | None:
    """Create a setting definition

     A new definition. `key` and `type` are fixed here, forever.

    Constraints that do not fit the type, or a default that does not satisfy
    them, are 422 `validation-error` naming the field; a key the environment
    already defines is 409 `setting-exists`; the 51st definition is 422
    `limit-exceeded` (user-settings.md §Model, §Limits).

    Args:
        environment_id (str):
        body (SettingDefinitionIn): `POST …/settings/definitions`.

            `key` and `type` are set here and never again (user-settings.md §Model).
            `constraints` may be omitted where the type needs none — a boolean always,
            a string or number falling back to its defaults — but an enum without
            `choices` is a 422, from the same validator every other write runs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | SettingDefinitionOut
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
            body=body,
        )
    ).parsed
