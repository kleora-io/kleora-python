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
from ...models.portal_out import PortalOut
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/account/v1/portal",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FlowProblem | PortalOut | None:
    if response.status_code == 200:
        response_200 = PortalOut.from_dict(response.json())

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
) -> Response[FlowProblem | PortalOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[FlowProblem | PortalOut]:
    r"""Where the hosted account portal is, and which sections it offers

     The portal's stable entry URL, and the sections this Environment offers.

    **`danger` is here when `Environment.self_deletion` is on, and absent otherwise**
    — the seam `U10-03` left (`PortalSection` already declared the value, `ALWAYS` did
    not list it), closed by `U10-05` with the column it needs. §\"The portal\" gives the
    condition as \"when the Environment offers it\", and this is the only place on the
    surface that answers that question in a document rather than as a `404`: §API says
    so in as many words, \"so a customer's own page renders the right links without
    hard-coding a path of ours or **guessing at `self_deletion`**\".

    It is still not the decision. The `/deletion` routes are `404` when the column is
    false whatever this list says, which is §\"Failure modes\"' \"the API's `404` is what
    decides it\" — a client-side route that hides itself is not a control.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlowProblem | PortalOut]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> FlowProblem | PortalOut | None:
    r"""Where the hosted account portal is, and which sections it offers

     The portal's stable entry URL, and the sections this Environment offers.

    **`danger` is here when `Environment.self_deletion` is on, and absent otherwise**
    — the seam `U10-03` left (`PortalSection` already declared the value, `ALWAYS` did
    not list it), closed by `U10-05` with the column it needs. §\"The portal\" gives the
    condition as \"when the Environment offers it\", and this is the only place on the
    surface that answers that question in a document rather than as a `404`: §API says
    so in as many words, \"so a customer's own page renders the right links without
    hard-coding a path of ours or **guessing at `self_deletion`**\".

    It is still not the decision. The `/deletion` routes are `404` when the column is
    false whatever this list says, which is §\"Failure modes\"' \"the API's `404` is what
    decides it\" — a client-side route that hides itself is not a control.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlowProblem | PortalOut
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[FlowProblem | PortalOut]:
    r"""Where the hosted account portal is, and which sections it offers

     The portal's stable entry URL, and the sections this Environment offers.

    **`danger` is here when `Environment.self_deletion` is on, and absent otherwise**
    — the seam `U10-03` left (`PortalSection` already declared the value, `ALWAYS` did
    not list it), closed by `U10-05` with the column it needs. §\"The portal\" gives the
    condition as \"when the Environment offers it\", and this is the only place on the
    surface that answers that question in a document rather than as a `404`: §API says
    so in as many words, \"so a customer's own page renders the right links without
    hard-coding a path of ours or **guessing at `self_deletion`**\".

    It is still not the decision. The `/deletion` routes are `404` when the column is
    false whatever this list says, which is §\"Failure modes\"' \"the API's `404` is what
    decides it\" — a client-side route that hides itself is not a control.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlowProblem | PortalOut]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> FlowProblem | PortalOut | None:
    r"""Where the hosted account portal is, and which sections it offers

     The portal's stable entry URL, and the sections this Environment offers.

    **`danger` is here when `Environment.self_deletion` is on, and absent otherwise**
    — the seam `U10-03` left (`PortalSection` already declared the value, `ALWAYS` did
    not list it), closed by `U10-05` with the column it needs. §\"The portal\" gives the
    condition as \"when the Environment offers it\", and this is the only place on the
    surface that answers that question in a document rather than as a `404`: §API says
    so in as many words, \"so a customer's own page renders the right links without
    hard-coding a path of ours or **guessing at `self_deletion`**\".

    It is still not the decision. The `/deletion` routes are `404` when the column is
    false whatever this list says, which is §\"Failure modes\"' \"the API's `404` is what
    decides it\" — a client-side route that hides itself is not a control.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlowProblem | PortalOut
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
