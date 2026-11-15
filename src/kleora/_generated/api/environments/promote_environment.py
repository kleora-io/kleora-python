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
from ...models.promotion_in import PromotionIn
from ...models.promotion_out import PromotionOut
from ...types import Response


def _get_kwargs(
    environment_id: str,
    *,
    body: PromotionIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/environments/{environment_id}/promote".format(
            environment_id=quote(str(environment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | PromotionOut | None:
    if response.status_code == 200:
        response_200 = PromotionOut.from_dict(response.json())

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
) -> Response[Problem | PromotionOut]:
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
    body: PromotionIn,
) -> Response[Problem | PromotionOut]:
    r"""Promote sandbox configuration to production

     Copy the sandbox's configuration onto its production sibling, in one transaction.

    Settings, branding, permissions, app-scoped roles and the twelve email
    templates — never a User, a Tenant, a Client, an ApiKey or a SigningKey,
    which is what lets a promoted App keep working with the credentials its
    callers already hold (environments.md §Promotion).

    `{\"dry_run\": true}` computes the identical diff, applies nothing and emits
    no audit event; the real call writes exactly one `promotion.applied` on the
    **production** environment, including when the diff is empty because
    nothing has changed since the last promotion.

    Authorised twice. `settings:write` at account scope opens the endpoint;
    then every section of the computed diff that is not empty must be one the
    caller could have written directly — `branding:write`,
    `email_templates:write`, `permissions:write`, `roles:write` — or the answer
    is 403 `insufficient-permission` naming all of the ones lacking, with
    nothing written and no audit event. A dry run is authorised identically, so
    it reports the refusal an apply would have given rather than a diff the
    caller could not have had.

    One column is more than a value. A diff moving `tenant_mode` to `single`
    runs the preconditions the settings `PATCH` runs — 409
    `tenant-mode-switch-blocked` while production holds another Tenant, 409
    `tenant-mode-backfill-pending` while an earlier sweep is in flight — and
    queues the membership backfill when it is allowed. A dry run reports those
    refusals too, because a rehearsal that omitted them would be a rehearsal of
    a different request.

    Args:
        environment_id (str):
        body (PromotionIn): `POST /api/v1/environments/{environment_id}/promote`.

            One field, defaulting to false, and `extra="forbid"` so a caller who
            mistyped it is told rather than silently promoted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | PromotionOut]
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
    body: PromotionIn,
) -> Problem | PromotionOut | None:
    r"""Promote sandbox configuration to production

     Copy the sandbox's configuration onto its production sibling, in one transaction.

    Settings, branding, permissions, app-scoped roles and the twelve email
    templates — never a User, a Tenant, a Client, an ApiKey or a SigningKey,
    which is what lets a promoted App keep working with the credentials its
    callers already hold (environments.md §Promotion).

    `{\"dry_run\": true}` computes the identical diff, applies nothing and emits
    no audit event; the real call writes exactly one `promotion.applied` on the
    **production** environment, including when the diff is empty because
    nothing has changed since the last promotion.

    Authorised twice. `settings:write` at account scope opens the endpoint;
    then every section of the computed diff that is not empty must be one the
    caller could have written directly — `branding:write`,
    `email_templates:write`, `permissions:write`, `roles:write` — or the answer
    is 403 `insufficient-permission` naming all of the ones lacking, with
    nothing written and no audit event. A dry run is authorised identically, so
    it reports the refusal an apply would have given rather than a diff the
    caller could not have had.

    One column is more than a value. A diff moving `tenant_mode` to `single`
    runs the preconditions the settings `PATCH` runs — 409
    `tenant-mode-switch-blocked` while production holds another Tenant, 409
    `tenant-mode-backfill-pending` while an earlier sweep is in flight — and
    queues the membership backfill when it is allowed. A dry run reports those
    refusals too, because a rehearsal that omitted them would be a rehearsal of
    a different request.

    Args:
        environment_id (str):
        body (PromotionIn): `POST /api/v1/environments/{environment_id}/promote`.

            One field, defaulting to false, and `extra="forbid"` so a caller who
            mistyped it is told rather than silently promoted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | PromotionOut
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
    body: PromotionIn,
) -> Response[Problem | PromotionOut]:
    r"""Promote sandbox configuration to production

     Copy the sandbox's configuration onto its production sibling, in one transaction.

    Settings, branding, permissions, app-scoped roles and the twelve email
    templates — never a User, a Tenant, a Client, an ApiKey or a SigningKey,
    which is what lets a promoted App keep working with the credentials its
    callers already hold (environments.md §Promotion).

    `{\"dry_run\": true}` computes the identical diff, applies nothing and emits
    no audit event; the real call writes exactly one `promotion.applied` on the
    **production** environment, including when the diff is empty because
    nothing has changed since the last promotion.

    Authorised twice. `settings:write` at account scope opens the endpoint;
    then every section of the computed diff that is not empty must be one the
    caller could have written directly — `branding:write`,
    `email_templates:write`, `permissions:write`, `roles:write` — or the answer
    is 403 `insufficient-permission` naming all of the ones lacking, with
    nothing written and no audit event. A dry run is authorised identically, so
    it reports the refusal an apply would have given rather than a diff the
    caller could not have had.

    One column is more than a value. A diff moving `tenant_mode` to `single`
    runs the preconditions the settings `PATCH` runs — 409
    `tenant-mode-switch-blocked` while production holds another Tenant, 409
    `tenant-mode-backfill-pending` while an earlier sweep is in flight — and
    queues the membership backfill when it is allowed. A dry run reports those
    refusals too, because a rehearsal that omitted them would be a rehearsal of
    a different request.

    Args:
        environment_id (str):
        body (PromotionIn): `POST /api/v1/environments/{environment_id}/promote`.

            One field, defaulting to false, and `extra="forbid"` so a caller who
            mistyped it is told rather than silently promoted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | PromotionOut]
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
    body: PromotionIn,
) -> Problem | PromotionOut | None:
    r"""Promote sandbox configuration to production

     Copy the sandbox's configuration onto its production sibling, in one transaction.

    Settings, branding, permissions, app-scoped roles and the twelve email
    templates — never a User, a Tenant, a Client, an ApiKey or a SigningKey,
    which is what lets a promoted App keep working with the credentials its
    callers already hold (environments.md §Promotion).

    `{\"dry_run\": true}` computes the identical diff, applies nothing and emits
    no audit event; the real call writes exactly one `promotion.applied` on the
    **production** environment, including when the diff is empty because
    nothing has changed since the last promotion.

    Authorised twice. `settings:write` at account scope opens the endpoint;
    then every section of the computed diff that is not empty must be one the
    caller could have written directly — `branding:write`,
    `email_templates:write`, `permissions:write`, `roles:write` — or the answer
    is 403 `insufficient-permission` naming all of the ones lacking, with
    nothing written and no audit event. A dry run is authorised identically, so
    it reports the refusal an apply would have given rather than a diff the
    caller could not have had.

    One column is more than a value. A diff moving `tenant_mode` to `single`
    runs the preconditions the settings `PATCH` runs — 409
    `tenant-mode-switch-blocked` while production holds another Tenant, 409
    `tenant-mode-backfill-pending` while an earlier sweep is in flight — and
    queues the membership backfill when it is allowed. A dry run reports those
    refusals too, because a rehearsal that omitted them would be a rehearsal of
    a different request.

    Args:
        environment_id (str):
        body (PromotionIn): `POST /api/v1/environments/{environment_id}/promote`.

            One field, defaulting to false, and `extra="forbid"` so a caller who
            mistyped it is told rather than silently promoted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | PromotionOut
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
            body=body,
        )
    ).parsed
