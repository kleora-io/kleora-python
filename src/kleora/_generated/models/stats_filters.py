# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.stats_filters_range import StatsFiltersRange
from ..types import UNSET, Unset

T = TypeVar("T", bound="StatsFilters")


@_attrs_define
class StatsFilters:
    """The one query parameter of `GET …/stats`.

    A schema rather than a handler argument, so the parameter appears in the
    document under its own name and the default lives in one place.

        Attributes:
            range_ (StatsFiltersRange | Unset):  Default: StatsFiltersRange.VALUE_0.
    """

    range_: StatsFiltersRange | Unset = StatsFiltersRange.VALUE_0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        range_: str | Unset = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if range_ is not UNSET:
            field_dict["range"] = range_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _range_ = d.pop("range", UNSET)
        range_: StatsFiltersRange | Unset
        if isinstance(_range_, Unset):
            range_ = UNSET
        else:
            range_ = StatsFiltersRange(_range_)

        stats_filters = cls(
            range_=range_,
        )

        stats_filters.additional_properties = d
        return stats_filters

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
