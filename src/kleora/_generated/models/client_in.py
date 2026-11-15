# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.client_in_kind import ClientInKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientIn")


@_attrs_define
class ClientIn:
    """`POST /api/v1/environments/{environment_id}/clients`.

    `extra="forbid"` is the whole of the "not an input field" rule: `client_id`,
    `client_secret`, `has_secret`, `environment_id` and `is_default` are 422 as
    unknown fields, and `is_default` in particular is settable only by `PATCH`
    and only to `true` — a new client is never silently the one the hosted pages
    fall back to (clients.md §`POST …/clients`).

    The one rule about the arrays that does not depend on the environment is
    here: at most `MAX_URIS` entries each, so the bound reaches the OpenAPI
    document and a generated client refuses the thirty-third before we do.

    The rest of the URI and scope rules are not here: they depend on the *environment*
    (`http://localhost` is a sandbox-only value), which a schema cannot see, so
    the router checks them against the resolved environment and names the array
    index the caller sent.

        Attributes:
            kind (ClientInKind):
            name (str):
            allowed_scopes (list[str] | Unset):
            device_grant_enabled (bool | Unset):  Default: False.
            initiate_login_uri (None | str | Unset):
            post_logout_redirect_uris (list[str] | Unset):
            redirect_uris (list[str] | Unset):
    """

    kind: ClientInKind
    name: str
    allowed_scopes: list[str] | Unset = UNSET
    device_grant_enabled: bool | Unset = False
    initiate_login_uri: None | str | Unset = UNSET
    post_logout_redirect_uris: list[str] | Unset = UNSET
    redirect_uris: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        name = self.name

        allowed_scopes: list[str] | Unset = UNSET
        if not isinstance(self.allowed_scopes, Unset):
            allowed_scopes = self.allowed_scopes

        device_grant_enabled = self.device_grant_enabled

        initiate_login_uri: None | str | Unset
        if isinstance(self.initiate_login_uri, Unset):
            initiate_login_uri = UNSET
        else:
            initiate_login_uri = self.initiate_login_uri

        post_logout_redirect_uris: list[str] | Unset = UNSET
        if not isinstance(self.post_logout_redirect_uris, Unset):
            post_logout_redirect_uris = self.post_logout_redirect_uris

        redirect_uris: list[str] | Unset = UNSET
        if not isinstance(self.redirect_uris, Unset):
            redirect_uris = self.redirect_uris

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "name": name,
            }
        )
        if allowed_scopes is not UNSET:
            field_dict["allowed_scopes"] = allowed_scopes
        if device_grant_enabled is not UNSET:
            field_dict["device_grant_enabled"] = device_grant_enabled
        if initiate_login_uri is not UNSET:
            field_dict["initiate_login_uri"] = initiate_login_uri
        if post_logout_redirect_uris is not UNSET:
            field_dict["post_logout_redirect_uris"] = post_logout_redirect_uris
        if redirect_uris is not UNSET:
            field_dict["redirect_uris"] = redirect_uris

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = ClientInKind(d.pop("kind"))

        name = d.pop("name")

        allowed_scopes = cast(list[str], d.pop("allowed_scopes", UNSET))

        device_grant_enabled = d.pop("device_grant_enabled", UNSET)

        def _parse_initiate_login_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        initiate_login_uri = _parse_initiate_login_uri(
            d.pop("initiate_login_uri", UNSET)
        )

        post_logout_redirect_uris = cast(
            list[str], d.pop("post_logout_redirect_uris", UNSET)
        )

        redirect_uris = cast(list[str], d.pop("redirect_uris", UNSET))

        client_in = cls(
            kind=kind,
            name=name,
            allowed_scopes=allowed_scopes,
            device_grant_enabled=device_grant_enabled,
            initiate_login_uri=initiate_login_uri,
            post_logout_redirect_uris=post_logout_redirect_uris,
            redirect_uris=redirect_uris,
        )

        return client_in
