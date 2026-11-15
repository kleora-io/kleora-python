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

T = TypeVar("T", bound="PromotionResourceDiff")


@_attrs_define
class PromotionResourceDiff:
    """What a promotion did to one kind of resource, matched by key.

    `created` and `updated` name the resources by their key: a permission by `name`, a role by
    `slug`, a template by `kind:locale`. `unchanged` counts the ones that matched and did not
    change. Resources that exist only in production are not listed: promotion never deletes.

        Attributes:
            created (list[str]):
            unchanged (int):
            updated (list[str]):
    """

    created: list[str]
    unchanged: int
    updated: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        unchanged = self.unchanged

        updated = self.updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "unchanged": unchanged,
                "updated": updated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created = cast(list[str], d.pop("created"))

        unchanged = d.pop("unchanged")

        updated = cast(list[str], d.pop("updated"))

        promotion_resource_diff = cls(
            created=created,
            unchanged=unchanged,
            updated=updated,
        )

        promotion_resource_diff.additional_properties = d
        return promotion_resource_diff

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
