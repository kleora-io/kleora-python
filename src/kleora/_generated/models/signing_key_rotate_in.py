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

from ..types import UNSET, Unset

T = TypeVar("T", bound="SigningKeyRotateIn")


@_attrs_define
class SigningKeyRotateIn:
    """The optional body of `POST …/signing-keys/rotate`.

    `retire_immediately` is the key-compromise case (security-baseline.md): the
    previously active key is deleted in the rotation's own transaction rather
    than retired, so it leaves JWKS at once. The default is `false`, which is
    the ordinary rotation every environment does on a schedule.

        Attributes:
            retire_immediately (bool | Unset):  Default: False.
    """

    retire_immediately: bool | Unset = False

    def to_dict(self) -> dict[str, Any]:
        retire_immediately = self.retire_immediately

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if retire_immediately is not UNSET:
            field_dict["retire_immediately"] = retire_immediately

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        retire_immediately = d.pop("retire_immediately", UNSET)

        signing_key_rotate_in = cls(
            retire_immediately=retire_immediately,
        )

        return signing_key_rotate_in
