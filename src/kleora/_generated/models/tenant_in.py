# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tenant_in_metadata import TenantInMetadata


T = TypeVar("T", bound="TenantIn")


@_attrs_define
class TenantIn:
    """The body of `POST /api/v1/environments/{environment_id}/tenants`.

    `slug` is required: it is the value of the `tenant` authorization parameter.

        Attributes:
            name (str):
            slug (str):
            metadata (TenantInMetadata | Unset):
    """

    name: str
    slug: str
    metadata: TenantInMetadata | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slug = self.slug

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "slug": slug,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.tenant_in_metadata import TenantInMetadata

        d = dict(src_dict)
        name = d.pop("name")

        slug = d.pop("slug")

        _metadata = d.pop("metadata", UNSET)
        metadata: TenantInMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = TenantInMetadata.from_dict(_metadata)

        tenant_in = cls(
            name=name,
            slug=slug,
            metadata=metadata,
        )

        return tenant_in
