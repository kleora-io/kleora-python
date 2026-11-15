"""The error taxonomy.

Four exceptions, one base. `TokenError` names the failure with a `code` from the
same eight-member closed set `@kleora-io/node` raises, so an application
that branches on one SDK's token codes branches on the other's unchanged.

**The parity is in `TokenError.code` and nowhere wider.** These are two
hand-written packages rather than one generated from the other, so a reader
comparing them is owed the places they stop agreeing:

* `@kleora-io/node` also exports `LoginRequired` — no credential presented at
  all — and puts a `code` on every `KleoraError`. Both exist for its express
  and fastify middlewares, which this package does not ship; nothing here reads
  an `Authorization` header, so nothing here can report the absence of one.
* `ApiError` is a different shape. This one carries `title`, `instance` and
  `request_id` with `errors` a tuple of `ProblemError`; node's keeps the document
  as it arrived, plus `Retry-After` and `Idempotency-Replayed`, under `problem`.
* `@kleora-io/browser` verifies no signature — redemption is the backend's
  job — so `invalid_signature` and `unknown_kid` never arise there, and it alone
  has `nonce_mismatch`, for the `nonce` it minted and no backend ever sees.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal

TokenErrorCode = Literal[
    "expired",
    "invalid_signature",
    "invalid_type",
    "issuer_mismatch",
    "audience_mismatch",
    "unknown_kid",
    "issuer_unavailable",
    "malformed",
]
"""Every value `TokenError.code` can take.

Two of them need a word, and `@kleora-io/node` carries both:

* `invalid_type` — an access token's header says `typ: "at+jwt"`, and an ID token
  differs from it only in `typ`, so refusing a token of the wrong type is a
  verification step of its own.
* `issuer_unavailable` — the JWKS document could not be read at all: refused,
  timed out, non-2xx, unparseable, or published no usable key. Distinct from
  `unknown_kid`, which means the document *was* read and simply does not list
  that `kid`. The two failures have opposite owners and opposite answers: an
  unknown key id is a bad token (401, the caller's problem), an unreachable
  issuer is our infrastructure (503, retryable). Folding the outage into
  `unknown_kid` tells every caller its token is bad and sends it back to an
  issuer that is already down.
"""


class KleoraError(Exception):
    """Base of every error this package raises."""


class TokenError(KleoraError):
    """An access token that did not verify.

    `code` is the machine-readable half; the message is for a developer's log
    and names the tolerance or the value that failed.
    """

    def __init__(self, code: TokenErrorCode, message: str) -> None:
        super().__init__(message)
        self.code: TokenErrorCode = code

    def __str__(self) -> str:
        return f"{self.code}: {super().__str__()}"


class EnvironmentMismatch(KleoraError):
    """A sandbox credential paired with a production issuer, or the reverse.

    A configuration error, not a runtime one: it is raised before the credential
    is used against the wrong environment.
    """


@dataclass(frozen=True, slots=True)
class ProblemError:
    """One entry of an RFC 9457 problem's `errors[]`.

    `field` is `None` for a failure about the request as a whole rather than one
    property.
    """

    field: str | None
    message: str
    code: str


class ApiError(KleoraError):
    """A management API response that was not a success.

    Carries the RFC 9457 problem body verbatim: `type`, `status`, `detail` and
    `errors` are what a caller branches on.
    A response that is not a problem document at all — an intermediary's HTML,
    say — still arrives here, with `type` `about:blank` and the body's first
    characters as `detail`, so no status escapes as something other than
    `ApiError`.
    """

    def __init__(
        self,
        *,
        type: str,
        status: int,
        title: str,
        detail: str | None = None,
        errors: Sequence[ProblemError] = (),
        instance: str | None = None,
        request_id: str | None = None,
    ) -> None:
        super().__init__(f"{status} {type}: {detail or title}")
        self.type = type
        self.status = status
        self.title = title
        self.detail = detail
        self.errors: tuple[ProblemError, ...] = tuple(errors)
        self.instance = instance
        self.request_id = request_id
