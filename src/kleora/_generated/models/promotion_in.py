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

T = TypeVar("T", bound="PromotionIn")


@_attrs_define
class PromotionIn:
    """`POST /api/v1/environments/{environment_id}/promote`.

    One field, defaulting to false, and `extra="forbid"` so a caller who
    mistyped it is told rather than silently promoted.

        Attributes:
            dry_run (bool | Unset):  Default: False.
    """

    dry_run: bool | Unset = False

    def to_dict(self) -> dict[str, Any]:
        dry_run = self.dry_run

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        dry_run = d.pop("dry_run", UNSET)

        promotion_in = cls(
            dry_run=dry_run,
        )

        return promotion_in
