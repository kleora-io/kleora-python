# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.environment_patch_default_locale import EnvironmentPatchDefaultLocale
from ..models.environment_patch_mfa_policy import EnvironmentPatchMfaPolicy
from ..models.environment_patch_no_tenant_behaviour import (
    EnvironmentPatchNoTenantBehaviour,
)
from ..models.environment_patch_tenant_mode import EnvironmentPatchTenantMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="EnvironmentPatch")


@_attrs_define
class EnvironmentPatch:
    """`PATCH /api/v1/environments/{environment_id}` — the settings columns.

    The ranges are the model's and the document's at once: declared here, they
    reach `/api/v1/openapi.json`, so a generated client refuses an
    `access_token_ttl` of 30 before the request is made, and a hand-written
    caller that sends one gets 422 with the field in `errors[]` rather than a
    500 from the check constraint.

    `issuer`, `kind` and `backfill_status` are named in `immutable_fields`
    rather than left off: the issuer is stored on this row because every token's
    `iss` and every cached JWKS entry names it, `kind` is what a `kl_test_` key
    is confined to, and `backfill_status` is a report on work in progress. All
    three are plainly properties of the resource, so refusing them as unknown
    keys would read as a typo (environments.md §API).

        Attributes:
            access_token_ttl (int | Unset):
            allow_browser_locale (bool | Unset):
            api_audience (None | str | Unset):
            default_locale (EnvironmentPatchDefaultLocale | Unset):
            mfa_policy (EnvironmentPatchMfaPolicy | Unset):
            no_tenant_behaviour (EnvironmentPatchNoTenantBehaviour | Unset):
            password_breach_check (bool | Unset):
            password_min_length (int | Unset):
            refresh_token_ttl (int | Unset):
            self_deletion (bool | Unset):
            self_registration (bool | Unset):
            session_idle_ttl (int | Unset):
            session_ttl (int | Unset):
            tenant_creator_role (None | str | Unset):
            tenant_mode (EnvironmentPatchTenantMode | Unset):
    """

    access_token_ttl: int | Unset = UNSET
    allow_browser_locale: bool | Unset = UNSET
    api_audience: None | str | Unset = UNSET
    default_locale: EnvironmentPatchDefaultLocale | Unset = UNSET
    mfa_policy: EnvironmentPatchMfaPolicy | Unset = UNSET
    no_tenant_behaviour: EnvironmentPatchNoTenantBehaviour | Unset = UNSET
    password_breach_check: bool | Unset = UNSET
    password_min_length: int | Unset = UNSET
    refresh_token_ttl: int | Unset = UNSET
    self_deletion: bool | Unset = UNSET
    self_registration: bool | Unset = UNSET
    session_idle_ttl: int | Unset = UNSET
    session_ttl: int | Unset = UNSET
    tenant_creator_role: None | str | Unset = UNSET
    tenant_mode: EnvironmentPatchTenantMode | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        access_token_ttl = self.access_token_ttl

        allow_browser_locale = self.allow_browser_locale

        api_audience: None | str | Unset
        if isinstance(self.api_audience, Unset):
            api_audience = UNSET
        else:
            api_audience = self.api_audience

        default_locale: str | Unset = UNSET
        if not isinstance(self.default_locale, Unset):
            default_locale = self.default_locale.value

        mfa_policy: str | Unset = UNSET
        if not isinstance(self.mfa_policy, Unset):
            mfa_policy = self.mfa_policy.value

        no_tenant_behaviour: str | Unset = UNSET
        if not isinstance(self.no_tenant_behaviour, Unset):
            no_tenant_behaviour = self.no_tenant_behaviour.value

        password_breach_check = self.password_breach_check

        password_min_length = self.password_min_length

        refresh_token_ttl = self.refresh_token_ttl

        self_deletion = self.self_deletion

        self_registration = self.self_registration

        session_idle_ttl = self.session_idle_ttl

        session_ttl = self.session_ttl

        tenant_creator_role: None | str | Unset
        if isinstance(self.tenant_creator_role, Unset):
            tenant_creator_role = UNSET
        else:
            tenant_creator_role = self.tenant_creator_role

        tenant_mode: str | Unset = UNSET
        if not isinstance(self.tenant_mode, Unset):
            tenant_mode = self.tenant_mode.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if access_token_ttl is not UNSET:
            field_dict["access_token_ttl"] = access_token_ttl
        if allow_browser_locale is not UNSET:
            field_dict["allow_browser_locale"] = allow_browser_locale
        if api_audience is not UNSET:
            field_dict["api_audience"] = api_audience
        if default_locale is not UNSET:
            field_dict["default_locale"] = default_locale
        if mfa_policy is not UNSET:
            field_dict["mfa_policy"] = mfa_policy
        if no_tenant_behaviour is not UNSET:
            field_dict["no_tenant_behaviour"] = no_tenant_behaviour
        if password_breach_check is not UNSET:
            field_dict["password_breach_check"] = password_breach_check
        if password_min_length is not UNSET:
            field_dict["password_min_length"] = password_min_length
        if refresh_token_ttl is not UNSET:
            field_dict["refresh_token_ttl"] = refresh_token_ttl
        if self_deletion is not UNSET:
            field_dict["self_deletion"] = self_deletion
        if self_registration is not UNSET:
            field_dict["self_registration"] = self_registration
        if session_idle_ttl is not UNSET:
            field_dict["session_idle_ttl"] = session_idle_ttl
        if session_ttl is not UNSET:
            field_dict["session_ttl"] = session_ttl
        if tenant_creator_role is not UNSET:
            field_dict["tenant_creator_role"] = tenant_creator_role
        if tenant_mode is not UNSET:
            field_dict["tenant_mode"] = tenant_mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        access_token_ttl = d.pop("access_token_ttl", UNSET)

        allow_browser_locale = d.pop("allow_browser_locale", UNSET)

        def _parse_api_audience(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_audience = _parse_api_audience(d.pop("api_audience", UNSET))

        _default_locale = d.pop("default_locale", UNSET)
        default_locale: EnvironmentPatchDefaultLocale | Unset
        if isinstance(_default_locale, Unset):
            default_locale = UNSET
        else:
            default_locale = EnvironmentPatchDefaultLocale(_default_locale)

        _mfa_policy = d.pop("mfa_policy", UNSET)
        mfa_policy: EnvironmentPatchMfaPolicy | Unset
        if isinstance(_mfa_policy, Unset):
            mfa_policy = UNSET
        else:
            mfa_policy = EnvironmentPatchMfaPolicy(_mfa_policy)

        _no_tenant_behaviour = d.pop("no_tenant_behaviour", UNSET)
        no_tenant_behaviour: EnvironmentPatchNoTenantBehaviour | Unset
        if isinstance(_no_tenant_behaviour, Unset):
            no_tenant_behaviour = UNSET
        else:
            no_tenant_behaviour = EnvironmentPatchNoTenantBehaviour(
                _no_tenant_behaviour
            )

        password_breach_check = d.pop("password_breach_check", UNSET)

        password_min_length = d.pop("password_min_length", UNSET)

        refresh_token_ttl = d.pop("refresh_token_ttl", UNSET)

        self_deletion = d.pop("self_deletion", UNSET)

        self_registration = d.pop("self_registration", UNSET)

        session_idle_ttl = d.pop("session_idle_ttl", UNSET)

        session_ttl = d.pop("session_ttl", UNSET)

        def _parse_tenant_creator_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_creator_role = _parse_tenant_creator_role(
            d.pop("tenant_creator_role", UNSET)
        )

        _tenant_mode = d.pop("tenant_mode", UNSET)
        tenant_mode: EnvironmentPatchTenantMode | Unset
        if isinstance(_tenant_mode, Unset):
            tenant_mode = UNSET
        else:
            tenant_mode = EnvironmentPatchTenantMode(_tenant_mode)

        environment_patch = cls(
            access_token_ttl=access_token_ttl,
            allow_browser_locale=allow_browser_locale,
            api_audience=api_audience,
            default_locale=default_locale,
            mfa_policy=mfa_policy,
            no_tenant_behaviour=no_tenant_behaviour,
            password_breach_check=password_breach_check,
            password_min_length=password_min_length,
            refresh_token_ttl=refresh_token_ttl,
            self_deletion=self_deletion,
            self_registration=self_registration,
            session_idle_ttl=session_idle_ttl,
            session_ttl=session_ttl,
            tenant_creator_role=tenant_creator_role,
            tenant_mode=tenant_mode,
        )

        return environment_patch
