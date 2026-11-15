# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="EnvironmentStatsTotals")


@_attrs_define
class EnvironmentStatsTotals:
    """What the environment holds now — current counts, not counts over the range.

    `users` excludes erased users, `api_keys` counts active keys only, and
    `active_sessions` is the "live" of sessions-and-tokens.md §"Browser
    session": each figure is the set its own console page lists, so a number
    here and a list there never disagree.

        Attributes:
            active_sessions (int):
            api_keys (int):
            clients (int):
            users (int):
    """

    active_sessions: int
    api_keys: int
    clients: int
    users: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_sessions = self.active_sessions

        api_keys = self.api_keys

        clients = self.clients

        users = self.users

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active_sessions": active_sessions,
                "api_keys": api_keys,
                "clients": clients,
                "users": users,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        active_sessions = d.pop("active_sessions")

        api_keys = d.pop("api_keys")

        clients = d.pop("clients")

        users = d.pop("users")

        environment_stats_totals = cls(
            active_sessions=active_sessions,
            api_keys=api_keys,
            clients=clients,
            users=users,
        )

        environment_stats_totals.additional_properties = d
        return environment_stats_totals

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
