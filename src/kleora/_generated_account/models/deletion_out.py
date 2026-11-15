# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed self-service API document
# (https://id.kleora.eu/account/v1/openapi.json). `kleora.account` wraps this tree; nothing outside the
# package imports it.
from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="DeletionOut")


@_attrs_define
class DeletionOut:
    """§API `POST /deletion`: `202 {"erase_after": "…"}`.

    One member, and it is the only thing a caller needs and the only thing we can
    honestly promise: the moment the hourly sweep will erase this person unless the
    cancellation link is opened. RFC 3339 UTC like every other timestamp here.

    **Not `{"deleted": true}` and not a `204`**, because neither would be true.
    §"What happens, and when" is a seven-day grace period, and "delete my account"
    not deleting immediately "has to be said on the page in plain words" — a screen
    can only say it if the API says when.

        Attributes:
            erase_after (datetime.datetime):
    """

    erase_after: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        erase_after = self.erase_after.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "erase_after": erase_after,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        erase_after = datetime.datetime.fromisoformat(d.pop("erase_after"))

        deletion_out = cls(
            erase_after=erase_after,
        )

        deletion_out.additional_properties = d
        return deletion_out

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
