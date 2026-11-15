# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="BlockedByDisplay")


@_attrs_define
class BlockedByDisplay:
    """Who `blocked_by` names, resolved when the user is read.

    Read time, never write time — audit-log.md §"Naming the actor and the
    target" settles this for the audit surface and the reason is identical
    here: a name denormalised onto the blocked user's row at block time would
    **survive the erasure of the operator it names**. Resolution follows
    erasure automatically, so an erased operator shows as one.

    Two fields and no more. `users:read` reaches this, and what it is allowed
    past is "what identifies a subject" — the name, and the email that tells
    two people sharing one apart. Not the avatar, not the picture: this is one
    line of prose on a detail page, not a second User resource.

        Attributes:
            email (str):
            name (str):
    """

    email: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        email = d.pop("email")

        name = d.pop("name")

        blocked_by_display = cls(
            email=email,
            name=name,
        )

        blocked_by_display.additional_properties = d
        return blocked_by_display

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
