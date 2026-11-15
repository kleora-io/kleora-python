# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IdentityProviderIn")


@_attrs_define
class IdentityProviderIn:
    """The body of `PUT /environments/{environment_id}/identity-providers/{kind}`: create or
    replace.

    `client_secret` is optional, and omitting it keeps the stored secret, so a configuration can be
    changed without sending the secret again. It is required on the first write for a kind (`422`).
    Sending a different value rotates it, and the previous secret keeps working for 24 hours. `null`
    is refused; to remove a provider, use `DELETE`.

        Attributes:
            client_id (str):
            allowed_email_domains (list[str] | Unset):
            button_label (str | Unset):  Default: ''.
            client_secret (None | str | Unset):
            enabled (bool | Unset):  Default: False.
            microsoft_tenant (None | str | Unset):
            scopes (list[str] | Unset):
    """

    client_id: str
    allowed_email_domains: list[str] | Unset = UNSET
    button_label: str | Unset = ""
    client_secret: None | str | Unset = UNSET
    enabled: bool | Unset = False
    microsoft_tenant: None | str | Unset = UNSET
    scopes: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        client_id = self.client_id

        allowed_email_domains: list[str] | Unset = UNSET
        if not isinstance(self.allowed_email_domains, Unset):
            allowed_email_domains = self.allowed_email_domains

        button_label = self.button_label

        client_secret: None | str | Unset
        if isinstance(self.client_secret, Unset):
            client_secret = UNSET
        else:
            client_secret = self.client_secret

        enabled = self.enabled

        microsoft_tenant: None | str | Unset
        if isinstance(self.microsoft_tenant, Unset):
            microsoft_tenant = UNSET
        else:
            microsoft_tenant = self.microsoft_tenant

        scopes: list[str] | Unset = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = self.scopes

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "client_id": client_id,
            }
        )
        if allowed_email_domains is not UNSET:
            field_dict["allowed_email_domains"] = allowed_email_domains
        if button_label is not UNSET:
            field_dict["button_label"] = button_label
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if microsoft_tenant is not UNSET:
            field_dict["microsoft_tenant"] = microsoft_tenant
        if scopes is not UNSET:
            field_dict["scopes"] = scopes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        client_id = d.pop("client_id")

        allowed_email_domains = cast(list[str], d.pop("allowed_email_domains", UNSET))

        button_label = d.pop("button_label", UNSET)

        def _parse_client_secret(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_secret = _parse_client_secret(d.pop("client_secret", UNSET))

        enabled = d.pop("enabled", UNSET)

        def _parse_microsoft_tenant(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        microsoft_tenant = _parse_microsoft_tenant(d.pop("microsoft_tenant", UNSET))

        scopes = cast(list[str], d.pop("scopes", UNSET))

        identity_provider_in = cls(
            client_id=client_id,
            allowed_email_domains=allowed_email_domains,
            button_label=button_label,
            client_secret=client_secret,
            enabled=enabled,
            microsoft_tenant=microsoft_tenant,
            scopes=scopes,
        )

        return identity_provider_in
