# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.checkout_in_interval import CheckoutInInterval
from ..models.checkout_in_plan import CheckoutInPlan
from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckoutIn")


@_attrs_define
class CheckoutIn:
    """The body of `POST /api/v1/account/billing/checkout`.

    The plan, the billing interval and the billing country. There is no return URL, currency or
    price: the return URL is fixed, and the price and currency follow from the plan and the country.

        Attributes:
            plan (CheckoutInPlan):
            billing_country (None | str | Unset): ISO 3166-1 alpha-2 billing country. Chooses the currency; never a locale.
            interval (CheckoutInInterval | Unset):  Default: CheckoutInInterval.MONTH.
    """

    plan: CheckoutInPlan
    billing_country: None | str | Unset = UNSET
    interval: CheckoutInInterval | Unset = CheckoutInInterval.MONTH
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plan = self.plan.value

        billing_country: None | str | Unset
        if isinstance(self.billing_country, Unset):
            billing_country = UNSET
        else:
            billing_country = self.billing_country

        interval: str | Unset = UNSET
        if not isinstance(self.interval, Unset):
            interval = self.interval.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plan": plan,
            }
        )
        if billing_country is not UNSET:
            field_dict["billing_country"] = billing_country
        if interval is not UNSET:
            field_dict["interval"] = interval

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        plan = CheckoutInPlan(d.pop("plan"))

        def _parse_billing_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        billing_country = _parse_billing_country(d.pop("billing_country", UNSET))

        _interval = d.pop("interval", UNSET)
        interval: CheckoutInInterval | Unset
        if isinstance(_interval, Unset):
            interval = UNSET
        else:
            interval = CheckoutInInterval(_interval)

        checkout_in = cls(
            plan=plan,
            billing_country=billing_country,
            interval=interval,
        )

        checkout_in.additional_properties = d
        return checkout_in

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
