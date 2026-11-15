# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.me_passkey_register_finish_body_credential import (
        MePasskeyRegisterFinishBodyCredential,
    )


T = TypeVar("T", bound="MePasskeyRegisterFinishBody")


@_attrs_define
class MePasskeyRegisterFinishBody:
    """
    Attributes:
        credential (MePasskeyRegisterFinishBodyCredential | Unset):
        name (str | Unset):  Default: ''.
    """

    credential: MePasskeyRegisterFinishBodyCredential | Unset = UNSET
    name: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credential: dict[str, Any] | Unset = UNSET
        if not isinstance(self.credential, Unset):
            credential = self.credential.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credential is not UNSET:
            field_dict["credential"] = credential
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.me_passkey_register_finish_body_credential import (
            MePasskeyRegisterFinishBodyCredential,
        )

        d = dict(src_dict)
        _credential = d.pop("credential", UNSET)
        credential: MePasskeyRegisterFinishBodyCredential | Unset
        if isinstance(_credential, Unset):
            credential = UNSET
        else:
            credential = MePasskeyRegisterFinishBodyCredential.from_dict(_credential)

        name = d.pop("name", UNSET)

        me_passkey_register_finish_body = cls(
            credential=credential,
            name=name,
        )

        me_passkey_register_finish_body.additional_properties = d
        return me_passkey_register_finish_body

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
