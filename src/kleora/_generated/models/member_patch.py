# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.member_patch_status import MemberPatchStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="MemberPatch")


@_attrs_define
class MemberPatch:
    """The body of `PATCH /api/v1/tenants/{tenant_id}/members/{member_id}`.

    `roles` replaces the whole set; `[]` is valid, `null` is not. `user`, `tenant_id` and the
    timestamps are refused as unknown fields: to move a membership, remove it and add another.

        Attributes:
            roles (list[UUID] | Unset):
            status (MemberPatchStatus | Unset):
    """

    roles: list[UUID] | Unset = UNSET
    status: MemberPatchStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        roles: list[str] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = str(roles_item_data)
                roles.append(roles_item)

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if roles is not UNSET:
            field_dict["roles"] = roles
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _roles = d.pop("roles", UNSET)
        roles: list[UUID] | Unset = UNSET
        if _roles is not UNSET:
            roles = []
            for roles_item_data in _roles:
                roles_item = UUID(roles_item_data)

                roles.append(roles_item)

        _status = d.pop("status", UNSET)
        status: MemberPatchStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = MemberPatchStatus(_status)

        member_patch = cls(
            roles=roles,
            status=status,
        )

        return member_patch
