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

T = TypeVar("T", bound="SentOut")


@_attrs_define
class SentOut:
    """The `200` of the two send actions: `{"sent": true | false}`.

    `false` for the one case that succeeds without sending anything — a
    verification resend to an address that is already verified, which
    users-and-credentials.md §"Email verification" calls "a no-op that still
    reports success". A send the throttle refused is a 429 and never reaches
    this shape.

    One status and one shape rather than a 200 and a bodiless 204, so a
    generated client has a single response type to unwrap and the difference
    lives in a field it can branch on. (Ruled in review of P2-10.)

    Required rather than defaulted: a default would make `sent` optional in the
    generated document, and a client that read a missing key as `false` — or as
    `true` — would be guessing at the one thing this response exists to say.
    Both call sites construct it explicitly.

        Attributes:
            sent (bool):
    """

    sent: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sent = self.sent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sent": sent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        sent = d.pop("sent")

        sent_out = cls(
            sent=sent,
        )

        sent_out.additional_properties = d
        return sent_out

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
