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
    from ..models.tenant_out_metadata import TenantOutMetadata


T = TypeVar("T", bound="TenantOut")


@_attrs_define
class TenantOut:
    """A tenant.

    Attributes:
        belongs_to_another_account (bool):
        created_at (datetime.datetime):
        environment_id (UUID):
        id (UUID):
        is_default (bool):
        member_count (int):
        metadata (TenantOutMetadata):
        name (str):
        slug (str):
        status (str):
        updated_at (datetime.datetime):
    """

    belongs_to_another_account: bool
    created_at: datetime.datetime
    environment_id: UUID
    id: UUID
    is_default: bool
    member_count: int
    metadata: TenantOutMetadata
    name: str
    slug: str
    status: str
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        belongs_to_another_account = self.belongs_to_another_account

        created_at = self.created_at.isoformat()

        environment_id = str(self.environment_id)

        id = str(self.id)

        is_default = self.is_default

        member_count = self.member_count

        metadata = self.metadata.to_dict()

        name = self.name

        slug = self.slug

        status = self.status

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "belongs_to_another_account": belongs_to_another_account,
                "created_at": created_at,
                "environment_id": environment_id,
                "id": id,
                "is_default": is_default,
                "member_count": member_count,
                "metadata": metadata,
                "name": name,
                "slug": slug,
                "status": status,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.tenant_out_metadata import TenantOutMetadata

        d = dict(src_dict)
        belongs_to_another_account = d.pop("belongs_to_another_account")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        environment_id = UUID(d.pop("environment_id"))

        id = UUID(d.pop("id"))

        is_default = d.pop("is_default")

        member_count = d.pop("member_count")

        metadata = TenantOutMetadata.from_dict(d.pop("metadata"))

        name = d.pop("name")

        slug = d.pop("slug")

        status = d.pop("status")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        tenant_out = cls(
            belongs_to_another_account=belongs_to_another_account,
            created_at=created_at,
            environment_id=environment_id,
            id=id,
            is_default=is_default,
            member_count=member_count,
            metadata=metadata,
            name=name,
            slug=slug,
            status=status,
            updated_at=updated_at,
        )

        tenant_out.additional_properties = d
        return tenant_out

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
