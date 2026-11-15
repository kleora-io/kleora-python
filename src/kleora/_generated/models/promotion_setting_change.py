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

T = TypeVar("T", bound="PromotionSettingChange")


@_attrs_define
class PromotionSettingChange:
    """
    Attributes:
        field (str):
        from_ (bool | int | None | str):
        to (bool | int | None | str):
    """

    field: str
    from_: bool | int | None | str
    to: bool | int | None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        from_: bool | int | None | str
        from_ = self.from_

        to: bool | int | None | str
        to = self.to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field": field,
                "from": from_,
                "to": to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        field = d.pop("field")

        def _parse_from_(data: object) -> bool | int | None | str:
            if data is None:
                return data
            return cast(bool | int | None | str, data)

        from_ = _parse_from_(d.pop("from"))

        def _parse_to(data: object) -> bool | int | None | str:
            if data is None:
                return data
            return cast(bool | int | None | str, data)

        to = _parse_to(d.pop("to"))

        promotion_setting_change = cls(
            field=field,
            from_=from_,
            to=to,
        )

        promotion_setting_change.additional_properties = d
        return promotion_setting_change

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
