# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProblemError")


@_attrs_define
class ProblemError:
    """One field-level failure inside a `validation-error` problem.

    `field` is `null` for a failure that concerns the request as a whole rather than one field, such
    as a rule over two settings.

        Attributes:
            code (str):
            field (None | str):
            message (str):
            construct (None | str | Unset):
            line (int | None | Unset):
            offset (int | None | Unset):
            slug (None | str | Unset):
            tenant_id (None | Unset | UUID):
    """

    code: str
    field: None | str
    message: str
    construct: None | str | Unset = UNSET
    line: int | None | Unset = UNSET
    offset: int | None | Unset = UNSET
    slug: None | str | Unset = UNSET
    tenant_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        field: None | str
        field = self.field

        message = self.message

        construct: None | str | Unset
        if isinstance(self.construct, Unset):
            construct = UNSET
        else:
            construct = self.construct

        line: int | None | Unset
        if isinstance(self.line, Unset):
            line = UNSET
        else:
            line = self.line

        offset: int | None | Unset
        if isinstance(self.offset, Unset):
            offset = UNSET
        else:
            offset = self.offset

        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        elif isinstance(self.tenant_id, UUID):
            tenant_id = str(self.tenant_id)
        else:
            tenant_id = self.tenant_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "field": field,
                "message": message,
            }
        )
        if construct is not UNSET:
            field_dict["construct"] = construct
        if line is not UNSET:
            field_dict["line"] = line
        if offset is not UNSET:
            field_dict["offset"] = offset
        if slug is not UNSET:
            field_dict["slug"] = slug
        if tenant_id is not UNSET:
            field_dict["tenant_id"] = tenant_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        code = d.pop("code")

        def _parse_field(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        field = _parse_field(d.pop("field"))

        message = d.pop("message")

        def _parse_construct(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        construct = _parse_construct(d.pop("construct", UNSET))

        def _parse_line(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        line = _parse_line(d.pop("line", UNSET))

        def _parse_offset(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        offset = _parse_offset(d.pop("offset", UNSET))

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        def _parse_tenant_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tenant_id_type_0 = UUID(data)

                return tenant_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        tenant_id = _parse_tenant_id(d.pop("tenant_id", UNSET))

        problem_error = cls(
            code=code,
            field=field,
            message=message,
            construct=construct,
            line=line,
            offset=offset,
            slug=slug,
            tenant_id=tenant_id,
        )

        problem_error.additional_properties = d
        return problem_error

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
