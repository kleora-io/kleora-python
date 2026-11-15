# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.plan_limits_out import PlanLimitsOut


T = TypeVar("T", bound="AppPlanOut")


@_attrs_define
class AppPlanOut:
    """One App, the plan it is actually held to, and that plan's limits.

    The plan is `effective_plan`'s answer, not the `plan` column: an Account on
    `scale` holds every one of its Apps to `scale` regardless of what its own
    row says (billing.md §"How this looks in the data"), and a response that
    reported the column would be telling half of it.

        Attributes:
            app_id (UUID):
            limits (PlanLimitsOut): The numbers a plan is held to — `apps.accounts.plan_limits`, verbatim.

                `AccountOut` deliberately carries no limits, so this is where a caller
                reads them (P6-13 scope). `tenant_limit` is the derived ceiling
                `effective_tenant_limit` returns, override included: what actually applies
                to this App right now, not what its plan implies.
            plan (str):
            slug (str):
    """

    app_id: UUID
    limits: PlanLimitsOut
    plan: str
    slug: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = str(self.app_id)

        limits = self.limits.to_dict()

        plan = self.plan

        slug = self.slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app_id": app_id,
                "limits": limits,
                "plan": plan,
                "slug": slug,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.plan_limits_out import PlanLimitsOut

        d = dict(src_dict)
        app_id = UUID(d.pop("app_id"))

        limits = PlanLimitsOut.from_dict(d.pop("limits"))

        plan = d.pop("plan")

        slug = d.pop("slug")

        app_plan_out = cls(
            app_id=app_id,
            limits=limits,
            plan=plan,
            slug=slug,
        )

        app_plan_out.additional_properties = d
        return app_plan_out

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
