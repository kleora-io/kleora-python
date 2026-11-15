# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.me_app import MeApp


T = TypeVar("T", bound="MeEnvironment")


@_attrs_define
class MeEnvironment:
    """
    Attributes:
        app (MeApp):
        id (UUID):
        issuer (str):
        kind (str):
    """

    app: MeApp
    id: UUID
    issuer: str
    kind: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app = self.app.to_dict()

        id = str(self.id)

        issuer = self.issuer

        kind = self.kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app": app,
                "id": id,
                "issuer": issuer,
                "kind": kind,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.me_app import MeApp

        d = dict(src_dict)
        app = MeApp.from_dict(d.pop("app"))

        id = UUID(d.pop("id"))

        issuer = d.pop("issuer")

        kind = d.pop("kind")

        me_environment = cls(
            app=app,
            id=id,
            issuer=issuer,
            kind=kind,
        )

        me_environment.additional_properties = d
        return me_environment

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
