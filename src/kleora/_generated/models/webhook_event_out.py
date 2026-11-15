# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.webhook_event_out_outcome import WebhookEventOutOutcome

T = TypeVar("T", bound="WebhookEventOut")


@_attrs_define
class WebhookEventOut:
    """One webhook event in a list, without its payload or delivery attempts (see
    `WebhookEventDetailOut`).

    `outcome` is the worst outcome among the endpoints the event was delivered to (failed, then
    pending, then succeeded), not the latest attempt, so a later success does not hide a failure.
    `succeeded_endpoints` and `total_endpoints` count the endpoints that currently read `succeeded`,
    and all the endpoints the event was delivered to; both are `0` before the first delivery.

        Attributes:
            dispatched_at (datetime.datetime | None):
            environment_id (UUID):
            event_type (str):
            id (UUID):
            occurred_at (datetime.datetime):
            outcome (WebhookEventOutOutcome):
            succeeded_endpoints (int):
            test (bool):
            total_endpoints (int):
    """

    dispatched_at: datetime.datetime | None
    environment_id: UUID
    event_type: str
    id: UUID
    occurred_at: datetime.datetime
    outcome: WebhookEventOutOutcome
    succeeded_endpoints: int
    test: bool
    total_endpoints: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        succeeded_endpoints = self.succeeded_endpoints

        test = self.test

        total_endpoints = self.total_endpoints

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dispatched_at": dispatched_at,
                "environment_id": environment_id,
                "event_type": event_type,
                "id": id,
                "occurred_at": occurred_at,
                "outcome": outcome,
                "succeeded_endpoints": succeeded_endpoints,
                "test": test,
                "total_endpoints": total_endpoints,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

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

        outcome = WebhookEventOutOutcome(d.pop("outcome"))

        succeeded_endpoints = d.pop("succeeded_endpoints")

        test = d.pop("test")

        total_endpoints = d.pop("total_endpoints")

        webhook_event_out = cls(
            dispatched_at=dispatched_at,
            environment_id=environment_id,
            event_type=event_type,
            id=id,
            occurred_at=occurred_at,
            outcome=outcome,
            succeeded_endpoints=succeeded_endpoints,
            test=test,
            total_endpoints=total_endpoints,
        )

        webhook_event_out.additional_properties = d
        return webhook_event_out

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
