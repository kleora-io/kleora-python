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
from ...models.user_merge_in import UserMergeIn
from ...models.user_out import UserOut
from ...types import Response


def _get_kwargs(
    environment_id: str,
    user_id: str,
    *,
    body: UserMergeIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/environments/{environment_id}/users/{user_id}/merge".format(
            environment_id=quote(str(environment_id), safe=""),
            user_id=quote(str(user_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | UserOut | None:
    if response.status_code == 200:
        response_200 = UserOut.from_dict(response.json())

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
) -> Response[Problem | UserOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    environment_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: UserMergeIn,
) -> Response[Problem | UserOut]:
    """Merge another user into this one

     Fold `source_id` into this user, and erase the source. **Irreversible.**

    The user in the path is the **winner**: it keeps its own `email`, `name`,
    `picture_url` and `locale`, because merging repairs how somebody signs in and
    never decides who they are. The user named in the body is erased, exactly as
    `DELETE …/users/{id}` erases, with a `merged_into` pointer to the winner — so
    `GET` on the old id keeps answering and says where the person went, for ever.
    That is the deliberate price of the rule below.

    In one transaction: the source's provider identities move (and its password
    only if the winner has none); its memberships move, and where both hold a
    membership of one tenant the roles become the union and the source's row is
    removed; its passkeys move, and a TOTP or a recovery set only onto a winner
    holding none of that kind; its per-user setting values move for the keys the
    winner has none; `metadata` is shallow-merged with the winner winning a
    collision; and **every session on both sides is revoked**, because a live token
    carries a `sub` that is about to stop being the right one.

    **No audit event is ever rewritten.** The source's history keeps naming the
    source id — that is what an audit log is for — and the merge is recorded as
    `user.merged` on the winner, with a count per category, beside `user.erased`
    on the source.

    Refusals: 422 `same-user`, 409 `user-erased` for either side, and 409
    `last-owner` when the source is the last active owner of an Account's tenant.
    A `tenant_member` never reaches it at all.

    **A `source_id` in another environment is a 404**, like any id this caller
    cannot see, and deliberately not a refusal of its own: a distinct answer would
    confirm that the id exists somewhere they have no access to.

    Args:
        environment_id (str):
        user_id (str):
        body (UserMergeIn): `POST …/users/{user_id}/merge` — the User being folded in and erased.

            One field, and `extra="forbid"` around it. There is deliberately nothing else
            to send: what a merge does is fixed by `social-login.md` §Merge, and an option
            (*"keep the source's authenticator"*, *"leave my own sessions alone"*) would be
            a caller choosing which half of a takeover-shaped operation to weaken. The
            winner is the path, so the row being **erased** is the one the caller had to
            name explicitly.

            A `str` rather than a `uuid.UUID`, so a malformed id is the same 404 as an id
            that names nothing (`merge.find_source`) rather than a 422 among the shape
            errors — the answer a caller who mistyped an id should get either way, and one
            that says nothing about which ids exist.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UserOut]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        user_id=user_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: UserMergeIn,
) -> Problem | UserOut | None:
    """Merge another user into this one

     Fold `source_id` into this user, and erase the source. **Irreversible.**

    The user in the path is the **winner**: it keeps its own `email`, `name`,
    `picture_url` and `locale`, because merging repairs how somebody signs in and
    never decides who they are. The user named in the body is erased, exactly as
    `DELETE …/users/{id}` erases, with a `merged_into` pointer to the winner — so
    `GET` on the old id keeps answering and says where the person went, for ever.
    That is the deliberate price of the rule below.

    In one transaction: the source's provider identities move (and its password
    only if the winner has none); its memberships move, and where both hold a
    membership of one tenant the roles become the union and the source's row is
    removed; its passkeys move, and a TOTP or a recovery set only onto a winner
    holding none of that kind; its per-user setting values move for the keys the
    winner has none; `metadata` is shallow-merged with the winner winning a
    collision; and **every session on both sides is revoked**, because a live token
    carries a `sub` that is about to stop being the right one.

    **No audit event is ever rewritten.** The source's history keeps naming the
    source id — that is what an audit log is for — and the merge is recorded as
    `user.merged` on the winner, with a count per category, beside `user.erased`
    on the source.

    Refusals: 422 `same-user`, 409 `user-erased` for either side, and 409
    `last-owner` when the source is the last active owner of an Account's tenant.
    A `tenant_member` never reaches it at all.

    **A `source_id` in another environment is a 404**, like any id this caller
    cannot see, and deliberately not a refusal of its own: a distinct answer would
    confirm that the id exists somewhere they have no access to.

    Args:
        environment_id (str):
        user_id (str):
        body (UserMergeIn): `POST …/users/{user_id}/merge` — the User being folded in and erased.

            One field, and `extra="forbid"` around it. There is deliberately nothing else
            to send: what a merge does is fixed by `social-login.md` §Merge, and an option
            (*"keep the source's authenticator"*, *"leave my own sessions alone"*) would be
            a caller choosing which half of a takeover-shaped operation to weaken. The
            winner is the path, so the row being **erased** is the one the caller had to
            name explicitly.

            A `str` rather than a `uuid.UUID`, so a malformed id is the same 404 as an id
            that names nothing (`merge.find_source`) rather than a 422 among the shape
            errors — the answer a caller who mistyped an id should get either way, and one
            that says nothing about which ids exist.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UserOut
    """

    return sync_detailed(
        environment_id=environment_id,
        user_id=user_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: UserMergeIn,
) -> Response[Problem | UserOut]:
    """Merge another user into this one

     Fold `source_id` into this user, and erase the source. **Irreversible.**

    The user in the path is the **winner**: it keeps its own `email`, `name`,
    `picture_url` and `locale`, because merging repairs how somebody signs in and
    never decides who they are. The user named in the body is erased, exactly as
    `DELETE …/users/{id}` erases, with a `merged_into` pointer to the winner — so
    `GET` on the old id keeps answering and says where the person went, for ever.
    That is the deliberate price of the rule below.

    In one transaction: the source's provider identities move (and its password
    only if the winner has none); its memberships move, and where both hold a
    membership of one tenant the roles become the union and the source's row is
    removed; its passkeys move, and a TOTP or a recovery set only onto a winner
    holding none of that kind; its per-user setting values move for the keys the
    winner has none; `metadata` is shallow-merged with the winner winning a
    collision; and **every session on both sides is revoked**, because a live token
    carries a `sub` that is about to stop being the right one.

    **No audit event is ever rewritten.** The source's history keeps naming the
    source id — that is what an audit log is for — and the merge is recorded as
    `user.merged` on the winner, with a count per category, beside `user.erased`
    on the source.

    Refusals: 422 `same-user`, 409 `user-erased` for either side, and 409
    `last-owner` when the source is the last active owner of an Account's tenant.
    A `tenant_member` never reaches it at all.

    **A `source_id` in another environment is a 404**, like any id this caller
    cannot see, and deliberately not a refusal of its own: a distinct answer would
    confirm that the id exists somewhere they have no access to.

    Args:
        environment_id (str):
        user_id (str):
        body (UserMergeIn): `POST …/users/{user_id}/merge` — the User being folded in and erased.

            One field, and `extra="forbid"` around it. There is deliberately nothing else
            to send: what a merge does is fixed by `social-login.md` §Merge, and an option
            (*"keep the source's authenticator"*, *"leave my own sessions alone"*) would be
            a caller choosing which half of a takeover-shaped operation to weaken. The
            winner is the path, so the row being **erased** is the one the caller had to
            name explicitly.

            A `str` rather than a `uuid.UUID`, so a malformed id is the same 404 as an id
            that names nothing (`merge.find_source`) rather than a 422 among the shape
            errors — the answer a caller who mistyped an id should get either way, and one
            that says nothing about which ids exist.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UserOut]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        user_id=user_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: UserMergeIn,
) -> Problem | UserOut | None:
    """Merge another user into this one

     Fold `source_id` into this user, and erase the source. **Irreversible.**

    The user in the path is the **winner**: it keeps its own `email`, `name`,
    `picture_url` and `locale`, because merging repairs how somebody signs in and
    never decides who they are. The user named in the body is erased, exactly as
    `DELETE …/users/{id}` erases, with a `merged_into` pointer to the winner — so
    `GET` on the old id keeps answering and says where the person went, for ever.
    That is the deliberate price of the rule below.

    In one transaction: the source's provider identities move (and its password
    only if the winner has none); its memberships move, and where both hold a
    membership of one tenant the roles become the union and the source's row is
    removed; its passkeys move, and a TOTP or a recovery set only onto a winner
    holding none of that kind; its per-user setting values move for the keys the
    winner has none; `metadata` is shallow-merged with the winner winning a
    collision; and **every session on both sides is revoked**, because a live token
    carries a `sub` that is about to stop being the right one.

    **No audit event is ever rewritten.** The source's history keeps naming the
    source id — that is what an audit log is for — and the merge is recorded as
    `user.merged` on the winner, with a count per category, beside `user.erased`
    on the source.

    Refusals: 422 `same-user`, 409 `user-erased` for either side, and 409
    `last-owner` when the source is the last active owner of an Account's tenant.
    A `tenant_member` never reaches it at all.

    **A `source_id` in another environment is a 404**, like any id this caller
    cannot see, and deliberately not a refusal of its own: a distinct answer would
    confirm that the id exists somewhere they have no access to.

    Args:
        environment_id (str):
        user_id (str):
        body (UserMergeIn): `POST …/users/{user_id}/merge` — the User being folded in and erased.

            One field, and `extra="forbid"` around it. There is deliberately nothing else
            to send: what a merge does is fixed by `social-login.md` §Merge, and an option
            (*"keep the source's authenticator"*, *"leave my own sessions alone"*) would be
            a caller choosing which half of a takeover-shaped operation to weaken. The
            winner is the path, so the row being **erased** is the one the caller had to
            name explicitly.

            A `str` rather than a `uuid.UUID`, so a malformed id is the same 404 as an id
            that names nothing (`merge.find_source`) rather than a 422 among the shape
            errors — the answer a caller who mistyped an id should get either way, and one
            that says nothing about which ids exist.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UserOut
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            user_id=user_id,
            client=client,
            body=body,
        )
    ).parsed
