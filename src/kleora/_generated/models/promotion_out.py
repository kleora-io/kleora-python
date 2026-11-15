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
    from ..models.promotion_branding import PromotionBranding
    from ..models.promotion_identity_providers import PromotionIdentityProviders
    from ..models.promotion_resource_diff import PromotionResourceDiff
    from ..models.promotion_setting_change import PromotionSettingChange


T = TypeVar("T", bound="PromotionOut")


@_attrs_define
class PromotionOut:
    """A summary of what a promotion changed, or would change.

    `applied` is `false` only for a dry run.

        Attributes:
            applied (bool):
            branding (PromotionBranding): `{"changed": true}` when the branding record differs. The diff never includes the
                values
                themselves.
            dry_run (bool):
            email_templates (PromotionResourceDiff): What a promotion did to one kind of resource, matched by key.

                `created` and `updated` name the resources by their key: a permission by `name`, a role by
                `slug`, a template by `kind:locale`. `unchanged` counts the ones that matched and did not
                change. Resources that exist only in production are not listed: promotion never deletes.
            identity_providers (PromotionIdentityProviders): Which identity provider kinds each environment has configured.

                Promotion never copies identity providers, because their credentials belong to one environment.
                `sandbox_only` names the providers configured in sandbox but not in production, and `promoted`
                is always `false`.
            permissions (PromotionResourceDiff): What a promotion did to one kind of resource, matched by key.

                `created` and `updated` name the resources by their key: a permission by `name`, a role by
                `slug`, a template by `kind:locale`. `unchanged` counts the ones that matched and did not
                change. Resources that exist only in production are not listed: promotion never deletes.
            roles (PromotionResourceDiff): What a promotion did to one kind of resource, matched by key.

                `created` and `updated` name the resources by their key: a permission by `name`, a role by
                `slug`, a template by `kind:locale`. `unchanged` counts the ones that matched and did not
                change. Resources that exist only in production are not listed: promotion never deletes.
            setting_definitions (PromotionResourceDiff): What a promotion did to one kind of resource, matched by key.

                `created` and `updated` name the resources by their key: a permission by `name`, a role by
                `slug`, a template by `kind:locale`. `unchanged` counts the ones that matched and did not
                change. Resources that exist only in production are not listed: promotion never deletes.
            settings (list[PromotionSettingChange]):
    """

    applied: bool
    branding: PromotionBranding
    dry_run: bool
    email_templates: PromotionResourceDiff
    identity_providers: PromotionIdentityProviders
    permissions: PromotionResourceDiff
    roles: PromotionResourceDiff
    setting_definitions: PromotionResourceDiff
    settings: list[PromotionSettingChange]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applied = self.applied

        branding = self.branding.to_dict()

        dry_run = self.dry_run

        email_templates = self.email_templates.to_dict()

        identity_providers = self.identity_providers.to_dict()

        permissions = self.permissions.to_dict()

        roles = self.roles.to_dict()

        setting_definitions = self.setting_definitions.to_dict()

        settings = []
        for settings_item_data in self.settings:
            settings_item = settings_item_data.to_dict()
            settings.append(settings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "applied": applied,
                "branding": branding,
                "dry_run": dry_run,
                "email_templates": email_templates,
                "identity_providers": identity_providers,
                "permissions": permissions,
                "roles": roles,
                "setting_definitions": setting_definitions,
                "settings": settings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.promotion_branding import PromotionBranding
        from ..models.promotion_identity_providers import PromotionIdentityProviders
        from ..models.promotion_resource_diff import PromotionResourceDiff
        from ..models.promotion_setting_change import PromotionSettingChange

        d = dict(src_dict)
        applied = d.pop("applied")

        branding = PromotionBranding.from_dict(d.pop("branding"))

        dry_run = d.pop("dry_run")

        email_templates = PromotionResourceDiff.from_dict(d.pop("email_templates"))

        identity_providers = PromotionIdentityProviders.from_dict(
            d.pop("identity_providers")
        )

        permissions = PromotionResourceDiff.from_dict(d.pop("permissions"))

        roles = PromotionResourceDiff.from_dict(d.pop("roles"))

        setting_definitions = PromotionResourceDiff.from_dict(
            d.pop("setting_definitions")
        )

        settings = []
        _settings = d.pop("settings")
        for settings_item_data in _settings:
            settings_item = PromotionSettingChange.from_dict(settings_item_data)

            settings.append(settings_item)

        promotion_out = cls(
            applied=applied,
            branding=branding,
            dry_run=dry_run,
            email_templates=email_templates,
            identity_providers=identity_providers,
            permissions=permissions,
            roles=roles,
            setting_definitions=setting_definitions,
            settings=settings,
        )

        promotion_out.additional_properties = d
        return promotion_out

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
