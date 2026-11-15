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

from ..types import UNSET, Unset

T = TypeVar("T", bound="PromotionIdentityProviders")


@_attrs_define
class PromotionIdentityProviders:
    """Which provider kinds each side has configured. Promotion copies **none** of them.

    D-7, and this shape is the second half of that decision: a promotion that
    silently left a difference behind would be a console that cannot explain why
    the production login page has no Google button. So the diff *names* the
    difference — `sandbox_only` is what the console turns into "sandbox has
    Google configured and production does not" — and `promoted` is flat `false`,
    stated rather than inferred from an empty list, because "nothing differed"
    and "nothing is ever copied" are different facts and only one of them is
    permanent.

    Why nothing is copied: a copied client secret would point production at a
    sandbox OAuth application, and copying `enabled` without the secret would be
    worse — an enabled provider with no credentials is a button on the production
    login page that cannot work. Promotion copies no credential anywhere
    (environments.md §Promotion: not Clients, not API keys, not webhook
    endpoints), and this is the same category.

        Attributes:
            both (list[str]):
            production_only (list[str]):
            sandbox_only (list[str]):
            promoted (bool | Unset):  Default: False.
    """

    both: list[str]
    production_only: list[str]
    sandbox_only: list[str]
    promoted: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        both = self.both

        production_only = self.production_only

        sandbox_only = self.sandbox_only

        promoted = self.promoted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "both": both,
                "production_only": production_only,
                "sandbox_only": sandbox_only,
            }
        )
        if promoted is not UNSET:
            field_dict["promoted"] = promoted

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        both = cast(list[str], d.pop("both"))

        production_only = cast(list[str], d.pop("production_only"))

        sandbox_only = cast(list[str], d.pop("sandbox_only"))

        promoted = d.pop("promoted", UNSET)

        promotion_identity_providers = cls(
            both=both,
            production_only=production_only,
            sandbox_only=sandbox_only,
            promoted=promoted,
        )

        promotion_identity_providers.additional_properties = d
        return promotion_identity_providers

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
