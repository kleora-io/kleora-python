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

from ..models.user_patch_locale_type_0 import UserPatchLocaleType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_patch_metadata import UserPatchMetadata


T = TypeVar("T", bound="UserPatch")


@_attrs_define
class UserPatch:
    """The body of `PATCH /api/v1/environments/{environment_id}/users/{user_id}`.

    `picture_url` and `locale` can be cleared with `null`; `email`, `name` and `metadata` cannot
    (use `""` for no name and `{}` for no metadata).

    `email_verified: true` marks the address verified, and suppresses the verification email an
    address change would otherwise send; `false` marks it unverified. To set a password, use `POST
    .../users/{user_id}/password`. `status` cannot be changed here: sending it is refused as
    immutable; use `block` and `unblock`.

        Attributes:
            email (str | Unset):
            email_verified (bool | Unset):
            locale (None | Unset | UserPatchLocaleType0):
            metadata (UserPatchMetadata | Unset):
            name (str | Unset):
            picture_url (None | str | Unset):
    """

    email: str | Unset = UNSET
    email_verified: bool | Unset = UNSET
    locale: None | Unset | UserPatchLocaleType0 = UNSET
    metadata: UserPatchMetadata | Unset = UNSET
    name: str | Unset = UNSET
    picture_url: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        email_verified = self.email_verified

        locale: None | str | Unset
        if isinstance(self.locale, Unset):
            locale = UNSET
        elif isinstance(self.locale, UserPatchLocaleType0):
            locale = self.locale.value
        else:
            locale = self.locale

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name

        picture_url: None | str | Unset
        if isinstance(self.picture_url, Unset):
            picture_url = UNSET
        else:
            picture_url = self.picture_url

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if email_verified is not UNSET:
            field_dict["email_verified"] = email_verified
        if locale is not UNSET:
            field_dict["locale"] = locale
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if picture_url is not UNSET:
            field_dict["picture_url"] = picture_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.user_patch_metadata import UserPatchMetadata

        d = dict(src_dict)
        email = d.pop("email", UNSET)

        email_verified = d.pop("email_verified", UNSET)

        def _parse_locale(data: object) -> None | Unset | UserPatchLocaleType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                locale_type_0 = UserPatchLocaleType0(data)

                return locale_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserPatchLocaleType0, data)

        locale = _parse_locale(d.pop("locale", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: UserPatchMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = UserPatchMetadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        def _parse_picture_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        picture_url = _parse_picture_url(d.pop("picture_url", UNSET))

        user_patch = cls(
            email=email,
            email_verified=email_verified,
            locale=locale,
            metadata=metadata,
            name=name,
            picture_url=picture_url,
        )

        return user_patch
