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
    from ..models.passkey_out import PasskeyOut


T = TypeVar("T", bound="PasskeysOut")


@_attrs_define
class PasskeysOut:
    """The person's passkeys, and where they can add one.

    Registering a passkey is not possible through this API: the passkey is bound to the issuer host,
    so browsers refuse to create it on another origin. `portal_url` is the hosted account portal's
    security page, which a customer's screen links to instead.

        Attributes:
            passkeys (list[PasskeyOut]):
            portal_url (str):
    """

    passkeys: list[PasskeyOut]
    portal_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        passkeys = []
        for passkeys_item_data in self.passkeys:
            passkeys_item = passkeys_item_data.to_dict()
            passkeys.append(passkeys_item)

        portal_url = self.portal_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "passkeys": passkeys,
                "portal_url": portal_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.passkey_out import PasskeyOut

        d = dict(src_dict)
        passkeys = []
        _passkeys = d.pop("passkeys")
        for passkeys_item_data in _passkeys:
            passkeys_item = PasskeyOut.from_dict(passkeys_item_data)

            passkeys.append(passkeys_item)

        portal_url = d.pop("portal_url")

        passkeys_out = cls(
            passkeys=passkeys,
            portal_url=portal_url,
        )

        passkeys_out.additional_properties = d
        return passkeys_out

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
