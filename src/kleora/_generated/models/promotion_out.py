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
    """The diff summary environments.md §Promotion prints.

    `applied` is false only for a dry run, and the two fields are both present
    because a client that stored a response needs to know which of the two it
    is holding without having kept the request.

        Attributes:
            applied (bool):
            branding (PromotionBranding): `branding: {"changed": true}` — that the record moved, never what it says.

                The values are a customer's stylesheet and their copy; the diff reports the
                fact and nothing else, for the reason `branding.updated` records key names
                rather than values (audit-log.md §Taxonomy).
            dry_run (bool):
            email_templates (PromotionResourceDiff): What happened to one collection matched by key.

                `created` and `updated` name the rows by the key they were matched on — a
                permission by `name`, a role by `slug`, a template by `kind:locale` — and
                `unchanged` counts the ones that matched and did not move. Rows that exist
                only on the target appear nowhere: promotion never deletes.
            identity_providers (PromotionIdentityProviders): Which provider kinds each side has configured. Promotion copies
                **none** of them.

                D-7, and this shape is the second half of that decision: a promotion that
                silently left a difference behind would be a console that cannot explain why
                the production login page has no Google button. So the diff *names* the
                difference — `sandbox_only` is what the console turns into "sandbox has
                Google configured and production does not" — and `promoted` is flat `false`,
                stated rather than inferred from an empty list, because "nothing differed"
                and "nothing is ever copied" are different facts and only one of them is
                permanent.

                Why nothing is copied: a copied client secret would point production at a
                sandbox OAuth application, and copying `enabled` without the secret would be
                worse — an enabled provider with no credentials is a button on the production
                login page that cannot work. Promotion copies no credential anywhere
                (environments.md §Promotion: not Clients, not API keys, not webhook
                endpoints), and this is the same category.
            permissions (PromotionResourceDiff): What happened to one collection matched by key.

                `created` and `updated` name the rows by the key they were matched on — a
                permission by `name`, a role by `slug`, a template by `kind:locale` — and
                `unchanged` counts the ones that matched and did not move. Rows that exist
                only on the target appear nowhere: promotion never deletes.
            roles (PromotionResourceDiff): What happened to one collection matched by key.

                `created` and `updated` name the rows by the key they were matched on — a
                permission by `name`, a role by `slug`, a template by `kind:locale` — and
                `unchanged` counts the ones that matched and did not move. Rows that exist
                only on the target appear nowhere: promotion never deletes.
            setting_definitions (PromotionResourceDiff): What happened to one collection matched by key.

                `created` and `updated` name the rows by the key they were matched on — a
                permission by `name`, a role by `slug`, a template by `kind:locale` — and
                `unchanged` counts the ones that matched and did not move. Rows that exist
                only on the target appear nowhere: promotion never deletes.
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
