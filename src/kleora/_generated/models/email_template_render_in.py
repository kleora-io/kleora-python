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

from ..models.email_template_render_in_samples import EmailTemplateRenderInSamples
from ..types import UNSET, Unset

T = TypeVar("T", bound="EmailTemplateRenderIn")


@_attrs_define
class EmailTemplateRenderIn:
    """The optional body of `POST …/email-templates/{kind}/{locale}/render`.

    Every field is optional and each one that is present replaces that column
    of the stored row for this render alone: a console that has edited only the
    HTML previews its draft HTML against the saved subject without having to
    echo back what it did not touch, and a `POST` with no body at all previews
    the stored row.

    `samples` picks the set email.md §Variables fixes — `all`, or
    `without_optional` with the two optional variables empty, which is the
    other rendering of a template whose only logic is `{% if support_url %}`.

        Attributes:
            body_html (None | str | Unset):
            body_text (None | str | Unset):
            samples (EmailTemplateRenderInSamples | Unset):  Default: EmailTemplateRenderInSamples.ALL.
            subject (None | str | Unset):
    """

    body_html: None | str | Unset = UNSET
    body_text: None | str | Unset = UNSET
    samples: EmailTemplateRenderInSamples | Unset = EmailTemplateRenderInSamples.ALL
    subject: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        body_html: None | str | Unset
        if isinstance(self.body_html, Unset):
            body_html = UNSET
        else:
            body_html = self.body_html

        body_text: None | str | Unset
        if isinstance(self.body_text, Unset):
            body_text = UNSET
        else:
            body_text = self.body_text

        samples: str | Unset = UNSET
        if not isinstance(self.samples, Unset):
            samples = self.samples.value

        subject: None | str | Unset
        if isinstance(self.subject, Unset):
            subject = UNSET
        else:
            subject = self.subject

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if body_html is not UNSET:
            field_dict["body_html"] = body_html
        if body_text is not UNSET:
            field_dict["body_text"] = body_text
        if samples is not UNSET:
            field_dict["samples"] = samples
        if subject is not UNSET:
            field_dict["subject"] = subject

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_body_html(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        body_html = _parse_body_html(d.pop("body_html", UNSET))

        def _parse_body_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        body_text = _parse_body_text(d.pop("body_text", UNSET))

        _samples = d.pop("samples", UNSET)
        samples: EmailTemplateRenderInSamples | Unset
        if isinstance(_samples, Unset):
            samples = UNSET
        else:
            samples = EmailTemplateRenderInSamples(_samples)

        def _parse_subject(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subject = _parse_subject(d.pop("subject", UNSET))

        email_template_render_in = cls(
            body_html=body_html,
            body_text=body_text,
            samples=samples,
            subject=subject,
        )

        return email_template_render_in
