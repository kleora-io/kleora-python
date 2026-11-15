# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.blocked_by_kind import BlockedByKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.blocked_by_display import BlockedByDisplay


T = TypeVar("T", bound="BlockedBy")


@_attrs_define
class BlockedBy:
    """The principal that blocked a user: `{"kind": …, "id": …}` plus a display.

    `display` is `null`, not absent, when there is nobody to name — an
    `api_key` blocker (a key is not a person and must not be given a
    placeholder name, audit-log.md's rule) or an id that no longer resolves.
    That is a deliberate divergence from `AuditActor`, which omits the key
    entirely: the audit endpoints can do that because they serialise with
    `exclude_unset=True`, and turning that on for `UserOut` would change how
    every *other* field of the busiest resource on this surface is serialised.
    A `null` here is readable and costs nothing, where that would.

        Attributes:
            id (UUID):
            kind (BlockedByKind):
            display (BlockedByDisplay | None | Unset):
    """

    id: UUID
    kind: BlockedByKind
    display: BlockedByDisplay | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.blocked_by_display import BlockedByDisplay

        id = str(self.id)

        kind = self.kind.value

        display: dict[str, Any] | None | Unset
        if isinstance(self.display, Unset):
            display = UNSET
        elif isinstance(self.display, BlockedByDisplay):
            display = self.display.to_dict()
        else:
            display = self.display

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "kind": kind,
            }
        )
        if display is not UNSET:
            field_dict["display"] = display

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.blocked_by_display import BlockedByDisplay

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        kind = BlockedByKind(d.pop("kind"))

        def _parse_display(data: object) -> BlockedByDisplay | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                display_type_0 = BlockedByDisplay.from_dict(data)

                return display_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlockedByDisplay | None | Unset, data)

        display = _parse_display(d.pop("display", UNSET))

        blocked_by = cls(
            id=id,
            kind=kind,
            display=display,
        )

        blocked_by.additional_properties = d
        return blocked_by

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
