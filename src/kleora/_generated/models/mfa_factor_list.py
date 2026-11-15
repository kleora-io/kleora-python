# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mfa_factor_out import MfaFactorOut


T = TypeVar("T", bound="MfaFactorList")


@_attrs_define
class MfaFactorList:
    """`GET …/users/{uid}/mfa` — every factor of the user's, confirmed or not.

    `items`/`next_cursor`, not `mfa.md` §API's literal `{factors: […]}`: every
    list envelope on this surface shares one shape for the generated clients
    (`SigningKeyList`'s own precedent — "It carries the field anyway so every
    list on the surface has one shape"), enforced by
    `tests/test_openapi_documents.py::test_every_list_envelope_is_a_named_schema`.
    `next_cursor` is always `null` — this platform never holds more than two
    rows per user (one `totp`, one `recovery`), the same reason the
    signing-key list gives. Noted in the P5-06 Log as a deviation from the
    spec's literal member name.

        Attributes:
            items (list[MfaFactorOut]):
            next_cursor (None | str | Unset):
    """

    items: list[MfaFactorOut]
    next_cursor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
            }
        )
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mfa_factor_out import MfaFactorOut

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = MfaFactorOut.from_dict(items_item_data)

            items.append(items_item)

        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor", UNSET))

        mfa_factor_list = cls(
            items=items,
            next_cursor=next_cursor,
        )

        mfa_factor_list.additional_properties = d
        return mfa_factor_list

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
