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
from ...models.user_setting_out import UserSettingOut
from ...models.user_setting_value_in import UserSettingValueIn
from ...types import Response


def _get_kwargs(
    key: str,
    *,
    body: UserSettingValueIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/me/settings/{key}".format(
            key=quote(str(key), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | UserSettingOut | None:
    if response.status_code == 200:
        response_200 = UserSettingOut.from_dict(response.json())

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
) -> Response[Problem | UserSettingOut]:
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
    body: UserSettingValueIn,
) -> Response[Problem | UserSettingOut]:
    """Write one of the calling console user's own settings

     One value, validated exactly as `write_value` validates every write.

    `404` for a `hidden` or unknown key — indistinguishable, so a write cannot
    enumerate hidden keys (the same reason `/account/v1/settings` answers this way);
    `403` `setting-not-editable` for `user_visible`, readable above but
    operator-written only; `422` `validation-error` for anything the
    constraints refuse.

    Args:
        key (str):
        body (UserSettingValueIn): `PUT …/settings/users/{user_id}/values/{key}` — one value,
            whole.

            Never `null`: a write writes a value, and the value's legality is the
            definition's business (`422` from the shared validator), not the schema's.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UserSettingOut]
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
    body: UserSettingValueIn,
) -> Problem | UserSettingOut | None:
    """Write one of the calling console user's own settings

     One value, validated exactly as `write_value` validates every write.

    `404` for a `hidden` or unknown key — indistinguishable, so a write cannot
    enumerate hidden keys (the same reason `/account/v1/settings` answers this way);
    `403` `setting-not-editable` for `user_visible`, readable above but
    operator-written only; `422` `validation-error` for anything the
    constraints refuse.

    Args:
        key (str):
        body (UserSettingValueIn): `PUT …/settings/users/{user_id}/values/{key}` — one value,
            whole.

            Never `null`: a write writes a value, and the value's legality is the
            definition's business (`422` from the shared validator), not the schema's.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UserSettingOut
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
    body: UserSettingValueIn,
) -> Response[Problem | UserSettingOut]:
    """Write one of the calling console user's own settings

     One value, validated exactly as `write_value` validates every write.

    `404` for a `hidden` or unknown key — indistinguishable, so a write cannot
    enumerate hidden keys (the same reason `/account/v1/settings` answers this way);
    `403` `setting-not-editable` for `user_visible`, readable above but
    operator-written only; `422` `validation-error` for anything the
    constraints refuse.

    Args:
        key (str):
        body (UserSettingValueIn): `PUT …/settings/users/{user_id}/values/{key}` — one value,
            whole.

            Never `null`: a write writes a value, and the value's legality is the
            definition's business (`422` from the shared validator), not the schema's.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UserSettingOut]
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
    body: UserSettingValueIn,
) -> Problem | UserSettingOut | None:
    """Write one of the calling console user's own settings

     One value, validated exactly as `write_value` validates every write.

    `404` for a `hidden` or unknown key — indistinguishable, so a write cannot
    enumerate hidden keys (the same reason `/account/v1/settings` answers this way);
    `403` `setting-not-editable` for `user_visible`, readable above but
    operator-written only; `422` `validation-error` for anything the
    constraints refuse.

    Args:
        key (str):
        body (UserSettingValueIn): `PUT …/settings/users/{user_id}/values/{key}` — one value,
            whole.

            Never `null`: a write writes a value, and the value's legality is the
            definition's business (`422` from the shared validator), not the schema's.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UserSettingOut
    """

    return (
        await asyncio_detailed(
            key=key,
            client=client,
            body=body,
        )
    ).parsed
