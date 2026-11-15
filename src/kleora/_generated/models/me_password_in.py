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
    """The body of `POST /me/password`: the current password and the new one. Both are required.

    Neither is ever returned; the response is `204` with no body.

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
