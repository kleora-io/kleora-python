# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed self-service API document
# (https://id.kleora.eu/account/v1/openapi.json). `kleora.account` wraps this tree; nothing outside the
# package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.mfa_factor_out import MfaFactorOut


T = TypeVar("T", bound="MfaOut")


@_attrs_define
class MfaOut:
    """The factors, and the policy that decides what may be removed.

    Attributes:
        factors (list[MfaFactorOut]):
        policy (str):
    """

    factors: list[MfaFactorOut]
    policy: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        factors = []
        for factors_item_data in self.factors:
            factors_item = factors_item_data.to_dict()
            factors.append(factors_item)

        policy = self.policy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "factors": factors,
                "policy": policy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mfa_factor_out import MfaFactorOut

        d = dict(src_dict)
        factors = []
        _factors = d.pop("factors")
        for factors_item_data in _factors:
            factors_item = MfaFactorOut.from_dict(factors_item_data)

            factors.append(factors_item)

        policy = d.pop("policy")

        mfa_out = cls(
            factors=factors,
            policy=policy,
        )

        mfa_out.additional_properties = d
        return mfa_out

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
