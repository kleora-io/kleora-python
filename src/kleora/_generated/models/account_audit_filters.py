# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.account_audit_filters_format import AccountAuditFiltersFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountAuditFilters")


@_attrs_define
class AccountAuditFilters:
    """The account endpoint's filters: `environment_id` as well.

    Only here, because it is the only endpoint whose scope spans more than one
    environment — and omitting it is what asks for every event of the Account,
    account-level ones included.

        Attributes:
            action (list[str] | None | Unset):
            actor_id (None | Unset | UUID):
            environment_id (None | Unset | UUID):
            format_ (AccountAuditFiltersFormat | Unset):  Default: AccountAuditFiltersFormat.JSON.
            from_ (datetime.datetime | None | Unset):
            target_id (None | Unset | UUID):
            tenant_id (None | Unset | UUID):
            to (datetime.datetime | None | Unset):
    """

    action: list[str] | None | Unset = UNSET
    actor_id: None | Unset | UUID = UNSET
    environment_id: None | Unset | UUID = UNSET
    format_: AccountAuditFiltersFormat | Unset = AccountAuditFiltersFormat.JSON
    from_: datetime.datetime | None | Unset = UNSET
    target_id: None | Unset | UUID = UNSET
    tenant_id: None | Unset | UUID = UNSET
    to: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action: list[str] | None | Unset
        if isinstance(self.action, Unset):
            action = UNSET
        elif isinstance(self.action, list):
            action = self.action

        else:
            action = self.action

        actor_id: None | str | Unset
        if isinstance(self.actor_id, Unset):
            actor_id = UNSET
        elif isinstance(self.actor_id, UUID):
            actor_id = str(self.actor_id)
        else:
            actor_id = self.actor_id

        environment_id: None | str | Unset
        if isinstance(self.environment_id, Unset):
            environment_id = UNSET
        elif isinstance(self.environment_id, UUID):
            environment_id = str(self.environment_id)
        else:
            environment_id = self.environment_id

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        from_: None | str | Unset
        if isinstance(self.from_, Unset):
            from_ = UNSET
        elif isinstance(self.from_, datetime.datetime):
            from_ = self.from_.isoformat()
        else:
            from_ = self.from_

        target_id: None | str | Unset
        if isinstance(self.target_id, Unset):
            target_id = UNSET
        elif isinstance(self.target_id, UUID):
            target_id = str(self.target_id)
        else:
            target_id = self.target_id

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        elif isinstance(self.tenant_id, UUID):
            tenant_id = str(self.tenant_id)
        else:
            tenant_id = self.tenant_id

        to: None | str | Unset
        if isinstance(self.to, Unset):
            to = UNSET
        elif isinstance(self.to, datetime.datetime):
            to = self.to.isoformat()
        else:
            to = self.to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if actor_id is not UNSET:
            field_dict["actor_id"] = actor_id
        if environment_id is not UNSET:
            field_dict["environment_id"] = environment_id
        if format_ is not UNSET:
            field_dict["format"] = format_
        if from_ is not UNSET:
            field_dict["from"] = from_
        if target_id is not UNSET:
            field_dict["target_id"] = target_id
        if tenant_id is not UNSET:
            field_dict["tenant_id"] = tenant_id
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_action(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                action_type_0 = cast(list[str], data)

                return action_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        action = _parse_action(d.pop("action", UNSET))

        def _parse_actor_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                actor_id_type_0 = UUID(data)

                return actor_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        actor_id = _parse_actor_id(d.pop("actor_id", UNSET))

        def _parse_environment_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                environment_id_type_0 = UUID(data)

                return environment_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        environment_id = _parse_environment_id(d.pop("environment_id", UNSET))

        _format_ = d.pop("format", UNSET)
        format_: AccountAuditFiltersFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = AccountAuditFiltersFormat(_format_)

        def _parse_from_(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                from_type_0 = datetime.datetime.fromisoformat(data)

                return from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        from_ = _parse_from_(d.pop("from", UNSET))

        def _parse_target_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                target_id_type_0 = UUID(data)

                return target_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        target_id = _parse_target_id(d.pop("target_id", UNSET))

        def _parse_tenant_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tenant_id_type_0 = UUID(data)

                return tenant_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        tenant_id = _parse_tenant_id(d.pop("tenant_id", UNSET))

        def _parse_to(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                to_type_0 = datetime.datetime.fromisoformat(data)

                return to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        to = _parse_to(d.pop("to", UNSET))

        account_audit_filters = cls(
            action=action,
            actor_id=actor_id,
            environment_id=environment_id,
            format_=format_,
            from_=from_,
            target_id=target_id,
            tenant_id=tenant_id,
            to=to,
        )

        account_audit_filters.additional_properties = d
        return account_audit_filters

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
