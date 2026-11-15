# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="WebhookEventReplayIn")


@_attrs_define
class WebhookEventReplayIn:
    """The body of `POST .../webhook-events/{webhook_event_id}/replay`.

    `endpoint_id` is required, because an event may have been delivered to more than one endpoint.

        Attributes:
            endpoint_id (UUID):
    """

    endpoint_id: UUID

    def to_dict(self) -> dict[str, Any]:
        endpoint_id = str(self.endpoint_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "endpoint_id": endpoint_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        endpoint_id = UUID(d.pop("endpoint_id"))

        webhook_event_replay_in = cls(
            endpoint_id=endpoint_id,
        )

        return webhook_event_replay_in
