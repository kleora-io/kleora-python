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

T = TypeVar("T", bound="WebhookTestOut")


@_attrs_define
class WebhookTestOut:
    """The `202` of a test send: the `WebhookEvent` it wrote, not the endpoint.

    Attributes:
        created_at (datetime.datetime):
        event_id (UUID):
        event_type (str):
        test (bool):
    """

    created_at: datetime.datetime
    event_id: UUID
    event_type: str
    test: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        event_id = str(self.event_id)

        event_type = self.event_type

        test = self.test

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "event_id": event_id,
                "event_type": event_type,
                "test": test,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        event_id = UUID(d.pop("event_id"))

        event_type = d.pop("event_type")

        test = d.pop("test")

        webhook_test_out = cls(
            created_at=created_at,
            event_id=event_id,
            event_type=event_type,
            test=test,
        )

        webhook_test_out.additional_properties = d
        return webhook_test_out

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
