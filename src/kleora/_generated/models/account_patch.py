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

T = TypeVar("T", bound="AccountPatch")


@_attrs_define
class AccountPatch:
    """`PATCH /api/v1/account` — one property, and one refusal worth explaining.

    `slug` is not a field of this schema, so it cannot be written; it is named
    in `immutable_fields` so that sending it is answered as what it is rather
    than as an unknown key. It is also the Account's tenant slug and the value
    `tenant=` carries when the console re-authorises, so renaming it would
    invalidate every bookmarked switch URL and every token in flight
    (platform-bootstrap.md §"The Account resource").

    `plan`, `status` and `tenant_id` are unknown fields on purpose:
    they are not properties a caller has any business addressing, and
    `extra="forbid"` says so.

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

        account_patch = cls(
            name=name,
        )

        return account_patch
