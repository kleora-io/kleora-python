# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.user_setting_out_access import UserSettingOutAccess
from ..models.user_setting_out_type import UserSettingOutType

T = TypeVar("T", bound="UserSettingOut")


@_attrs_define
class UserSettingOut:
    """One definition's answer for one user: the stored value, or the default.

    `value` is what the user *has* — their written value where one exists, the
    definition's default otherwise, `null` where there is neither — which is
    the same resolution the public surface will serve the user themself
    (user-settings.md §API).

        Attributes:
            access (UserSettingOutAccess):
            key (str):
            type_ (UserSettingOutType):
            value (bool | float | int | None | str):
    """

    access: UserSettingOutAccess
    key: str
    type_: UserSettingOutType
    value: bool | float | int | None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access = self.access.value

        key = self.key

        type_ = self.type_.value

        value: bool | float | int | None | str
        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access": access,
                "key": key,
                "type": type_,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        access = UserSettingOutAccess(d.pop("access"))

        key = d.pop("key")

        type_ = UserSettingOutType(d.pop("type"))

        def _parse_value(data: object) -> bool | float | int | None | str:
            if data is None:
                return data
            return cast(bool | float | int | None | str, data)

        value = _parse_value(d.pop("value"))

        user_setting_out = cls(
            access=access,
            key=key,
            type_=type_,
            value=value,
        )

        user_setting_out.additional_properties = d
        return user_setting_out

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
