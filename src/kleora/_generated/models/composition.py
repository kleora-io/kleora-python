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
    """`composition`: the layout document a record may carry.

    Typed rather than the free-form object `icons` is, because the block names
    *are* the vocabulary a customer writes against and the generated clients
    should name them (ADR 0003). `pages` is a map rather than a model per page
    so that a later phase's page arrives without a schema edit; which pages and
    regions exist is a validation rule, in `branding_validation` against
    `COMPOSITION_REGIONS`, exactly as `layout`'s per-`kind` keys are.

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
