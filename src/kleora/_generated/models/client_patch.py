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

from ..models.client_patch_kind import ClientPatchKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientPatch")


@_attrs_define
class ClientPatch:
    """`PATCH /api/v1/environments/{environment_id}/clients/{client_id}`.

    `initiate_login_uri` is the one clearable field: `null` means "this client
    names no landing", and the hosted pages then carry no link at all. The two
    URI arrays are replaced whole by a merge patch, and `[]` is a valid value
    distinct from the `null` neither of them accepts.

    `is_default` is a plain `bool`, which is what makes `{"is_default": null}`
    answer 422 `field-not-nullable` rather than a type error: the field has no
    null state, and a merge patch's `null` would mean the same impossible thing
    `false` does. `false` itself passes the schema and is refused by the
    resource, as 409 `client-default`.

    `client_id`, `client_secret`, `has_secret` and `environment_id` are unknown
    fields rather than immutable ones, because the spec answers them that way:
    the identifier is not a property a caller addresses at all
    (clients.md §"Failure modes").

        Attributes:
            allowed_scopes (list[str] | Unset):
            device_grant_enabled (bool | Unset):
            initiate_login_uri (None | str | Unset):
            is_default (bool | Unset):
            kind (ClientPatchKind | Unset):
            name (str | Unset):
            post_logout_redirect_uris (list[str] | Unset):
            redirect_uris (list[str] | Unset):
    """

    allowed_scopes: list[str] | Unset = UNSET
    device_grant_enabled: bool | Unset = UNSET
    initiate_login_uri: None | str | Unset = UNSET
    is_default: bool | Unset = UNSET
    kind: ClientPatchKind | Unset = UNSET
    name: str | Unset = UNSET
    post_logout_redirect_uris: list[str] | Unset = UNSET
    redirect_uris: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        allowed_scopes: list[str] | Unset = UNSET
        if not isinstance(self.allowed_scopes, Unset):
            allowed_scopes = self.allowed_scopes

        device_grant_enabled = self.device_grant_enabled

        initiate_login_uri: None | str | Unset
        if isinstance(self.initiate_login_uri, Unset):
            initiate_login_uri = UNSET
        else:
            initiate_login_uri = self.initiate_login_uri

        is_default = self.is_default

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        name = self.name

        post_logout_redirect_uris: list[str] | Unset = UNSET
        if not isinstance(self.post_logout_redirect_uris, Unset):
            post_logout_redirect_uris = self.post_logout_redirect_uris

        redirect_uris: list[str] | Unset = UNSET
        if not isinstance(self.redirect_uris, Unset):
            redirect_uris = self.redirect_uris

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if allowed_scopes is not UNSET:
            field_dict["allowed_scopes"] = allowed_scopes
        if device_grant_enabled is not UNSET:
            field_dict["device_grant_enabled"] = device_grant_enabled
        if initiate_login_uri is not UNSET:
            field_dict["initiate_login_uri"] = initiate_login_uri
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if kind is not UNSET:
            field_dict["kind"] = kind
        if name is not UNSET:
            field_dict["name"] = name
        if post_logout_redirect_uris is not UNSET:
            field_dict["post_logout_redirect_uris"] = post_logout_redirect_uris
        if redirect_uris is not UNSET:
            field_dict["redirect_uris"] = redirect_uris

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
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

        is_default = d.pop("is_default", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: ClientPatchKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = ClientPatchKind(_kind)

        name = d.pop("name", UNSET)

        post_logout_redirect_uris = cast(
            list[str], d.pop("post_logout_redirect_uris", UNSET)
        )

        redirect_uris = cast(list[str], d.pop("redirect_uris", UNSET))

        client_patch = cls(
            allowed_scopes=allowed_scopes,
            device_grant_enabled=device_grant_enabled,
            initiate_login_uri=initiate_login_uri,
            is_default=is_default,
            kind=kind,
            name=name,
            post_logout_redirect_uris=post_logout_redirect_uris,
            redirect_uris=redirect_uris,
        )

        return client_patch
