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

T = TypeVar("T", bound="ExportSession")


@_attrs_define
class ExportSession:
    """One Session in the export, with the clients it minted tokens for.

    Attributes:
        client_ids (list[str]):
        created_at (datetime.datetime):
        expires_at (datetime.datetime):
        id (UUID):
        ip (str):
        last_seen_at (datetime.datetime):
        revoked_at (datetime.datetime | None):
        user_agent (str):
    """

    client_ids: list[str]
    created_at: datetime.datetime
    expires_at: datetime.datetime
    id: UUID
    ip: str
    last_seen_at: datetime.datetime
    revoked_at: datetime.datetime | None
    user_agent: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_ids = self.client_ids

        created_at = self.created_at.isoformat()

        expires_at = self.expires_at.isoformat()

        id = str(self.id)

        ip = self.ip

        last_seen_at = self.last_seen_at.isoformat()

        revoked_at: None | str
        if isinstance(self.revoked_at, datetime.datetime):
            revoked_at = self.revoked_at.isoformat()
        else:
            revoked_at = self.revoked_at

        user_agent = self.user_agent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "client_ids": client_ids,
                "created_at": created_at,
                "expires_at": expires_at,
                "id": id,
                "ip": ip,
                "last_seen_at": last_seen_at,
                "revoked_at": revoked_at,
                "user_agent": user_agent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        client_ids = cast(list[str], d.pop("client_ids"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        id = UUID(d.pop("id"))

        ip = d.pop("ip")

        last_seen_at = datetime.datetime.fromisoformat(d.pop("last_seen_at"))

        def _parse_revoked_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                revoked_at_type_0 = datetime.datetime.fromisoformat(data)

                return revoked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        revoked_at = _parse_revoked_at(d.pop("revoked_at"))

        user_agent = d.pop("user_agent")

        export_session = cls(
            client_ids=client_ids,
            created_at=created_at,
            expires_at=expires_at,
            id=id,
            ip=ip,
            last_seen_at=last_seen_at,
            revoked_at=revoked_at,
            user_agent=user_agent,
        )

        export_session.additional_properties = d
        return export_session

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
