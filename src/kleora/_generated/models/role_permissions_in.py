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

T = TypeVar("T", bound="RolePermissionsIn")


@_attrs_define
class RolePermissionsIn:
    """`PUT /api/v1/roles/{role_id}/permissions` — the whole set, atomically.

    A `PUT` rather than a `PATCH` because there is no add-one or remove-one
    operation: the body is the set the role will have, and the response is the
    Role that resulted.

        Attributes:
            permissions (list[UUID]):
    """

    permissions: list[UUID]

    def to_dict(self) -> dict[str, Any]:
        permissions = []
        for permissions_item_data in self.permissions:
            permissions_item = str(permissions_item_data)
            permissions.append(permissions_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "permissions": permissions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        permissions = []
        _permissions = d.pop("permissions")
        for permissions_item_data in _permissions:
            permissions_item = UUID(permissions_item_data)

            permissions.append(permissions_item)

        role_permissions_in = cls(
            permissions=permissions,
        )

        return role_permissions_in
