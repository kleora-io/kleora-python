# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.me_account import MeAccount
    from ..models.me_environment import MeEnvironment
    from ..models.me_membership import MeMembership
    from ..models.me_principal import MePrincipal
    from ..models.me_tenant import MeTenant


T = TypeVar("T", bound="MeOut")


@_attrs_define
class MeOut:
    """Everything a caller can learn about itself (management-api.md §`GET /me`).

    Attributes:
        permissions (list[str]):
        principal (MePrincipal):
        account (MeAccount | None | Unset):
        account_tenant_permissions (list[str] | Unset):
        environment (MeEnvironment | None | Unset):
        memberships (list[MeMembership] | Unset):
        tenant (MeTenant | None | Unset):
    """

    permissions: list[str]
    principal: MePrincipal
    account: MeAccount | None | Unset = UNSET
    account_tenant_permissions: list[str] | Unset = UNSET
    environment: MeEnvironment | None | Unset = UNSET
    memberships: list[MeMembership] | Unset = UNSET
    tenant: MeTenant | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.me_account import MeAccount
        from ..models.me_environment import MeEnvironment
        from ..models.me_tenant import MeTenant

        permissions = self.permissions

        principal = self.principal.to_dict()

        account: dict[str, Any] | None | Unset
        if isinstance(self.account, Unset):
            account = UNSET
        elif isinstance(self.account, MeAccount):
            account = self.account.to_dict()
        else:
            account = self.account

        account_tenant_permissions: list[str] | Unset = UNSET
        if not isinstance(self.account_tenant_permissions, Unset):
            account_tenant_permissions = self.account_tenant_permissions

        environment: dict[str, Any] | None | Unset
        if isinstance(self.environment, Unset):
            environment = UNSET
        elif isinstance(self.environment, MeEnvironment):
            environment = self.environment.to_dict()
        else:
            environment = self.environment

        memberships: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.memberships, Unset):
            memberships = []
            for memberships_item_data in self.memberships:
                memberships_item = memberships_item_data.to_dict()
                memberships.append(memberships_item)

        tenant: dict[str, Any] | None | Unset
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, MeTenant):
            tenant = self.tenant.to_dict()
        else:
            tenant = self.tenant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "permissions": permissions,
                "principal": principal,
            }
        )
        if account is not UNSET:
            field_dict["account"] = account
        if account_tenant_permissions is not UNSET:
            field_dict["account_tenant_permissions"] = account_tenant_permissions
        if environment is not UNSET:
            field_dict["environment"] = environment
        if memberships is not UNSET:
            field_dict["memberships"] = memberships
        if tenant is not UNSET:
            field_dict["tenant"] = tenant

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.me_account import MeAccount
        from ..models.me_environment import MeEnvironment
        from ..models.me_membership import MeMembership
        from ..models.me_principal import MePrincipal
        from ..models.me_tenant import MeTenant

        d = dict(src_dict)
        permissions = cast(list[str], d.pop("permissions"))

        principal = MePrincipal.from_dict(d.pop("principal"))

        def _parse_account(data: object) -> MeAccount | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                account_type_0 = MeAccount.from_dict(data)

                return account_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MeAccount | None | Unset, data)

        account = _parse_account(d.pop("account", UNSET))

        account_tenant_permissions = cast(
            list[str], d.pop("account_tenant_permissions", UNSET)
        )

        def _parse_environment(data: object) -> MeEnvironment | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                environment_type_0 = MeEnvironment.from_dict(data)

                return environment_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MeEnvironment | None | Unset, data)

        environment = _parse_environment(d.pop("environment", UNSET))

        _memberships = d.pop("memberships", UNSET)
        memberships: list[MeMembership] | Unset = UNSET
        if _memberships is not UNSET:
            memberships = []
            for memberships_item_data in _memberships:
                memberships_item = MeMembership.from_dict(memberships_item_data)

                memberships.append(memberships_item)

        def _parse_tenant(data: object) -> MeTenant | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tenant_type_0 = MeTenant.from_dict(data)

                return tenant_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MeTenant | None | Unset, data)

        tenant = _parse_tenant(d.pop("tenant", UNSET))

        me_out = cls(
            permissions=permissions,
            principal=principal,
            account=account,
            account_tenant_permissions=account_tenant_permissions,
            environment=environment,
            memberships=memberships,
            tenant=tenant,
        )

        me_out.additional_properties = d
        return me_out

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
