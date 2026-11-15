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

T = TypeVar("T", bound="EmailConfirmIn")


@_attrs_define
class EmailConfirmIn:
    """`POST /email/confirm` with `{token}` — the row drafted in `U10-05`'s Log.

    The operation §API omits: §"Changing an email address" step 2 requires a route
    the mailed token is `POST`ed to ("only the `POST` spends it, so a mail scanner
    cannot") and §"Failure modes" declares its two refusals, but the table has no row.

    No `max_length` bound below the column's: a token is 32 random bytes as URL-safe
    base64 and the only thing that matters about a wrong one is that it is wrong, so
    a length refusal would answer `422` where §"Failure modes" says `400
    invalid-token` — one answer for unknown, spent and expired, and a bound would
    make a fourth.

        Attributes:
            token (str):
    """

    token: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        token = d.pop("token")

        email_confirm_in = cls(
            token=token,
        )

        email_confirm_in.additional_properties = d
        return email_confirm_in

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
