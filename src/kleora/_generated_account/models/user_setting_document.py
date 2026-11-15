# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed self-service API document
# (https://id.kleora.eu/account/v1/openapi.json). `kleora.account` wraps this tree; nothing outside the
# package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.user_setting_type import UserSettingType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_setting_document_constraints import (
        UserSettingDocumentConstraints,
    )


T = TypeVar("T", bound="UserSettingDocument")


@_attrs_define
class UserSettingDocument:
    """One definition-with-value row (user-settings.md §API, public surface).

    Explicit nulls: a `value` of `null` means "no stored value and no default",
    which is the answer rather than the absence of one. `value` is otherwise the
    user's written value where one exists and the definition's default where
    not — the same resolution the management surface serves an operator.

    `constraints` is the stored, normalised record whose by-type shape
    user-settings.md §Model fixes: `choices` for `enum`, `max_length` for
    `string` (always present, the default made explicit), `min`/`max` for
    `number`, `{}` for `boolean`. The member list is the spec's — key, type,
    constraints, label, value — and carries no `access`: the listing only ever
    holds the two visible levels, and "read-only" is the `PUT`'s `403` to give.

        Attributes:
            constraints (UserSettingDocumentConstraints):
            key (str):
            label (str):
            type_ (UserSettingType):
            value (bool | float | int | None | str | Unset):
    """

    constraints: UserSettingDocumentConstraints
    key: str
    label: str
    type_: UserSettingType
    value: bool | float | int | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        constraints = self.constraints.to_dict()

        key = self.key

        label = self.label

        type_ = self.type_.value

        value: bool | float | int | None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "constraints": constraints,
                "key": key,
                "label": label,
                "type": type_,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.user_setting_document_constraints import (
            UserSettingDocumentConstraints,
        )

        d = dict(src_dict)
        constraints = UserSettingDocumentConstraints.from_dict(d.pop("constraints"))

        key = d.pop("key")

        label = d.pop("label")

        type_ = UserSettingType(d.pop("type"))

        def _parse_value(data: object) -> bool | float | int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | float | int | None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        user_setting_document = cls(
            constraints=constraints,
            key=key,
            label=label,
            type_=type_,
            value=value,
        )

        user_setting_document.additional_properties = d
        return user_setting_document

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
