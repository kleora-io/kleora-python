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
from ...models.profile_out import ProfileOut
from ...models.profile_patch import ProfilePatch
from ...types import Response


def _get_kwargs(
    *,
    body: ProfilePatch,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/account/v1/profile",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FlowProblem | ProfileOut | None:
    if response.status_code == 200:
        response_200 = ProfileOut.from_dict(response.json())

        return response_200

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
) -> Response[FlowProblem | ProfileOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ProfilePatch,
) -> Response[FlowProblem | ProfileOut]:
    r"""Change the signed-in person's own name, language or picture

     Not sensitive, and §\"The operations\" says so by leaving the column empty.

    Nothing here is a credential: a name, a language and a picture are how a
    person is addressed, and putting a password prompt in front of correcting the
    spelling of your own name would teach people to type their password at
    prompts that did not need it — which is the habit every phishing page relies
    on.

    Only the members the caller actually sent are written, which is what makes
    \"a key present and already equal to the stored value changed nothing\" true:
    `Schema.dict(exclude_unset=True)` is the same `api.management.patching`
    distinction between \"set this to null\" and \"do not touch this\".

    Args:
        body (ProfilePatch): Name, language and picture. Every member optional, and `None` clears
            it.

            The address is **not** here: it is the login identity and cannot change on one
            request (§"Changing an email address"), so it has its own two-step operation
            and a `PATCH` that accepted it would be a way round the confirmation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlowProblem | ProfileOut]
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
    body: ProfilePatch,
) -> FlowProblem | ProfileOut | None:
    r"""Change the signed-in person's own name, language or picture

     Not sensitive, and §\"The operations\" says so by leaving the column empty.

    Nothing here is a credential: a name, a language and a picture are how a
    person is addressed, and putting a password prompt in front of correcting the
    spelling of your own name would teach people to type their password at
    prompts that did not need it — which is the habit every phishing page relies
    on.

    Only the members the caller actually sent are written, which is what makes
    \"a key present and already equal to the stored value changed nothing\" true:
    `Schema.dict(exclude_unset=True)` is the same `api.management.patching`
    distinction between \"set this to null\" and \"do not touch this\".

    Args:
        body (ProfilePatch): Name, language and picture. Every member optional, and `None` clears
            it.

            The address is **not** here: it is the login identity and cannot change on one
            request (§"Changing an email address"), so it has its own two-step operation
            and a `PATCH` that accepted it would be a way round the confirmation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlowProblem | ProfileOut
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ProfilePatch,
) -> Response[FlowProblem | ProfileOut]:
    r"""Change the signed-in person's own name, language or picture

     Not sensitive, and §\"The operations\" says so by leaving the column empty.

    Nothing here is a credential: a name, a language and a picture are how a
    person is addressed, and putting a password prompt in front of correcting the
    spelling of your own name would teach people to type their password at
    prompts that did not need it — which is the habit every phishing page relies
    on.

    Only the members the caller actually sent are written, which is what makes
    \"a key present and already equal to the stored value changed nothing\" true:
    `Schema.dict(exclude_unset=True)` is the same `api.management.patching`
    distinction between \"set this to null\" and \"do not touch this\".

    Args:
        body (ProfilePatch): Name, language and picture. Every member optional, and `None` clears
            it.

            The address is **not** here: it is the login identity and cannot change on one
            request (§"Changing an email address"), so it has its own two-step operation
            and a `PATCH` that accepted it would be a way round the confirmation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlowProblem | ProfileOut]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ProfilePatch,
) -> FlowProblem | ProfileOut | None:
    r"""Change the signed-in person's own name, language or picture

     Not sensitive, and §\"The operations\" says so by leaving the column empty.

    Nothing here is a credential: a name, a language and a picture are how a
    person is addressed, and putting a password prompt in front of correcting the
    spelling of your own name would teach people to type their password at
    prompts that did not need it — which is the habit every phishing page relies
    on.

    Only the members the caller actually sent are written, which is what makes
    \"a key present and already equal to the stored value changed nothing\" true:
    `Schema.dict(exclude_unset=True)` is the same `api.management.patching`
    distinction between \"set this to null\" and \"do not touch this\".

    Args:
        body (ProfilePatch): Name, language and picture. Every member optional, and `None` clears
            it.

            The address is **not** here: it is the login identity and cannot change on one
            request (§"Changing an email address"), so it has its own two-step operation
            and a `PATCH` that accepted it would be a way round the confirmation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlowProblem | ProfileOut
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
