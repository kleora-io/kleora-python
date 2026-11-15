# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.webhook_event_detail_out_outcome import WebhookEventDetailOutOutcome

if TYPE_CHECKING:
    from ..models.webhook_delivery_out import WebhookDeliveryOut
    from ..models.webhook_event_detail_out_payload import WebhookEventDetailOutPayload


T = TypeVar("T", bound="WebhookEventDetailOut")


@_attrs_define
class WebhookEventDetailOut:
    """The body of `GET .../webhook-events/{webhook_event_id}`: the event's envelope and every
    delivery attempt.

    `payload` is exactly the envelope every delivery sent; its `data` is `{}` for an event about a
    user who has since been erased. `deliveries` is every attempt, to every endpoint, newest first.

        Attributes:
            deliveries (list[WebhookDeliveryOut]):
            dispatched_at (datetime.datetime | None):
            environment_id (UUID):
            event_type (str):
            id (UUID):
            occurred_at (datetime.datetime):
            outcome (WebhookEventDetailOutOutcome):
            payload (WebhookEventDetailOutPayload):
            succeeded_endpoints (int):
            test (bool):
            total_endpoints (int):
    """

    deliveries: list[WebhookDeliveryOut]
    dispatched_at: datetime.datetime | None
    environment_id: UUID
    event_type: str
    id: UUID
    occurred_at: datetime.datetime
    outcome: WebhookEventDetailOutOutcome
    payload: WebhookEventDetailOutPayload
    succeeded_endpoints: int
    test: bool
    total_endpoints: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deliveries = []
        for deliveries_item_data in self.deliveries:
            deliveries_item = deliveries_item_data.to_dict()
            deliveries.append(deliveries_item)

        dispatched_at: None | str
        if isinstance(self.dispatched_at, datetime.datetime):
            dispatched_at = self.dispatched_at.isoformat()
        else:
            dispatched_at = self.dispatched_at

        environment_id = str(self.environment_id)

        event_type = self.event_type

        id = str(self.id)

        occurred_at = self.occurred_at.isoformat()

        outcome = self.outcome.value

        payload = self.payload.to_dict()

        succeeded_endpoints = self.succeeded_endpoints

        test = self.test

        total_endpoints = self.total_endpoints

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deliveries": deliveries,
                "dispatched_at": dispatched_at,
                "environment_id": environment_id,
                "event_type": event_type,
                "id": id,
                "occurred_at": occurred_at,
                "outcome": outcome,
                "payload": payload,
                "succeeded_endpoints": succeeded_endpoints,
                "test": test,
                "total_endpoints": total_endpoints,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.webhook_delivery_out import WebhookDeliveryOut
        from ..models.webhook_event_detail_out_payload import (
            WebhookEventDetailOutPayload,
        )

        d = dict(src_dict)
        deliveries = []
        _deliveries = d.pop("deliveries")
        for deliveries_item_data in _deliveries:
            deliveries_item = WebhookDeliveryOut.from_dict(deliveries_item_data)

            deliveries.append(deliveries_item)

        def _parse_dispatched_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dispatched_at_type_0 = datetime.datetime.fromisoformat(data)

                return dispatched_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        dispatched_at = _parse_dispatched_at(d.pop("dispatched_at"))

        environment_id = UUID(d.pop("environment_id"))

        event_type = d.pop("event_type")

        id = UUID(d.pop("id"))

        occurred_at = datetime.datetime.fromisoformat(d.pop("occurred_at"))

        outcome = WebhookEventDetailOutOutcome(d.pop("outcome"))

        payload = WebhookEventDetailOutPayload.from_dict(d.pop("payload"))

        succeeded_endpoints = d.pop("succeeded_endpoints")

        test = d.pop("test")

        total_endpoints = d.pop("total_endpoints")

        webhook_event_detail_out = cls(
            deliveries=deliveries,
            dispatched_at=dispatched_at,
            environment_id=environment_id,
            event_type=event_type,
            id=id,
            occurred_at=occurred_at,
            outcome=outcome,
            payload=payload,
            succeeded_endpoints=succeeded_endpoints,
            test=test,
            total_endpoints=total_endpoints,
        )

        webhook_event_detail_out.additional_properties = d
        return webhook_event_detail_out

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
