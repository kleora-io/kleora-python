# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed self-service API document
# (https://id.kleora.eu/account/v1/openapi.json). `kleora.account` wraps this tree; nothing outside the
# package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.user_setting_document import UserSettingDocument


T = TypeVar("T", bound="UserSettingsDocument")


@_attrs_define
class UserSettingsDocument:
    """`GET /account/v1/settings` — one row per definition the user may see.

    At most 50 rows (the definitions cap), in key order. `hidden` definitions
    are absent — not present-but-masked — which is the enumeration property the
    404s rest on.

        Attributes:
            settings (list[UserSettingDocument]):
    """

    settings: list[UserSettingDocument]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        settings = []
        for settings_item_data in self.settings:
            settings_item = settings_item_data.to_dict()
            settings.append(settings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "settings": settings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.user_setting_document import UserSettingDocument

        d = dict(src_dict)
        settings = []
        _settings = d.pop("settings")
        for settings_item_data in _settings:
            settings_item = UserSettingDocument.from_dict(settings_item_data)

            settings.append(settings_item)

        user_settings_document = cls(
            settings=settings,
        )

        user_settings_document.additional_properties = d
        return user_settings_document

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
