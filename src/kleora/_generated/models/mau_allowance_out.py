# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.mau_allowance_out_scope import MauAllowanceOutScope

T = TypeVar("T", bound="MauAllowanceOut")


@_attrs_define
class MauAllowanceOut:
    """One pool of monthly active users and the allowance it is measured against.

    Allowances are pooled differently by plan: `free` pools every `free` App of the Account, `pro`
    counts each App separately, and `scale` pools the whole Account. `scope` is `account` for a pool
    and `app` for a single `pro` App, and `app_id` is set only for the latter.

    `over_allowance` is informational: exceeding an allowance never blocks sign-in.

        Attributes:
            allowance (int):
            app_id (None | UUID):
            mau (int):
            over_allowance (bool):
            plan (str):
            scope (MauAllowanceOutScope):
    """

    allowance: int
    app_id: None | UUID
    mau: int
    over_allowance: bool
    plan: str
    scope: MauAllowanceOutScope
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowance = self.allowance

        app_id: None | str
        if isinstance(self.app_id, UUID):
            app_id = str(self.app_id)
        else:
            app_id = self.app_id

        mau = self.mau

        over_allowance = self.over_allowance

        plan = self.plan

        scope = self.scope.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowance": allowance,
                "app_id": app_id,
                "mau": mau,
                "over_allowance": over_allowance,
                "plan": plan,
                "scope": scope,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        allowance = d.pop("allowance")

        def _parse_app_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                app_id_type_0 = UUID(data)

                return app_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        app_id = _parse_app_id(d.pop("app_id"))

        mau = d.pop("mau")

        over_allowance = d.pop("over_allowance")

        plan = d.pop("plan")

        scope = MauAllowanceOutScope(d.pop("scope"))

        mau_allowance_out = cls(
            allowance=allowance,
            app_id=app_id,
            mau=mau,
            over_allowance=over_allowance,
            plan=plan,
            scope=scope,
        )

        mau_allowance_out.additional_properties = d
        return mau_allowance_out

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
