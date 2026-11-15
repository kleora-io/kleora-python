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

if TYPE_CHECKING:
    from ..models.email_kind_variables import EmailKindVariables


T = TypeVar("T", bound="EmailVariables")


@_attrs_define
class EmailVariables:
    """The body of `GET .../email-templates/variables`: the variables each kind of email may use.

    Samples use the environment's own App name and issuer.

        Attributes:
            kinds (list[EmailKindVariables]):
    """

    kinds: list[EmailKindVariables]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kinds = []
        for kinds_item_data in self.kinds:
            kinds_item = kinds_item_data.to_dict()
            kinds.append(kinds_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kinds": kinds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.email_kind_variables import EmailKindVariables

        d = dict(src_dict)
        kinds = []
        _kinds = d.pop("kinds")
        for kinds_item_data in _kinds:
            kinds_item = EmailKindVariables.from_dict(kinds_item_data)

            kinds.append(kinds_item)

        email_variables = cls(
            kinds=kinds,
        )

        email_variables.additional_properties = d
        return email_variables

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
