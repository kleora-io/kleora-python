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

T = TypeVar("T", bound="UserPasswordIn")


@_attrs_define
class UserPasswordIn:
    """`POST …/users/{user_id}/password` — one field, and no response body.

    A schema of its own rather than a bare string, so the document names the
    property and a generated client sends `{"password": "…"}` rather than a
    JSON scalar.

        Attributes:
            password (str):
    """

    password: str

    def to_dict(self) -> dict[str, Any]:
        password = self.password

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "password": password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        password = d.pop("password")

        user_password_in = cls(
            password=password,
        )

        return user_password_in
