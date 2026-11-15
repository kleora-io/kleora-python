# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.composition_pages import CompositionPages


T = TypeVar("T", bound="Composition")


@_attrs_define
class Composition:
    """`composition`: which blocks each region of each page shows, and in what order.

    `pages` is a map keyed by page name.

        Attributes:
            pages (CompositionPages):
            version (int):
    """

    pages: CompositionPages
    version: int

    def to_dict(self) -> dict[str, Any]:
        pages = self.pages.to_dict()

        version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "pages": pages,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.composition_pages import CompositionPages

        d = dict(src_dict)
        pages = CompositionPages.from_dict(d.pop("pages"))

        version = d.pop("version")

        composition = cls(
            pages=pages,
            version=version,
        )

        return composition
