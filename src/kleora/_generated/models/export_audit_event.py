# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.export_audit_event_data import ExportAuditEventData


T = TypeVar("T", bound="ExportAuditEvent")


@_attrs_define
class ExportAuditEvent:
    """One audit event in a user export, in the same shape as the audit event API.

    Attributes:
        action (str):
        actor_id (None | UUID):
        actor_kind (str):
        data (ExportAuditEventData):
        id (UUID):
        ip (None | str):
        occurred_at (datetime.datetime):
        target_id (None | UUID):
        target_kind (None | str):
    """

    action: str
    actor_id: None | UUID
    actor_kind: str
    data: ExportAuditEventData
    id: UUID
    ip: None | str
    occurred_at: datetime.datetime
    target_id: None | UUID
    target_kind: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        actor_id: None | str
        if isinstance(self.actor_id, UUID):
            actor_id = str(self.actor_id)
        else:
            actor_id = self.actor_id

        actor_kind = self.actor_kind

        data = self.data.to_dict()

        id = str(self.id)

        ip: None | str
        ip = self.ip

        occurred_at = self.occurred_at.isoformat()

        target_id: None | str
        if isinstance(self.target_id, UUID):
            target_id = str(self.target_id)
        else:
            target_id = self.target_id

        target_kind: None | str
        target_kind = self.target_kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "actor_id": actor_id,
                "actor_kind": actor_kind,
                "data": data,
                "id": id,
                "ip": ip,
                "occurred_at": occurred_at,
                "target_id": target_id,
                "target_kind": target_kind,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.export_audit_event_data import ExportAuditEventData

        d = dict(src_dict)
        action = d.pop("action")

        def _parse_actor_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                actor_id_type_0 = UUID(data)

                return actor_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        actor_id = _parse_actor_id(d.pop("actor_id"))

        actor_kind = d.pop("actor_kind")

        data = ExportAuditEventData.from_dict(d.pop("data"))

        id = UUID(d.pop("id"))

        def _parse_ip(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ip = _parse_ip(d.pop("ip"))

        occurred_at = datetime.datetime.fromisoformat(d.pop("occurred_at"))

        def _parse_target_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                target_id_type_0 = UUID(data)

                return target_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        target_id = _parse_target_id(d.pop("target_id"))

        def _parse_target_kind(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        target_kind = _parse_target_kind(d.pop("target_kind"))

        export_audit_event = cls(
            action=action,
            actor_id=actor_id,
            actor_kind=actor_kind,
            data=data,
            id=id,
            ip=ip,
            occurred_at=occurred_at,
            target_id=target_id,
            target_kind=target_kind,
        )

        export_audit_event.additional_properties = d
        return export_audit_event

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
