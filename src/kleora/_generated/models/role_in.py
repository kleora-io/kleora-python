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
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RoleIn")


@_attrs_define
class RoleIn:
    """`POST E/roles` and `POST T/roles` — one body for both scopes.

    `tenant_id` is not an input field: a role's scope is decided by the endpoint
    it was created at and never changes (rbac.md §Roles). The environment path
    writes the app-scoped role, assignable in every tenant; the tenant path
    writes the one that tenant keeps to itself.

        Attributes:
            name (str):
            slug (str):
            description (str | Unset):  Default: ''.
            permissions (list[UUID] | Unset):
    """

    name: str
    slug: str
    description: str | Unset = ""
    permissions: list[UUID] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slug = self.slug

        description = self.description

        permissions: list[str] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for permissions_item_data in self.permissions:
                permissions_item = str(permissions_item_data)
                permissions.append(permissions_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "slug": slug,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        slug = d.pop("slug")

        description = d.pop("description", UNSET)

        _permissions = d.pop("permissions", UNSET)
        permissions: list[UUID] | Unset = UNSET
        if _permissions is not UNSET:
            permissions = []
            for permissions_item_data in _permissions:
                permissions_item = UUID(permissions_item_data)

                permissions.append(permissions_item)

        role_in = cls(
            name=name,
            slug=slug,
            description=description,
            permissions=permissions,
        )

        return role_in
