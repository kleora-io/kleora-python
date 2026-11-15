# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.identity_in_provider import IdentityInProvider

T = TypeVar("T", bound="IdentityIn")


@_attrs_define
class IdentityIn:
    """The body of `POST .../users/{user_id}/identities`: an external provider account to link, by
    subject.

    `provider_subject` is the provider's own permanent id for the person (Google's `sub`, GitHub's
    numeric `id`, Microsoft's `oid`, Facebook's app-scoped `id`), never an email address. Any other
    field, such as a provider email, token or secret, is refused as unknown.

        Attributes:
            provider (IdentityInProvider):
            provider_subject (str):
    """

    provider: IdentityInProvider
    provider_subject: str

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        provider_subject = self.provider_subject

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "provider": provider,
                "provider_subject": provider_subject,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        provider = IdentityInProvider(d.pop("provider"))

        provider_subject = d.pop("provider_subject")

        identity_in = cls(
            provider=provider,
            provider_subject=provider_subject,
        )

        return identity_in
