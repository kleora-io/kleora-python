# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="ClientOut")


@_attrs_define
class ClientOut:
    """An OAuth client.

    The client secret is never returned. `has_secret` says whether the client has one.

        Attributes:
            allowed_scopes (list[str]):
            client_id (str):
            created_at (datetime.datetime):
            device_grant_enabled (bool):
            environment_id (UUID):
            has_secret (bool):
            id (UUID):
            initiate_login_uri (None | str):
            is_default (bool):
            kind (str):
            name (str):
            post_logout_redirect_uris (list[str]):
            redirect_uris (list[str]):
            updated_at (datetime.datetime):
    """

    allowed_scopes: list[str]
    client_id: str
    created_at: datetime.datetime
    device_grant_enabled: bool
    environment_id: UUID
    has_secret: bool
    id: UUID
    initiate_login_uri: None | str
    is_default: bool
    kind: str
    name: str
    post_logout_redirect_uris: list[str]
    redirect_uris: list[str]
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed_scopes = self.allowed_scopes

        client_id = self.client_id

        created_at = self.created_at.isoformat()

        device_grant_enabled = self.device_grant_enabled

        environment_id = str(self.environment_id)

        has_secret = self.has_secret

        id = str(self.id)

        initiate_login_uri: None | str
        initiate_login_uri = self.initiate_login_uri

        is_default = self.is_default

        kind = self.kind

        name = self.name

        post_logout_redirect_uris = self.post_logout_redirect_uris

        redirect_uris = self.redirect_uris

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowed_scopes": allowed_scopes,
                "client_id": client_id,
                "created_at": created_at,
                "device_grant_enabled": device_grant_enabled,
                "environment_id": environment_id,
                "has_secret": has_secret,
                "id": id,
                "initiate_login_uri": initiate_login_uri,
                "is_default": is_default,
                "kind": kind,
                "name": name,
                "post_logout_redirect_uris": post_logout_redirect_uris,
                "redirect_uris": redirect_uris,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        allowed_scopes = cast(list[str], d.pop("allowed_scopes"))

        client_id = d.pop("client_id")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        device_grant_enabled = d.pop("device_grant_enabled")

        environment_id = UUID(d.pop("environment_id"))

        has_secret = d.pop("has_secret")

        id = UUID(d.pop("id"))

        def _parse_initiate_login_uri(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        initiate_login_uri = _parse_initiate_login_uri(d.pop("initiate_login_uri"))

        is_default = d.pop("is_default")

        kind = d.pop("kind")

        name = d.pop("name")

        post_logout_redirect_uris = cast(list[str], d.pop("post_logout_redirect_uris"))

        redirect_uris = cast(list[str], d.pop("redirect_uris"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        client_out = cls(
            allowed_scopes=allowed_scopes,
            client_id=client_id,
            created_at=created_at,
            device_grant_enabled=device_grant_enabled,
            environment_id=environment_id,
            has_secret=has_secret,
            id=id,
            initiate_login_uri=initiate_login_uri,
            is_default=is_default,
            kind=kind,
            name=name,
            post_logout_redirect_uris=post_logout_redirect_uris,
            redirect_uris=redirect_uris,
            updated_at=updated_at,
        )

        client_out.additional_properties = d
        return client_out

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
