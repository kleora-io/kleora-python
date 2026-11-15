# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiKeyIn")


@_attrs_define
class ApiKeyIn:
    """`POST /api/v1/environments/{environment_id}/api-keys`.

    `extra="forbid"` is the whole of the "not an input field" rule: `prefix`,
    `key`, `key_hash`, `status`, `environment_id` and `created_by` are 422 as
    unknown fields. The prefix in particular is never a caller's choice — it
    follows the environment's kind, which is what makes a `kl_test_` key
    structurally unable to reach production (api-keys.md §Format).

    The scope rules are not here. They are the resource's — the allowed set is
    the reserved permission table minus the account-level half — and they
    answer 422 `invalid-scope` rather than `validation-error`, which is a slug
    a schema cannot produce.

        Attributes:
            name (str):
            scopes (list[str]):
            expires_at (datetime.datetime | None | Unset):
    """

    name: str
    scopes: list[str]
    expires_at: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        scopes = self.scopes

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "scopes": scopes,
            }
        )
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        scopes = cast(list[str], d.pop("scopes"))

        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        api_key_in = cls(
            name=name,
            scopes=scopes,
            expires_at=expires_at,
        )

        return api_key_in
