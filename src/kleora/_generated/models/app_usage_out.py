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
    from ..models.environment_usage import EnvironmentUsage


T = TypeVar("T", bound="AppUsageOut")


@_attrs_define
class AppUsageOut:
    """One App of the Account, with the `active` User count of both its sides.

    Attributes:
        app_id (UUID):
        production (EnvironmentUsage): One environment's contribution to an App's row.
        sandbox (EnvironmentUsage): One environment's contribution to an App's row.
        slug (str):
    """

    app_id: UUID
    production: EnvironmentUsage
    sandbox: EnvironmentUsage
    slug: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = str(self.app_id)

        production = self.production.to_dict()

        sandbox = self.sandbox.to_dict()

        slug = self.slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app_id": app_id,
                "production": production,
                "sandbox": sandbox,
                "slug": slug,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.environment_usage import EnvironmentUsage

        d = dict(src_dict)
        app_id = UUID(d.pop("app_id"))

        production = EnvironmentUsage.from_dict(d.pop("production"))

        sandbox = EnvironmentUsage.from_dict(d.pop("sandbox"))

        slug = d.pop("slug")

        app_usage_out = cls(
            app_id=app_id,
            production=production,
            sandbox=sandbox,
            slug=slug,
        )

        app_usage_out.additional_properties = d
        return app_usage_out

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
