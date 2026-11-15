# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="EnvironmentMauOut")


@_attrs_define
class EnvironmentMauOut:
    """One environment's figures for the period.

    `mau` is always zero for a sandbox environment: sandbox usage is never counted. `tenants` is the
    count the tenant limit is applied to, per environment.

        Attributes:
            environment_id (UUID):
            kind (str):
            mau (int):
            tenants (int):
    """

    environment_id: UUID
    kind: str
    mau: int
    tenants: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        environment_id = str(self.environment_id)

        kind = self.kind

        mau = self.mau

        tenants = self.tenants

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "environment_id": environment_id,
                "kind": kind,
                "mau": mau,
                "tenants": tenants,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        environment_id = UUID(d.pop("environment_id"))

        kind = d.pop("kind")

        mau = d.pop("mau")

        tenants = d.pop("tenants")

        environment_mau_out = cls(
            environment_id=environment_id,
            kind=kind,
            mau=mau,
            tenants=tenants,
        )

        environment_mau_out.additional_properties = d
        return environment_mau_out

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
