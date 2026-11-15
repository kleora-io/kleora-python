# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    environment_id: str,
    user_id: str,
    factor_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/environments/{environment_id}/users/{user_id}/mfa/{factor_id}".format(
            environment_id=quote(str(environment_id), safe=""),
            user_id=quote(str(user_id), safe=""),
            factor_id=quote(str(factor_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Problem | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    environment_id: str,
    user_id: str,
    factor_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | Problem]:
    r"""Administrative MFA reset

     Remove the user's factors and send the `mfa_removed` notice.

    Removing either kind removes both (`mfa.md` §\"Administrative reset\"), so
    the id in the path only has to name *a* factor of this user's — the same
    404-not-403 shape `_target_session` gives a foreign id, so an id from
    another user or another environment reveals nothing. Existing sessions are
    not revoked by this action; under `required` the next login forces
    re-enrolment.

    **Never plan-gated, on any plan.** billing.md §Plans, billing.md §\"What is
    gated\" and mfa.md §\"What a plan gates\" all put \"fleet MFA management /
    administrative reset\" behind `pro`, and P6-15 first implemented that. It
    was removed on review, and the reason belongs here rather than in a commit
    message, because the next person tidying gates will match on the resource
    name and re-add it.

    mfa.md §\"Failure modes\" says, of a user whose recovery codes are exhausted
    and whose device is lost: \"**Administrative reset is the only path**; the
    page says so.\" Gating this route therefore withholds nothing from *our*
    customer — it permanently locks out **their** end user, a person who never
    agreed to anything with us and cannot even find out why. That is the exact
    outcome billing.md §\"The rule everything else bends around\" exists to
    forbid, and it is the rule P6-11 established, P6-12 upheld in metering,
    P6-14 proved through a day-60 OAuth flow and P6-15 proves for passkeys. A
    lockout we cause, on a path the spec calls the only one, is a worse outcome
    than an ungated feature on a free plan.

    The three documents are describing *fleet MFA management at scale* as a
    paid capability and sweeping this route up with it by resource name.
    Administering users' MFA at scale is reasonably paid — the `?mfa=` filter on
    the users listing still is. Being the sole exit from a lockout is not.
    `tests/test_plan_gates.py` pins this with a test whose whole job is to say
    so.

    Args:
        environment_id (str):
        user_id (str):
        factor_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        user_id=user_id,
        factor_id=factor_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    user_id: str,
    factor_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | Problem | None:
    r"""Administrative MFA reset

     Remove the user's factors and send the `mfa_removed` notice.

    Removing either kind removes both (`mfa.md` §\"Administrative reset\"), so
    the id in the path only has to name *a* factor of this user's — the same
    404-not-403 shape `_target_session` gives a foreign id, so an id from
    another user or another environment reveals nothing. Existing sessions are
    not revoked by this action; under `required` the next login forces
    re-enrolment.

    **Never plan-gated, on any plan.** billing.md §Plans, billing.md §\"What is
    gated\" and mfa.md §\"What a plan gates\" all put \"fleet MFA management /
    administrative reset\" behind `pro`, and P6-15 first implemented that. It
    was removed on review, and the reason belongs here rather than in a commit
    message, because the next person tidying gates will match on the resource
    name and re-add it.

    mfa.md §\"Failure modes\" says, of a user whose recovery codes are exhausted
    and whose device is lost: \"**Administrative reset is the only path**; the
    page says so.\" Gating this route therefore withholds nothing from *our*
    customer — it permanently locks out **their** end user, a person who never
    agreed to anything with us and cannot even find out why. That is the exact
    outcome billing.md §\"The rule everything else bends around\" exists to
    forbid, and it is the rule P6-11 established, P6-12 upheld in metering,
    P6-14 proved through a day-60 OAuth flow and P6-15 proves for passkeys. A
    lockout we cause, on a path the spec calls the only one, is a worse outcome
    than an ungated feature on a free plan.

    The three documents are describing *fleet MFA management at scale* as a
    paid capability and sweeping this route up with it by resource name.
    Administering users' MFA at scale is reasonably paid — the `?mfa=` filter on
    the users listing still is. Being the sole exit from a lockout is not.
    `tests/test_plan_gates.py` pins this with a test whose whole job is to say
    so.

    Args:
        environment_id (str):
        user_id (str):
        factor_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Problem
    """

    return sync_detailed(
        environment_id=environment_id,
        user_id=user_id,
        factor_id=factor_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    user_id: str,
    factor_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | Problem]:
    r"""Administrative MFA reset

     Remove the user's factors and send the `mfa_removed` notice.

    Removing either kind removes both (`mfa.md` §\"Administrative reset\"), so
    the id in the path only has to name *a* factor of this user's — the same
    404-not-403 shape `_target_session` gives a foreign id, so an id from
    another user or another environment reveals nothing. Existing sessions are
    not revoked by this action; under `required` the next login forces
    re-enrolment.

    **Never plan-gated, on any plan.** billing.md §Plans, billing.md §\"What is
    gated\" and mfa.md §\"What a plan gates\" all put \"fleet MFA management /
    administrative reset\" behind `pro`, and P6-15 first implemented that. It
    was removed on review, and the reason belongs here rather than in a commit
    message, because the next person tidying gates will match on the resource
    name and re-add it.

    mfa.md §\"Failure modes\" says, of a user whose recovery codes are exhausted
    and whose device is lost: \"**Administrative reset is the only path**; the
    page says so.\" Gating this route therefore withholds nothing from *our*
    customer — it permanently locks out **their** end user, a person who never
    agreed to anything with us and cannot even find out why. That is the exact
    outcome billing.md §\"The rule everything else bends around\" exists to
    forbid, and it is the rule P6-11 established, P6-12 upheld in metering,
    P6-14 proved through a day-60 OAuth flow and P6-15 proves for passkeys. A
    lockout we cause, on a path the spec calls the only one, is a worse outcome
    than an ungated feature on a free plan.

    The three documents are describing *fleet MFA management at scale* as a
    paid capability and sweeping this route up with it by resource name.
    Administering users' MFA at scale is reasonably paid — the `?mfa=` filter on
    the users listing still is. Being the sole exit from a lockout is not.
    `tests/test_plan_gates.py` pins this with a test whose whole job is to say
    so.

    Args:
        environment_id (str):
        user_id (str):
        factor_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        user_id=user_id,
        factor_id=factor_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    user_id: str,
    factor_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | Problem | None:
    r"""Administrative MFA reset

     Remove the user's factors and send the `mfa_removed` notice.

    Removing either kind removes both (`mfa.md` §\"Administrative reset\"), so
    the id in the path only has to name *a* factor of this user's — the same
    404-not-403 shape `_target_session` gives a foreign id, so an id from
    another user or another environment reveals nothing. Existing sessions are
    not revoked by this action; under `required` the next login forces
    re-enrolment.

    **Never plan-gated, on any plan.** billing.md §Plans, billing.md §\"What is
    gated\" and mfa.md §\"What a plan gates\" all put \"fleet MFA management /
    administrative reset\" behind `pro`, and P6-15 first implemented that. It
    was removed on review, and the reason belongs here rather than in a commit
    message, because the next person tidying gates will match on the resource
    name and re-add it.

    mfa.md §\"Failure modes\" says, of a user whose recovery codes are exhausted
    and whose device is lost: \"**Administrative reset is the only path**; the
    page says so.\" Gating this route therefore withholds nothing from *our*
    customer — it permanently locks out **their** end user, a person who never
    agreed to anything with us and cannot even find out why. That is the exact
    outcome billing.md §\"The rule everything else bends around\" exists to
    forbid, and it is the rule P6-11 established, P6-12 upheld in metering,
    P6-14 proved through a day-60 OAuth flow and P6-15 proves for passkeys. A
    lockout we cause, on a path the spec calls the only one, is a worse outcome
    than an ungated feature on a free plan.

    The three documents are describing *fleet MFA management at scale* as a
    paid capability and sweeping this route up with it by resource name.
    Administering users' MFA at scale is reasonably paid — the `?mfa=` filter on
    the users listing still is. Being the sole exit from a lockout is not.
    `tests/test_plan_gates.py` pins this with a test whose whole job is to say
    so.

    Args:
        environment_id (str):
        user_id (str):
        factor_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Problem
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            user_id=user_id,
            factor_id=factor_id,
            client=client,
        )
    ).parsed
