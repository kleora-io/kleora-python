# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.member_role import MemberRole
    from ..models.member_user import MemberUser


T = TypeVar("T", bound="MemberOut")


@_attrs_define
class MemberOut:
    """A Member as every read of it reports it.

    Attributes:
        created_at (datetime.datetime):
        id (UUID):
        roles (list[MemberRole]):
        status (str):
        tenant_id (UUID):
        updated_at (datetime.datetime):
        user (MemberUser): The User a Member is of, as the Member resource embeds it.
    """

    created_at: datetime.datetime
    id: UUID
    roles: list[MemberRole]
    status: str
    tenant_id: UUID
    updated_at: datetime.datetime
    user: MemberUser
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = str(self.id)

        roles = []
        for roles_item_data in self.roles:
            roles_item = roles_item_data.to_dict()
            roles.append(roles_item)

        status = self.status

        tenant_id = str(self.tenant_id)

        updated_at = self.updated_at.isoformat()

        user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "roles": roles,
                "status": status,
                "tenant_id": tenant_id,
                "updated_at": updated_at,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.member_role import MemberRole
        from ..models.member_user import MemberUser

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = UUID(d.pop("id"))

        roles = []
        _roles = d.pop("roles")
        for roles_item_data in _roles:
            roles_item = MemberRole.from_dict(roles_item_data)

            roles.append(roles_item)

        status = d.pop("status")

        tenant_id = UUID(d.pop("tenant_id"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        user = MemberUser.from_dict(d.pop("user"))

        member_out = cls(
            created_at=created_at,
            id=id,
            roles=roles,
            status=status,
            tenant_id=tenant_id,
            updated_at=updated_at,
            user=user,
        )

        member_out.additional_properties = d
        return member_out

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
