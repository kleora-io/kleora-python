"""The claim `errors.py` makes about `@kleora-io/node`, held as a test.

`errors.py`'s module docstring tells a reader that `TokenError.code` is drawn
from the same closed set the Node SDK raises, so "an application that branches
on one SDK's token codes branches on the other's unchanged". A comment that is
wrong is worse than no comment — nobody re-reads a claim they have already
believed once — so the claim is a test.

The Node SDK lives in its own repository
(https://github.com/kleora-io/kleora-node), so its `TokenErrorCode` union in
`src/errors.ts` is restated here. A change to either set has to change this
literal, which is the moment to change the other SDK too.
"""

from __future__ import annotations

from typing import get_args

from kleora import TokenErrorCode

#: `TokenErrorCode` in `@kleora-io/node`'s `src/errors.ts`.
NODE_CODES = frozenset(
    {
        "expired",
        "invalid_signature",
        "invalid_type",
        "issuer_mismatch",
        "audience_mismatch",
        "unknown_kid",
        "issuer_unavailable",
        "malformed",
    }
)


def test_the_token_error_codes_are_exactly_the_ones_node_raises() -> None:
    """The parity `errors.py` promises, in both directions.

    A member either SDK gains alone breaks the promise, and which direction it
    broke in is the first thing the failure has to say.
    """

    python = frozenset(get_args(TokenErrorCode))
    node = NODE_CODES

    assert python - node == frozenset(), f"only Python has {sorted(python - node)}"
    assert node - python == frozenset(), f"only node has {sorted(node - python)}"


def test_issuer_unavailable_is_one_of_them() -> None:
    """Named rather than left to the set comparison above.

    The set comparison would also go green if both SDKs dropped the member, and
    the point is that an unreachable issuer has a code of its own.
    """

    assert "issuer_unavailable" in get_args(TokenErrorCode)
