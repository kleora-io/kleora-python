# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    Literal,
    TypeVar,
    cast,
)
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.user_filters_mfa_type_0 import UserFiltersMfaType0
from ..models.user_filters_status_type_0 import UserFiltersStatusType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserFilters")


@_attrs_define
class UserFilters:
    """The six filters of `GET .../users`.

    `tenant_id` narrows the list to members of one tenant of this environment.

        Attributes:
            email (None | str | Unset):
            mfa (None | Unset | UserFiltersMfaType0):
            q (None | str | Unset):
            session (Literal['active'] | None | Unset):
            status (None | Unset | UserFiltersStatusType0):
            tenant_id (None | Unset | UUID):
    """

    email: None | str | Unset = UNSET
    mfa: None | Unset | UserFiltersMfaType0 = UNSET
    q: None | str | Unset = UNSET
    session: Literal["active"] | None | Unset = UNSET
    status: None | Unset | UserFiltersStatusType0 = UNSET
    tenant_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        mfa: None | str | Unset
        if isinstance(self.mfa, Unset):
            mfa = UNSET
        elif isinstance(self.mfa, UserFiltersMfaType0):
            mfa = self.mfa.value
        else:
            mfa = self.mfa

        q: None | str | Unset
        if isinstance(self.q, Unset):
            q = UNSET
        else:
            q = self.q

        session: Literal["active"] | None | Unset
        if isinstance(self.session, Unset):
            session = UNSET
        else:
            session = self.session

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, UserFiltersStatusType0):
            status = self.status.value
        else:
            status = self.status

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        elif isinstance(self.tenant_id, UUID):
            tenant_id = str(self.tenant_id)
        else:
            tenant_id = self.tenant_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if mfa is not UNSET:
            field_dict["mfa"] = mfa
        if q is not UNSET:
            field_dict["q"] = q
        if session is not UNSET:
            field_dict["session"] = session
        if status is not UNSET:
            field_dict["status"] = status
        if tenant_id is not UNSET:
            field_dict["tenant_id"] = tenant_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_mfa(data: object) -> None | Unset | UserFiltersMfaType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mfa_type_0 = UserFiltersMfaType0(data)

                return mfa_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserFiltersMfaType0, data)

        mfa = _parse_mfa(d.pop("mfa", UNSET))

        def _parse_q(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        q = _parse_q(d.pop("q", UNSET))

        def _parse_session(data: object) -> Literal["active"] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            session_type_0 = cast(Literal["active"], data)
            if session_type_0 != "active":
                raise ValueError(
                    f"session_type_0 must match const 'active', got '{session_type_0}'"
                )
            return session_type_0
            return cast(Literal["active"] | None | Unset, data)

        session = _parse_session(d.pop("session", UNSET))

        def _parse_status(data: object) -> None | Unset | UserFiltersStatusType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = UserFiltersStatusType0(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserFiltersStatusType0, data)

        status = _parse_status(d.pop("status", UNSET))

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

        user_filters = cls(
            email=email,
            mfa=mfa,
            q=q,
            session=session,
            status=status,
            tenant_id=tenant_id,
        )

        user_filters.additional_properties = d
        return user_filters

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
