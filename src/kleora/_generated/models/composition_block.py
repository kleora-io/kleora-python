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

T = TypeVar("T", bound="CompositionBlock")


@_attrs_define
class CompositionBlock:
    """One block of a composed region: the name of a block the page renders, and nothing else. Any
    other member is `422`.

        Attributes:
            block (str):
    """

    block: str

    def to_dict(self) -> dict[str, Any]:
        block = self.block

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "block": block,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        block = d.pop("block")

        composition_block = cls(
            block=block,
        )

        return composition_block
