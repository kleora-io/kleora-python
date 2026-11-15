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

T = TypeVar("T", bound="AccountOut")


@_attrs_define
class AccountOut:
    """An Account as `POST /accounts` reports it.

    Attributes:
        created_at (datetime.datetime):
        id (UUID):
        name (str):
        plan (str):
        slug (str):
        status (str):
        tenant_id (None | UUID):
    """

    created_at: datetime.datetime
    id: UUID
    name: str
    plan: str
    slug: str
    status: str
    tenant_id: None | UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = str(self.id)

        name = self.name

        plan = self.plan

        slug = self.slug

        status = self.status

        tenant_id: None | str
        if isinstance(self.tenant_id, UUID):
            tenant_id = str(self.tenant_id)
        else:
            tenant_id = self.tenant_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "name": name,
                "plan": plan,
                "slug": slug,
                "status": status,
                "tenant_id": tenant_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = UUID(d.pop("id"))

        name = d.pop("name")

        plan = d.pop("plan")

        slug = d.pop("slug")

        status = d.pop("status")

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

        account_out = cls(
            created_at=created_at,
            id=id,
            name=name,
            plan=plan,
            slug=slug,
            status=status,
            tenant_id=tenant_id,
        )

        account_out.additional_properties = d
        return account_out

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
