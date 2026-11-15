# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed self-service API document
# (https://id.kleora.eu/account/v1/openapi.json). `kleora.account` wraps this tree; nothing outside the
# package imports it.
from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="IdentityOut")


@_attrs_define
class IdentityOut:
    """One provider link. No `provider_subject` — it is the operator's projection.

    Attributes:
        id (UUID):
        kind (str):
        last_login_at (datetime.datetime | None):
        linked_at (datetime.datetime | None):
        provider_email (None | str):
    """

    id: UUID
    kind: str
    last_login_at: datetime.datetime | None
    linked_at: datetime.datetime | None
    provider_email: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        kind = self.kind

        last_login_at: None | str
        if isinstance(self.last_login_at, datetime.datetime):
            last_login_at = self.last_login_at.isoformat()
        else:
            last_login_at = self.last_login_at

        linked_at: None | str
        if isinstance(self.linked_at, datetime.datetime):
            linked_at = self.linked_at.isoformat()
        else:
            linked_at = self.linked_at

        provider_email: None | str
        provider_email = self.provider_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "kind": kind,
                "last_login_at": last_login_at,
                "linked_at": linked_at,
                "provider_email": provider_email,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        kind = d.pop("kind")

        def _parse_last_login_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_login_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_login_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_login_at = _parse_last_login_at(d.pop("last_login_at"))

        def _parse_linked_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                linked_at_type_0 = datetime.datetime.fromisoformat(data)

                return linked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        linked_at = _parse_linked_at(d.pop("linked_at"))

        def _parse_provider_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        provider_email = _parse_provider_email(d.pop("provider_email"))

        identity_out = cls(
            id=id,
            kind=kind,
            last_login_at=last_login_at,
            linked_at=linked_at,
            provider_email=provider_email,
        )

        identity_out.additional_properties = d
        return identity_out

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
