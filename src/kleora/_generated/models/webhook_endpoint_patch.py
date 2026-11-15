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

T = TypeVar("T", bound="WebhookEndpointPatch")


@_attrs_define
class WebhookEndpointPatch:
    """The body of `PATCH
    /api/v1/environments/{environment_id}/webhook-endpoints/{webhook_endpoint_id}`.

    `event_types` is replaced whole; `[]` unsubscribes from everything, and `null` is not accepted.

    `enabled: false` disables the endpoint and is audited as `webhook_endpoint.disabled`. `enabled:
    true` re-enables it, whether it was disabled by a person or automatically after repeated
    failures, and clears `disabled_at` and `disabled_reason`.

        Attributes:
            enabled (bool | Unset):
            event_types (list[str] | Unset):
            name (str | Unset):
            url (str | Unset):
    """

    enabled: bool | Unset = UNSET
    event_types: list[str] | Unset = UNSET
    name: str | Unset = UNSET
    url: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        event_types: list[str] | Unset = UNSET
        if not isinstance(self.event_types, Unset):
            event_types = self.event_types

        name = self.name

        url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if event_types is not UNSET:
            field_dict["event_types"] = event_types
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        event_types = cast(list[str], d.pop("event_types", UNSET))

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        webhook_endpoint_patch = cls(
            enabled=enabled,
            event_types=event_types,
            name=name,
            url=url,
        )

        return webhook_endpoint_patch
