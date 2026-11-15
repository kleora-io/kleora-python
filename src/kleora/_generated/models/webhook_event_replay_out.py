# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="WebhookEventReplayOut")


@_attrs_define
class WebhookEventReplayOut:
    """The `202` of a replay: which event, to which endpoint, and when it was scheduled.

    Attributes:
        endpoint_id (UUID):
        event_id (UUID):
        replayed_at (datetime.datetime):
    """

    endpoint_id: UUID
    event_id: UUID
    replayed_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        endpoint_id = str(self.endpoint_id)

        event_id = str(self.event_id)

        replayed_at = self.replayed_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpoint_id": endpoint_id,
                "event_id": event_id,
                "replayed_at": replayed_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        endpoint_id = UUID(d.pop("endpoint_id"))

        event_id = UUID(d.pop("event_id"))

        replayed_at = datetime.datetime.fromisoformat(d.pop("replayed_at"))

        webhook_event_replay_out = cls(
            endpoint_id=endpoint_id,
            event_id=event_id,
            replayed_at=replayed_at,
        )

        webhook_event_replay_out.additional_properties = d
        return webhook_event_replay_out

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
