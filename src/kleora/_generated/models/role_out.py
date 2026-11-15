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
    from ..models.role_permission import RolePermission


T = TypeVar("T", bound="RoleOut")


@_attrs_define
class RoleOut:
    """A Role as every read of it reports it (rbac.md §API).

    Attributes:
        created_at (datetime.datetime):
        description (str):
        environment_id (UUID):
        id (UUID):
        is_system (bool):
        member_count (int):
        name (str):
        permissions (list[RolePermission]):
        scope (str):
        slug (str):
        tenant_id (None | UUID):
        updated_at (datetime.datetime):
    """

    created_at: datetime.datetime
    description: str
    environment_id: UUID
    id: UUID
    is_system: bool
    member_count: int
    name: str
    permissions: list[RolePermission]
    scope: str
    slug: str
    tenant_id: None | UUID
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        description = self.description

        environment_id = str(self.environment_id)

        id = str(self.id)

        is_system = self.is_system

        member_count = self.member_count

        name = self.name

        permissions = []
        for permissions_item_data in self.permissions:
            permissions_item = permissions_item_data.to_dict()
            permissions.append(permissions_item)

        scope = self.scope

        slug = self.slug

        tenant_id: None | str
        if isinstance(self.tenant_id, UUID):
            tenant_id = str(self.tenant_id)
        else:
            tenant_id = self.tenant_id

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
                "member_count": member_count,
                "name": name,
                "permissions": permissions,
                "scope": scope,
                "slug": slug,
                "tenant_id": tenant_id,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.role_permission import RolePermission

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        description = d.pop("description")

        environment_id = UUID(d.pop("environment_id"))

        id = UUID(d.pop("id"))

        is_system = d.pop("is_system")

        member_count = d.pop("member_count")

        name = d.pop("name")

        permissions = []
        _permissions = d.pop("permissions")
        for permissions_item_data in _permissions:
            permissions_item = RolePermission.from_dict(permissions_item_data)

            permissions.append(permissions_item)

        scope = d.pop("scope")

        slug = d.pop("slug")

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

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        role_out = cls(
            created_at=created_at,
            description=description,
            environment_id=environment_id,
            id=id,
            is_system=is_system,
            member_count=member_count,
            name=name,
            permissions=permissions,
            scope=scope,
            slug=slug,
            tenant_id=tenant_id,
            updated_at=updated_at,
        )

        role_out.additional_properties = d
        return role_out

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
