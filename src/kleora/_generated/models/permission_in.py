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

T = TypeVar("T", bound="PermissionIn")


@_attrs_define
class PermissionIn:
    """The body of `POST /api/v1/environments/{environment_id}/permissions`.

    `is_system` is not an input field. A name in the reserved namespace is `422
    reserved-permission`.

        Attributes:
            name (str):
            description (str | Unset):  Default: ''.
    """

    name: str
    description: str | Unset = ""

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        permission_in = cls(
            name=name,
            description=description,
        )

        return permission_in
