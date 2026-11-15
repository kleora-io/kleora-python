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


T = TypeVar("T", bound="AuditActor")


@_attrs_define
class AuditActor:
    """Who acted: `{"kind": …, "id": …}`, with `id` null for `system`/`anonymous`.

    `display` names a `user` actor — resolved when the page is read
    (audit-log.md §"Naming the actor and the target") — and is absent, not
    null, for `api_key`, `system` and `anonymous`: none of them has a name.

        Attributes:
            id (None | UUID):
            kind (str):
            display (AuditDisplay | None | Unset):
    """

    id: None | UUID
    kind: str
    display: AuditDisplay | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.audit_display import AuditDisplay

        id: None | str
        if isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

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

        def _parse_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        id = _parse_id(d.pop("id"))

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

        audit_actor = cls(
            id=id,
            kind=kind,
            display=display,
        )

        audit_actor.additional_properties = d
        return audit_actor

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
