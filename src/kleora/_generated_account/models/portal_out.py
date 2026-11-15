# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed self-service API document
# (https://id.kleora.eu/account/v1/openapi.json). `kleora.account` wraps this tree; nothing outside the
# package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.portal_section import PortalSection

T = TypeVar("T", bound="PortalOut")


@_attrs_define
class PortalOut:
    """§API `GET /portal`: `{url, sections[]}`.

    "One document naming the portal URL and which sections this Environment
    offers, so a customer's own page renders the right links without hard-coding a
    path of ours or guessing at `self_deletion`."

    `url` is the portal's stable entry point, `{issuer}/account`. The `client_id`
    and `return_to` parameters §"Getting there and back" describes are the
    caller's to add — they are about where the *customer's* browser should come
    back to, which this endpoint cannot know and an SDK helper builds
    (`accountPortalUrl`, `U10-04`).

        Attributes:
            sections (list[PortalSection]):
            url (str):
    """

    sections: list[PortalSection]
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sections = []
        for sections_item_data in self.sections:
            sections_item = sections_item_data.value
            sections.append(sections_item)

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sections": sections,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        sections = []
        _sections = d.pop("sections")
        for sections_item_data in _sections:
            sections_item = PortalSection(sections_item_data)

            sections.append(sections_item)

        url = d.pop("url")

        portal_out = cls(
            sections=sections,
            url=url,
        )

        portal_out.additional_properties = d
        return portal_out

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
