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

T = TypeVar("T", bound="ProfileOut")


@_attrs_define
class ProfileOut:
    """The person's profile. Custom `metadata` is never included.

    Attributes:
        created_at (datetime.datetime):
        email (str):
        email_verified (bool):
        has_password (bool):
        id (UUID):
        locale (None | str):
        mfa_enrolled (bool):
        name (None | str):
        picture_url (None | str):
    """

    created_at: datetime.datetime
    email: str
    email_verified: bool
    has_password: bool
    id: UUID
    locale: None | str
    mfa_enrolled: bool
    name: None | str
    picture_url: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        email = self.email

        email_verified = self.email_verified

        has_password = self.has_password

        id = str(self.id)

        locale: None | str
        locale = self.locale

        mfa_enrolled = self.mfa_enrolled

        name: None | str
        name = self.name

        picture_url: None | str
        picture_url = self.picture_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "email": email,
                "email_verified": email_verified,
                "has_password": has_password,
                "id": id,
                "locale": locale,
                "mfa_enrolled": mfa_enrolled,
                "name": name,
                "picture_url": picture_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        email = d.pop("email")

        email_verified = d.pop("email_verified")

        has_password = d.pop("has_password")

        id = UUID(d.pop("id"))

        def _parse_locale(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        locale = _parse_locale(d.pop("locale"))

        mfa_enrolled = d.pop("mfa_enrolled")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_picture_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        picture_url = _parse_picture_url(d.pop("picture_url"))

        profile_out = cls(
            created_at=created_at,
            email=email,
            email_verified=email_verified,
            has_password=has_password,
            id=id,
            locale=locale,
            mfa_enrolled=mfa_enrolled,
            name=name,
            picture_url=picture_url,
        )

        profile_out.additional_properties = d
        return profile_out

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
