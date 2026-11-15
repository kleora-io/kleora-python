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
    from ..models.membership_tenant import MembershipTenant


T = TypeVar("T", bound="MembershipOut")


@_attrs_define
class MembershipOut:
    """One row of `GET …/users/{user_id}/memberships`.

    Attributes:
        created_at (datetime.datetime):
        member_id (UUID):
        roles (list[str]):
        status (str):
        tenant (MembershipTenant): The Tenant a membership is in, as the membership embeds it.
    """

    created_at: datetime.datetime
    member_id: UUID
    roles: list[str]
    status: str
    tenant: MembershipTenant
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        member_id = str(self.member_id)

        roles = self.roles

        status = self.status

        tenant = self.tenant.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "member_id": member_id,
                "roles": roles,
                "status": status,
                "tenant": tenant,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.membership_tenant import MembershipTenant

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        member_id = UUID(d.pop("member_id"))

        roles = cast(list[str], d.pop("roles"))

        status = d.pop("status")

        tenant = MembershipTenant.from_dict(d.pop("tenant"))

        membership_out = cls(
            created_at=created_at,
            member_id=member_id,
            roles=roles,
            status=status,
            tenant=tenant,
        )

        membership_out.additional_properties = d
        return membership_out

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
