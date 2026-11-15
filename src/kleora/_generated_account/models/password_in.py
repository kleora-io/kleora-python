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

from ..types import UNSET, Unset

T = TypeVar("T", bound="PasswordIn")


@_attrs_define
class PasswordIn:
    """The body of `POST /password`.

    `current_password` is required when the person has a password, and omitted when they have none;
    a missing or wrong one is `401 invalid-credentials`. Length is checked by the environment's
    password policy, which answers `422 password-policy` with `errors[].field = "password"`.

        Attributes:
            new_password (str):
            current_password (str | Unset):  Default: ''.
    """

    new_password: str
    current_password: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_password = self.new_password

        current_password = self.current_password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "new_password": new_password,
            }
        )
        if current_password is not UNSET:
            field_dict["current_password"] = current_password

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        new_password = d.pop("new_password")

        current_password = d.pop("current_password", UNSET)

        password_in = cls(
            new_password=new_password,
            current_password=current_password,
        )

        password_in.additional_properties = d
        return password_in

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
