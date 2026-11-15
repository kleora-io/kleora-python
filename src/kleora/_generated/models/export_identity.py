# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="ExportIdentity")


@_attrs_define
class ExportIdentity:
    """One identity in a user export, without any secret.

    Includes what the provider reported about the user and when the identity was linked and last
    used. For a `password` identity these provider fields are empty.

        Attributes:
            last_login_at (datetime.datetime | None):
            linked_at (datetime.datetime | None):
            linked_via (str):
            provider (str):
            provider_email (str):
            provider_email_verified (bool):
            provider_name (str):
            provider_picture_url (None | str):
            provider_subject (None | str):
            secret_updated_at (datetime.datetime):
    """

    last_login_at: datetime.datetime | None
    linked_at: datetime.datetime | None
    linked_via: str
    provider: str
    provider_email: str
    provider_email_verified: bool
    provider_name: str
    provider_picture_url: None | str
    provider_subject: None | str
    secret_updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        linked_via = self.linked_via

        provider = self.provider

        provider_email = self.provider_email

        provider_email_verified = self.provider_email_verified

        provider_name = self.provider_name

        provider_picture_url: None | str
        provider_picture_url = self.provider_picture_url

        provider_subject: None | str
        provider_subject = self.provider_subject

        secret_updated_at = self.secret_updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "last_login_at": last_login_at,
                "linked_at": linked_at,
                "linked_via": linked_via,
                "provider": provider,
                "provider_email": provider_email,
                "provider_email_verified": provider_email_verified,
                "provider_name": provider_name,
                "provider_picture_url": provider_picture_url,
                "provider_subject": provider_subject,
                "secret_updated_at": secret_updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

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

        linked_via = d.pop("linked_via")

        provider = d.pop("provider")

        provider_email = d.pop("provider_email")

        provider_email_verified = d.pop("provider_email_verified")

        provider_name = d.pop("provider_name")

        def _parse_provider_picture_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        provider_picture_url = _parse_provider_picture_url(
            d.pop("provider_picture_url")
        )

        def _parse_provider_subject(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        provider_subject = _parse_provider_subject(d.pop("provider_subject"))

        secret_updated_at = datetime.datetime.fromisoformat(d.pop("secret_updated_at"))

        export_identity = cls(
            last_login_at=last_login_at,
            linked_at=linked_at,
            linked_via=linked_via,
            provider=provider,
            provider_email=provider_email,
            provider_email_verified=provider_email_verified,
            provider_name=provider_name,
            provider_picture_url=provider_picture_url,
            provider_subject=provider_subject,
            secret_updated_at=secret_updated_at,
        )

        export_identity.additional_properties = d
        return export_identity

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
