# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.invitation_out_status import InvitationOutStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invitation_inviter import InvitationInviter
    from ..models.invitation_role import InvitationRole


T = TypeVar("T", bound="InvitationOut")


@_attrs_define
class InvitationOut:
    """An Invitation as every read of it reports it.

    Attributes:
        created_at (datetime.datetime):
        email (str):
        expires_at (datetime.datetime):
        id (UUID):
        roles (list[InvitationRole]):
        status (InvitationOutStatus):
        tenant_id (UUID):
        accepted_at (datetime.datetime | None | Unset):
        invited_by (InvitationInviter | None | Unset):
        revoked_at (datetime.datetime | None | Unset):
    """

    created_at: datetime.datetime
    email: str
    expires_at: datetime.datetime
    id: UUID
    roles: list[InvitationRole]
    status: InvitationOutStatus
    tenant_id: UUID
    accepted_at: datetime.datetime | None | Unset = UNSET
    invited_by: InvitationInviter | None | Unset = UNSET
    revoked_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.invitation_inviter import InvitationInviter

        created_at = self.created_at.isoformat()

        email = self.email

        expires_at = self.expires_at.isoformat()

        id = str(self.id)

        roles = []
        for roles_item_data in self.roles:
            roles_item = roles_item_data.to_dict()
            roles.append(roles_item)

        status = self.status.value

        tenant_id = str(self.tenant_id)

        accepted_at: None | str | Unset
        if isinstance(self.accepted_at, Unset):
            accepted_at = UNSET
        elif isinstance(self.accepted_at, datetime.datetime):
            accepted_at = self.accepted_at.isoformat()
        else:
            accepted_at = self.accepted_at

        invited_by: dict[str, Any] | None | Unset
        if isinstance(self.invited_by, Unset):
            invited_by = UNSET
        elif isinstance(self.invited_by, InvitationInviter):
            invited_by = self.invited_by.to_dict()
        else:
            invited_by = self.invited_by

        revoked_at: None | str | Unset
        if isinstance(self.revoked_at, Unset):
            revoked_at = UNSET
        elif isinstance(self.revoked_at, datetime.datetime):
            revoked_at = self.revoked_at.isoformat()
        else:
            revoked_at = self.revoked_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "email": email,
                "expires_at": expires_at,
                "id": id,
                "roles": roles,
                "status": status,
                "tenant_id": tenant_id,
            }
        )
        if accepted_at is not UNSET:
            field_dict["accepted_at"] = accepted_at
        if invited_by is not UNSET:
            field_dict["invited_by"] = invited_by
        if revoked_at is not UNSET:
            field_dict["revoked_at"] = revoked_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.invitation_inviter import InvitationInviter
        from ..models.invitation_role import InvitationRole

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        email = d.pop("email")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        id = UUID(d.pop("id"))

        roles = []
        _roles = d.pop("roles")
        for roles_item_data in _roles:
            roles_item = InvitationRole.from_dict(roles_item_data)

            roles.append(roles_item)

        status = InvitationOutStatus(d.pop("status"))

        tenant_id = UUID(d.pop("tenant_id"))

        def _parse_accepted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                accepted_at_type_0 = datetime.datetime.fromisoformat(data)

                return accepted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        accepted_at = _parse_accepted_at(d.pop("accepted_at", UNSET))

        def _parse_invited_by(data: object) -> InvitationInviter | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invited_by_type_0 = InvitationInviter.from_dict(data)

                return invited_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvitationInviter | None | Unset, data)

        invited_by = _parse_invited_by(d.pop("invited_by", UNSET))

        def _parse_revoked_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                revoked_at_type_0 = datetime.datetime.fromisoformat(data)

                return revoked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        revoked_at = _parse_revoked_at(d.pop("revoked_at", UNSET))

        invitation_out = cls(
            created_at=created_at,
            email=email,
            expires_at=expires_at,
            id=id,
            roles=roles,
            status=status,
            tenant_id=tenant_id,
            accepted_at=accepted_at,
            invited_by=invited_by,
            revoked_at=revoked_at,
        )

        invitation_out.additional_properties = d
        return invitation_out

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
