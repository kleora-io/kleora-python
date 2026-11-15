# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed self-service API document
# (https://id.kleora.eu/account/v1/openapi.json). `kleora.account` wraps this tree; nothing outside the
# package imports it.
from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="MfaFactorOut")


@_attrs_define
class MfaFactorOut:
    """One factor, in `GET /flow/mfa`'s own shape. Never a seed and never a hash.

    Attributes:
        confirmed_at (datetime.datetime | None):
        created_at (datetime.datetime):
        id (UUID):
        kind (str):
        last_used_at (datetime.datetime | None):
        recovery_codes_remaining (int | None):
    """

    confirmed_at: datetime.datetime | None
    created_at: datetime.datetime
    id: UUID
    kind: str
    last_used_at: datetime.datetime | None
    recovery_codes_remaining: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        confirmed_at: None | str
        if isinstance(self.confirmed_at, datetime.datetime):
            confirmed_at = self.confirmed_at.isoformat()
        else:
            confirmed_at = self.confirmed_at

        created_at = self.created_at.isoformat()

        id = str(self.id)

        kind = self.kind

        last_used_at: None | str
        if isinstance(self.last_used_at, datetime.datetime):
            last_used_at = self.last_used_at.isoformat()
        else:
            last_used_at = self.last_used_at

        recovery_codes_remaining: int | None
        recovery_codes_remaining = self.recovery_codes_remaining

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "confirmed_at": confirmed_at,
                "created_at": created_at,
                "id": id,
                "kind": kind,
                "last_used_at": last_used_at,
                "recovery_codes_remaining": recovery_codes_remaining,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_confirmed_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                confirmed_at_type_0 = datetime.datetime.fromisoformat(data)

                return confirmed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        confirmed_at = _parse_confirmed_at(d.pop("confirmed_at"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = UUID(d.pop("id"))

        kind = d.pop("kind")

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

        def _parse_recovery_codes_remaining(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        recovery_codes_remaining = _parse_recovery_codes_remaining(
            d.pop("recovery_codes_remaining")
        )

        mfa_factor_out = cls(
            confirmed_at=confirmed_at,
            created_at=created_at,
            id=id,
            kind=kind,
            last_used_at=last_used_at,
            recovery_codes_remaining=recovery_codes_remaining,
        )

        mfa_factor_out.additional_properties = d
        return mfa_factor_out

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
