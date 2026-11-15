# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditDisplay")


@_attrs_define
class AuditDisplay:
    """Who or what an `actor`/`target` id names, resolved when the page is
    read — never captured when the event was written (audit-log.md
    §"Naming the actor and the target").

    Bounded by `audit:read`, not `users:read`: a name, the email that tells
    two people sharing one apart, and the avatar — nothing else a User
    resource carries. Every field below is set only when it applies to what
    was resolved: `email`, `avatar_color` and `picture_url` never appear on a
    tenant's `display`, and nothing but `removed` appears when the id no
    longer resolves to any row (a hard-deleted Tenant, mainly — a User is
    only ever erased in place and always resolves). The three audit-events
    endpoints declare `exclude_unset=True` for exactly this: a field the
    resolver did not set is absent from the response, not `null`.

        Attributes:
            avatar_color (None | str | Unset):
            email (None | str | Unset):
            name (None | str | Unset):
            picture_url (None | str | Unset):
            removed (bool | None | Unset):
    """

    avatar_color: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    picture_url: None | str | Unset = UNSET
    removed: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar_color: None | str | Unset
        if isinstance(self.avatar_color, Unset):
            avatar_color = UNSET
        else:
            avatar_color = self.avatar_color

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        picture_url: None | str | Unset
        if isinstance(self.picture_url, Unset):
            picture_url = UNSET
        else:
            picture_url = self.picture_url

        removed: bool | None | Unset
        if isinstance(self.removed, Unset):
            removed = UNSET
        else:
            removed = self.removed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar_color is not UNSET:
            field_dict["avatar_color"] = avatar_color
        if email is not UNSET:
            field_dict["email"] = email
        if name is not UNSET:
            field_dict["name"] = name
        if picture_url is not UNSET:
            field_dict["picture_url"] = picture_url
        if removed is not UNSET:
            field_dict["removed"] = removed

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_avatar_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_color = _parse_avatar_color(d.pop("avatar_color", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_picture_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        picture_url = _parse_picture_url(d.pop("picture_url", UNSET))

        def _parse_removed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        removed = _parse_removed(d.pop("removed", UNSET))

        audit_display = cls(
            avatar_color=avatar_color,
            email=email,
            name=name,
            picture_url=picture_url,
            removed=removed,
        )

        audit_display.additional_properties = d
        return audit_display

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
