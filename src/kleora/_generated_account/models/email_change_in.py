# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed self-service API document
# (https://id.kleora.eu/account/v1/openapi.json). `kleora.account` wraps this tree; nothing outside the
# package imports it.
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="EmailChangeIn")


@_attrs_define
class EmailChangeIn:
    """§"Changing an email address" step 1: `POST /email` with `{email}`.

    **The member is `email`, which `authz.SUBJECT_NAMES` refuses**, so `POST /email`
    declares `writes_own={"email"}` — the one declared exception on this surface, and
    `api.public.v1.account.authz`'s module docstring argues it. The spec gives the
    body as `{email}` and the spec wins; what the declaration says is that this
    `email` is a value written onto the caller's own row rather than a way to name
    somebody else's.

    `max_length` and nothing else. §"Failure modes" wants a malformed or over-length
    address to be `422 validation-error` with `field = "email"` — "the caller is a
    program here, not a login form, so there is no oracle to protect: it never saw an
    address it did not supply" — and the normalisation and the real validation are
    `users-and-credentials.md` §Email's, applied by the service through
    `normalise_email` and `validate_user_email`. A pydantic `EmailStr` here would be
    a *second* definition of a valid address, which is the thing `User.email` is a
    `CharField` rather than an `EmailField` to avoid.

        Attributes:
            email (str):
    """

    email: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        email = d.pop("email")

        email_change_in = cls(
            email=email,
        )

        email_change_in.additional_properties = d
        return email_change_in

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
