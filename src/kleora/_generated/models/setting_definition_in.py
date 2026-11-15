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

from ..models.setting_definition_in_access import SettingDefinitionInAccess
from ..models.setting_definition_in_type import SettingDefinitionInType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.setting_constraints import SettingConstraints


T = TypeVar("T", bound="SettingDefinitionIn")


@_attrs_define
class SettingDefinitionIn:
    """`POST …/settings/definitions`.

    `key` and `type` are set here and never again (user-settings.md §Model).
    `constraints` may be omitted where the type needs none — a boolean always,
    a string or number falling back to its defaults — but an enum without
    `choices` is a 422, from the same validator every other write runs.

        Attributes:
            key (str):
            type_ (SettingDefinitionInType):
            access (SettingDefinitionInAccess | Unset):  Default: SettingDefinitionInAccess.USER_EDITABLE.
            constraints (None | SettingConstraints | Unset):
            default (bool | float | int | None | str | Unset):
            description (str | Unset):  Default: ''.
            label (str | Unset):  Default: ''.
    """

    key: str
    type_: SettingDefinitionInType
    access: SettingDefinitionInAccess | Unset = SettingDefinitionInAccess.USER_EDITABLE
    constraints: None | SettingConstraints | Unset = UNSET
    default: bool | float | int | None | str | Unset = UNSET
    description: str | Unset = ""
    label: str | Unset = ""

    def to_dict(self) -> dict[str, Any]:
        from ..models.setting_constraints import SettingConstraints

        key = self.key

        type_ = self.type_.value

        access: str | Unset = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.value

        constraints: dict[str, Any] | None | Unset
        if isinstance(self.constraints, Unset):
            constraints = UNSET
        elif isinstance(self.constraints, SettingConstraints):
            constraints = self.constraints.to_dict()
        else:
            constraints = self.constraints

        default: bool | float | int | None | str | Unset
        if isinstance(self.default, Unset):
            default = UNSET
        else:
            default = self.default

        description = self.description

        label = self.label

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "type": type_,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if constraints is not UNSET:
            field_dict["constraints"] = constraints
        if default is not UNSET:
            field_dict["default"] = default
        if description is not UNSET:
            field_dict["description"] = description
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.setting_constraints import SettingConstraints

        d = dict(src_dict)
        key = d.pop("key")

        type_ = SettingDefinitionInType(d.pop("type"))

        _access = d.pop("access", UNSET)
        access: SettingDefinitionInAccess | Unset
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = SettingDefinitionInAccess(_access)

        def _parse_constraints(data: object) -> None | SettingConstraints | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                constraints_type_0 = SettingConstraints.from_dict(data)

                return constraints_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SettingConstraints | Unset, data)

        constraints = _parse_constraints(d.pop("constraints", UNSET))

        def _parse_default(data: object) -> bool | float | int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | float | int | None | str | Unset, data)

        default = _parse_default(d.pop("default", UNSET))

        description = d.pop("description", UNSET)

        label = d.pop("label", UNSET)

        setting_definition_in = cls(
            key=key,
            type_=type_,
            access=access,
            constraints=constraints,
            default=default,
            description=description,
            label=label,
        )

        return setting_definition_in
