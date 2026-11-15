# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed self-service API document
# (https://id.kleora.eu/account/v1/openapi.json). `kleora.account` wraps this tree; nothing outside the
# package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="PasswordPolicyOut")


@_attrs_define
class PasswordPolicyOut:
    """What a password form needs before anything is typed: whether the person has a password (and
    so must give the current one), the minimum length, and whether new passwords are checked
    against known breaches.

        Attributes:
            breach_check (bool):
            has_password (bool):
            min_length (int):
    """

    breach_check: bool
    has_password: bool
    min_length: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        breach_check = self.breach_check

        has_password = self.has_password

        min_length = self.min_length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "breach_check": breach_check,
                "has_password": has_password,
                "min_length": min_length,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        breach_check = d.pop("breach_check")

        has_password = d.pop("has_password")

        min_length = d.pop("min_length")

        password_policy_out = cls(
            breach_check=breach_check,
            has_password=has_password,
            min_length=min_length,
        )

        password_policy_out.additional_properties = d
        return password_policy_out

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
