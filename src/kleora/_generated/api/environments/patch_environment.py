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
    r"""Change an environment's settings

     Any subset of the settings columns, validated against domain-model.md.

    Refusals that are not the schema's. `tenant_mode` and `no_tenant_behaviour`
    on the `id` App's environments are 409 `platform-protected`: they decide how
    the console's own users are grouped, and a customer switching them would be
    changing the shape of every Account's membership (platform-bootstrap.md
    §Invariants). `no_tenant_behaviour=create` needs a `tenant_creator_role`,
    and a `tenant_creator_role` has to name an app-scoped role of this
    environment — both are the model's rules, arriving as a `ValidationError`
    and leaving as a 422 naming the field. And `multi` → `single` is refused
    while another Tenant exists (409 `tenant-mode-switch-blocked`) or while an
    earlier switch's backfill is still in flight (409
    `tenant-mode-backfill-pending`).

    **202, not 200**, for the `PATCH` that starts that backfill: the settings
    are applied and durable, but the memberships `single` mode owes are written
    by a Celery task, and the body reports `backfill_status: \"pending\"` until it
    is done (environments.md §API, tenants-and-membership.md §\"Tenant modes\").

    And `mfa_policy: required` is 402 `payment-required` on a plan that does
    not carry MFA enforcement (billing.md §Plans; mfa.md §\"What a plan gates\").
    Only that value: `off` and `optional` are on every plan, and a downgrade
    writes a stored `required` **down** to `optional` rather than leaving the
    column saying one thing while the login flow does another
    (`apps.billing.dunning.relax_mfa_policy`).

    **The authentication policy is a person's to change.** `mfa_policy`,
    `password_min_length` and `password_breach_check` are accepted only from a
    `console_user`. Any other credential that sends one of them, whatever the
    value — an API key holding `settings:write` among them — gets 403
    `insufficient-scope` naming the fields, and nothing in the request is
    applied (environments.md §API).

    Args:
        environment_id (str):
        body (EnvironmentPatch): `PATCH /api/v1/environments/{environment_id}` — the settings
            columns.

            The ranges are the model's and the document's at once: declared here, they
            reach `/api/v1/openapi.json`, so a generated client refuses an
            `access_token_ttl` of 30 before the request is made, and a hand-written
            caller that sends one gets 422 with the field in `errors[]` rather than a
            500 from the check constraint.

            `issuer`, `kind` and `backfill_status` are named in `immutable_fields`
            rather than left off: the issuer is stored on this row because every token's
            `iss` and every cached JWKS entry names it, `kind` is what a `kl_test_` key
            is confined to, and `backfill_status` is a report on work in progress. All
            three are plainly properties of the resource, so refusing them as unknown
            keys would read as a typo (environments.md §API).

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
    r"""Change an environment's settings

     Any subset of the settings columns, validated against domain-model.md.

    Refusals that are not the schema's. `tenant_mode` and `no_tenant_behaviour`
    on the `id` App's environments are 409 `platform-protected`: they decide how
    the console's own users are grouped, and a customer switching them would be
    changing the shape of every Account's membership (platform-bootstrap.md
    §Invariants). `no_tenant_behaviour=create` needs a `tenant_creator_role`,
    and a `tenant_creator_role` has to name an app-scoped role of this
    environment — both are the model's rules, arriving as a `ValidationError`
    and leaving as a 422 naming the field. And `multi` → `single` is refused
    while another Tenant exists (409 `tenant-mode-switch-blocked`) or while an
    earlier switch's backfill is still in flight (409
    `tenant-mode-backfill-pending`).

    **202, not 200**, for the `PATCH` that starts that backfill: the settings
    are applied and durable, but the memberships `single` mode owes are written
    by a Celery task, and the body reports `backfill_status: \"pending\"` until it
    is done (environments.md §API, tenants-and-membership.md §\"Tenant modes\").

    And `mfa_policy: required` is 402 `payment-required` on a plan that does
    not carry MFA enforcement (billing.md §Plans; mfa.md §\"What a plan gates\").
    Only that value: `off` and `optional` are on every plan, and a downgrade
    writes a stored `required` **down** to `optional` rather than leaving the
    column saying one thing while the login flow does another
    (`apps.billing.dunning.relax_mfa_policy`).

    **The authentication policy is a person's to change.** `mfa_policy`,
    `password_min_length` and `password_breach_check` are accepted only from a
    `console_user`. Any other credential that sends one of them, whatever the
    value — an API key holding `settings:write` among them — gets 403
    `insufficient-scope` naming the fields, and nothing in the request is
    applied (environments.md §API).

    Args:
        environment_id (str):
        body (EnvironmentPatch): `PATCH /api/v1/environments/{environment_id}` — the settings
            columns.

            The ranges are the model's and the document's at once: declared here, they
            reach `/api/v1/openapi.json`, so a generated client refuses an
            `access_token_ttl` of 30 before the request is made, and a hand-written
            caller that sends one gets 422 with the field in `errors[]` rather than a
            500 from the check constraint.

            `issuer`, `kind` and `backfill_status` are named in `immutable_fields`
            rather than left off: the issuer is stored on this row because every token's
            `iss` and every cached JWKS entry names it, `kind` is what a `kl_test_` key
            is confined to, and `backfill_status` is a report on work in progress. All
            three are plainly properties of the resource, so refusing them as unknown
            keys would read as a typo (environments.md §API).

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
    r"""Change an environment's settings

     Any subset of the settings columns, validated against domain-model.md.

    Refusals that are not the schema's. `tenant_mode` and `no_tenant_behaviour`
    on the `id` App's environments are 409 `platform-protected`: they decide how
    the console's own users are grouped, and a customer switching them would be
    changing the shape of every Account's membership (platform-bootstrap.md
    §Invariants). `no_tenant_behaviour=create` needs a `tenant_creator_role`,
    and a `tenant_creator_role` has to name an app-scoped role of this
    environment — both are the model's rules, arriving as a `ValidationError`
    and leaving as a 422 naming the field. And `multi` → `single` is refused
    while another Tenant exists (409 `tenant-mode-switch-blocked`) or while an
    earlier switch's backfill is still in flight (409
    `tenant-mode-backfill-pending`).

    **202, not 200**, for the `PATCH` that starts that backfill: the settings
    are applied and durable, but the memberships `single` mode owes are written
    by a Celery task, and the body reports `backfill_status: \"pending\"` until it
    is done (environments.md §API, tenants-and-membership.md §\"Tenant modes\").

    And `mfa_policy: required` is 402 `payment-required` on a plan that does
    not carry MFA enforcement (billing.md §Plans; mfa.md §\"What a plan gates\").
    Only that value: `off` and `optional` are on every plan, and a downgrade
    writes a stored `required` **down** to `optional` rather than leaving the
    column saying one thing while the login flow does another
    (`apps.billing.dunning.relax_mfa_policy`).

    **The authentication policy is a person's to change.** `mfa_policy`,
    `password_min_length` and `password_breach_check` are accepted only from a
    `console_user`. Any other credential that sends one of them, whatever the
    value — an API key holding `settings:write` among them — gets 403
    `insufficient-scope` naming the fields, and nothing in the request is
    applied (environments.md §API).

    Args:
        environment_id (str):
        body (EnvironmentPatch): `PATCH /api/v1/environments/{environment_id}` — the settings
            columns.

            The ranges are the model's and the document's at once: declared here, they
            reach `/api/v1/openapi.json`, so a generated client refuses an
            `access_token_ttl` of 30 before the request is made, and a hand-written
            caller that sends one gets 422 with the field in `errors[]` rather than a
            500 from the check constraint.

            `issuer`, `kind` and `backfill_status` are named in `immutable_fields`
            rather than left off: the issuer is stored on this row because every token's
            `iss` and every cached JWKS entry names it, `kind` is what a `kl_test_` key
            is confined to, and `backfill_status` is a report on work in progress. All
            three are plainly properties of the resource, so refusing them as unknown
            keys would read as a typo (environments.md §API).

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
    r"""Change an environment's settings

     Any subset of the settings columns, validated against domain-model.md.

    Refusals that are not the schema's. `tenant_mode` and `no_tenant_behaviour`
    on the `id` App's environments are 409 `platform-protected`: they decide how
    the console's own users are grouped, and a customer switching them would be
    changing the shape of every Account's membership (platform-bootstrap.md
    §Invariants). `no_tenant_behaviour=create` needs a `tenant_creator_role`,
    and a `tenant_creator_role` has to name an app-scoped role of this
    environment — both are the model's rules, arriving as a `ValidationError`
    and leaving as a 422 naming the field. And `multi` → `single` is refused
    while another Tenant exists (409 `tenant-mode-switch-blocked`) or while an
    earlier switch's backfill is still in flight (409
    `tenant-mode-backfill-pending`).

    **202, not 200**, for the `PATCH` that starts that backfill: the settings
    are applied and durable, but the memberships `single` mode owes are written
    by a Celery task, and the body reports `backfill_status: \"pending\"` until it
    is done (environments.md §API, tenants-and-membership.md §\"Tenant modes\").

    And `mfa_policy: required` is 402 `payment-required` on a plan that does
    not carry MFA enforcement (billing.md §Plans; mfa.md §\"What a plan gates\").
    Only that value: `off` and `optional` are on every plan, and a downgrade
    writes a stored `required` **down** to `optional` rather than leaving the
    column saying one thing while the login flow does another
    (`apps.billing.dunning.relax_mfa_policy`).

    **The authentication policy is a person's to change.** `mfa_policy`,
    `password_min_length` and `password_breach_check` are accepted only from a
    `console_user`. Any other credential that sends one of them, whatever the
    value — an API key holding `settings:write` among them — gets 403
    `insufficient-scope` naming the fields, and nothing in the request is
    applied (environments.md §API).

    Args:
        environment_id (str):
        body (EnvironmentPatch): `PATCH /api/v1/environments/{environment_id}` — the settings
            columns.

            The ranges are the model's and the document's at once: declared here, they
            reach `/api/v1/openapi.json`, so a generated client refuses an
            `access_token_ttl` of 30 before the request is made, and a hand-written
            caller that sends one gets 422 with the field in `errors[]` rather than a
            500 from the check constraint.

            `issuer`, `kind` and `backfill_status` are named in `immutable_fields`
            rather than left off: the issuer is stored on this row because every token's
            `iss` and every cached JWKS entry names it, `kind` is what a `kl_test_` key
            is confined to, and `backfill_status` is a report on work in progress. All
            three are plainly properties of the resource, so refusing them as unknown
            keys would read as a typo (environments.md §API).

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
