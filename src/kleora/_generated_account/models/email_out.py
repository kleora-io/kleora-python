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

T = TypeVar("T", bound="EmailOut")


@_attrs_define
class EmailOut:
    """The person's email address, whether it is verified, and whether a change of address is
    waiting for confirmation.

    `change_pending` is `true` while a confirmation link sent by `POST /email` is outstanding. The
    pending address itself is never returned.

        Attributes:
            change_pending (bool):
            email (str):
            email_verified (bool):
    """

    change_pending: bool
    email: str
    email_verified: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        change_pending = self.change_pending

        email = self.email

        email_verified = self.email_verified

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "change_pending": change_pending,
                "email": email,
                "email_verified": email_verified,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        change_pending = d.pop("change_pending")

        email = d.pop("email")

        email_verified = d.pop("email_verified")

        email_out = cls(
            change_pending=change_pending,
            email=email,
            email_verified=email_verified,
        )

        email_out.additional_properties = d
        return email_out

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
