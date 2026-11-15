# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed self-service API document
# (https://id.kleora.eu/account/v1/openapi.json). `kleora.account` wraps this tree; nothing outside the
# package imports it.
from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="SessionOut")


@_attrs_define
class SessionOut:
    """§Sessions, member for member. Not `tenant_id` and not `client_ids`.

    Attributes:
        amr (list[str]):
        created_at (datetime.datetime):
        current (bool):
        expires_at (datetime.datetime):
        id (UUID):
        ip (None | str):
        last_seen_at (datetime.datetime):
        user_agent (None | str):
    """

    amr: list[str]
    created_at: datetime.datetime
    current: bool
    expires_at: datetime.datetime
    id: UUID
    ip: None | str
    last_seen_at: datetime.datetime
    user_agent: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amr = self.amr

        created_at = self.created_at.isoformat()

        current = self.current

        expires_at = self.expires_at.isoformat()

        id = str(self.id)

        ip: None | str
        ip = self.ip

        last_seen_at = self.last_seen_at.isoformat()

        user_agent: None | str
        user_agent = self.user_agent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amr": amr,
                "created_at": created_at,
                "current": current,
                "expires_at": expires_at,
                "id": id,
                "ip": ip,
                "last_seen_at": last_seen_at,
                "user_agent": user_agent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amr = cast(list[str], d.pop("amr"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        current = d.pop("current")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        id = UUID(d.pop("id"))

        def _parse_ip(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ip = _parse_ip(d.pop("ip"))

        last_seen_at = datetime.datetime.fromisoformat(d.pop("last_seen_at"))

        def _parse_user_agent(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        user_agent = _parse_user_agent(d.pop("user_agent"))

        session_out = cls(
            amr=amr,
            created_at=created_at,
            current=current,
            expires_at=expires_at,
            id=id,
            ip=ip,
            last_seen_at=last_seen_at,
            user_agent=user_agent,
        )

        session_out.additional_properties = d
        return session_out

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
