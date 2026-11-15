# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="MePasswordIn")


@_attrs_define
class MePasswordIn:
    """`POST /me/password` — the person's own password change (`Q3-151`).

    Two fields, both required, and the current one is not optional on any path:
    users-and-credentials.md §"Password change (user-initiated)" asks for it, and
    it is what makes this a change rather than an administrator's set
    (`UserPasswordIn` above has no `current_password` precisely because an
    administrator does not know it).

    `extra="forbid"` for the reason that schema gives. Neither value is ever
    echoed: the response is `204` with no body.

        Attributes:
            current_password (str):
            new_password (str):
    """

    current_password: str
    new_password: str

    def to_dict(self) -> dict[str, Any]:
        current_password = self.current_password

        new_password = self.new_password

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "current_password": current_password,
                "new_password": new_password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        current_password = d.pop("current_password")

        new_password = d.pop("new_password")

        me_password_in = cls(
            current_password=current_password,
            new_password=new_password,
        )

        return me_password_in
