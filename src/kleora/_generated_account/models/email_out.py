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
    """§API `GET /email`: `{email, email_verified, change_pending}`.

    `change_pending` is read from the existence of an unspent `change_email`
    `ActionToken` and from nowhere else — §"Changing an email address": "A pending
    change lives only on the `ActionToken`, and there is no `pending_email`
    column", so there is exactly one place the pending address is written and no
    second place for it to be wrong.

    It is declared here, and in this pull request it is always `false`: the
    operation that creates such a token (`POST /email`) is deferred with the rest
    of the email change — see `U10-03`'s Log. Declaring it now rather than adding
    it later keeps the member off the list of things that break a generated client.

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
