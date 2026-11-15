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
    """`current_password` and `new_password`, the second required.

    `current_password` is optional **only** because a person who has none has none
    to send (§"The operations": "Set a password (person has none) … No
    `current_password` to supply"). It is not a way to skip the check: a person who
    *does* have a password and omits it gets `401 invalid-credentials` and not a
    `422`, because "naming the missing field would distinguish 'you have a
    password' from 'you do not' to a caller holding somebody's token"
    (§"Failure modes").

    Neither field carries a `min_length`. The policy is the Environment's and its
    refusal is `422 password-policy` with `errors[].field = "password"`; a schema
    bound would answer first, in django-ninja's shape, for the one input whose
    refusal §"Failure modes" writes out.

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
