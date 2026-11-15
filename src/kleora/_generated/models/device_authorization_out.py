# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.device_authorization_out_status import DeviceAuthorizationOutStatus

T = TypeVar("T", bound="DeviceAuthorizationOut")


@_attrs_define
class DeviceAuthorizationOut:
    """One device authorization a user approved.

    `client_name` is the client's configured name, and `client_id` its id. `last_used_at` is when a
    token was last refreshed under it; an authorization expires after 90 days without use. `ip` and
    `user_agent` are those of the browser that approved it.

        Attributes:
            approved_at (datetime.datetime | None):
            client_id (str):
            client_name (str):
            created_at (datetime.datetime):
            id (UUID):
            ip (str):
            last_used_at (datetime.datetime | None):
            scope (str):
            session_id (None | UUID):
            status (DeviceAuthorizationOutStatus):
            user_agent (str):
            user_id (UUID):
    """

    approved_at: datetime.datetime | None
    client_id: str
    client_name: str
    created_at: datetime.datetime
    id: UUID
    ip: str
    last_used_at: datetime.datetime | None
    scope: str
    session_id: None | UUID
    status: DeviceAuthorizationOutStatus
    user_agent: str
    user_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        approved_at: None | str
        if isinstance(self.approved_at, datetime.datetime):
            approved_at = self.approved_at.isoformat()
        else:
            approved_at = self.approved_at

        client_id = self.client_id

        client_name = self.client_name

        created_at = self.created_at.isoformat()

        id = str(self.id)

        ip = self.ip

        last_used_at: None | str
        if isinstance(self.last_used_at, datetime.datetime):
            last_used_at = self.last_used_at.isoformat()
        else:
            last_used_at = self.last_used_at

        scope = self.scope

        session_id: None | str
        if isinstance(self.session_id, UUID):
            session_id = str(self.session_id)
        else:
            session_id = self.session_id

        status = self.status.value

        user_agent = self.user_agent

        user_id = str(self.user_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "approved_at": approved_at,
                "client_id": client_id,
                "client_name": client_name,
                "created_at": created_at,
                "id": id,
                "ip": ip,
                "last_used_at": last_used_at,
                "scope": scope,
                "session_id": session_id,
                "status": status,
                "user_agent": user_agent,
                "user_id": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_approved_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_at_type_0 = datetime.datetime.fromisoformat(data)

                return approved_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        approved_at = _parse_approved_at(d.pop("approved_at"))

        client_id = d.pop("client_id")

        client_name = d.pop("client_name")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = UUID(d.pop("id"))

        ip = d.pop("ip")

        def _parse_last_used_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_used_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_used_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_used_at = _parse_last_used_at(d.pop("last_used_at"))

        scope = d.pop("scope")

        def _parse_session_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                session_id_type_0 = UUID(data)

                return session_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        session_id = _parse_session_id(d.pop("session_id"))

        status = DeviceAuthorizationOutStatus(d.pop("status"))

        user_agent = d.pop("user_agent")

        user_id = UUID(d.pop("user_id"))

        device_authorization_out = cls(
            approved_at=approved_at,
            client_id=client_id,
            client_name=client_name,
            created_at=created_at,
            id=id,
            ip=ip,
            last_used_at=last_used_at,
            scope=scope,
            session_id=session_id,
            status=status,
            user_agent=user_agent,
            user_id=user_id,
        )

        device_authorization_out.additional_properties = d
        return device_authorization_out

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
