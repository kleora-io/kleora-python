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
from ...models.flow_problem import FlowProblem
from ...models.resend_out import ResendOut
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/account/v1/email/resend",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FlowProblem | ResendOut | None:
    if response.status_code == 200:
        response_200 = ResendOut.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = FlowProblem.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FlowProblem.from_dict(response.json())

        return response_403

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
) -> Response[FlowProblem | ResendOut]:
    r"""Send another verification link to the signed-in person's own address

     Send the person's address verification email again.

    Counts toward the person's shared budget for emailed links, the same budget the hosted pages'
    resend uses. When the address is already verified, the answer is `{\"sent\": false}` and nothing
    is sent. Answers `503 unavailable` when the rate limit cannot be checked.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlowProblem | ResendOut]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> FlowProblem | ResendOut | None:
    r"""Send another verification link to the signed-in person's own address

     Send the person's address verification email again.

    Counts toward the person's shared budget for emailed links, the same budget the hosted pages'
    resend uses. When the address is already verified, the answer is `{\"sent\": false}` and nothing
    is sent. Answers `503 unavailable` when the rate limit cannot be checked.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlowProblem | ResendOut
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[FlowProblem | ResendOut]:
    r"""Send another verification link to the signed-in person's own address

     Send the person's address verification email again.

    Counts toward the person's shared budget for emailed links, the same budget the hosted pages'
    resend uses. When the address is already verified, the answer is `{\"sent\": false}` and nothing
    is sent. Answers `503 unavailable` when the rate limit cannot be checked.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlowProblem | ResendOut]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> FlowProblem | ResendOut | None:
    r"""Send another verification link to the signed-in person's own address

     Send the person's address verification email again.

    Counts toward the person's shared budget for emailed links, the same budget the hosted pages'
    resend uses. When the address is already verified, the answer is `{\"sent\": false}` and nothing
    is sent. Answers `503 unavailable` when the rate limit cannot be checked.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlowProblem | ResendOut
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
