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

T = TypeVar("T", bound="UserMergeIn")


@_attrs_define
class UserMergeIn:
    """The body of `POST .../users/{user_id}/merge`: the user to merge into this one. That user is
    erased.

    There are no options. A malformed id is `404`, like an id that names no user.

        Attributes:
            source_id (str):
    """

    source_id: str

    def to_dict(self) -> dict[str, Any]:
        source_id = self.source_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "source_id": source_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        source_id = d.pop("source_id")

        user_merge_in = cls(
            source_id=source_id,
        )

        return user_merge_in
