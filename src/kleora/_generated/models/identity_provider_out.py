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

from ..models.identity_provider_out_kind import IdentityProviderOutKind

T = TypeVar("T", bound="IdentityProviderOut")


@_attrs_define
class IdentityProviderOut:
    """One configured provider. Never its client secret, in any shape.

    `callback_url` is the whole reason a customer opens this resource: it is the
    one string they have to paste into Google Cloud Console or Entra, it differs
    between production and sandbox because the issuer does (ADR 0006), and it is
    **computed** from the environment's issuer rather than stored — so a stack
    whose ports moved answers with the URL that works now rather than the one
    that worked when the row was written.

    `scopes` is the extras the customer added; `requested_scopes` is what an
    authorization request will actually ask for, the provider's own minimum
    included. Both, because "why is it asking for `openid`?" and "what did I
    add?" are different questions and one field cannot answer both.

        Attributes:
            allowed_email_domains (list[str]):
            button_label (str):
            callback_url (str):
            client_id (str):
            client_secret_set (bool):
            client_secret_updated_at (datetime.datetime):
            created_at (datetime.datetime):
            enabled (bool):
            environment_id (UUID):
            id (UUID):
            kind (IdentityProviderOutKind):
            microsoft_tenant (None | str):
            previous_secret_expires_at (datetime.datetime | None):
            requested_scopes (list[str]):
            scopes (list[str]):
            updated_at (datetime.datetime):
    """

    allowed_email_domains: list[str]
    button_label: str
    callback_url: str
    client_id: str
    client_secret_set: bool
    client_secret_updated_at: datetime.datetime
    created_at: datetime.datetime
    enabled: bool
    environment_id: UUID
    id: UUID
    kind: IdentityProviderOutKind
    microsoft_tenant: None | str
    previous_secret_expires_at: datetime.datetime | None
    requested_scopes: list[str]
    scopes: list[str]
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed_email_domains = self.allowed_email_domains

        button_label = self.button_label

        callback_url = self.callback_url

        client_id = self.client_id

        client_secret_set = self.client_secret_set

        client_secret_updated_at = self.client_secret_updated_at.isoformat()

        created_at = self.created_at.isoformat()

        enabled = self.enabled

        environment_id = str(self.environment_id)

        id = str(self.id)

        kind = self.kind.value

        microsoft_tenant: None | str
        microsoft_tenant = self.microsoft_tenant

        previous_secret_expires_at: None | str
        if isinstance(self.previous_secret_expires_at, datetime.datetime):
            previous_secret_expires_at = self.previous_secret_expires_at.isoformat()
        else:
            previous_secret_expires_at = self.previous_secret_expires_at

        requested_scopes = self.requested_scopes

        scopes = self.scopes

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowed_email_domains": allowed_email_domains,
                "button_label": button_label,
                "callback_url": callback_url,
                "client_id": client_id,
                "client_secret_set": client_secret_set,
                "client_secret_updated_at": client_secret_updated_at,
                "created_at": created_at,
                "enabled": enabled,
                "environment_id": environment_id,
                "id": id,
                "kind": kind,
                "microsoft_tenant": microsoft_tenant,
                "previous_secret_expires_at": previous_secret_expires_at,
                "requested_scopes": requested_scopes,
                "scopes": scopes,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        allowed_email_domains = cast(list[str], d.pop("allowed_email_domains"))

        button_label = d.pop("button_label")

        callback_url = d.pop("callback_url")

        client_id = d.pop("client_id")

        client_secret_set = d.pop("client_secret_set")

        client_secret_updated_at = datetime.datetime.fromisoformat(
            d.pop("client_secret_updated_at")
        )

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        enabled = d.pop("enabled")

        environment_id = UUID(d.pop("environment_id"))

        id = UUID(d.pop("id"))

        kind = IdentityProviderOutKind(d.pop("kind"))

        def _parse_microsoft_tenant(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        microsoft_tenant = _parse_microsoft_tenant(d.pop("microsoft_tenant"))

        def _parse_previous_secret_expires_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                previous_secret_expires_at_type_0 = datetime.datetime.fromisoformat(
                    data
                )

                return previous_secret_expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        previous_secret_expires_at = _parse_previous_secret_expires_at(
            d.pop("previous_secret_expires_at")
        )

        requested_scopes = cast(list[str], d.pop("requested_scopes"))

        scopes = cast(list[str], d.pop("scopes"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        identity_provider_out = cls(
            allowed_email_domains=allowed_email_domains,
            button_label=button_label,
            callback_url=callback_url,
            client_id=client_id,
            client_secret_set=client_secret_set,
            client_secret_updated_at=client_secret_updated_at,
            created_at=created_at,
            enabled=enabled,
            environment_id=environment_id,
            id=id,
            kind=kind,
            microsoft_tenant=microsoft_tenant,
            previous_secret_expires_at=previous_secret_expires_at,
            requested_scopes=requested_scopes,
            scopes=scopes,
            updated_at=updated_at,
        )

        identity_provider_out.additional_properties = d
        return identity_provider_out

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
