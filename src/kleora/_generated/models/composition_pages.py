# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.composition_pages_additional_property import (
        CompositionPagesAdditionalProperty,
    )


T = TypeVar("T", bound="CompositionPages")


@_attrs_define
class CompositionPages:
    """ """

    additional_properties: dict[str, CompositionPagesAdditionalProperty] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.composition_pages_additional_property import (
            CompositionPagesAdditionalProperty,
        )

        d = dict(src_dict)
        composition_pages = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = CompositionPagesAdditionalProperty.from_dict(
                prop_dict
            )

            additional_properties[prop_name] = additional_property

        composition_pages.additional_properties = additional_properties
        return composition_pages

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> CompositionPagesAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: CompositionPagesAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
