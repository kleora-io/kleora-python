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

T = TypeVar("T", bound="UserSettingValueIn")


@_attrs_define
class UserSettingValueIn:
    """The body of `PUT .../settings/users/{user_id}/values/{key}`: the whole value.

    Never `null`. A value the setting's constraints refuse is `422`.

        Attributes:
            value (bool | float | int | str):
    """

    value: bool | float | int | str

    def to_dict(self) -> dict[str, Any]:
        value: bool | float | int | str
        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_value(data: object) -> bool | float | int | str:
            return cast(bool | float | int | str, data)

        value = _parse_value(d.pop("value"))

        user_setting_value_in = cls(
            value=value,
        )

        return user_setting_value_in
