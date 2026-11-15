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

from ..types import UNSET, Unset

T = TypeVar("T", bound="SettingConstraints")


@_attrs_define
class SettingConstraints:
    """The by-type constraints of one definition (user-settings.md §Model).

    One schema for all four types rather than a union, because which fields
    apply is decided by the sibling `type` field: `choices` for `enum` (1-32
    strings, each ≤ 64 chars), `max_length` for `string` (≤ 1024, default 256,
    always present on a stored definition), `min`/`max` for `number`, nothing
    for `boolean`. A field sent for another type is a 422 naming it; the
    server stores the constraints normalised, so a reader never has to know a
    default.

        Attributes:
            choices (list[str] | None | Unset):
            max_ (float | int | None | Unset):
            max_length (int | None | Unset):
            min_ (float | int | None | Unset):
    """

    choices: list[str] | None | Unset = UNSET
    max_: float | int | None | Unset = UNSET
    max_length: int | None | Unset = UNSET
    min_: float | int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        choices: list[str] | None | Unset
        if isinstance(self.choices, Unset):
            choices = UNSET
        elif isinstance(self.choices, list):
            choices = self.choices

        else:
            choices = self.choices

        max_: float | int | None | Unset
        if isinstance(self.max_, Unset):
            max_ = UNSET
        else:
            max_ = self.max_

        max_length: int | None | Unset
        if isinstance(self.max_length, Unset):
            max_length = UNSET
        else:
            max_length = self.max_length

        min_: float | int | None | Unset
        if isinstance(self.min_, Unset):
            min_ = UNSET
        else:
            min_ = self.min_

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if choices is not UNSET:
            field_dict["choices"] = choices
        if max_ is not UNSET:
            field_dict["max"] = max_
        if max_length is not UNSET:
            field_dict["max_length"] = max_length
        if min_ is not UNSET:
            field_dict["min"] = min_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_choices(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                choices_type_0 = cast(list[str], data)

                return choices_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        choices = _parse_choices(d.pop("choices", UNSET))

        def _parse_max_(data: object) -> float | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | int | None | Unset, data)

        max_ = _parse_max_(d.pop("max", UNSET))

        def _parse_max_length(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_length = _parse_max_length(d.pop("max_length", UNSET))

        def _parse_min_(data: object) -> float | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | int | None | Unset, data)

        min_ = _parse_min_(d.pop("min", UNSET))

        setting_constraints = cls(
            choices=choices,
            max_=max_,
            max_length=max_length,
            min_=min_,
        )

        return setting_constraints
