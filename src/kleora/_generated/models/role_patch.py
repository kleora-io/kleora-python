# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RolePatch")


@_attrs_define
class RolePatch:
    """`PATCH /api/v1/roles/{role_id}` — `name` and `description`.

    `slug` is named in `immutable_fields`: it is what a token's `roles` array
    carries, so moving it would change what every deployed integration reads
    while the role's identity stayed the same (rbac.md §Roles). `permissions`
    has its own `PUT`, and `scope`, `tenant_id`, `is_system` and `member_count`
    are unknown fields — the first two are decided at creation, the third is
    ours, and the last is a projection.

        Attributes:
            description (str | Unset):
            name (str | Unset):
    """

    description: str | Unset = UNSET
    name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        role_patch = cls(
            description=description,
            name=name,
        )

        return role_patch
