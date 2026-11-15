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

T = TypeVar("T", bound="BrandingColors")


@_attrs_define
class BrandingColors:
    """The palette: seven required six-digit hex entries, and three optional ones.

    `border` is the colour of every control's border: inputs, secondary and
    quiet buttons, the strength meter's segments. `null`, or left out, borders
    them in `muted`, which is how every page rendered before the key existed
    (branding.md §Validation). It is optional because it was added after
    2026-09-18, and a key added since then never turns an existing client's
    unchanged `PUT` into a `422`. `GET` always carries it.

    `on_background` and `success` are the same shape: each is `null` by
    default, each names the colour it falls back to, and a record that says
    nothing about either renders exactly as it did before that key existed.

        Attributes:
            background (str):
            error (str):
            muted (str):
            on_primary (str):
            primary (str):
            surface (str):
            text (str):
            border (None | str | Unset):
            on_background (None | str | Unset):
            success (None | str | Unset):
    """

    background: str
    error: str
    muted: str
    on_primary: str
    primary: str
    surface: str
    text: str
    border: None | str | Unset = UNSET
    on_background: None | str | Unset = UNSET
    success: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        background = self.background

        error = self.error

        muted = self.muted

        on_primary = self.on_primary

        primary = self.primary

        surface = self.surface

        text = self.text

        border: None | str | Unset
        if isinstance(self.border, Unset):
            border = UNSET
        else:
            border = self.border

        on_background: None | str | Unset
        if isinstance(self.on_background, Unset):
            on_background = UNSET
        else:
            on_background = self.on_background

        success: None | str | Unset
        if isinstance(self.success, Unset):
            success = UNSET
        else:
            success = self.success

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "background": background,
                "error": error,
                "muted": muted,
                "on_primary": on_primary,
                "primary": primary,
                "surface": surface,
                "text": text,
            }
        )
        if border is not UNSET:
            field_dict["border"] = border
        if on_background is not UNSET:
            field_dict["on_background"] = on_background
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        background = d.pop("background")

        error = d.pop("error")

        muted = d.pop("muted")

        on_primary = d.pop("on_primary")

        primary = d.pop("primary")

        surface = d.pop("surface")

        text = d.pop("text")

        def _parse_border(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        border = _parse_border(d.pop("border", UNSET))

        def _parse_on_background(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        on_background = _parse_on_background(d.pop("on_background", UNSET))

        def _parse_success(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        success = _parse_success(d.pop("success", UNSET))

        branding_colors = cls(
            background=background,
            error=error,
            muted=muted,
            on_primary=on_primary,
            primary=primary,
            surface=surface,
            text=text,
            border=border,
            on_background=on_background,
            success=success,
        )

        return branding_colors
