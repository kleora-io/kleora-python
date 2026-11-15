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
    """`POST /api/v1/environments/{environment_id}/webhook-endpoints`.

    `event_types` defaults to empty — webhooks.md §"Volume, and why
    subscription is explicit": "a new endpoint starts subscribed to nothing".
    There is no "all events" value this field accepts; every entry is checked
    against `apps.webhooks.catalogue.EVENT_TYPES` by the resource, which
    answers 422 `invalid-event-type` rather than `validation-error` for one
    that is not — a slug this schema cannot produce, the same reason
    `ApiKeyIn.scopes`'s catalogue check is not here either.

    `extra="forbid"`: `id`, `secret`, `enabled`, `disabled_at`,
    `disabled_reason`, `environment_id` are 422 as unknown fields. A new
    endpoint is always `enabled: true`; there is no way to create one disabled.

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
