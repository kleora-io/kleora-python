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

from ..models.webhook_delivery_out_outcome import WebhookDeliveryOutOutcome

T = TypeVar("T", bound="WebhookDeliveryOut")


@_attrs_define
class WebhookDeliveryOut:
    """One `WebhookDelivery` row — one attempt, to one endpoint.

    `endpoint_id` is nullable exactly as the column is: `SET_NULL` on the
    endpoint's own deletion means an attempt's log outlives the row it was
    aimed at (webhooks.md §"Failure modes": "the log survives its retention").
    `response_body` is already truncated, by `apps.webhooks.transport` at the
    point it was read — this reports it as stored, not a second truncation.

        Attributes:
            attempt (int):
            created_at (datetime.datetime):
            duration_ms (int | None):
            endpoint_id (None | UUID):
            error (str):
            http_status (int | None):
            id (UUID):
            next_attempt_at (datetime.datetime | None):
            outcome (WebhookDeliveryOutOutcome):
            response_body (str):
            status (str):
    """

    attempt: int
    created_at: datetime.datetime
    duration_ms: int | None
    endpoint_id: None | UUID
    error: str
    http_status: int | None
    id: UUID
    next_attempt_at: datetime.datetime | None
    outcome: WebhookDeliveryOutOutcome
    response_body: str
    status: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attempt = self.attempt

        created_at = self.created_at.isoformat()

        duration_ms: int | None
        duration_ms = self.duration_ms

        endpoint_id: None | str
        if isinstance(self.endpoint_id, UUID):
            endpoint_id = str(self.endpoint_id)
        else:
            endpoint_id = self.endpoint_id

        error = self.error

        http_status: int | None
        http_status = self.http_status

        id = str(self.id)

        next_attempt_at: None | str
        if isinstance(self.next_attempt_at, datetime.datetime):
            next_attempt_at = self.next_attempt_at.isoformat()
        else:
            next_attempt_at = self.next_attempt_at

        outcome = self.outcome.value

        response_body = self.response_body

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attempt": attempt,
                "created_at": created_at,
                "duration_ms": duration_ms,
                "endpoint_id": endpoint_id,
                "error": error,
                "http_status": http_status,
                "id": id,
                "next_attempt_at": next_attempt_at,
                "outcome": outcome,
                "response_body": response_body,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        attempt = d.pop("attempt")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_duration_ms(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        duration_ms = _parse_duration_ms(d.pop("duration_ms"))

        def _parse_endpoint_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                endpoint_id_type_0 = UUID(data)

                return endpoint_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        endpoint_id = _parse_endpoint_id(d.pop("endpoint_id"))

        error = d.pop("error")

        def _parse_http_status(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        http_status = _parse_http_status(d.pop("http_status"))

        id = UUID(d.pop("id"))

        def _parse_next_attempt_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_attempt_at_type_0 = datetime.datetime.fromisoformat(data)

                return next_attempt_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        next_attempt_at = _parse_next_attempt_at(d.pop("next_attempt_at"))

        outcome = WebhookDeliveryOutOutcome(d.pop("outcome"))

        response_body = d.pop("response_body")

        status = d.pop("status")

        webhook_delivery_out = cls(
            attempt=attempt,
            created_at=created_at,
            duration_ms=duration_ms,
            endpoint_id=endpoint_id,
            error=error,
            http_status=http_status,
            id=id,
            next_attempt_at=next_attempt_at,
            outcome=outcome,
            response_body=response_body,
            status=status,
        )

        webhook_delivery_out.additional_properties = d
        return webhook_delivery_out

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
