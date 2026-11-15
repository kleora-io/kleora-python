# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="EmailTemplateIn")


@_attrs_define
class EmailTemplateIn:
    """`PUT …/email-templates/{kind}/{locale}` — the whole resource, at once.

    Not a merge patch, which is why it is a plain `Schema`: a subject and the
    body it belongs to are one edit (email.md §API names all three fields
    required), and a template half-written by one request and half by another
    is a message no one composed.

        Attributes:
            body_html (str):
            body_text (str):
            subject (str):
    """

    body_html: str
    body_text: str
    subject: str

    def to_dict(self) -> dict[str, Any]:
        body_html = self.body_html

        body_text = self.body_text

        subject = self.subject

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "body_html": body_html,
                "body_text": body_text,
                "subject": subject,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        body_html = d.pop("body_html")

        body_text = d.pop("body_text")

        subject = d.pop("subject")

        email_template_in = cls(
            body_html=body_html,
            body_text=body_text,
            subject=subject,
        )

        return email_template_in
