# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.email_template_out_kind import EmailTemplateOutKind
from ..models.email_template_out_locale import EmailTemplateOutLocale

T = TypeVar("T", bound="EmailTemplateOut")


@_attrs_define
class EmailTemplateOut:
    """One `(kind, locale)` row, with its source rather than its rendering.

    `is_default` is what the console's "reset" action keys off: true while the
    row is byte-for-byte the shipped file, false from the first edit.

        Attributes:
            body_html (str):
            body_text (str):
            is_default (bool):
            kind (EmailTemplateOutKind):
            locale (EmailTemplateOutLocale):
            subject (str):
            updated_at (datetime.datetime):
    """

    body_html: str
    body_text: str
    is_default: bool
    kind: EmailTemplateOutKind
    locale: EmailTemplateOutLocale
    subject: str
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body_html = self.body_html

        body_text = self.body_text

        is_default = self.is_default

        kind = self.kind.value

        locale = self.locale.value

        subject = self.subject

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body_html": body_html,
                "body_text": body_text,
                "is_default": is_default,
                "kind": kind,
                "locale": locale,
                "subject": subject,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        body_html = d.pop("body_html")

        body_text = d.pop("body_text")

        is_default = d.pop("is_default")

        kind = EmailTemplateOutKind(d.pop("kind"))

        locale = EmailTemplateOutLocale(d.pop("locale"))

        subject = d.pop("subject")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        email_template_out = cls(
            body_html=body_html,
            body_text=body_text,
            is_default=is_default,
            kind=kind,
            locale=locale,
            subject=subject,
            updated_at=updated_at,
        )

        email_template_out.additional_properties = d
        return email_template_out

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
