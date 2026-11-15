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

T = TypeVar("T", bound="BrandingLinks")


@_attrs_define
class BrandingLinks:
    """The three footer links. `null` means the link is not rendered.

    Attributes:
        privacy_url (None | str | Unset):
        support_url (None | str | Unset):
        terms_url (None | str | Unset):
    """

    privacy_url: None | str | Unset = UNSET
    support_url: None | str | Unset = UNSET
    terms_url: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        privacy_url: None | str | Unset
        if isinstance(self.privacy_url, Unset):
            privacy_url = UNSET
        else:
            privacy_url = self.privacy_url

        support_url: None | str | Unset
        if isinstance(self.support_url, Unset):
            support_url = UNSET
        else:
            support_url = self.support_url

        terms_url: None | str | Unset
        if isinstance(self.terms_url, Unset):
            terms_url = UNSET
        else:
            terms_url = self.terms_url

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if privacy_url is not UNSET:
            field_dict["privacy_url"] = privacy_url
        if support_url is not UNSET:
            field_dict["support_url"] = support_url
        if terms_url is not UNSET:
            field_dict["terms_url"] = terms_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_privacy_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        privacy_url = _parse_privacy_url(d.pop("privacy_url", UNSET))

        def _parse_support_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_url = _parse_support_url(d.pop("support_url", UNSET))

        def _parse_terms_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        terms_url = _parse_terms_url(d.pop("terms_url", UNSET))

        branding_links = cls(
            privacy_url=privacy_url,
            support_url=support_url,
            terms_url=terms_url,
        )

        return branding_links
