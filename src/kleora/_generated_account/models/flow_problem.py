# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed self-service API document
# (https://id.kleora.eu/account/v1/openapi.json). `kleora.account` wraps this tree; nothing outside the
# package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flow_field_error import FlowFieldError


T = TypeVar("T", bound="FlowProblem")


@_attrs_define
class FlowProblem:
    """RFC 9457 problem details, plus the `code` every flow refusal carries.

    A plain `BaseModel` for `api.management.v1.schemas.Problem`'s reason: a
    `Schema` validates through django-ninja's attribute getter, which would
    silently drop the extension members RFC 9457 exists to allow.

        Attributes:
            code (str):
            status (int):
            title (str):
            type_ (str):
            detail (None | str | Unset):
            errors (list[FlowFieldError] | None | Unset):
            feature (None | str | Unset):
            instance (None | str | Unset):
            plan (None | str | Unset):
            request_id (None | str | Unset):
            required_plans (list[str] | None | Unset):
            retry_after (int | None | Unset):
    """

    code: str
    status: int
    title: str
    type_: str
    detail: None | str | Unset = UNSET
    errors: list[FlowFieldError] | None | Unset = UNSET
    feature: None | str | Unset = UNSET
    instance: None | str | Unset = UNSET
    plan: None | str | Unset = UNSET
    request_id: None | str | Unset = UNSET
    required_plans: list[str] | None | Unset = UNSET
    retry_after: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        status = self.status

        title = self.title

        type_ = self.type_

        detail: None | str | Unset
        if isinstance(self.detail, Unset):
            detail = UNSET
        else:
            detail = self.detail

        errors: list[dict[str, Any]] | None | Unset
        if isinstance(self.errors, Unset):
            errors = UNSET
        elif isinstance(self.errors, list):
            errors = []
            for errors_type_0_item_data in self.errors:
                errors_type_0_item = errors_type_0_item_data.to_dict()
                errors.append(errors_type_0_item)

        else:
            errors = self.errors

        feature: None | str | Unset
        if isinstance(self.feature, Unset):
            feature = UNSET
        else:
            feature = self.feature

        instance: None | str | Unset
        if isinstance(self.instance, Unset):
            instance = UNSET
        else:
            instance = self.instance

        plan: None | str | Unset
        if isinstance(self.plan, Unset):
            plan = UNSET
        else:
            plan = self.plan

        request_id: None | str | Unset
        if isinstance(self.request_id, Unset):
            request_id = UNSET
        else:
            request_id = self.request_id

        required_plans: list[str] | None | Unset
        if isinstance(self.required_plans, Unset):
            required_plans = UNSET
        elif isinstance(self.required_plans, list):
            required_plans = self.required_plans

        else:
            required_plans = self.required_plans

        retry_after: int | None | Unset
        if isinstance(self.retry_after, Unset):
            retry_after = UNSET
        else:
            retry_after = self.retry_after

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "status": status,
                "title": title,
                "type": type_,
            }
        )
        if detail is not UNSET:
            field_dict["detail"] = detail
        if errors is not UNSET:
            field_dict["errors"] = errors
        if feature is not UNSET:
            field_dict["feature"] = feature
        if instance is not UNSET:
            field_dict["instance"] = instance
        if plan is not UNSET:
            field_dict["plan"] = plan
        if request_id is not UNSET:
            field_dict["request_id"] = request_id
        if required_plans is not UNSET:
            field_dict["required_plans"] = required_plans
        if retry_after is not UNSET:
            field_dict["retry_after"] = retry_after

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.flow_field_error import FlowFieldError

        d = dict(src_dict)
        code = d.pop("code")

        status = d.pop("status")

        title = d.pop("title")

        type_ = d.pop("type")

        def _parse_detail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detail = _parse_detail(d.pop("detail", UNSET))

        def _parse_errors(data: object) -> list[FlowFieldError] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                errors_type_0 = []
                _errors_type_0 = data
                for errors_type_0_item_data in _errors_type_0:
                    errors_type_0_item = FlowFieldError.from_dict(
                        errors_type_0_item_data
                    )

                    errors_type_0.append(errors_type_0_item)

                return errors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FlowFieldError] | None | Unset, data)

        errors = _parse_errors(d.pop("errors", UNSET))

        def _parse_feature(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        feature = _parse_feature(d.pop("feature", UNSET))

        def _parse_instance(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instance = _parse_instance(d.pop("instance", UNSET))

        def _parse_plan(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plan = _parse_plan(d.pop("plan", UNSET))

        def _parse_request_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        request_id = _parse_request_id(d.pop("request_id", UNSET))

        def _parse_required_plans(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                required_plans_type_0 = cast(list[str], data)

                return required_plans_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        required_plans = _parse_required_plans(d.pop("required_plans", UNSET))

        def _parse_retry_after(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retry_after = _parse_retry_after(d.pop("retry_after", UNSET))

        flow_problem = cls(
            code=code,
            status=status,
            title=title,
            type_=type_,
            detail=detail,
            errors=errors,
            feature=feature,
            instance=instance,
            plan=plan,
            request_id=request_id,
            required_plans=required_plans,
            retry_after=retry_after,
        )

        flow_problem.additional_properties = d
        return flow_problem

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
