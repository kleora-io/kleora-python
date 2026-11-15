# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.branding_colors import BrandingColors
    from ..models.branding_links import BrandingLinks
    from ..models.branding_out_background import BrandingOutBackground
    from ..models.branding_out_icons import BrandingOutIcons
    from ..models.branding_out_layout import BrandingOutLayout
    from ..models.branding_out_texts import BrandingOutTexts
    from ..models.composition import Composition


T = TypeVar("T", bound="BrandingOut")


@_attrs_define
class BrandingOut:
    """The stored record, plus when it last changed.

    `updated_at` is the Environment's, which is what the compiled-CSS cache key
    is built from (branding.md §Behaviour) — a console that has just saved can
    compare it and know whether the copy it is holding is the stored one.

    `background` and `layout` widen to free-form objects on the way out, and
    only here. A stored `{"kind": "solid"}` has to read back as
    `{"kind": "solid"}`, and a stored `{"kind": "split"}` as `{"kind": "split"}`
    — branding.md test 1 asks for the default record byte for byte after
    normalisation, and a `PUT` of the members a typed model would emit beside
    them (`from: null`, `side: null`, …) is a 422. The alternative, a
    serialiser that drops them, collapses the whole schema to a bare object in
    the OpenAPI document (django-ninja generates the response schema from the
    serialiser's return type), which would lose the *input* declaration too.
    So the input is typed, where the per-`kind` key rule is enforced, and the
    output says "object".

        Attributes:
            background (BrandingOutBackground):
            color_scheme (str):
            colors (BrandingColors): The palette: seven required six-digit hex entries, and three optional ones.

                `border` is the colour of every control's border: inputs, secondary and
                quiet buttons, the strength meter's segments. `null`, or left out, borders
                them in `muted`, which is how every page rendered before the key existed
                (branding.md §Validation). It is optional because it was added after
                2026-09-18, and a key added since then never turns an existing client's
                unchanged `PUT` into a `422`. `GET` always carries it.

                `on_background` and `success` are the same shape: each is `null` by
                default, each names the colour it falls back to, and a record that says
                nothing about either renders exactly as it did before that key existed.
            colors_dark (BrandingColors | None):
            composition (Composition | None):
            custom_css (str):
            favicon_url (None | str):
            font (str):
            icons (BrandingOutIcons):
            layout (BrandingOutLayout):
            links (BrandingLinks): The three footer links. `null` means the link is not rendered.
            logo_url (None | str):
            radius (str):
            sandbox_marker (str):
            show_powered_by (bool):
            texts (BrandingOutTexts):
            updated_at (datetime.datetime):
    """

    background: BrandingOutBackground
    color_scheme: str
    colors: BrandingColors
    colors_dark: BrandingColors | None
    composition: Composition | None
    custom_css: str
    favicon_url: None | str
    font: str
    icons: BrandingOutIcons
    layout: BrandingOutLayout
    links: BrandingLinks
    logo_url: None | str
    radius: str
    sandbox_marker: str
    show_powered_by: bool
    texts: BrandingOutTexts
    updated_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        from ..models.branding_colors import BrandingColors
        from ..models.composition import Composition

        background = self.background.to_dict()

        color_scheme = self.color_scheme

        colors = self.colors.to_dict()

        colors_dark: dict[str, Any] | None
        if isinstance(self.colors_dark, BrandingColors):
            colors_dark = self.colors_dark.to_dict()
        else:
            colors_dark = self.colors_dark

        composition: dict[str, Any] | None
        if isinstance(self.composition, Composition):
            composition = self.composition.to_dict()
        else:
            composition = self.composition

        custom_css = self.custom_css

        favicon_url: None | str
        favicon_url = self.favicon_url

        font = self.font

        icons = self.icons.to_dict()

        layout = self.layout.to_dict()

        links = self.links.to_dict()

        logo_url: None | str
        logo_url = self.logo_url

        radius = self.radius

        sandbox_marker = self.sandbox_marker

        show_powered_by = self.show_powered_by

        texts = self.texts.to_dict()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "background": background,
                "color_scheme": color_scheme,
                "colors": colors,
                "colors_dark": colors_dark,
                "composition": composition,
                "custom_css": custom_css,
                "favicon_url": favicon_url,
                "font": font,
                "icons": icons,
                "layout": layout,
                "links": links,
                "logo_url": logo_url,
                "radius": radius,
                "sandbox_marker": sandbox_marker,
                "show_powered_by": show_powered_by,
                "texts": texts,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.branding_colors import BrandingColors
        from ..models.branding_links import BrandingLinks
        from ..models.branding_out_background import BrandingOutBackground
        from ..models.branding_out_icons import BrandingOutIcons
        from ..models.branding_out_layout import BrandingOutLayout
        from ..models.branding_out_texts import BrandingOutTexts
        from ..models.composition import Composition

        d = dict(src_dict)
        background = BrandingOutBackground.from_dict(d.pop("background"))

        color_scheme = d.pop("color_scheme")

        colors = BrandingColors.from_dict(d.pop("colors"))

        def _parse_colors_dark(data: object) -> BrandingColors | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                colors_dark_type_0 = BrandingColors.from_dict(data)

                return colors_dark_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BrandingColors | None, data)

        colors_dark = _parse_colors_dark(d.pop("colors_dark"))

        def _parse_composition(data: object) -> Composition | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                composition_type_0 = Composition.from_dict(data)

                return composition_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Composition | None, data)

        composition = _parse_composition(d.pop("composition"))

        custom_css = d.pop("custom_css")

        def _parse_favicon_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        favicon_url = _parse_favicon_url(d.pop("favicon_url"))

        font = d.pop("font")

        icons = BrandingOutIcons.from_dict(d.pop("icons"))

        layout = BrandingOutLayout.from_dict(d.pop("layout"))

        links = BrandingLinks.from_dict(d.pop("links"))

        def _parse_logo_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        logo_url = _parse_logo_url(d.pop("logo_url"))

        radius = d.pop("radius")

        sandbox_marker = d.pop("sandbox_marker")

        show_powered_by = d.pop("show_powered_by")

        texts = BrandingOutTexts.from_dict(d.pop("texts"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        branding_out = cls(
            background=background,
            color_scheme=color_scheme,
            colors=colors,
            colors_dark=colors_dark,
            composition=composition,
            custom_css=custom_css,
            favicon_url=favicon_url,
            font=font,
            icons=icons,
            layout=layout,
            links=links,
            logo_url=logo_url,
            radius=radius,
            sandbox_marker=sandbox_marker,
            show_powered_by=show_powered_by,
            texts=texts,
            updated_at=updated_at,
        )

        return branding_out
