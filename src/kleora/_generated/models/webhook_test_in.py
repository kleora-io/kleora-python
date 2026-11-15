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

T = TypeVar("T", bound="WebhookTestIn")


@_attrs_define
class WebhookTestIn:
    """`POST …/webhook-endpoints/{id}/test` — the one event type to send.

    Attributes:
        event_type (str):
    """

    event_type: str

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "event_type": event_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        event_type = d.pop("event_type")

        webhook_test_in = cls(
            event_type=event_type,
        )

        return webhook_test_in
