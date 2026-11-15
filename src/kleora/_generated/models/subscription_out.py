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
    """The mirror of Stripe — and it says so.

    `as_of` is when the mirror last agreed with Stripe, which is the whole
    reason it is here: billing.md §"Failure modes" says that when Stripe is
    down "the page renders from our mirror, marked possibly stale", and a
    console cannot mark staleness it has no way to measure.

    **`status` alone cannot say whether this Account may currently write**, and
    that is why the two fields below it exist. billing.md §"When payment fails"
    makes the day-60 downgrade the moment the write refusal *ends* — "in code
    the condition is `status == unpaid AND downgraded_at IS NULL`, not `status
    == unpaid`" — so day 15-59 and day 60-onwards both read `unpaid` while
    meaning opposite things: pay the invoice and everything resumes, against
    you are on `free` now and nothing was deleted. A client holding only
    `status` has to say one of those two sentences to the reader who needs the
    other.

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
