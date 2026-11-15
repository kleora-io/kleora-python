# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.setting_definition_out_access import SettingDefinitionOutAccess
from ..models.setting_definition_out_type import SettingDefinitionOutType

if TYPE_CHECKING:
    from ..models.setting_constraints import SettingConstraints


T = TypeVar("T", bound="SettingDefinitionOut")


@_attrs_define
class SettingDefinitionOut:
    """One definition, as `GET …/settings/definitions/{key}` answers it.

    `value_count` is how many users hold a written value — what the console's
    confirmed delete names, since deleting the definition deletes exactly
    those rows (user-settings.md §Model).

        Attributes:
            access (SettingDefinitionOutAccess):
            constraints (SettingConstraints): The by-type constraints of one definition (user-settings.md §Model).

                One schema for all four types rather than a union, because which fields
                apply is decided by the sibling `type` field: `choices` for `enum` (1-32
                strings, each ≤ 64 chars), `max_length` for `string` (≤ 1024, default 256,
                always present on a stored definition), `min`/`max` for `number`, nothing
                for `boolean`. A field sent for another type is a 422 naming it; the
                server stores the constraints normalised, so a reader never has to know a
                default.
            created_at (datetime.datetime):
            default (bool | float | int | None | str):
            description (str):
            environment_id (UUID):
            id (UUID):
            key (str):
            label (str):
            type_ (SettingDefinitionOutType):
            updated_at (datetime.datetime):
            value_count (int):
    """

    access: SettingDefinitionOutAccess
    constraints: SettingConstraints
    created_at: datetime.datetime
    default: bool | float | int | None | str
    description: str
    environment_id: UUID
    id: UUID
    key: str
    label: str
    type_: SettingDefinitionOutType
    updated_at: datetime.datetime
    value_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access = self.access.value

        constraints = self.constraints.to_dict()

        created_at = self.created_at.isoformat()

        default: bool | float | int | None | str
        default = self.default

        description = self.description

        environment_id = str(self.environment_id)

        id = str(self.id)

        key = self.key

        label = self.label

        type_ = self.type_.value

        updated_at = self.updated_at.isoformat()

        value_count = self.value_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access": access,
                "constraints": constraints,
                "created_at": created_at,
                "default": default,
                "description": description,
                "environment_id": environment_id,
                "id": id,
                "key": key,
                "label": label,
                "type": type_,
                "updated_at": updated_at,
                "value_count": value_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.setting_constraints import SettingConstraints

        d = dict(src_dict)
        access = SettingDefinitionOutAccess(d.pop("access"))

        constraints = SettingConstraints.from_dict(d.pop("constraints"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_default(data: object) -> bool | float | int | None | str:
            if data is None:
                return data
            return cast(bool | float | int | None | str, data)

        default = _parse_default(d.pop("default"))

        description = d.pop("description")

        environment_id = UUID(d.pop("environment_id"))

        id = UUID(d.pop("id"))

        key = d.pop("key")

        label = d.pop("label")

        type_ = SettingDefinitionOutType(d.pop("type"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        value_count = d.pop("value_count")

        setting_definition_out = cls(
            access=access,
            constraints=constraints,
            created_at=created_at,
            default=default,
            description=description,
            environment_id=environment_id,
            id=id,
            key=key,
            label=label,
            type_=type_,
            updated_at=updated_at,
            value_count=value_count,
        )

        setting_definition_out.additional_properties = d
        return setting_definition_out

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
