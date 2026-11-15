# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.export_audit_event import ExportAuditEvent
    from ..models.export_factor import ExportFactor
    from ..models.export_identity import ExportIdentity
    from ..models.export_membership import ExportMembership
    from ..models.export_session import ExportSession
    from ..models.user_out import UserOut


T = TypeVar("T", bound="UserExport")


@_attrs_define
class UserExport:
    """`GET …/users/{user_id}/export` (users-and-credentials.md §Export).

    One document, so that a subject access request is one call: the user
    record, the identities without their secrets, the MFA factors without their
    seeds, the memberships, the sessions, and the audit events where this user
    is actor or target — newest first, capped, with the cap reported rather
    than silently applied.

        Attributes:
            audit_events (list[ExportAuditEvent]):
            audit_events_truncated (bool):
            exported_at (datetime.datetime):
            identities (list[ExportIdentity]):
            memberships (list[ExportMembership]):
            mfa_factors (list[ExportFactor]):
            sessions (list[ExportSession]):
            user (UserOut): A User as every read of it reports it (users-and-credentials.md §API).

                Three fields are derived rather than stored. `status` folds `erased_at` in,
                because `erased` is a state a caller has to be able to see and not a value
                the column holds; `has_password` is whether a `password` Identity exists,
                which is the only thing a read ever says about a credential; and
                `mfa_enrolled` is whether a confirmed factor exists.
    """

    audit_events: list[ExportAuditEvent]
    audit_events_truncated: bool
    exported_at: datetime.datetime
    identities: list[ExportIdentity]
    memberships: list[ExportMembership]
    mfa_factors: list[ExportFactor]
    sessions: list[ExportSession]
    user: UserOut
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audit_events = []
        for audit_events_item_data in self.audit_events:
            audit_events_item = audit_events_item_data.to_dict()
            audit_events.append(audit_events_item)

        audit_events_truncated = self.audit_events_truncated

        exported_at = self.exported_at.isoformat()

        identities = []
        for identities_item_data in self.identities:
            identities_item = identities_item_data.to_dict()
            identities.append(identities_item)

        memberships = []
        for memberships_item_data in self.memberships:
            memberships_item = memberships_item_data.to_dict()
            memberships.append(memberships_item)

        mfa_factors = []
        for mfa_factors_item_data in self.mfa_factors:
            mfa_factors_item = mfa_factors_item_data.to_dict()
            mfa_factors.append(mfa_factors_item)

        sessions = []
        for sessions_item_data in self.sessions:
            sessions_item = sessions_item_data.to_dict()
            sessions.append(sessions_item)

        user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "audit_events": audit_events,
                "audit_events_truncated": audit_events_truncated,
                "exported_at": exported_at,
                "identities": identities,
                "memberships": memberships,
                "mfa_factors": mfa_factors,
                "sessions": sessions,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.export_audit_event import ExportAuditEvent
        from ..models.export_factor import ExportFactor
        from ..models.export_identity import ExportIdentity
        from ..models.export_membership import ExportMembership
        from ..models.export_session import ExportSession
        from ..models.user_out import UserOut

        d = dict(src_dict)
        audit_events = []
        _audit_events = d.pop("audit_events")
        for audit_events_item_data in _audit_events:
            audit_events_item = ExportAuditEvent.from_dict(audit_events_item_data)

            audit_events.append(audit_events_item)

        audit_events_truncated = d.pop("audit_events_truncated")

        exported_at = datetime.datetime.fromisoformat(d.pop("exported_at"))

        identities = []
        _identities = d.pop("identities")
        for identities_item_data in _identities:
            identities_item = ExportIdentity.from_dict(identities_item_data)

            identities.append(identities_item)

        memberships = []
        _memberships = d.pop("memberships")
        for memberships_item_data in _memberships:
            memberships_item = ExportMembership.from_dict(memberships_item_data)

            memberships.append(memberships_item)

        mfa_factors = []
        _mfa_factors = d.pop("mfa_factors")
        for mfa_factors_item_data in _mfa_factors:
            mfa_factors_item = ExportFactor.from_dict(mfa_factors_item_data)

            mfa_factors.append(mfa_factors_item)

        sessions = []
        _sessions = d.pop("sessions")
        for sessions_item_data in _sessions:
            sessions_item = ExportSession.from_dict(sessions_item_data)

            sessions.append(sessions_item)

        user = UserOut.from_dict(d.pop("user"))

        user_export = cls(
            audit_events=audit_events,
            audit_events_truncated=audit_events_truncated,
            exported_at=exported_at,
            identities=identities,
            memberships=memberships,
            mfa_factors=mfa_factors,
            sessions=sessions,
            user=user,
        )

        user_export.additional_properties = d
        return user_export

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
