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

from ..models.setting_definition_patch_access import SettingDefinitionPatchAccess
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.setting_constraints import SettingConstraints


T = TypeVar("T", bound="SettingDefinitionPatch")


@_attrs_define
class SettingDefinitionPatch:
    """The body of `PATCH .../settings/definitions/{key}`.

    `key` and `type` are refused as immutable. `constraints` replaces the whole object, and `null`
    resets it to the type's defaults. `default: null` removes the default.

        Attributes:
            access (SettingDefinitionPatchAccess | Unset):
            constraints (None | SettingConstraints | Unset):
            default (bool | float | int | None | str | Unset):
            description (None | str | Unset):
            label (None | str | Unset):
    """

    access: SettingDefinitionPatchAccess | Unset = UNSET
    constraints: None | SettingConstraints | Unset = UNSET
    default: bool | float | int | None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    label: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.setting_constraints import SettingConstraints

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

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        field_dict: dict[str, Any] = {}

        field_dict.update({})
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
        _access = d.pop("access", UNSET)
        access: SettingDefinitionPatchAccess | Unset
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = SettingDefinitionPatchAccess(_access)

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

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        setting_definition_patch = cls(
            access=access,
            constraints=constraints,
            default=default,
            description=description,
            label=label,
        )

        return setting_definition_patch
