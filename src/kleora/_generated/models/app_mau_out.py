# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.environment_mau_out import EnvironmentMauOut


T = TypeVar("T", bound="AppMauOut")


@_attrs_define
class AppMauOut:
    """One App: the plan that applies to it, and its usage this period.

    `mau` is the sum over the App's production environments, which is what a `pro` allowance is
    measured against. `plan` is the plan actually applied, so a `free` App of a `scale` Account
    reads `scale`.

        Attributes:
            app_id (UUID):
            environments (list[EnvironmentMauOut]):
            mau (int):
            plan (str):
            slug (str):
            tenant_limit (int):
            tenants (int):
    """

    app_id: UUID
    environments: list[EnvironmentMauOut]
    mau: int
    plan: str
    slug: str
    tenant_limit: int
    tenants: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = str(self.app_id)

        environments = []
        for environments_item_data in self.environments:
            environments_item = environments_item_data.to_dict()
            environments.append(environments_item)

        mau = self.mau

        plan = self.plan

        slug = self.slug

        tenant_limit = self.tenant_limit

        tenants = self.tenants

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app_id": app_id,
                "environments": environments,
                "mau": mau,
                "plan": plan,
                "slug": slug,
                "tenant_limit": tenant_limit,
                "tenants": tenants,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.environment_mau_out import EnvironmentMauOut

        d = dict(src_dict)
        app_id = UUID(d.pop("app_id"))

        environments = []
        _environments = d.pop("environments")
        for environments_item_data in _environments:
            environments_item = EnvironmentMauOut.from_dict(environments_item_data)

            environments.append(environments_item)

        mau = d.pop("mau")

        plan = d.pop("plan")

        slug = d.pop("slug")

        tenant_limit = d.pop("tenant_limit")

        tenants = d.pop("tenants")

        app_mau_out = cls(
            app_id=app_id,
            environments=environments,
            mau=mau,
            plan=plan,
            slug=slug,
            tenant_limit=tenant_limit,
            tenants=tenants,
        )

        app_mau_out.additional_properties = d
        return app_mau_out

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
