# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="PermissionOut")


@_attrs_define
class PermissionOut:
    """A Permission as every read of it reports it.

    Attributes:
        created_at (datetime.datetime):
        description (str):
        environment_id (UUID):
        id (UUID):
        is_system (bool):
        name (str):
        updated_at (datetime.datetime):
    """

    created_at: datetime.datetime
    description: str
    environment_id: UUID
    id: UUID
    is_system: bool
    name: str
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        description = self.description

        environment_id = str(self.environment_id)

        id = str(self.id)

        is_system = self.is_system

        name = self.name

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "description": description,
                "environment_id": environment_id,
                "id": id,
                "is_system": is_system,
                "name": name,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        description = d.pop("description")

        environment_id = UUID(d.pop("environment_id"))

        id = UUID(d.pop("id"))

        is_system = d.pop("is_system")

        name = d.pop("name")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        permission_out = cls(
            created_at=created_at,
            description=description,
            environment_id=environment_id,
            id=id,
            is_system=is_system,
            name=name,
            updated_at=updated_at,
        )

        permission_out.additional_properties = d
        return permission_out

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
