# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="BrandingLayout")


@_attrs_define
class BrandingLayout:
    """One of the two `layout.kind` shapes.

    Declared as one model with optional members, mirroring `BrandingBackground`
    for the same reason — the union would put two schemas in the document for
    a three-key object. Which keys each `kind` may carry is a validation rule,
    enforced in `branding_validation` and stated in `branding.md` §Validation:
    a `centered` layout carrying `side` is a 422 naming `layout.side` as an
    unknown field, not a type error.

        Attributes:
            kind (str):
            form (None | str | Unset):
            panel (None | str | Unset):
            side (None | str | Unset):
    """

    kind: str
    form: None | str | Unset = UNSET
    panel: None | str | Unset = UNSET
    side: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        form: None | str | Unset
        if isinstance(self.form, Unset):
            form = UNSET
        else:
            form = self.form

        panel: None | str | Unset
        if isinstance(self.panel, Unset):
            panel = UNSET
        else:
            panel = self.panel

        side: None | str | Unset
        if isinstance(self.side, Unset):
            side = UNSET
        else:
            side = self.side

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
            }
        )
        if form is not UNSET:
            field_dict["form"] = form
        if panel is not UNSET:
            field_dict["panel"] = panel
        if side is not UNSET:
            field_dict["side"] = side

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = d.pop("kind")

        def _parse_form(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        form = _parse_form(d.pop("form", UNSET))

        def _parse_panel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        panel = _parse_panel(d.pop("panel", UNSET))

        def _parse_side(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        side = _parse_side(d.pop("side", UNSET))

        branding_layout = cls(
            kind=kind,
            form=form,
            panel=panel,
            side=side,
        )

        return branding_layout
