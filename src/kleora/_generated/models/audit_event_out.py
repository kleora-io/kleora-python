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
    from ..models.audit_actor import AuditActor
    from ..models.audit_event_out_data import AuditEventOutData
    from ..models.audit_target import AuditTarget


T = TypeVar("T", bound="AuditEventOut")


@_attrs_define
class AuditEventOut:
    """One audit event.

    `environment_id` and `tenant_id` may be `null`: an account-level event has no environment, and
    deleting an App clears the environment of the events recorded inside it, while the events
    themselves are kept.

        Attributes:
            account_id (UUID):
            action (str):
            actor (AuditActor): Who acted: `{"kind": ..., "id": ...}`, with `id` `null` for `system` and `anonymous`.

                `display` names a `user` actor, as they are now, and is absent for `api_key`, `system` and
                `anonymous`.
            data (AuditEventOutData):
            environment_id (None | UUID):
            id (UUID):
            ip (None | str):
            occurred_at (datetime.datetime):
            target (AuditTarget | None):
            tenant_id (None | UUID):
            user_agent (None | str):
    """

    account_id: UUID
    action: str
    actor: AuditActor
    data: AuditEventOutData
    environment_id: None | UUID
    id: UUID
    ip: None | str
    occurred_at: datetime.datetime
    target: AuditTarget | None
    tenant_id: None | UUID
    user_agent: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.audit_target import AuditTarget

        account_id = str(self.account_id)

        action = self.action

        actor = self.actor.to_dict()

        data = self.data.to_dict()

        environment_id: None | str
        if isinstance(self.environment_id, UUID):
            environment_id = str(self.environment_id)
        else:
            environment_id = self.environment_id

        id = str(self.id)

        ip: None | str
        ip = self.ip

        occurred_at = self.occurred_at.isoformat()

        target: dict[str, Any] | None
        if isinstance(self.target, AuditTarget):
            target = self.target.to_dict()
        else:
            target = self.target

        tenant_id: None | str
        if isinstance(self.tenant_id, UUID):
            tenant_id = str(self.tenant_id)
        else:
            tenant_id = self.tenant_id

        user_agent: None | str
        user_agent = self.user_agent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "action": action,
                "actor": actor,
                "data": data,
                "environment_id": environment_id,
                "id": id,
                "ip": ip,
                "occurred_at": occurred_at,
                "target": target,
                "tenant_id": tenant_id,
                "user_agent": user_agent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.audit_actor import AuditActor
        from ..models.audit_event_out_data import AuditEventOutData
        from ..models.audit_target import AuditTarget

        d = dict(src_dict)
        account_id = UUID(d.pop("account_id"))

        action = d.pop("action")

        actor = AuditActor.from_dict(d.pop("actor"))

        data = AuditEventOutData.from_dict(d.pop("data"))

        def _parse_environment_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                environment_id_type_0 = UUID(data)

                return environment_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        environment_id = _parse_environment_id(d.pop("environment_id"))

        id = UUID(d.pop("id"))

        def _parse_ip(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ip = _parse_ip(d.pop("ip"))

        occurred_at = datetime.datetime.fromisoformat(d.pop("occurred_at"))

        def _parse_target(data: object) -> AuditTarget | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                target_type_0 = AuditTarget.from_dict(data)

                return target_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AuditTarget | None, data)

        target = _parse_target(d.pop("target"))

        def _parse_tenant_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tenant_id_type_0 = UUID(data)

                return tenant_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        tenant_id = _parse_tenant_id(d.pop("tenant_id"))

        def _parse_user_agent(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        user_agent = _parse_user_agent(d.pop("user_agent"))

        audit_event_out = cls(
            account_id=account_id,
            action=action,
            actor=actor,
            data=data,
            environment_id=environment_id,
            id=id,
            ip=ip,
            occurred_at=occurred_at,
            target=target,
            tenant_id=tenant_id,
            user_agent=user_agent,
        )

        audit_event_out.additional_properties = d
        return audit_event_out

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
