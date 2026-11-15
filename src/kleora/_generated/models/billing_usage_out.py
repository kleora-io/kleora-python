# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.app_mau_out import AppMauOut
    from ..models.mau_allowance_out import MauAllowanceOut


T = TypeVar("T", bound="BillingUsageOut")


@_attrs_define
class BillingUsageOut:
    """The body of `GET /api/v1/account/billing/usage`: monthly active users and App counts for the
    current period.

    The period is the half-open window `[period_start, period_end)`, as RFC 3339 UTC timestamps, so
    the figures can be reconciled exactly.

    `mau` is the Account total: the sum of its Apps' figures. A person active in two Apps counts in
    each, because users belong to an environment.

        Attributes:
            allowances (list[MauAllowanceOut]):
            apps (list[AppMauOut]):
            apps_used (int):
            as_of (datetime.datetime):
            mau (int):
            period_end (datetime.datetime):
            period_start (datetime.datetime):
            tenants (int):
    """

    allowances: list[MauAllowanceOut]
    apps: list[AppMauOut]
    apps_used: int
    as_of: datetime.datetime
    mau: int
    period_end: datetime.datetime
    period_start: datetime.datetime
    tenants: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowances = []
        for allowances_item_data in self.allowances:
            allowances_item = allowances_item_data.to_dict()
            allowances.append(allowances_item)

        apps = []
        for apps_item_data in self.apps:
            apps_item = apps_item_data.to_dict()
            apps.append(apps_item)

        apps_used = self.apps_used

        as_of = self.as_of.isoformat()

        mau = self.mau

        period_end = self.period_end.isoformat()

        period_start = self.period_start.isoformat()

        tenants = self.tenants

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowances": allowances,
                "apps": apps,
                "apps_used": apps_used,
                "as_of": as_of,
                "mau": mau,
                "period_end": period_end,
                "period_start": period_start,
                "tenants": tenants,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.app_mau_out import AppMauOut
        from ..models.mau_allowance_out import MauAllowanceOut

        d = dict(src_dict)
        allowances = []
        _allowances = d.pop("allowances")
        for allowances_item_data in _allowances:
            allowances_item = MauAllowanceOut.from_dict(allowances_item_data)

            allowances.append(allowances_item)

        apps = []
        _apps = d.pop("apps")
        for apps_item_data in _apps:
            apps_item = AppMauOut.from_dict(apps_item_data)

            apps.append(apps_item)

        apps_used = d.pop("apps_used")

        as_of = datetime.datetime.fromisoformat(d.pop("as_of"))

        mau = d.pop("mau")

        period_end = datetime.datetime.fromisoformat(d.pop("period_end"))

        period_start = datetime.datetime.fromisoformat(d.pop("period_start"))

        tenants = d.pop("tenants")

        billing_usage_out = cls(
            allowances=allowances,
            apps=apps,
            apps_used=apps_used,
            as_of=as_of,
            mau=mau,
            period_end=period_end,
            period_start=period_start,
            tenants=tenants,
        )

        billing_usage_out.additional_properties = d
        return billing_usage_out

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
