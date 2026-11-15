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

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_display import AuditDisplay


T = TypeVar("T", bound="AuditTarget")


@_attrs_define
class AuditTarget:
    """What was acted on: the model label and the row's id, never a foreign key.

    Present only when the action had a target — `target` is `null` on the
    response otherwise, rather than an object with two nulls in it.

    `display` names a `user` or `tenant` target the same way `AuditActor`'s
    does, and is absent for every other target kind.

        Attributes:
            id (UUID):
            kind (str):
            display (AuditDisplay | None | Unset):
    """

    id: UUID
    kind: str
    display: AuditDisplay | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.audit_display import AuditDisplay

        id = str(self.id)

        kind = self.kind

        display: dict[str, Any] | None | Unset
        if isinstance(self.display, Unset):
            display = UNSET
        elif isinstance(self.display, AuditDisplay):
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
        from ..models.audit_display import AuditDisplay

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        kind = d.pop("kind")

        def _parse_display(data: object) -> AuditDisplay | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                display_type_0 = AuditDisplay.from_dict(data)

                return display_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AuditDisplay | None | Unset, data)

        display = _parse_display(d.pop("display", UNSET))

        audit_target = cls(
            id=id,
            kind=kind,
            display=display,
        )

        audit_target.additional_properties = d
        return audit_target

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
