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
    """`PATCH /api/v1/environments/{environment_id}/webhook-endpoints/{id}`.

    `event_types` is replaced whole by a merge patch, like `ClientPatch`'s URI
    arrays — `[]` unsubscribes from everything and is a valid value distinct
    from the `null` this field does not accept (it is not nullable: a
    subscription is always a list, possibly empty).

    `enabled` is a plain `bool`: `false` disables — audited as
    `webhook_endpoint.disabled` rather than the generic `.updated`
    (webhooks.md §API) — and `true` re-enables an endpoint the seven-day
    failure sweep (P6-08) or a person turned off, clearing `disabled_at`/
    `disabled_reason` on the row.

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
