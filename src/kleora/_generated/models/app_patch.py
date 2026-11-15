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

T = TypeVar("T", bound="AppPatch")


@_attrs_define
class AppPatch:
    """The body of `PATCH /api/v1/apps/{app_id}`: `name`, and nothing else.

    `slug` cannot be changed, because both of the App's issuers are derived from it: sending it is
    refused as immutable. `is_platform`, `account_id` and `environments` are refused as unknown
    fields.

        Attributes:
            name (str | Unset):
    """

    name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        app_patch = cls(
            name=name,
        )

        return app_patch
