# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.branding_background import BrandingBackground
    from ..models.branding_colors import BrandingColors
    from ..models.branding_in_icons import BrandingInIcons
    from ..models.branding_in_texts import BrandingInTexts
    from ..models.branding_layout import BrandingLayout
    from ..models.branding_links import BrandingLinks
    from ..models.composition import Composition


T = TypeVar("T", bound="BrandingIn")


@_attrs_define
class BrandingIn:
    """`PUT /api/v1/environments/{id}/branding` and `POST …/branding/preview`.

    Every top-level key that existed on 2026-09-18 is required — this is a
    whole-record replacement and branding.md says partial updates are not
    offered — and a key added since may be left out and is stored as its
    default. `extra="forbid"` is what makes an unknown key a 422 rather than a
    value silently dropped on the way to storage.

        Attributes:
            background (BrandingBackground): One of the three `background.kind` shapes.

                Declared as one model with optional members rather than as a discriminated
                union, because the union would put three schemas in the document for a
                three-key object and generated clients would name them
                `BrandingBackgroundType0`. Which keys each `kind` may carry is a validation
                rule, enforced in `branding_validation` and stated in `branding.md`
                §Validation — a `solid` background carrying `angle` is a 422 naming
                `background.angle` as an unknown field, not a type error.

                `from` is a Python keyword, so the field is `from_` with the alias the wire
                uses; `populate_by_name` keeps both readable from Python.
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
            custom_css (str):
            favicon_url (None | str):
            font (str):
            layout (BrandingLayout): One of the two `layout.kind` shapes.

                Declared as one model with optional members, mirroring `BrandingBackground`
                for the same reason — the union would put two schemas in the document for
                a three-key object. Which keys each `kind` may carry is a validation rule,
                enforced in `branding_validation` and stated in `branding.md` §Validation:
                a `centered` layout carrying `side` is a 422 naming `layout.side` as an
                unknown field, not a type error.
            links (BrandingLinks): The three footer links. `null` means the link is not rendered.
            logo_url (None | str):
            radius (str):
            show_powered_by (bool):
            texts (BrandingInTexts):
            color_scheme (str | Unset): `light`, `dark` or `auto`; left out, `light`. `auto` follows the reader's `prefers-
                color-scheme` while the page is open.
            colors_dark (BrandingColors | None | Unset): The palette rendered when the page is dark: the same keys and rules
                as `colors`. Required when `color_scheme` is `dark` or `auto`; kept, not applied, under `light`.
            composition (Composition | None | Unset): `null` (the default) renders every page in the order hosted-login.md
                §Pages gives. A document selects and orders the blocks of a covered region: v1 covers `/login`'s form region,
                whose blocks are `subtitle`, `credentials`, `actions` and `passkey`. `credentials`, `actions` and `passkey`
                appear exactly once and `credentials` comes before `actions`; `subtitle` is the one block that may be left out.
            icons (BrandingInIcons | Unset): `enabled` (default true), `button` (an icon name or null) and `panel_features`
                (up to three names). Names come from the curated set in branding.md §Icons. A non-empty `panel_features` needs a
                split layout with the brand panel.
            sandbox_marker (str | Unset): `none`, `rail` or `canvas`; left out, `none`. The sandbox's pages carry the
                console's hatch; a production environment never renders it, whatever this says.
    """

    background: BrandingBackground
    colors: BrandingColors
    custom_css: str
    favicon_url: None | str
    font: str
    layout: BrandingLayout
    links: BrandingLinks
    logo_url: None | str
    radius: str
    show_powered_by: bool
    texts: BrandingInTexts
    color_scheme: str | Unset = UNSET
    colors_dark: BrandingColors | None | Unset = UNSET
    composition: Composition | None | Unset = UNSET
    icons: BrandingInIcons | Unset = UNSET
    sandbox_marker: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.branding_colors import BrandingColors
        from ..models.composition import Composition

        background = self.background.to_dict()

        colors = self.colors.to_dict()

        custom_css = self.custom_css

        favicon_url: None | str
        favicon_url = self.favicon_url

        font = self.font

        layout = self.layout.to_dict()

        links = self.links.to_dict()

        logo_url: None | str
        logo_url = self.logo_url

        radius = self.radius

        show_powered_by = self.show_powered_by

        texts = self.texts.to_dict()

        color_scheme = self.color_scheme

        colors_dark: dict[str, Any] | None | Unset
        if isinstance(self.colors_dark, Unset):
            colors_dark = UNSET
        elif isinstance(self.colors_dark, BrandingColors):
            colors_dark = self.colors_dark.to_dict()
        else:
            colors_dark = self.colors_dark

        composition: dict[str, Any] | None | Unset
        if isinstance(self.composition, Unset):
            composition = UNSET
        elif isinstance(self.composition, Composition):
            composition = self.composition.to_dict()
        else:
            composition = self.composition

        icons: dict[str, Any] | Unset = UNSET
        if not isinstance(self.icons, Unset):
            icons = self.icons.to_dict()

        sandbox_marker = self.sandbox_marker

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "background": background,
                "colors": colors,
                "custom_css": custom_css,
                "favicon_url": favicon_url,
                "font": font,
                "layout": layout,
                "links": links,
                "logo_url": logo_url,
                "radius": radius,
                "show_powered_by": show_powered_by,
                "texts": texts,
            }
        )
        if color_scheme is not UNSET:
            field_dict["color_scheme"] = color_scheme
        if colors_dark is not UNSET:
            field_dict["colors_dark"] = colors_dark
        if composition is not UNSET:
            field_dict["composition"] = composition
        if icons is not UNSET:
            field_dict["icons"] = icons
        if sandbox_marker is not UNSET:
            field_dict["sandbox_marker"] = sandbox_marker

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.branding_background import BrandingBackground
        from ..models.branding_colors import BrandingColors
        from ..models.branding_in_icons import BrandingInIcons
        from ..models.branding_in_texts import BrandingInTexts
        from ..models.branding_layout import BrandingLayout
        from ..models.branding_links import BrandingLinks
        from ..models.composition import Composition

        d = dict(src_dict)
        background = BrandingBackground.from_dict(d.pop("background"))

        colors = BrandingColors.from_dict(d.pop("colors"))

        custom_css = d.pop("custom_css")

        def _parse_favicon_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        favicon_url = _parse_favicon_url(d.pop("favicon_url"))

        font = d.pop("font")

        layout = BrandingLayout.from_dict(d.pop("layout"))

        links = BrandingLinks.from_dict(d.pop("links"))

        def _parse_logo_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        logo_url = _parse_logo_url(d.pop("logo_url"))

        radius = d.pop("radius")

        show_powered_by = d.pop("show_powered_by")

        texts = BrandingInTexts.from_dict(d.pop("texts"))

        color_scheme = d.pop("color_scheme", UNSET)

        def _parse_colors_dark(data: object) -> BrandingColors | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                colors_dark_type_0 = BrandingColors.from_dict(data)

                return colors_dark_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BrandingColors | None | Unset, data)

        colors_dark = _parse_colors_dark(d.pop("colors_dark", UNSET))

        def _parse_composition(data: object) -> Composition | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                composition_type_0 = Composition.from_dict(data)

                return composition_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Composition | None | Unset, data)

        composition = _parse_composition(d.pop("composition", UNSET))

        _icons = d.pop("icons", UNSET)
        icons: BrandingInIcons | Unset
        if isinstance(_icons, Unset):
            icons = UNSET
        else:
            icons = BrandingInIcons.from_dict(_icons)

        sandbox_marker = d.pop("sandbox_marker", UNSET)

        branding_in = cls(
            background=background,
            colors=colors,
            custom_css=custom_css,
            favicon_url=favicon_url,
            font=font,
            layout=layout,
            links=links,
            logo_url=logo_url,
            radius=radius,
            show_powered_by=show_powered_by,
            texts=texts,
            color_scheme=color_scheme,
            colors_dark=colors_dark,
            composition=composition,
            icons=icons,
            sandbox_marker=sandbox_marker,
        )

        return branding_in
