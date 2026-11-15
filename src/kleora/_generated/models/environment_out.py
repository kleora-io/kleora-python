# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.environment_out_backfill_status_type_0 import (
    EnvironmentOutBackfillStatusType0,
)

T = TypeVar("T", bound="EnvironmentOut")


@_attrs_define
class EnvironmentOut:
    """An Environment as `GET`/`PATCH /environments/{environment_id}` report it.

    Attributes:
        access_token_ttl (int):
        allow_browser_locale (bool):
        api_audience (None | str):
        app_id (UUID):
        backfill_status (EnvironmentOutBackfillStatusType0 | None):
        created_at (datetime.datetime):
        default_locale (str):
        id (UUID):
        issuer (str):
        kind (str):
        mfa_policy (str):
        no_tenant_behaviour (str):
        password_breach_check (bool):
        password_min_length (int):
        refresh_token_ttl (int):
        self_deletion (bool):
        self_registration (bool):
        session_idle_ttl (int):
        session_ttl (int):
        tenant_creator_role (None | str):
        tenant_mode (str):
        updated_at (datetime.datetime):
    """

    access_token_ttl: int
    allow_browser_locale: bool
    api_audience: None | str
    app_id: UUID
    backfill_status: EnvironmentOutBackfillStatusType0 | None
    created_at: datetime.datetime
    default_locale: str
    id: UUID
    issuer: str
    kind: str
    mfa_policy: str
    no_tenant_behaviour: str
    password_breach_check: bool
    password_min_length: int
    refresh_token_ttl: int
    self_deletion: bool
    self_registration: bool
    session_idle_ttl: int
    session_ttl: int
    tenant_creator_role: None | str
    tenant_mode: str
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_token_ttl = self.access_token_ttl

        allow_browser_locale = self.allow_browser_locale

        api_audience: None | str
        api_audience = self.api_audience

        app_id = str(self.app_id)

        backfill_status: None | str
        if isinstance(self.backfill_status, EnvironmentOutBackfillStatusType0):
            backfill_status = self.backfill_status.value
        else:
            backfill_status = self.backfill_status

        created_at = self.created_at.isoformat()

        default_locale = self.default_locale

        id = str(self.id)

        issuer = self.issuer

        kind = self.kind

        mfa_policy = self.mfa_policy

        no_tenant_behaviour = self.no_tenant_behaviour

        password_breach_check = self.password_breach_check

        password_min_length = self.password_min_length

        refresh_token_ttl = self.refresh_token_ttl

        self_deletion = self.self_deletion

        self_registration = self.self_registration

        session_idle_ttl = self.session_idle_ttl

        session_ttl = self.session_ttl

        tenant_creator_role: None | str
        tenant_creator_role = self.tenant_creator_role

        tenant_mode = self.tenant_mode

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access_token_ttl": access_token_ttl,
                "allow_browser_locale": allow_browser_locale,
                "api_audience": api_audience,
                "app_id": app_id,
                "backfill_status": backfill_status,
                "created_at": created_at,
                "default_locale": default_locale,
                "id": id,
                "issuer": issuer,
                "kind": kind,
                "mfa_policy": mfa_policy,
                "no_tenant_behaviour": no_tenant_behaviour,
                "password_breach_check": password_breach_check,
                "password_min_length": password_min_length,
                "refresh_token_ttl": refresh_token_ttl,
                "self_deletion": self_deletion,
                "self_registration": self_registration,
                "session_idle_ttl": session_idle_ttl,
                "session_ttl": session_ttl,
                "tenant_creator_role": tenant_creator_role,
                "tenant_mode": tenant_mode,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        access_token_ttl = d.pop("access_token_ttl")

        allow_browser_locale = d.pop("allow_browser_locale")

        def _parse_api_audience(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        api_audience = _parse_api_audience(d.pop("api_audience"))

        app_id = UUID(d.pop("app_id"))

        def _parse_backfill_status(
            data: object,
        ) -> EnvironmentOutBackfillStatusType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backfill_status_type_0 = EnvironmentOutBackfillStatusType0(data)

                return backfill_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnvironmentOutBackfillStatusType0 | None, data)

        backfill_status = _parse_backfill_status(d.pop("backfill_status"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        default_locale = d.pop("default_locale")

        id = UUID(d.pop("id"))

        issuer = d.pop("issuer")

        kind = d.pop("kind")

        mfa_policy = d.pop("mfa_policy")

        no_tenant_behaviour = d.pop("no_tenant_behaviour")

        password_breach_check = d.pop("password_breach_check")

        password_min_length = d.pop("password_min_length")

        refresh_token_ttl = d.pop("refresh_token_ttl")

        self_deletion = d.pop("self_deletion")

        self_registration = d.pop("self_registration")

        session_idle_ttl = d.pop("session_idle_ttl")

        session_ttl = d.pop("session_ttl")

        def _parse_tenant_creator_role(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tenant_creator_role = _parse_tenant_creator_role(d.pop("tenant_creator_role"))

        tenant_mode = d.pop("tenant_mode")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        environment_out = cls(
            access_token_ttl=access_token_ttl,
            allow_browser_locale=allow_browser_locale,
            api_audience=api_audience,
            app_id=app_id,
            backfill_status=backfill_status,
            created_at=created_at,
            default_locale=default_locale,
            id=id,
            issuer=issuer,
            kind=kind,
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
            updated_at=updated_at,
        )

        environment_out.additional_properties = d
        return environment_out

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
