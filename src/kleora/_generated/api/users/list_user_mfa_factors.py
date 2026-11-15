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
from ...models.mfa_factor_list import MfaFactorList
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    environment_id: str,
    user_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/environments/{environment_id}/users/{user_id}/mfa".format(
            environment_id=quote(str(environment_id), safe=""),
            user_id=quote(str(user_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MfaFactorList | Problem | None:
    if response.status_code == 200:
        response_200 = MfaFactorList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Problem.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Problem.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Problem.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

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
) -> Response[MfaFactorList | Problem]:
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
) -> Response[MfaFactorList | Problem]:
    r"""A user's MFA factors

     Every factor of the user's — confirmed and unconfirmed alike.

    **Never plan-gated**, and for a reason that is not obvious from this
    operation alone: it is the **only** route on this surface that hands out
    another user's `MfaFactor` id, and `DELETE …/users/{uid}/mfa/{factor_id}`
    needs one. The user export carries a factor's kind and timestamps
    (`api.management.v1.schemas.ExportFactor`) and deliberately no id, so there
    is no second source. Gating this while leaving the reset open would make
    the reset unreachable — an ungated exit behind a locked door.

    So the line P6-15 draws is: reading or resetting **one named user's**
    factors, which is what an operator does to get somebody back in, is on
    every plan; asking the fleet-wide question — `?mfa=` on the users
    listing — is `pro` and above. See `delete_user_mfa_factor` below for the
    whole argument.

    Not paginated: this platform never holds more than two rows per user (one
    `totp`, one `recovery`), the same reason the signing-key list gives.
    \"Never seeds or hashes\" (`mfa.md` §API) — `_mfa_factor_body` is the only
    thing this endpoint reads a row through, and it has no seed or hash to
    leave off because it never asks for one.

    Args:
        environment_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MfaFactorList | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        user_id=user_id,
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
) -> MfaFactorList | Problem | None:
    r"""A user's MFA factors

     Every factor of the user's — confirmed and unconfirmed alike.

    **Never plan-gated**, and for a reason that is not obvious from this
    operation alone: it is the **only** route on this surface that hands out
    another user's `MfaFactor` id, and `DELETE …/users/{uid}/mfa/{factor_id}`
    needs one. The user export carries a factor's kind and timestamps
    (`api.management.v1.schemas.ExportFactor`) and deliberately no id, so there
    is no second source. Gating this while leaving the reset open would make
    the reset unreachable — an ungated exit behind a locked door.

    So the line P6-15 draws is: reading or resetting **one named user's**
    factors, which is what an operator does to get somebody back in, is on
    every plan; asking the fleet-wide question — `?mfa=` on the users
    listing — is `pro` and above. See `delete_user_mfa_factor` below for the
    whole argument.

    Not paginated: this platform never holds more than two rows per user (one
    `totp`, one `recovery`), the same reason the signing-key list gives.
    \"Never seeds or hashes\" (`mfa.md` §API) — `_mfa_factor_body` is the only
    thing this endpoint reads a row through, and it has no seed or hash to
    leave off because it never asks for one.

    Args:
        environment_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MfaFactorList | Problem
    """

    return sync_detailed(
        environment_id=environment_id,
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[MfaFactorList | Problem]:
    r"""A user's MFA factors

     Every factor of the user's — confirmed and unconfirmed alike.

    **Never plan-gated**, and for a reason that is not obvious from this
    operation alone: it is the **only** route on this surface that hands out
    another user's `MfaFactor` id, and `DELETE …/users/{uid}/mfa/{factor_id}`
    needs one. The user export carries a factor's kind and timestamps
    (`api.management.v1.schemas.ExportFactor`) and deliberately no id, so there
    is no second source. Gating this while leaving the reset open would make
    the reset unreachable — an ungated exit behind a locked door.

    So the line P6-15 draws is: reading or resetting **one named user's**
    factors, which is what an operator does to get somebody back in, is on
    every plan; asking the fleet-wide question — `?mfa=` on the users
    listing — is `pro` and above. See `delete_user_mfa_factor` below for the
    whole argument.

    Not paginated: this platform never holds more than two rows per user (one
    `totp`, one `recovery`), the same reason the signing-key list gives.
    \"Never seeds or hashes\" (`mfa.md` §API) — `_mfa_factor_body` is the only
    thing this endpoint reads a row through, and it has no seed or hash to
    leave off because it never asks for one.

    Args:
        environment_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MfaFactorList | Problem]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> MfaFactorList | Problem | None:
    r"""A user's MFA factors

     Every factor of the user's — confirmed and unconfirmed alike.

    **Never plan-gated**, and for a reason that is not obvious from this
    operation alone: it is the **only** route on this surface that hands out
    another user's `MfaFactor` id, and `DELETE …/users/{uid}/mfa/{factor_id}`
    needs one. The user export carries a factor's kind and timestamps
    (`api.management.v1.schemas.ExportFactor`) and deliberately no id, so there
    is no second source. Gating this while leaving the reset open would make
    the reset unreachable — an ungated exit behind a locked door.

    So the line P6-15 draws is: reading or resetting **one named user's**
    factors, which is what an operator does to get somebody back in, is on
    every plan; asking the fleet-wide question — `?mfa=` on the users
    listing — is `pro` and above. See `delete_user_mfa_factor` below for the
    whole argument.

    Not paginated: this platform never holds more than two rows per user (one
    `totp`, one `recovery`), the same reason the signing-key list gives.
    \"Never seeds or hashes\" (`mfa.md` §API) — `_mfa_factor_body` is the only
    thing this endpoint reads a row through, and it has no seed or hash to
    leave off because it never asks for one.

    Args:
        environment_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MfaFactorList | Problem
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            user_id=user_id,
            client=client,
        )
    ).parsed
