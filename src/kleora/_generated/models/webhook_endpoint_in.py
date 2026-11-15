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

T = TypeVar("T", bound="WebhookEndpointIn")


@_attrs_define
class WebhookEndpointIn:
    """The body of `POST /api/v1/environments/{environment_id}/webhook-endpoints`.

    `event_types` is empty by default: a new endpoint receives nothing until it subscribes. There is
    no "all events" value; an event type outside the catalogue is `422 invalid-event-type`.

    `id`, `secret`, `enabled`, `disabled_at`, `disabled_reason` and `environment_id` are refused as
    unknown fields. A new endpoint is always enabled.

        Attributes:
            name (str):
            url (str):
            event_types (list[str] | Unset):
    """

    name: str
    url: str
    event_types: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        url = self.url

        event_types: list[str] | Unset = UNSET
        if not isinstance(self.event_types, Unset):
            event_types = self.event_types

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "url": url,
            }
        )
        if event_types is not UNSET:
            field_dict["event_types"] = event_types

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        url = d.pop("url")

        event_types = cast(list[str], d.pop("event_types", UNSET))

        webhook_endpoint_in = cls(
            name=name,
            url=url,
            event_types=event_types,
        )

        return webhook_endpoint_in
