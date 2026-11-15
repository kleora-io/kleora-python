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
    from ..models.app_environment import AppEnvironment


T = TypeVar("T", bound="AppOut")


@_attrs_define
class AppOut:
    """An App.

    Attributes:
        account_id (UUID):
        created_at (datetime.datetime):
        environments (list[AppEnvironment]):
        id (UUID):
        is_platform (bool):
        name (str):
        slug (str):
        updated_at (datetime.datetime):
    """

    account_id: UUID
    created_at: datetime.datetime
    environments: list[AppEnvironment]
    id: UUID
    is_platform: bool
    name: str
    slug: str
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = str(self.account_id)

        created_at = self.created_at.isoformat()

        environments = []
        for environments_item_data in self.environments:
            environments_item = environments_item_data.to_dict()
            environments.append(environments_item)

        id = str(self.id)

        is_platform = self.is_platform

        name = self.name

        slug = self.slug

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "created_at": created_at,
                "environments": environments,
                "id": id,
                "is_platform": is_platform,
                "name": name,
                "slug": slug,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.app_environment import AppEnvironment

        d = dict(src_dict)
        account_id = UUID(d.pop("account_id"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        environments = []
        _environments = d.pop("environments")
        for environments_item_data in _environments:
            environments_item = AppEnvironment.from_dict(environments_item_data)

            environments.append(environments_item)

        id = UUID(d.pop("id"))

        is_platform = d.pop("is_platform")

        name = d.pop("name")

        slug = d.pop("slug")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        app_out = cls(
            account_id=account_id,
            created_at=created_at,
            environments=environments,
            id=id,
            is_platform=is_platform,
            name=name,
            slug=slug,
            updated_at=updated_at,
        )

        app_out.additional_properties = d
        return app_out

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
