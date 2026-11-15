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

T = TypeVar("T", bound="WebhookEndpointCreated")


@_attrs_define
class WebhookEndpointCreated:
    """The `201` of creation: the resource, plus the secret — always, unlike
    `ClientCreated`'s optional one, because every `WebhookEndpoint` has a
    secret from the moment it exists.

        Attributes:
            created_at (datetime.datetime):
            disabled_at (datetime.datetime | None):
            disabled_reason (str):
            enabled (bool):
            environment_id (UUID):
            event_types (list[str]):
            id (UUID):
            name (str):
            previous_secret_expires_at (datetime.datetime | None):
            secret (str):
            updated_at (datetime.datetime):
            url (str):
    """

    created_at: datetime.datetime
    disabled_at: datetime.datetime | None
    disabled_reason: str
    enabled: bool
    environment_id: UUID
    event_types: list[str]
    id: UUID
    name: str
    previous_secret_expires_at: datetime.datetime | None
    secret: str
    updated_at: datetime.datetime
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        disabled_at: None | str
        if isinstance(self.disabled_at, datetime.datetime):
            disabled_at = self.disabled_at.isoformat()
        else:
            disabled_at = self.disabled_at

        disabled_reason = self.disabled_reason

        enabled = self.enabled

        environment_id = str(self.environment_id)

        event_types = self.event_types

        id = str(self.id)

        name = self.name

        previous_secret_expires_at: None | str
        if isinstance(self.previous_secret_expires_at, datetime.datetime):
            previous_secret_expires_at = self.previous_secret_expires_at.isoformat()
        else:
            previous_secret_expires_at = self.previous_secret_expires_at

        secret = self.secret

        updated_at = self.updated_at.isoformat()

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "disabled_at": disabled_at,
                "disabled_reason": disabled_reason,
                "enabled": enabled,
                "environment_id": environment_id,
                "event_types": event_types,
                "id": id,
                "name": name,
                "previous_secret_expires_at": previous_secret_expires_at,
                "secret": secret,
                "updated_at": updated_at,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_disabled_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                disabled_at_type_0 = datetime.datetime.fromisoformat(data)

                return disabled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        disabled_at = _parse_disabled_at(d.pop("disabled_at"))

        disabled_reason = d.pop("disabled_reason")

        enabled = d.pop("enabled")

        environment_id = UUID(d.pop("environment_id"))

        event_types = cast(list[str], d.pop("event_types"))

        id = UUID(d.pop("id"))

        name = d.pop("name")

        def _parse_previous_secret_expires_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                previous_secret_expires_at_type_0 = datetime.datetime.fromisoformat(
                    data
                )

                return previous_secret_expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        previous_secret_expires_at = _parse_previous_secret_expires_at(
            d.pop("previous_secret_expires_at")
        )

        secret = d.pop("secret")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        url = d.pop("url")

        webhook_endpoint_created = cls(
            created_at=created_at,
            disabled_at=disabled_at,
            disabled_reason=disabled_reason,
            enabled=enabled,
            environment_id=environment_id,
            event_types=event_types,
            id=id,
            name=name,
            previous_secret_expires_at=previous_secret_expires_at,
            secret=secret,
            updated_at=updated_at,
            url=url,
        )

        webhook_endpoint_created.additional_properties = d
        return webhook_endpoint_created

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
