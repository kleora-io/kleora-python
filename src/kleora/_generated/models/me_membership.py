# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.me_account import MeAccount


T = TypeVar("T", bound="MeMembership")


@_attrs_define
class MeMembership:
    """One Account the console user may switch to (ADR 0010).

    Attributes:
        account (MeAccount):
        roles (list[str]):
        tenant_id (UUID):
    """

    account: MeAccount
    roles: list[str]
    tenant_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account = self.account.to_dict()

        roles = self.roles

        tenant_id = str(self.tenant_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account": account,
                "roles": roles,
                "tenant_id": tenant_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.me_account import MeAccount

        d = dict(src_dict)
        account = MeAccount.from_dict(d.pop("account"))

        roles = cast(list[str], d.pop("roles"))

        tenant_id = UUID(d.pop("tenant_id"))

        me_membership = cls(
            account=account,
            roles=roles,
            tenant_id=tenant_id,
        )

        me_membership.additional_properties = d
        return me_membership

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
