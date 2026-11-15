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
    from ..models.tenant_patch_metadata import TenantPatchMetadata


T = TypeVar("T", bound="TenantPatch")


@_attrs_define
class TenantPatch:
    """The body of `PATCH /api/v1/tenants/{tenant_id}`: `name`, `slug` and `metadata`.

    `metadata` is replaced whole. `is_default`, `status`, `member_count` and `environment_id` are
    refused as unknown fields; use `suspend` and `unsuspend` to change the status. The default
    tenant's `slug` cannot be changed (`422` with `code: "immutable"`).

        Attributes:
            metadata (TenantPatchMetadata | Unset):
            name (str | Unset):
            slug (str | Unset):
    """

    metadata: TenantPatchMetadata | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name

        slug = self.slug

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.tenant_patch_metadata import TenantPatchMetadata

        d = dict(src_dict)
        _metadata = d.pop("metadata", UNSET)
        metadata: TenantPatchMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = TenantPatchMetadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        tenant_patch = cls(
            metadata=metadata,
            name=name,
            slug=slug,
        )

        return tenant_patch
