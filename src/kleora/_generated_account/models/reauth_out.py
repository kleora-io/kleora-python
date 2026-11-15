# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed self-service API document
# (https://id.kleora.eu/account/v1/openapi.json). `kleora.account` wraps this tree; nothing outside the
# package imports it.
from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.provider_out import ProviderOut


T = TypeVar("T", bound="ReauthOut")


@_attrs_define
class ReauthOut:
    """What the person can re-authenticate with.

    `reauthenticated_until` is `null` when the session has no current re-authentication, so a screen
    can tell whether to ask for one before the person fills in a form.

        Attributes:
            has_password (bool):
            passkey_available (bool):
            reauth_providers (list[ProviderOut]):
            reauthenticated_until (datetime.datetime | None):
    """

    has_password: bool
    passkey_available: bool
    reauth_providers: list[ProviderOut]
    reauthenticated_until: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        has_password = self.has_password

        passkey_available = self.passkey_available

        reauth_providers = []
        for reauth_providers_item_data in self.reauth_providers:
            reauth_providers_item = reauth_providers_item_data.to_dict()
            reauth_providers.append(reauth_providers_item)

        reauthenticated_until: None | str
        if isinstance(self.reauthenticated_until, datetime.datetime):
            reauthenticated_until = self.reauthenticated_until.isoformat()
        else:
            reauthenticated_until = self.reauthenticated_until

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "has_password": has_password,
                "passkey_available": passkey_available,
                "reauth_providers": reauth_providers,
                "reauthenticated_until": reauthenticated_until,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.provider_out import ProviderOut

        d = dict(src_dict)
        has_password = d.pop("has_password")

        passkey_available = d.pop("passkey_available")

        reauth_providers = []
        _reauth_providers = d.pop("reauth_providers")
        for reauth_providers_item_data in _reauth_providers:
            reauth_providers_item = ProviderOut.from_dict(reauth_providers_item_data)

            reauth_providers.append(reauth_providers_item)

        def _parse_reauthenticated_until(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reauthenticated_until_type_0 = datetime.datetime.fromisoformat(data)

                return reauthenticated_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        reauthenticated_until = _parse_reauthenticated_until(
            d.pop("reauthenticated_until")
        )

        reauth_out = cls(
            has_password=has_password,
            passkey_available=passkey_available,
            reauth_providers=reauth_providers,
            reauthenticated_until=reauthenticated_until,
        )

        reauth_out.additional_properties = d
        return reauth_out

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
