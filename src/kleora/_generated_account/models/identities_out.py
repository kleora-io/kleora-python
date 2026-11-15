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
    from ..models.identity_out import IdentityOut
    from ..models.provider_out import ProviderOut


T = TypeVar("T", bound="IdentitiesOut")


@_attrs_define
class IdentitiesOut:
    """The person's provider identities, the providers this environment offers, and whether the
    person has a password.

    Each provider carries a `start_url`. Linking a provider is a browser redirect through `GET
    /oauth/social/{kind}/start?intent=link`, made top-level by the customer's screen.

        Attributes:
            has_password (bool):
            identities (list[IdentityOut]):
            providers (list[ProviderOut]):
    """

    has_password: bool
    identities: list[IdentityOut]
    providers: list[ProviderOut]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        has_password = self.has_password

        identities = []
        for identities_item_data in self.identities:
            identities_item = identities_item_data.to_dict()
            identities.append(identities_item)

        providers = []
        for providers_item_data in self.providers:
            providers_item = providers_item_data.to_dict()
            providers.append(providers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "has_password": has_password,
                "identities": identities,
                "providers": providers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.identity_out import IdentityOut
        from ..models.provider_out import ProviderOut

        d = dict(src_dict)
        has_password = d.pop("has_password")

        identities = []
        _identities = d.pop("identities")
        for identities_item_data in _identities:
            identities_item = IdentityOut.from_dict(identities_item_data)

            identities.append(identities_item)

        providers = []
        _providers = d.pop("providers")
        for providers_item_data in _providers:
            providers_item = ProviderOut.from_dict(providers_item_data)

            providers.append(providers_item)

        identities_out = cls(
            has_password=has_password,
            identities=identities,
            providers=providers,
        )

        identities_out.additional_properties = d
        return identities_out

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
