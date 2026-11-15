# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.me_passkey_out import MePasskeyOut


T = TypeVar("T", bound="MePasskeyRegisterFinishOut")


@_attrs_define
class MePasskeyRegisterFinishOut:
    """The registered passkey. `recovery_codes` is present, once, only the first time the user
    registers a second factor of any kind.

        Attributes:
            passkey (MePasskeyOut): The one passkey `POST /me/passkeys/register/finish` just registered —
                the richer shape `GET /me/mfa` does not carry (see `MfaFactorOut`).
            recovery_codes (list[str] | None | Unset):
    """

    passkey: MePasskeyOut
    recovery_codes: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        passkey = self.passkey.to_dict()

        recovery_codes: list[str] | None | Unset
        if isinstance(self.recovery_codes, Unset):
            recovery_codes = UNSET
        elif isinstance(self.recovery_codes, list):
            recovery_codes = self.recovery_codes

        else:
            recovery_codes = self.recovery_codes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "passkey": passkey,
            }
        )
        if recovery_codes is not UNSET:
            field_dict["recovery_codes"] = recovery_codes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.me_passkey_out import MePasskeyOut

        d = dict(src_dict)
        passkey = MePasskeyOut.from_dict(d.pop("passkey"))

        def _parse_recovery_codes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                recovery_codes_type_0 = cast(list[str], data)

                return recovery_codes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        recovery_codes = _parse_recovery_codes(d.pop("recovery_codes", UNSET))

        me_passkey_register_finish_out = cls(
            passkey=passkey,
            recovery_codes=recovery_codes,
        )

        me_passkey_register_finish_out.additional_properties = d
        return me_passkey_register_finish_out

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
