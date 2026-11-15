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

if TYPE_CHECKING:
    from ..models.signing_key_out import SigningKeyOut


T = TypeVar("T", bound="SigningKeyRotated")


@_attrs_define
class SigningKeyRotated:
    """The `200` of a rotation: the three states, after the fact.

    `next` is never null — App creation writes one and every rotation
    pre-announces the following one — so the field is required rather than
    optional. `retired` is a list because more than one key can still be inside
    its retention window, and it is empty after a `retire_immediately` rotation
    of an environment that had none before.

        Attributes:
            active (SigningKeyOut): One signing key as every read reports it (sessions-and-tokens.md §API).

                `public_jwk` is RFC 7517's public JWK: `kty`, `crv`, `x`, `y`, `kid`, `alg`,
                `use`. Typed `dict[str, str]` rather than a model of its own because it is
                published verbatim and a JWK's membership is the RFC's to decide, not ours.
            next_ (SigningKeyOut): One signing key as every read reports it (sessions-and-tokens.md §API).

                `public_jwk` is RFC 7517's public JWK: `kty`, `crv`, `x`, `y`, `kid`, `alg`,
                `use`. Typed `dict[str, str]` rather than a model of its own because it is
                published verbatim and a JWK's membership is the RFC's to decide, not ours.
            retired (list[SigningKeyOut]):
    """

    active: SigningKeyOut
    next_: SigningKeyOut
    retired: list[SigningKeyOut]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active.to_dict()

        next_ = self.next_.to_dict()

        retired = []
        for retired_item_data in self.retired:
            retired_item = retired_item_data.to_dict()
            retired.append(retired_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active": active,
                "next": next_,
                "retired": retired,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.signing_key_out import SigningKeyOut

        d = dict(src_dict)
        active = SigningKeyOut.from_dict(d.pop("active"))

        next_ = SigningKeyOut.from_dict(d.pop("next"))

        retired = []
        _retired = d.pop("retired")
        for retired_item_data in _retired:
            retired_item = SigningKeyOut.from_dict(retired_item_data)

            retired.append(retired_item)

        signing_key_rotated = cls(
            active=active,
            next_=next_,
            retired=retired,
        )

        signing_key_rotated.additional_properties = d
        return signing_key_rotated

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
