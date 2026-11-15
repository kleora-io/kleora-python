# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.app_plan_out import AppPlanOut
    from ..models.subscription_out import SubscriptionOut
    from ..models.usage_out import UsageOut


T = TypeVar("T", bound="BillingOut")


@_attrs_define
class BillingOut:
    """`GET /api/v1/account/billing` (billing.md §API).

    Plan, limits, usage, status and period end — and `subscription` is `null`
    for an Account that has never bought anything, which is most of them.
    `pro_apps` is what `quantity` is supposed to equal; the two are reported
    separately on purpose, because a disagreement between what we would charge
    for and what Stripe is charging for is exactly the drift reconciliation
    exists to find, and hiding it behind one number would hide it from the
    customer too.

        Attributes:
            account_plan (str):
            apps (list[AppPlanOut]):
            pro_apps (int):
            subscription (None | SubscriptionOut):
            usage (UsageOut): `GET /api/v1/account/usage` (environments.md §API).

                `sandbox_users` is reported so the console can show it and is never counted
                toward anything. `mau` is the Account's monthly active users for the current
                calendar month, from the same roll-up `GET /account/billing/usage` reads
                (`apps.billing.metering`, P6-12) — it was declared as a `null` placeholder
                first so that filling it in would be additive for every generated client,
                and the type stays optional for exactly that reason. It is read from the
                roll-up rather than counted here, because two arithmetics for one figure is
                how a usage page and an invoice come to disagree.
    """

    account_plan: str
    apps: list[AppPlanOut]
    pro_apps: int
    subscription: None | SubscriptionOut
    usage: UsageOut
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.subscription_out import SubscriptionOut

        account_plan = self.account_plan

        apps = []
        for apps_item_data in self.apps:
            apps_item = apps_item_data.to_dict()
            apps.append(apps_item)

        pro_apps = self.pro_apps

        subscription: dict[str, Any] | None
        if isinstance(self.subscription, SubscriptionOut):
            subscription = self.subscription.to_dict()
        else:
            subscription = self.subscription

        usage = self.usage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_plan": account_plan,
                "apps": apps,
                "pro_apps": pro_apps,
                "subscription": subscription,
                "usage": usage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.app_plan_out import AppPlanOut
        from ..models.subscription_out import SubscriptionOut
        from ..models.usage_out import UsageOut

        d = dict(src_dict)
        account_plan = d.pop("account_plan")

        apps = []
        _apps = d.pop("apps")
        for apps_item_data in _apps:
            apps_item = AppPlanOut.from_dict(apps_item_data)

            apps.append(apps_item)

        pro_apps = d.pop("pro_apps")

        def _parse_subscription(data: object) -> None | SubscriptionOut:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                subscription_type_0 = SubscriptionOut.from_dict(data)

                return subscription_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SubscriptionOut, data)

        subscription = _parse_subscription(d.pop("subscription"))

        usage = UsageOut.from_dict(d.pop("usage"))

        billing_out = cls(
            account_plan=account_plan,
            apps=apps,
            pro_apps=pro_apps,
            subscription=subscription,
            usage=usage,
        )

        billing_out.additional_properties = d
        return billing_out

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
