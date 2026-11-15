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

from ..models.signing_key_out_status import SigningKeyOutStatus

if TYPE_CHECKING:
    from ..models.signing_key_out_public_jwk import SigningKeyOutPublicJwk


T = TypeVar("T", bound="SigningKeyOut")


@_attrs_define
class SigningKeyOut:
    """One signing key as every read reports it (sessions-and-tokens.md §API).

    `public_jwk` is RFC 7517's public JWK: `kty`, `crv`, `x`, `y`, `kid`, `alg`,
    `use`. Typed `dict[str, str]` rather than a model of its own because it is
    published verbatim and a JWK's membership is the RFC's to decide, not ours.

        Attributes:
            activated_at (datetime.datetime | None):
            algorithm (str):
            created_at (datetime.datetime):
            id (UUID):
            kid (str):
            public_jwk (SigningKeyOutPublicJwk):
            retired_at (datetime.datetime | None):
            status (SigningKeyOutStatus):
    """

    activated_at: datetime.datetime | None
    algorithm: str
    created_at: datetime.datetime
    id: UUID
    kid: str
    public_jwk: SigningKeyOutPublicJwk
    retired_at: datetime.datetime | None
    status: SigningKeyOutStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activated_at: None | str
        if isinstance(self.activated_at, datetime.datetime):
            activated_at = self.activated_at.isoformat()
        else:
            activated_at = self.activated_at

        algorithm = self.algorithm

        created_at = self.created_at.isoformat()

        id = str(self.id)

        kid = self.kid

        public_jwk = self.public_jwk.to_dict()

        retired_at: None | str
        if isinstance(self.retired_at, datetime.datetime):
            retired_at = self.retired_at.isoformat()
        else:
            retired_at = self.retired_at

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activated_at": activated_at,
                "algorithm": algorithm,
                "created_at": created_at,
                "id": id,
                "kid": kid,
                "public_jwk": public_jwk,
                "retired_at": retired_at,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.signing_key_out_public_jwk import SigningKeyOutPublicJwk

        d = dict(src_dict)

        def _parse_activated_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                activated_at_type_0 = datetime.datetime.fromisoformat(data)

                return activated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        activated_at = _parse_activated_at(d.pop("activated_at"))

        algorithm = d.pop("algorithm")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = UUID(d.pop("id"))

        kid = d.pop("kid")

        public_jwk = SigningKeyOutPublicJwk.from_dict(d.pop("public_jwk"))

        def _parse_retired_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                retired_at_type_0 = datetime.datetime.fromisoformat(data)

                return retired_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        retired_at = _parse_retired_at(d.pop("retired_at"))

        status = SigningKeyOutStatus(d.pop("status"))

        signing_key_out = cls(
            activated_at=activated_at,
            algorithm=algorithm,
            created_at=created_at,
            id=id,
            kid=kid,
            public_jwk=public_jwk,
            retired_at=retired_at,
            status=status,
        )

        signing_key_out.additional_properties = d
        return signing_key_out

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
