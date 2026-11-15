# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.email_kind_variables_kind import EmailKindVariablesKind

if TYPE_CHECKING:
    from ..models.email_variable import EmailVariable


T = TypeVar("T", bound="EmailKindVariables")


@_attrs_define
class EmailKindVariables:
    """The variables one kind of email may use.

    Attributes:
        kind (EmailKindVariablesKind):
        variables (list[EmailVariable]):
    """

    kind: EmailKindVariablesKind
    variables: list[EmailVariable]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        variables = []
        for variables_item_data in self.variables:
            variables_item = variables_item_data.to_dict()
            variables.append(variables_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "variables": variables,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.email_variable import EmailVariable

        d = dict(src_dict)
        kind = EmailKindVariablesKind(d.pop("kind"))

        variables = []
        _variables = d.pop("variables")
        for variables_item_data in _variables:
            variables_item = EmailVariable.from_dict(variables_item_data)

            variables.append(variables_item)

        email_kind_variables = cls(
            kind=kind,
            variables=variables,
        )

        email_kind_variables.additional_properties = d
        return email_kind_variables

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
