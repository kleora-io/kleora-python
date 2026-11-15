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
from ...models.environment_out import EnvironmentOut
from ...models.environment_patch import EnvironmentPatch
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    environment_id: str,
    *,
    body: EnvironmentPatch,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/environments/{environment_id}".format(
            environment_id=quote(str(environment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EnvironmentOut | Problem | None:
    if response.status_code == 200:
        response_200 = EnvironmentOut.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = EnvironmentOut.from_dict(response.json())

        return response_202

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
) -> Response[EnvironmentOut | Problem]:
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
    body: EnvironmentPatch,
) -> Response[EnvironmentOut | Problem]:
    """Change an environment's settings

     Update any subset of the environment's settings.

    - `tenant_mode` and `no_tenant_behaviour` cannot be changed on the platform's own `id` App: `409
      platform-protected`.
    - `no_tenant_behaviour=create` needs a `tenant_creator_role`, which must name an app-scoped role
      of this environment; otherwise `422` naming the field.
    - Switching `tenant_mode` from `multi` to `single` is refused while another tenant exists (`409
      tenant-mode-switch-blocked`) or while an earlier switch is still being applied (`409
      tenant-mode-backfill-pending`).

    The `PATCH` that switches to `single` answers `202`: the settings are saved, but the memberships
    the new mode needs are written in the background, and `backfill_status` reads `pending` until
    that is done.

    `mfa_policy: required` is `402 payment-required` on a plan without MFA enforcement; `off` and
    `optional` are available on every plan.

    `mfa_policy`, `password_min_length` and `password_breach_check` can only be changed by a console
    user. Any other credential sending one of them, whatever the value, gets `403
    insufficient-scope` naming the fields, and nothing in the request is applied.

    Args:
        environment_id (str):
        body (EnvironmentPatch): The body of `PATCH /api/v1/environments/{environment_id}`: the
            environment's settings.

            Out-of-range values are `422` naming the field. `issuer`, `kind` and `backfill_status`
            cannot be
            changed and are refused as immutable.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnvironmentOut | Problem]
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
    body: EnvironmentPatch,
) -> EnvironmentOut | Problem | None:
    """Change an environment's settings

     Update any subset of the environment's settings.

    - `tenant_mode` and `no_tenant_behaviour` cannot be changed on the platform's own `id` App: `409
      platform-protected`.
    - `no_tenant_behaviour=create` needs a `tenant_creator_role`, which must name an app-scoped role
      of this environment; otherwise `422` naming the field.
    - Switching `tenant_mode` from `multi` to `single` is refused while another tenant exists (`409
      tenant-mode-switch-blocked`) or while an earlier switch is still being applied (`409
      tenant-mode-backfill-pending`).

    The `PATCH` that switches to `single` answers `202`: the settings are saved, but the memberships
    the new mode needs are written in the background, and `backfill_status` reads `pending` until
    that is done.

    `mfa_policy: required` is `402 payment-required` on a plan without MFA enforcement; `off` and
    `optional` are available on every plan.

    `mfa_policy`, `password_min_length` and `password_breach_check` can only be changed by a console
    user. Any other credential sending one of them, whatever the value, gets `403
    insufficient-scope` naming the fields, and nothing in the request is applied.

    Args:
        environment_id (str):
        body (EnvironmentPatch): The body of `PATCH /api/v1/environments/{environment_id}`: the
            environment's settings.

            Out-of-range values are `422` naming the field. `issuer`, `kind` and `backfill_status`
            cannot be
            changed and are refused as immutable.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnvironmentOut | Problem
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
    body: EnvironmentPatch,
) -> Response[EnvironmentOut | Problem]:
    """Change an environment's settings

     Update any subset of the environment's settings.

    - `tenant_mode` and `no_tenant_behaviour` cannot be changed on the platform's own `id` App: `409
      platform-protected`.
    - `no_tenant_behaviour=create` needs a `tenant_creator_role`, which must name an app-scoped role
      of this environment; otherwise `422` naming the field.
    - Switching `tenant_mode` from `multi` to `single` is refused while another tenant exists (`409
      tenant-mode-switch-blocked`) or while an earlier switch is still being applied (`409
      tenant-mode-backfill-pending`).

    The `PATCH` that switches to `single` answers `202`: the settings are saved, but the memberships
    the new mode needs are written in the background, and `backfill_status` reads `pending` until
    that is done.

    `mfa_policy: required` is `402 payment-required` on a plan without MFA enforcement; `off` and
    `optional` are available on every plan.

    `mfa_policy`, `password_min_length` and `password_breach_check` can only be changed by a console
    user. Any other credential sending one of them, whatever the value, gets `403
    insufficient-scope` naming the fields, and nothing in the request is applied.

    Args:
        environment_id (str):
        body (EnvironmentPatch): The body of `PATCH /api/v1/environments/{environment_id}`: the
            environment's settings.

            Out-of-range values are `422` naming the field. `issuer`, `kind` and `backfill_status`
            cannot be
            changed and are refused as immutable.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnvironmentOut | Problem]
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
    body: EnvironmentPatch,
) -> EnvironmentOut | Problem | None:
    """Change an environment's settings

     Update any subset of the environment's settings.

    - `tenant_mode` and `no_tenant_behaviour` cannot be changed on the platform's own `id` App: `409
      platform-protected`.
    - `no_tenant_behaviour=create` needs a `tenant_creator_role`, which must name an app-scoped role
      of this environment; otherwise `422` naming the field.
    - Switching `tenant_mode` from `multi` to `single` is refused while another tenant exists (`409
      tenant-mode-switch-blocked`) or while an earlier switch is still being applied (`409
      tenant-mode-backfill-pending`).

    The `PATCH` that switches to `single` answers `202`: the settings are saved, but the memberships
    the new mode needs are written in the background, and `backfill_status` reads `pending` until
    that is done.

    `mfa_policy: required` is `402 payment-required` on a plan without MFA enforcement; `off` and
    `optional` are available on every plan.

    `mfa_policy`, `password_min_length` and `password_breach_check` can only be changed by a console
    user. Any other credential sending one of them, whatever the value, gets `403
    insufficient-scope` naming the fields, and nothing in the request is applied.

    Args:
        environment_id (str):
        body (EnvironmentPatch): The body of `PATCH /api/v1/environments/{environment_id}`: the
            environment's settings.

            Out-of-range values are `422` naming the field. `issuer`, `kind` and `backfill_status`
            cannot be
            changed and are refused as immutable.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnvironmentOut | Problem
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
            body=body,
        )
    ).parsed
