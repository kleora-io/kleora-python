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

from ..models.api_key_created_status import ApiKeyCreatedStatus

T = TypeVar("T", bound="ApiKeyCreated")


@_attrs_define
class ApiKeyCreated:
    """The `201` of a creation, and the `200` of `POST …/rotate`: the resource,
    plus the full key, once.

    Required rather than optional, unlike `ClientCreated`: both operations mint
    exactly one credential, so there is always one to carry. These are the only
    two responses in the surface that will ever hold it.

        Attributes:
            created_at (datetime.datetime):
            created_by (None | UUID):
            environment_id (UUID):
            expires_at (datetime.datetime | None):
            id (UUID):
            key (str):
            last_used_at (datetime.datetime | None):
            name (str):
            prefix (str):
            revoked_at (datetime.datetime | None):
            scopes (list[str]):
            status (ApiKeyCreatedStatus):
    """

    created_at: datetime.datetime
    created_by: None | UUID
    environment_id: UUID
    expires_at: datetime.datetime | None
    id: UUID
    key: str
    last_used_at: datetime.datetime | None
    name: str
    prefix: str
    revoked_at: datetime.datetime | None
    scopes: list[str]
    status: ApiKeyCreatedStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        created_by: None | str
        if isinstance(self.created_by, UUID):
            created_by = str(self.created_by)
        else:
            created_by = self.created_by

        environment_id = str(self.environment_id)

        expires_at: None | str
        if isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        id = str(self.id)

        key = self.key

        last_used_at: None | str
        if isinstance(self.last_used_at, datetime.datetime):
            last_used_at = self.last_used_at.isoformat()
        else:
            last_used_at = self.last_used_at

        name = self.name

        prefix = self.prefix

        revoked_at: None | str
        if isinstance(self.revoked_at, datetime.datetime):
            revoked_at = self.revoked_at.isoformat()
        else:
            revoked_at = self.revoked_at

        scopes = self.scopes

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "created_by": created_by,
                "environment_id": environment_id,
                "expires_at": expires_at,
                "id": id,
                "key": key,
                "last_used_at": last_used_at,
                "name": name,
                "prefix": prefix,
                "revoked_at": revoked_at,
                "scopes": scopes,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_created_by(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_type_0 = UUID(data)

                return created_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        created_by = _parse_created_by(d.pop("created_by"))

        environment_id = UUID(d.pop("environment_id"))

        def _parse_expires_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        expires_at = _parse_expires_at(d.pop("expires_at"))

        id = UUID(d.pop("id"))

        key = d.pop("key")

        def _parse_last_used_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_used_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_used_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_used_at = _parse_last_used_at(d.pop("last_used_at"))

        name = d.pop("name")

        prefix = d.pop("prefix")

        def _parse_revoked_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                revoked_at_type_0 = datetime.datetime.fromisoformat(data)

                return revoked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        revoked_at = _parse_revoked_at(d.pop("revoked_at"))

        scopes = cast(list[str], d.pop("scopes"))

        status = ApiKeyCreatedStatus(d.pop("status"))

        api_key_created = cls(
            created_at=created_at,
            created_by=created_by,
            environment_id=environment_id,
            expires_at=expires_at,
            id=id,
            key=key,
            last_used_at=last_used_at,
            name=name,
            prefix=prefix,
            revoked_at=revoked_at,
            scopes=scopes,
            status=status,
        )

        api_key_created.additional_properties = d
        return api_key_created

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
