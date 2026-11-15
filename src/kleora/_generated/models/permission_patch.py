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

T = TypeVar("T", bound="PermissionPatch")


@_attrs_define
class PermissionPatch:
    """The body of `PATCH /api/v1/permissions/{permission_id}`: the description, and nothing else.

    `name` cannot be changed: sending it is refused as immutable.

        Attributes:
            description (str | Unset):
    """

    description: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        permission_patch = cls(
            description=description,
        )

        return permission_patch
