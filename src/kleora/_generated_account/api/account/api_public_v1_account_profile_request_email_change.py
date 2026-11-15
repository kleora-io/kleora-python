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

     Step 1 of changing the email address: email a confirmation link to the new address.

    Requires a recent re-authentication. Nothing changes until the link is confirmed with `POST
    /email/confirm`.

    Always answers `202 {\"sent\": true}`, including when the address is already registered in this
    environment (in which case nothing is sent), so the answer does not reveal which addresses
    exist. Counts toward the person's shared budget for emailed links, along with verification and
    password reset mail.

    Args:
        body (EmailChangeIn): The body of `POST /email`: the new address.

            A malformed or over-long address is `422 validation-error` with `field = "email"`.

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

     Step 1 of changing the email address: email a confirmation link to the new address.

    Requires a recent re-authentication. Nothing changes until the link is confirmed with `POST
    /email/confirm`.

    Always answers `202 {\"sent\": true}`, including when the address is already registered in this
    environment (in which case nothing is sent), so the answer does not reveal which addresses
    exist. Counts toward the person's shared budget for emailed links, along with verification and
    password reset mail.

    Args:
        body (EmailChangeIn): The body of `POST /email`: the new address.

            A malformed or over-long address is `422 validation-error` with `field = "email"`.

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

     Step 1 of changing the email address: email a confirmation link to the new address.

    Requires a recent re-authentication. Nothing changes until the link is confirmed with `POST
    /email/confirm`.

    Always answers `202 {\"sent\": true}`, including when the address is already registered in this
    environment (in which case nothing is sent), so the answer does not reveal which addresses
    exist. Counts toward the person's shared budget for emailed links, along with verification and
    password reset mail.

    Args:
        body (EmailChangeIn): The body of `POST /email`: the new address.

            A malformed or over-long address is `422 validation-error` with `field = "email"`.

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

     Step 1 of changing the email address: email a confirmation link to the new address.

    Requires a recent re-authentication. Nothing changes until the link is confirmed with `POST
    /email/confirm`.

    Always answers `202 {\"sent\": true}`, including when the address is already registered in this
    environment (in which case nothing is sent), so the answer does not reveal which addresses
    exist. Counts toward the person's shared budget for emailed links, along with verification and
    password reset mail.

    Args:
        body (EmailChangeIn): The body of `POST /email`: the new address.

            A malformed or over-long address is `422 validation-error` with `field = "email"`.

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
