# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="PlanLimitsOut")


@_attrs_define
class PlanLimitsOut:
    """The limits a plan sets.

    `tenant_limit` is the limit that applies to this App now, including any override.

        Attributes:
            audit_retention_days (int):
            tenant_limit (int):
            webhook_retention_days (int):
    """

    audit_retention_days: int
    tenant_limit: int
    webhook_retention_days: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audit_retention_days = self.audit_retention_days

        tenant_limit = self.tenant_limit

        webhook_retention_days = self.webhook_retention_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "audit_retention_days": audit_retention_days,
                "tenant_limit": tenant_limit,
                "webhook_retention_days": webhook_retention_days,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        audit_retention_days = d.pop("audit_retention_days")

        tenant_limit = d.pop("tenant_limit")

        webhook_retention_days = d.pop("webhook_retention_days")

        plan_limits_out = cls(
            audit_retention_days=audit_retention_days,
            tenant_limit=tenant_limit,
            webhook_retention_days=webhook_retention_days,
        )

        plan_limits_out.additional_properties = d
        return plan_limits_out

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
