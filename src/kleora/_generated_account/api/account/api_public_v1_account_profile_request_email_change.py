# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed self-service API document
# (https://id.kleora.eu/account/v1/openapi.json). `kleora.account` wraps this tree; nothing outside the
# package imports it.
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.email_change_in import EmailChangeIn
from ...models.flow_problem import FlowProblem
from ...models.resend_out import ResendOut
from ...types import Response


def _get_kwargs(
    *,
    body: EmailChangeIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/account/v1/email",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FlowProblem | ResendOut | None:
    if response.status_code == 202:
        response_202 = ResendOut.from_dict(response.json())

        return response_202

    if response.status_code == 401:
        response_401 = FlowProblem.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FlowProblem.from_dict(response.json())

        return response_403

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
) -> Response[FlowProblem | ResendOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: EmailChangeIn,
) -> Response[FlowProblem | ResendOut]:
    r"""Ask to change the signed-in person's own email address

     Step 1 of two: mail a confirmation link to the **new** address.

    Sensitive — §\"The operations\" marks it — so `@self_service` has already refused an
    un-re-authenticated caller before this body runs. That gate is the reason the
    operation can be so plain: it changes nothing, and everything it could change is
    behind a link that arrives somewhere the caller may not be able to read.

    **`202 {\"sent\": true}` whatever happens**, which is §API's row and
    §\"Failure modes\"' \"`POST /email` with an address already registered in this
    Environment | `202` | identical to success, and nothing is sent\". `ResendOut` is
    reused rather than a `SentOut` of its own: it is `{\"sent\": bool}` and the bool is
    always `true` here, which is exactly the point — a generated client sees one shape
    for \"a mail was asked for\" across this surface, and a second schema with the same
    single member would be two names for one thing.

    Why `true` and not the truth: the document is what a stranger reads. §API declares
    the literal and the no-enumeration rule requires it, so the one branch that sends
    nothing must be indistinguishable — including in the budget, which is why
    `mail_send` is spent here, ahead of the service's decision.

    **The shared per-user mailed-link budget, not a bucket of its own.**
    §\"Rate limits\" gives this row as \"*the shared per-user mailed-link budget*\" — one
    window across verification, reset and this, counted for the person. So the
    `@self_service` limiter stays the catch-all row (there is no `account-email` bucket
    to declare) and `throttles.mail_send` is the real limit, exactly as
    `POST /email/resend` above spends it.

    Args:
        body (EmailChangeIn): §"Changing an email address" step 1: `POST /email` with `{email}`.

            **The member is `email`, which `authz.SUBJECT_NAMES` refuses**, so `POST /email`
            declares `writes_own={"email"}` — the one declared exception on this surface, and
            `api.public.v1.account.authz`'s module docstring argues it. The spec gives the
            body as `{email}` and the spec wins; what the declaration says is that this
            `email` is a value written onto the caller's own row rather than a way to name
            somebody else's.

            `max_length` and nothing else. §"Failure modes" wants a malformed or over-length
            address to be `422 validation-error` with `field = "email"` — "the caller is a
            program here, not a login form, so there is no oracle to protect: it never saw an
            address it did not supply" — and the normalisation and the real validation are
            `users-and-credentials.md` §Email's, applied by the service through
            `normalise_email` and `validate_user_email`. A pydantic `EmailStr` here would be
            a *second* definition of a valid address, which is the thing `User.email` is a
            `CharField` rather than an `EmailField` to avoid.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlowProblem | ResendOut]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: EmailChangeIn,
) -> FlowProblem | ResendOut | None:
    r"""Ask to change the signed-in person's own email address

     Step 1 of two: mail a confirmation link to the **new** address.

    Sensitive — §\"The operations\" marks it — so `@self_service` has already refused an
    un-re-authenticated caller before this body runs. That gate is the reason the
    operation can be so plain: it changes nothing, and everything it could change is
    behind a link that arrives somewhere the caller may not be able to read.

    **`202 {\"sent\": true}` whatever happens**, which is §API's row and
    §\"Failure modes\"' \"`POST /email` with an address already registered in this
    Environment | `202` | identical to success, and nothing is sent\". `ResendOut` is
    reused rather than a `SentOut` of its own: it is `{\"sent\": bool}` and the bool is
    always `true` here, which is exactly the point — a generated client sees one shape
    for \"a mail was asked for\" across this surface, and a second schema with the same
    single member would be two names for one thing.

    Why `true` and not the truth: the document is what a stranger reads. §API declares
    the literal and the no-enumeration rule requires it, so the one branch that sends
    nothing must be indistinguishable — including in the budget, which is why
    `mail_send` is spent here, ahead of the service's decision.

    **The shared per-user mailed-link budget, not a bucket of its own.**
    §\"Rate limits\" gives this row as \"*the shared per-user mailed-link budget*\" — one
    window across verification, reset and this, counted for the person. So the
    `@self_service` limiter stays the catch-all row (there is no `account-email` bucket
    to declare) and `throttles.mail_send` is the real limit, exactly as
    `POST /email/resend` above spends it.

    Args:
        body (EmailChangeIn): §"Changing an email address" step 1: `POST /email` with `{email}`.

            **The member is `email`, which `authz.SUBJECT_NAMES` refuses**, so `POST /email`
            declares `writes_own={"email"}` — the one declared exception on this surface, and
            `api.public.v1.account.authz`'s module docstring argues it. The spec gives the
            body as `{email}` and the spec wins; what the declaration says is that this
            `email` is a value written onto the caller's own row rather than a way to name
            somebody else's.

            `max_length` and nothing else. §"Failure modes" wants a malformed or over-length
            address to be `422 validation-error` with `field = "email"` — "the caller is a
            program here, not a login form, so there is no oracle to protect: it never saw an
            address it did not supply" — and the normalisation and the real validation are
            `users-and-credentials.md` §Email's, applied by the service through
            `normalise_email` and `validate_user_email`. A pydantic `EmailStr` here would be
            a *second* definition of a valid address, which is the thing `User.email` is a
            `CharField` rather than an `EmailField` to avoid.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlowProblem | ResendOut
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: EmailChangeIn,
) -> Response[FlowProblem | ResendOut]:
    r"""Ask to change the signed-in person's own email address

     Step 1 of two: mail a confirmation link to the **new** address.

    Sensitive — §\"The operations\" marks it — so `@self_service` has already refused an
    un-re-authenticated caller before this body runs. That gate is the reason the
    operation can be so plain: it changes nothing, and everything it could change is
    behind a link that arrives somewhere the caller may not be able to read.

    **`202 {\"sent\": true}` whatever happens**, which is §API's row and
    §\"Failure modes\"' \"`POST /email` with an address already registered in this
    Environment | `202` | identical to success, and nothing is sent\". `ResendOut` is
    reused rather than a `SentOut` of its own: it is `{\"sent\": bool}` and the bool is
    always `true` here, which is exactly the point — a generated client sees one shape
    for \"a mail was asked for\" across this surface, and a second schema with the same
    single member would be two names for one thing.

    Why `true` and not the truth: the document is what a stranger reads. §API declares
    the literal and the no-enumeration rule requires it, so the one branch that sends
    nothing must be indistinguishable — including in the budget, which is why
    `mail_send` is spent here, ahead of the service's decision.

    **The shared per-user mailed-link budget, not a bucket of its own.**
    §\"Rate limits\" gives this row as \"*the shared per-user mailed-link budget*\" — one
    window across verification, reset and this, counted for the person. So the
    `@self_service` limiter stays the catch-all row (there is no `account-email` bucket
    to declare) and `throttles.mail_send` is the real limit, exactly as
    `POST /email/resend` above spends it.

    Args:
        body (EmailChangeIn): §"Changing an email address" step 1: `POST /email` with `{email}`.

            **The member is `email`, which `authz.SUBJECT_NAMES` refuses**, so `POST /email`
            declares `writes_own={"email"}` — the one declared exception on this surface, and
            `api.public.v1.account.authz`'s module docstring argues it. The spec gives the
            body as `{email}` and the spec wins; what the declaration says is that this
            `email` is a value written onto the caller's own row rather than a way to name
            somebody else's.

            `max_length` and nothing else. §"Failure modes" wants a malformed or over-length
            address to be `422 validation-error` with `field = "email"` — "the caller is a
            program here, not a login form, so there is no oracle to protect: it never saw an
            address it did not supply" — and the normalisation and the real validation are
            `users-and-credentials.md` §Email's, applied by the service through
            `normalise_email` and `validate_user_email`. A pydantic `EmailStr` here would be
            a *second* definition of a valid address, which is the thing `User.email` is a
            `CharField` rather than an `EmailField` to avoid.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlowProblem | ResendOut]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: EmailChangeIn,
) -> FlowProblem | ResendOut | None:
    r"""Ask to change the signed-in person's own email address

     Step 1 of two: mail a confirmation link to the **new** address.

    Sensitive — §\"The operations\" marks it — so `@self_service` has already refused an
    un-re-authenticated caller before this body runs. That gate is the reason the
    operation can be so plain: it changes nothing, and everything it could change is
    behind a link that arrives somewhere the caller may not be able to read.

    **`202 {\"sent\": true}` whatever happens**, which is §API's row and
    §\"Failure modes\"' \"`POST /email` with an address already registered in this
    Environment | `202` | identical to success, and nothing is sent\". `ResendOut` is
    reused rather than a `SentOut` of its own: it is `{\"sent\": bool}` and the bool is
    always `true` here, which is exactly the point — a generated client sees one shape
    for \"a mail was asked for\" across this surface, and a second schema with the same
    single member would be two names for one thing.

    Why `true` and not the truth: the document is what a stranger reads. §API declares
    the literal and the no-enumeration rule requires it, so the one branch that sends
    nothing must be indistinguishable — including in the budget, which is why
    `mail_send` is spent here, ahead of the service's decision.

    **The shared per-user mailed-link budget, not a bucket of its own.**
    §\"Rate limits\" gives this row as \"*the shared per-user mailed-link budget*\" — one
    window across verification, reset and this, counted for the person. So the
    `@self_service` limiter stays the catch-all row (there is no `account-email` bucket
    to declare) and `throttles.mail_send` is the real limit, exactly as
    `POST /email/resend` above spends it.

    Args:
        body (EmailChangeIn): §"Changing an email address" step 1: `POST /email` with `{email}`.

            **The member is `email`, which `authz.SUBJECT_NAMES` refuses**, so `POST /email`
            declares `writes_own={"email"}` — the one declared exception on this surface, and
            `api.public.v1.account.authz`'s module docstring argues it. The spec gives the
            body as `{email}` and the spec wins; what the declaration says is that this
            `email` is a value written onto the caller's own row rather than a way to name
            somebody else's.

            `max_length` and nothing else. §"Failure modes" wants a malformed or over-length
            address to be `422 validation-error` with `field = "email"` — "the caller is a
            program here, not a login form, so there is no oracle to protect: it never saw an
            address it did not supply" — and the normalisation and the real validation are
            `users-and-credentials.md` §Email's, applied by the service through
            `normalise_email` and `validate_user_email`. A pydantic `EmailStr` here would be
            a *second* definition of a valid address, which is the thing `User.email` is a
            `CharField` rather than an `EmailField` to avoid.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlowProblem | ResendOut
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
