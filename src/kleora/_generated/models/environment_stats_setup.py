# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="EnvironmentStatsSetup")


@_attrs_define
class EnvironmentStatsSetup:
    """The four "is this App set up" facts behind the overview's checklist.

    Booleans rather than counts: the checklist asks whether a thing has ever
    happened, and it disappears when all four are true.

        Attributes:
            callback_registered (bool):
            custom_branding (bool):
            first_login (bool):
            first_user_created (bool):
    """

    callback_registered: bool
    custom_branding: bool
    first_login: bool
    first_user_created: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        callback_registered = self.callback_registered

        custom_branding = self.custom_branding

        first_login = self.first_login

        first_user_created = self.first_user_created

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "callback_registered": callback_registered,
                "custom_branding": custom_branding,
                "first_login": first_login,
                "first_user_created": first_user_created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        callback_registered = d.pop("callback_registered")

        custom_branding = d.pop("custom_branding")

        first_login = d.pop("first_login")

        first_user_created = d.pop("first_user_created")

        environment_stats_setup = cls(
            callback_registered=callback_registered,
            custom_branding=custom_branding,
            first_login=first_login,
            first_user_created=first_user_created,
        )

        environment_stats_setup.additional_properties = d
        return environment_stats_setup

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
