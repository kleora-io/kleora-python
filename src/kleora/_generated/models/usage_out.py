# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_usage_out import AppUsageOut


T = TypeVar("T", bound="UsageOut")


@_attrs_define
class UsageOut:
    """The body of `GET /api/v1/account/usage`.

    `sandbox_users` is reported but never counted toward a limit. `mau` is the Account's monthly
    active users for the current calendar month, the same figure `GET /account/billing/usage`
    reports; it may be `null`.

        Attributes:
            apps (list[AppUsageOut]):
            apps_used (int):
            as_of (datetime.datetime):
            production_users (int):
            sandbox_users (int):
            mau (int | None | Unset):
    """

    apps: list[AppUsageOut]
    apps_used: int
    as_of: datetime.datetime
    production_users: int
    sandbox_users: int
    mau: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        apps = []
        for apps_item_data in self.apps:
            apps_item = apps_item_data.to_dict()
            apps.append(apps_item)

        apps_used = self.apps_used

        as_of = self.as_of.isoformat()

        production_users = self.production_users

        sandbox_users = self.sandbox_users

        mau: int | None | Unset
        if isinstance(self.mau, Unset):
            mau = UNSET
        else:
            mau = self.mau

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apps": apps,
                "apps_used": apps_used,
                "as_of": as_of,
                "production_users": production_users,
                "sandbox_users": sandbox_users,
            }
        )
        if mau is not UNSET:
            field_dict["mau"] = mau

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.app_usage_out import AppUsageOut

        d = dict(src_dict)
        apps = []
        _apps = d.pop("apps")
        for apps_item_data in _apps:
            apps_item = AppUsageOut.from_dict(apps_item_data)

            apps.append(apps_item)

        apps_used = d.pop("apps_used")

        as_of = datetime.datetime.fromisoformat(d.pop("as_of"))

        production_users = d.pop("production_users")

        sandbox_users = d.pop("sandbox_users")

        def _parse_mau(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        mau = _parse_mau(d.pop("mau", UNSET))

        usage_out = cls(
            apps=apps,
            apps_used=apps_used,
            as_of=as_of,
            production_users=production_users,
            sandbox_users=sandbox_users,
            mau=mau,
        )

        usage_out.additional_properties = d
        return usage_out

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
