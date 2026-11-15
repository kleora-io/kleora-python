# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.user_in_locale_type_0 import UserInLocaleType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_in_metadata import UserInMetadata


T = TypeVar("T", bound="UserIn")


@_attrs_define
class UserIn:
    """The body of `POST /api/v1/environments/{environment_id}/users`.

    `id`, `status`, `has_password`, `email_verified_at`, `last_login_at` and `locked_until` are
    refused as unknown fields. `email_verified` marks the address verified, and `send_verification`
    emails a verification link; neither is a field of the user.

    `password` is optional, and is never returned.

        Attributes:
            email (str):
            email_verified (bool | Unset):  Default: False.
            locale (None | Unset | UserInLocaleType0):
            metadata (UserInMetadata | Unset):
            name (str | Unset):  Default: ''.
            password (None | str | Unset):
            send_verification (bool | Unset):  Default: False.
    """

    email: str
    email_verified: bool | Unset = False
    locale: None | Unset | UserInLocaleType0 = UNSET
    metadata: UserInMetadata | Unset = UNSET
    name: str | Unset = ""
    password: None | str | Unset = UNSET
    send_verification: bool | Unset = False

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        email_verified = self.email_verified

        locale: None | str | Unset
        if isinstance(self.locale, Unset):
            locale = UNSET
        elif isinstance(self.locale, UserInLocaleType0):
            locale = self.locale.value
        else:
            locale = self.locale

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        send_verification = self.send_verification

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "email": email,
            }
        )
        if email_verified is not UNSET:
            field_dict["email_verified"] = email_verified
        if locale is not UNSET:
            field_dict["locale"] = locale
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if password is not UNSET:
            field_dict["password"] = password
        if send_verification is not UNSET:
            field_dict["send_verification"] = send_verification

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.user_in_metadata import UserInMetadata

        d = dict(src_dict)
        email = d.pop("email")

        email_verified = d.pop("email_verified", UNSET)

        def _parse_locale(data: object) -> None | Unset | UserInLocaleType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                locale_type_0 = UserInLocaleType0(data)

                return locale_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserInLocaleType0, data)

        locale = _parse_locale(d.pop("locale", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: UserInMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = UserInMetadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))

        send_verification = d.pop("send_verification", UNSET)

        user_in = cls(
            email=email,
            email_verified=email_verified,
            locale=locale,
            metadata=metadata,
            name=name,
            password=password,
            send_verification=send_verification,
        )

        return user_in
