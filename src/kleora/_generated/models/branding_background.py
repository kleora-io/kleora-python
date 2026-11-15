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

T = TypeVar("T", bound="BrandingBackground")


@_attrs_define
class BrandingBackground:
    """The page background: one of three `kind`s.

    Each `kind` allows only its own members; for example, `angle` on a `solid` background is `422`
    naming `background.angle` as an unknown field. `from` is a gradient's starting colour.

        Attributes:
            kind (str):
            angle (int | None | Unset):
            from_ (None | str | Unset):
            image_url (None | str | Unset):
            overlay (None | str | Unset):
            overlay_opacity (float | None | Unset):
            to (None | str | Unset):
    """

    kind: str
    angle: int | None | Unset = UNSET
    from_: None | str | Unset = UNSET
    image_url: None | str | Unset = UNSET
    overlay: None | str | Unset = UNSET
    overlay_opacity: float | None | Unset = UNSET
    to: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        angle: int | None | Unset
        if isinstance(self.angle, Unset):
            angle = UNSET
        else:
            angle = self.angle

        from_: None | str | Unset
        if isinstance(self.from_, Unset):
            from_ = UNSET
        else:
            from_ = self.from_

        image_url: None | str | Unset
        if isinstance(self.image_url, Unset):
            image_url = UNSET
        else:
            image_url = self.image_url

        overlay: None | str | Unset
        if isinstance(self.overlay, Unset):
            overlay = UNSET
        else:
            overlay = self.overlay

        overlay_opacity: float | None | Unset
        if isinstance(self.overlay_opacity, Unset):
            overlay_opacity = UNSET
        else:
            overlay_opacity = self.overlay_opacity

        to: None | str | Unset
        if isinstance(self.to, Unset):
            to = UNSET
        else:
            to = self.to

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
            }
        )
        if angle is not UNSET:
            field_dict["angle"] = angle
        if from_ is not UNSET:
            field_dict["from"] = from_
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if overlay is not UNSET:
            field_dict["overlay"] = overlay
        if overlay_opacity is not UNSET:
            field_dict["overlay_opacity"] = overlay_opacity
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = d.pop("kind")

        def _parse_angle(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        angle = _parse_angle(d.pop("angle", UNSET))

        def _parse_from_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_ = _parse_from_(d.pop("from", UNSET))

        def _parse_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_url = _parse_image_url(d.pop("image_url", UNSET))

        def _parse_overlay(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        overlay = _parse_overlay(d.pop("overlay", UNSET))

        def _parse_overlay_opacity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        overlay_opacity = _parse_overlay_opacity(d.pop("overlay_opacity", UNSET))

        def _parse_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        to = _parse_to(d.pop("to", UNSET))

        branding_background = cls(
            kind=kind,
            angle=angle,
            from_=from_,
            image_url=image_url,
            overlay=overlay,
            overlay_opacity=overlay_opacity,
            to=to,
        )

        return branding_background
