# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed self-service API document
# (https://id.kleora.eu/account/v1/openapi.json). `kleora.account` wraps this tree; nothing outside the
# package imports it.
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.deletion_cancel_in import DeletionCancelIn
from ...models.flow_problem import FlowProblem
from ...types import Response


def _get_kwargs(
    *,
    body: DeletionCancelIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/account/v1/deletion",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | FlowProblem | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = FlowProblem.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FlowProblem.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FlowProblem.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = FlowProblem.from_dict(response.json())

        return response_404

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
) -> Response[Any | FlowProblem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DeletionCancelIn,
) -> Response[Any | FlowProblem]:
    """Cancel a deletion request with the token from the emailed link

     Cancel a scheduled account deletion with the token from the emailed link.

    The only operation on this API that takes no bearer token: requesting the deletion revoked every
    session, so the person has none to present. Rate limited per IP address.

    Answers `204` when the deletion is cancelled, and also when there was nothing outstanding to
    cancel. An unknown, already used or expired token, or a token of another environment, is `400
    invalid-token`.

    Args:
        body (DeletionCancelIn): The body of `DELETE /deletion`: the token from the emailed
            cancellation link.

            An unknown, used or expired token is `400 invalid-token`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FlowProblem]
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
    client: AuthenticatedClient | Client,
    body: DeletionCancelIn,
) -> Any | FlowProblem | None:
    """Cancel a deletion request with the token from the emailed link

     Cancel a scheduled account deletion with the token from the emailed link.

    The only operation on this API that takes no bearer token: requesting the deletion revoked every
    session, so the person has none to present. Rate limited per IP address.

    Answers `204` when the deletion is cancelled, and also when there was nothing outstanding to
    cancel. An unknown, already used or expired token, or a token of another environment, is `400
    invalid-token`.

    Args:
        body (DeletionCancelIn): The body of `DELETE /deletion`: the token from the emailed
            cancellation link.

            An unknown, used or expired token is `400 invalid-token`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FlowProblem
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DeletionCancelIn,
) -> Response[Any | FlowProblem]:
    """Cancel a deletion request with the token from the emailed link

     Cancel a scheduled account deletion with the token from the emailed link.

    The only operation on this API that takes no bearer token: requesting the deletion revoked every
    session, so the person has none to present. Rate limited per IP address.

    Answers `204` when the deletion is cancelled, and also when there was nothing outstanding to
    cancel. An unknown, already used or expired token, or a token of another environment, is `400
    invalid-token`.

    Args:
        body (DeletionCancelIn): The body of `DELETE /deletion`: the token from the emailed
            cancellation link.

            An unknown, used or expired token is `400 invalid-token`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FlowProblem]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DeletionCancelIn,
) -> Any | FlowProblem | None:
    """Cancel a deletion request with the token from the emailed link

     Cancel a scheduled account deletion with the token from the emailed link.

    The only operation on this API that takes no bearer token: requesting the deletion revoked every
    session, so the person has none to present. Rate limited per IP address.

    Answers `204` when the deletion is cancelled, and also when there was nothing outstanding to
    cancel. An unknown, already used or expired token, or a token of another environment, is `400
    invalid-token`.

    Args:
        body (DeletionCancelIn): The body of `DELETE /deletion`: the token from the emailed
            cancellation link.

            An unknown, used or expired token is `400 invalid-token`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FlowProblem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
