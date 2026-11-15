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
from ...models.flow_problem import FlowProblem
from ...models.password_in import PasswordIn
from ...types import Response


def _get_kwargs(
    *,
    body: PasswordIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/account/v1/password",
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
) -> Response[Any | FlowProblem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PasswordIn,
) -> Response[Any | FlowProblem]:
    r"""Change the signed-in person's own password

     `current_password` **and** the re-auth mark, exactly as `/me/password` requires both.

    The mark is the decorator's (`@self_service(sensitive=True)`), so by the time
    this runs the session has re-proved itself inside five minutes.

    Two paths, decided by what the person *has* and never by what the caller
    sent:

    * **They have a password** → `passwords.change_password`, which verifies
      `current_password`. A wrong one — or a missing one — is
      `401 invalid-credentials`, never a `422`, because \"naming the missing field
      would distinguish 'you have a password' from 'you do not' to a caller
      holding somebody's token\" (§\"Failure modes\"). Every *other* session is
      revoked and this one survives, so the screen the change was made on keeps
      working.
    * **They have none** → `passwords.set_password`, the §\"The operations\" row
      \"Set a password (person has none)\": there is no `current_password` to
      supply, \"the re-auth gate is what stands in for it, and a person who can
      satisfy it holds a passkey or a provider identity\". That service revokes
      **every** session including this one, which is its own rule for an
      administrative set — and is the right one here too: a person who had no
      password now has a credential that did not exist a moment ago, and the
      sessions opened before it should not outlive the change.

    A new password the policy refuses is `422 password-policy` or
    `422 password-breached`, with `errors[].field = \"password\"`, which is the same
    pair every other password endpoint in this codebase answers with.

    Args:
        body (PasswordIn): `current_password` and `new_password`, the second required.

            `current_password` is optional **only** because a person who has none has none
            to send (§"The operations": "Set a password (person has none) … No
            `current_password` to supply"). It is not a way to skip the check: a person who
            *does* have a password and omits it gets `401 invalid-credentials` and not a
            `422`, because "naming the missing field would distinguish 'you have a
            password' from 'you do not' to a caller holding somebody's token"
            (§"Failure modes").

            Neither field carries a `min_length`. The policy is the Environment's and its
            refusal is `422 password-policy` with `errors[].field = "password"`; a schema
            bound would answer first, in django-ninja's shape, for the one input whose
            refusal §"Failure modes" writes out.

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
    client: AuthenticatedClient,
    body: PasswordIn,
) -> Any | FlowProblem | None:
    r"""Change the signed-in person's own password

     `current_password` **and** the re-auth mark, exactly as `/me/password` requires both.

    The mark is the decorator's (`@self_service(sensitive=True)`), so by the time
    this runs the session has re-proved itself inside five minutes.

    Two paths, decided by what the person *has* and never by what the caller
    sent:

    * **They have a password** → `passwords.change_password`, which verifies
      `current_password`. A wrong one — or a missing one — is
      `401 invalid-credentials`, never a `422`, because \"naming the missing field
      would distinguish 'you have a password' from 'you do not' to a caller
      holding somebody's token\" (§\"Failure modes\"). Every *other* session is
      revoked and this one survives, so the screen the change was made on keeps
      working.
    * **They have none** → `passwords.set_password`, the §\"The operations\" row
      \"Set a password (person has none)\": there is no `current_password` to
      supply, \"the re-auth gate is what stands in for it, and a person who can
      satisfy it holds a passkey or a provider identity\". That service revokes
      **every** session including this one, which is its own rule for an
      administrative set — and is the right one here too: a person who had no
      password now has a credential that did not exist a moment ago, and the
      sessions opened before it should not outlive the change.

    A new password the policy refuses is `422 password-policy` or
    `422 password-breached`, with `errors[].field = \"password\"`, which is the same
    pair every other password endpoint in this codebase answers with.

    Args:
        body (PasswordIn): `current_password` and `new_password`, the second required.

            `current_password` is optional **only** because a person who has none has none
            to send (§"The operations": "Set a password (person has none) … No
            `current_password` to supply"). It is not a way to skip the check: a person who
            *does* have a password and omits it gets `401 invalid-credentials` and not a
            `422`, because "naming the missing field would distinguish 'you have a
            password' from 'you do not' to a caller holding somebody's token"
            (§"Failure modes").

            Neither field carries a `min_length`. The policy is the Environment's and its
            refusal is `422 password-policy` with `errors[].field = "password"`; a schema
            bound would answer first, in django-ninja's shape, for the one input whose
            refusal §"Failure modes" writes out.

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
    client: AuthenticatedClient,
    body: PasswordIn,
) -> Response[Any | FlowProblem]:
    r"""Change the signed-in person's own password

     `current_password` **and** the re-auth mark, exactly as `/me/password` requires both.

    The mark is the decorator's (`@self_service(sensitive=True)`), so by the time
    this runs the session has re-proved itself inside five minutes.

    Two paths, decided by what the person *has* and never by what the caller
    sent:

    * **They have a password** → `passwords.change_password`, which verifies
      `current_password`. A wrong one — or a missing one — is
      `401 invalid-credentials`, never a `422`, because \"naming the missing field
      would distinguish 'you have a password' from 'you do not' to a caller
      holding somebody's token\" (§\"Failure modes\"). Every *other* session is
      revoked and this one survives, so the screen the change was made on keeps
      working.
    * **They have none** → `passwords.set_password`, the §\"The operations\" row
      \"Set a password (person has none)\": there is no `current_password` to
      supply, \"the re-auth gate is what stands in for it, and a person who can
      satisfy it holds a passkey or a provider identity\". That service revokes
      **every** session including this one, which is its own rule for an
      administrative set — and is the right one here too: a person who had no
      password now has a credential that did not exist a moment ago, and the
      sessions opened before it should not outlive the change.

    A new password the policy refuses is `422 password-policy` or
    `422 password-breached`, with `errors[].field = \"password\"`, which is the same
    pair every other password endpoint in this codebase answers with.

    Args:
        body (PasswordIn): `current_password` and `new_password`, the second required.

            `current_password` is optional **only** because a person who has none has none
            to send (§"The operations": "Set a password (person has none) … No
            `current_password` to supply"). It is not a way to skip the check: a person who
            *does* have a password and omits it gets `401 invalid-credentials` and not a
            `422`, because "naming the missing field would distinguish 'you have a
            password' from 'you do not' to a caller holding somebody's token"
            (§"Failure modes").

            Neither field carries a `min_length`. The policy is the Environment's and its
            refusal is `422 password-policy` with `errors[].field = "password"`; a schema
            bound would answer first, in django-ninja's shape, for the one input whose
            refusal §"Failure modes" writes out.

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
    client: AuthenticatedClient,
    body: PasswordIn,
) -> Any | FlowProblem | None:
    r"""Change the signed-in person's own password

     `current_password` **and** the re-auth mark, exactly as `/me/password` requires both.

    The mark is the decorator's (`@self_service(sensitive=True)`), so by the time
    this runs the session has re-proved itself inside five minutes.

    Two paths, decided by what the person *has* and never by what the caller
    sent:

    * **They have a password** → `passwords.change_password`, which verifies
      `current_password`. A wrong one — or a missing one — is
      `401 invalid-credentials`, never a `422`, because \"naming the missing field
      would distinguish 'you have a password' from 'you do not' to a caller
      holding somebody's token\" (§\"Failure modes\"). Every *other* session is
      revoked and this one survives, so the screen the change was made on keeps
      working.
    * **They have none** → `passwords.set_password`, the §\"The operations\" row
      \"Set a password (person has none)\": there is no `current_password` to
      supply, \"the re-auth gate is what stands in for it, and a person who can
      satisfy it holds a passkey or a provider identity\". That service revokes
      **every** session including this one, which is its own rule for an
      administrative set — and is the right one here too: a person who had no
      password now has a credential that did not exist a moment ago, and the
      sessions opened before it should not outlive the change.

    A new password the policy refuses is `422 password-policy` or
    `422 password-breached`, with `errors[].field = \"password\"`, which is the same
    pair every other password endpoint in this codebase answers with.

    Args:
        body (PasswordIn): `current_password` and `new_password`, the second required.

            `current_password` is optional **only** because a person who has none has none
            to send (§"The operations": "Set a password (person has none) … No
            `current_password` to supply"). It is not a way to skip the check: a person who
            *does* have a password and omits it gets `401 invalid-credentials` and not a
            `422`, because "naming the missing field would distinguish 'you have a
            password' from 'you do not' to a caller holding somebody's token"
            (§"Failure modes").

            Neither field carries a `min_length`. The policy is the Environment's and its
            refusal is `422 password-policy` with `errors[].field = "password"`; a schema
            bound would answer first, in django-ninja's shape, for the one input whose
            refusal §"Failure modes" writes out.

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
