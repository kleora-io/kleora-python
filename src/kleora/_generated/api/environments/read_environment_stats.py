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
from ...models.environment_stats import EnvironmentStats
from ...models.problem import Problem
from ...models.read_environment_stats_range import ReadEnvironmentStatsRange
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app_id: str,
    environment_id: str,
    *,
    range_: ReadEnvironmentStatsRange | Unset = ReadEnvironmentStatsRange.VALUE_0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_range_: str | Unset = UNSET
    if not isinstance(range_, Unset):
        json_range_ = range_.value

    params["range"] = json_range_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/apps/{app_id}/environments/{environment_id}/stats".format(
            app_id=quote(str(app_id), safe=""),
            environment_id=quote(str(environment_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EnvironmentStats | Problem | None:
    if response.status_code == 200:
        response_200 = EnvironmentStats.from_dict(response.json())

        return response_200

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
) -> Response[EnvironmentStats | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    environment_id: str,
    *,
    client: AuthenticatedClient,
    range_: ReadEnvironmentStatsRange | Unset = ReadEnvironmentStatsRange.VALUE_0,
) -> Response[EnvironmentStats | Problem]:
    """Environment statistics

     The overview's numbers: totals now, a daily series, and four setup facts.

    One request rather than five, because the overview draws all of it at once
    and five round trips would be five chances for the cards to disagree about
    which environment they are describing.

    Cached for 60 seconds per environment and range
    (`apps.accounts.services.stats`), so the range switcher's three answers cost
    one computation each however often somebody clicks between them —
    `computed_at` is the moment of that computation, not of this request.

    Args:
        app_id (str):
        environment_id (str):
        range_ (ReadEnvironmentStatsRange | Unset):  Default: ReadEnvironmentStatsRange.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnvironmentStats | Problem]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        environment_id=environment_id,
        range_=range_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    environment_id: str,
    *,
    client: AuthenticatedClient,
    range_: ReadEnvironmentStatsRange | Unset = ReadEnvironmentStatsRange.VALUE_0,
) -> EnvironmentStats | Problem | None:
    """Environment statistics

     The overview's numbers: totals now, a daily series, and four setup facts.

    One request rather than five, because the overview draws all of it at once
    and five round trips would be five chances for the cards to disagree about
    which environment they are describing.

    Cached for 60 seconds per environment and range
    (`apps.accounts.services.stats`), so the range switcher's three answers cost
    one computation each however often somebody clicks between them —
    `computed_at` is the moment of that computation, not of this request.

    Args:
        app_id (str):
        environment_id (str):
        range_ (ReadEnvironmentStatsRange | Unset):  Default: ReadEnvironmentStatsRange.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnvironmentStats | Problem
    """

    return sync_detailed(
        app_id=app_id,
        environment_id=environment_id,
        client=client,
        range_=range_,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    environment_id: str,
    *,
    client: AuthenticatedClient,
    range_: ReadEnvironmentStatsRange | Unset = ReadEnvironmentStatsRange.VALUE_0,
) -> Response[EnvironmentStats | Problem]:
    """Environment statistics

     The overview's numbers: totals now, a daily series, and four setup facts.

    One request rather than five, because the overview draws all of it at once
    and five round trips would be five chances for the cards to disagree about
    which environment they are describing.

    Cached for 60 seconds per environment and range
    (`apps.accounts.services.stats`), so the range switcher's three answers cost
    one computation each however often somebody clicks between them —
    `computed_at` is the moment of that computation, not of this request.

    Args:
        app_id (str):
        environment_id (str):
        range_ (ReadEnvironmentStatsRange | Unset):  Default: ReadEnvironmentStatsRange.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnvironmentStats | Problem]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        environment_id=environment_id,
        range_=range_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    environment_id: str,
    *,
    client: AuthenticatedClient,
    range_: ReadEnvironmentStatsRange | Unset = ReadEnvironmentStatsRange.VALUE_0,
) -> EnvironmentStats | Problem | None:
    """Environment statistics

     The overview's numbers: totals now, a daily series, and four setup facts.

    One request rather than five, because the overview draws all of it at once
    and five round trips would be five chances for the cards to disagree about
    which environment they are describing.

    Cached for 60 seconds per environment and range
    (`apps.accounts.services.stats`), so the range switcher's three answers cost
    one computation each however often somebody clicks between them —
    `computed_at` is the moment of that computation, not of this request.

    Args:
        app_id (str):
        environment_id (str):
        range_ (ReadEnvironmentStatsRange | Unset):  Default: ReadEnvironmentStatsRange.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnvironmentStats | Problem
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            environment_id=environment_id,
            client=client,
            range_=range_,
        )
    ).parsed
