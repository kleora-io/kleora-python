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

from ..models.user_out_avatar_color import UserOutAvatarColor
from ..models.user_out_locale_type_0 import UserOutLocaleType0
from ..models.user_out_status import UserOutStatus

if TYPE_CHECKING:
    from ..models.blocked_by import BlockedBy
    from ..models.user_out_metadata import UserOutMetadata


T = TypeVar("T", bound="UserOut")


@_attrs_define
class UserOut:
    """A User as every read of it reports it (users-and-credentials.md §API).

    Three fields are derived rather than stored. `status` folds `erased_at` in,
    because `erased` is a state a caller has to be able to see and not a value
    the column holds; `has_password` is whether a `password` Identity exists,
    which is the only thing a read ever says about a credential; and
    `mfa_enrolled` is whether a confirmed factor exists.

        Attributes:
            avatar_color (UserOutAvatarColor):
            belongs_to_another_account (bool):
            blocked_at (datetime.datetime | None):
            blocked_by (BlockedBy | None):
            blocked_reason (None | str):
            created_at (datetime.datetime):
            email (str):
            email_verified_at (datetime.datetime | None):
            environment_id (UUID):
            has_password (bool):
            id (UUID):
            last_login_at (datetime.datetime | None):
            locale (None | UserOutLocaleType0):
            locked_until (datetime.datetime | None):
            merged_into (None | UUID):
            metadata (UserOutMetadata):
            mfa_enrolled (bool):
            name (str):
            picture_url (None | str):
            status (UserOutStatus):
            updated_at (datetime.datetime):
    """

    avatar_color: UserOutAvatarColor
    belongs_to_another_account: bool
    blocked_at: datetime.datetime | None
    blocked_by: BlockedBy | None
    blocked_reason: None | str
    created_at: datetime.datetime
    email: str
    email_verified_at: datetime.datetime | None
    environment_id: UUID
    has_password: bool
    id: UUID
    last_login_at: datetime.datetime | None
    locale: None | UserOutLocaleType0
    locked_until: datetime.datetime | None
    merged_into: None | UUID
    metadata: UserOutMetadata
    mfa_enrolled: bool
    name: str
    picture_url: None | str
    status: UserOutStatus
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.blocked_by import BlockedBy

        avatar_color = self.avatar_color.value

        belongs_to_another_account = self.belongs_to_another_account

        blocked_at: None | str
        if isinstance(self.blocked_at, datetime.datetime):
            blocked_at = self.blocked_at.isoformat()
        else:
            blocked_at = self.blocked_at

        blocked_by: dict[str, Any] | None
        if isinstance(self.blocked_by, BlockedBy):
            blocked_by = self.blocked_by.to_dict()
        else:
            blocked_by = self.blocked_by

        blocked_reason: None | str
        blocked_reason = self.blocked_reason

        created_at = self.created_at.isoformat()

        email = self.email

        email_verified_at: None | str
        if isinstance(self.email_verified_at, datetime.datetime):
            email_verified_at = self.email_verified_at.isoformat()
        else:
            email_verified_at = self.email_verified_at

        environment_id = str(self.environment_id)

        has_password = self.has_password

        id = str(self.id)

        last_login_at: None | str
        if isinstance(self.last_login_at, datetime.datetime):
            last_login_at = self.last_login_at.isoformat()
        else:
            last_login_at = self.last_login_at

        locale: None | str
        if isinstance(self.locale, UserOutLocaleType0):
            locale = self.locale.value
        else:
            locale = self.locale

        locked_until: None | str
        if isinstance(self.locked_until, datetime.datetime):
            locked_until = self.locked_until.isoformat()
        else:
            locked_until = self.locked_until

        merged_into: None | str
        if isinstance(self.merged_into, UUID):
            merged_into = str(self.merged_into)
        else:
            merged_into = self.merged_into

        metadata = self.metadata.to_dict()

        mfa_enrolled = self.mfa_enrolled

        name = self.name

        picture_url: None | str
        picture_url = self.picture_url

        status = self.status.value

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "avatar_color": avatar_color,
                "belongs_to_another_account": belongs_to_another_account,
                "blocked_at": blocked_at,
                "blocked_by": blocked_by,
                "blocked_reason": blocked_reason,
                "created_at": created_at,
                "email": email,
                "email_verified_at": email_verified_at,
                "environment_id": environment_id,
                "has_password": has_password,
                "id": id,
                "last_login_at": last_login_at,
                "locale": locale,
                "locked_until": locked_until,
                "merged_into": merged_into,
                "metadata": metadata,
                "mfa_enrolled": mfa_enrolled,
                "name": name,
                "picture_url": picture_url,
                "status": status,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.blocked_by import BlockedBy
        from ..models.user_out_metadata import UserOutMetadata

        d = dict(src_dict)
        avatar_color = UserOutAvatarColor(d.pop("avatar_color"))

        belongs_to_another_account = d.pop("belongs_to_another_account")

        def _parse_blocked_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                blocked_at_type_0 = datetime.datetime.fromisoformat(data)

                return blocked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        blocked_at = _parse_blocked_at(d.pop("blocked_at"))

        def _parse_blocked_by(data: object) -> BlockedBy | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                blocked_by_type_0 = BlockedBy.from_dict(data)

                return blocked_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlockedBy | None, data)

        blocked_by = _parse_blocked_by(d.pop("blocked_by"))

        def _parse_blocked_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        blocked_reason = _parse_blocked_reason(d.pop("blocked_reason"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        email = d.pop("email")

        def _parse_email_verified_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                email_verified_at_type_0 = datetime.datetime.fromisoformat(data)

                return email_verified_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        email_verified_at = _parse_email_verified_at(d.pop("email_verified_at"))

        environment_id = UUID(d.pop("environment_id"))

        has_password = d.pop("has_password")

        id = UUID(d.pop("id"))

        def _parse_last_login_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_login_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_login_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_login_at = _parse_last_login_at(d.pop("last_login_at"))

        def _parse_locale(data: object) -> None | UserOutLocaleType0:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                locale_type_0 = UserOutLocaleType0(data)

                return locale_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UserOutLocaleType0, data)

        locale = _parse_locale(d.pop("locale"))

        def _parse_locked_until(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                locked_until_type_0 = datetime.datetime.fromisoformat(data)

                return locked_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        locked_until = _parse_locked_until(d.pop("locked_until"))

        def _parse_merged_into(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                merged_into_type_0 = UUID(data)

                return merged_into_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        merged_into = _parse_merged_into(d.pop("merged_into"))

        metadata = UserOutMetadata.from_dict(d.pop("metadata"))

        mfa_enrolled = d.pop("mfa_enrolled")

        name = d.pop("name")

        def _parse_picture_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        picture_url = _parse_picture_url(d.pop("picture_url"))

        status = UserOutStatus(d.pop("status"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        user_out = cls(
            avatar_color=avatar_color,
            belongs_to_another_account=belongs_to_another_account,
            blocked_at=blocked_at,
            blocked_by=blocked_by,
            blocked_reason=blocked_reason,
            created_at=created_at,
            email=email,
            email_verified_at=email_verified_at,
            environment_id=environment_id,
            has_password=has_password,
            id=id,
            last_login_at=last_login_at,
            locale=locale,
            locked_until=locked_until,
            merged_into=merged_into,
            metadata=metadata,
            mfa_enrolled=mfa_enrolled,
            name=name,
            picture_url=picture_url,
            status=status,
            updated_at=updated_at,
        )

        user_out.additional_properties = d
        return user_out

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
