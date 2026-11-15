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
    """`POST …/users/{user_id}/merge` — the User being folded in and erased.

    One field, and `extra="forbid"` around it. There is deliberately nothing else
    to send: what a merge does is fixed by `social-login.md` §Merge, and an option
    (*"keep the source's authenticator"*, *"leave my own sessions alone"*) would be
    a caller choosing which half of a takeover-shaped operation to weaken. The
    winner is the path, so the row being **erased** is the one the caller had to
    name explicitly.

    A `str` rather than a `uuid.UUID`, so a malformed id is the same 404 as an id
    that names nothing (`merge.find_source`) rather than a 422 among the shape
    errors — the answer a caller who mistyped an id should get either way, and one
    that says nothing about which ids exist.

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
