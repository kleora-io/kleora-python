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

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvitationIn")


@_attrs_define
class InvitationIn:
    """The body of `POST /api/v1/tenants/{tenant_id}/invitations`.

    `email` is validated by the same rules as a user's address. `roles` is a list of role ids,
    validated as `POST /tenants/{tenant_id}/members` validates them, and empty by default.

        Attributes:
            email (str):
            roles (list[UUID] | Unset):
    """

    email: str
    roles: list[UUID] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        roles: list[str] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = str(roles_item_data)
                roles.append(roles_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "email": email,
            }
        )
        if roles is not UNSET:
            field_dict["roles"] = roles

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        email = d.pop("email")

        _roles = d.pop("roles", UNSET)
        roles: list[UUID] | Unset = UNSET
        if _roles is not UNSET:
            roles = []
            for roles_item_data in _roles:
                roles_item = UUID(roles_item_data)

                roles.append(roles_item)

        invitation_in = cls(
            email=email,
            roles=roles,
        )

        return invitation_in
