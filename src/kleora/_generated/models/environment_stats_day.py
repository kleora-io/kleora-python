# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="EnvironmentStatsDay")


@_attrs_define
class EnvironmentStatsDay:
    """One UTC day of the range.

    Every day appears, zeroed when nothing happened on it: a chart drawn from a
    sparse series would put Monday's bar where Wednesday's belongs.

        Attributes:
            date (datetime.date):
            logins_failed (int):
            logins_succeeded (int):
            users_created (int):
    """

    date: datetime.date
    logins_failed: int
    logins_succeeded: int
    users_created: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        logins_failed = self.logins_failed

        logins_succeeded = self.logins_succeeded

        users_created = self.users_created

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "logins_failed": logins_failed,
                "logins_succeeded": logins_succeeded,
                "users_created": users_created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        date = datetime.date.fromisoformat(d.pop("date"))

        logins_failed = d.pop("logins_failed")

        logins_succeeded = d.pop("logins_succeeded")

        users_created = d.pop("users_created")

        environment_stats_day = cls(
            date=date,
            logins_failed=logins_failed,
            logins_succeeded=logins_succeeded,
            users_created=users_created,
        )

        environment_stats_day.additional_properties = d
        return environment_stats_day

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
