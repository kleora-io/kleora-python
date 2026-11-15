# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="SubscriptionOut")


@_attrs_define
class SubscriptionOut:
    """The subscription, as last synchronised with the payment provider.

    `as_of` is when it was last synchronised, so a client can show that the information may be
    stale.

    `status` alone does not say whether the Account can currently make changes: an `unpaid` Account
    is first blocked from writing until the invoice is paid, and is later moved to the `free` plan,
    after which writes are allowed again. `writes_refused` and `downgraded_at` tell the two apart.

        Attributes:
            as_of (datetime.datetime | None):
            billing_country (None | str):
            cancel_at_period_end (bool):
            currency (None | str):
            current_period_end (datetime.datetime | None):
            downgraded_at (datetime.datetime | None):
            plan (None | str):
            quantity (int):
            status (str):
            writes_refused (bool):
    """

    as_of: datetime.datetime | None
    billing_country: None | str
    cancel_at_period_end: bool
    currency: None | str
    current_period_end: datetime.datetime | None
    downgraded_at: datetime.datetime | None
    plan: None | str
    quantity: int
    status: str
    writes_refused: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        as_of: None | str
        if isinstance(self.as_of, datetime.datetime):
            as_of = self.as_of.isoformat()
        else:
            as_of = self.as_of

        billing_country: None | str
        billing_country = self.billing_country

        cancel_at_period_end = self.cancel_at_period_end

        currency: None | str
        currency = self.currency

        current_period_end: None | str
        if isinstance(self.current_period_end, datetime.datetime):
            current_period_end = self.current_period_end.isoformat()
        else:
            current_period_end = self.current_period_end

        downgraded_at: None | str
        if isinstance(self.downgraded_at, datetime.datetime):
            downgraded_at = self.downgraded_at.isoformat()
        else:
            downgraded_at = self.downgraded_at

        plan: None | str
        plan = self.plan

        quantity = self.quantity

        status = self.status

        writes_refused = self.writes_refused

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "as_of": as_of,
                "billing_country": billing_country,
                "cancel_at_period_end": cancel_at_period_end,
                "currency": currency,
                "current_period_end": current_period_end,
                "downgraded_at": downgraded_at,
                "plan": plan,
                "quantity": quantity,
                "status": status,
                "writes_refused": writes_refused,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_as_of(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                as_of_type_0 = datetime.datetime.fromisoformat(data)

                return as_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        as_of = _parse_as_of(d.pop("as_of"))

        def _parse_billing_country(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        billing_country = _parse_billing_country(d.pop("billing_country"))

        cancel_at_period_end = d.pop("cancel_at_period_end")

        def _parse_currency(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        currency = _parse_currency(d.pop("currency"))

        def _parse_current_period_end(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                current_period_end_type_0 = datetime.datetime.fromisoformat(data)

                return current_period_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        current_period_end = _parse_current_period_end(d.pop("current_period_end"))

        def _parse_downgraded_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                downgraded_at_type_0 = datetime.datetime.fromisoformat(data)

                return downgraded_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        downgraded_at = _parse_downgraded_at(d.pop("downgraded_at"))

        def _parse_plan(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        plan = _parse_plan(d.pop("plan"))

        quantity = d.pop("quantity")

        status = d.pop("status")

        writes_refused = d.pop("writes_refused")

        subscription_out = cls(
            as_of=as_of,
            billing_country=billing_country,
            cancel_at_period_end=cancel_at_period_end,
            currency=currency,
            current_period_end=current_period_end,
            downgraded_at=downgraded_at,
            plan=plan,
            quantity=quantity,
            status=status,
            writes_refused=writes_refused,
        )

        subscription_out.additional_properties = d
        return subscription_out

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
