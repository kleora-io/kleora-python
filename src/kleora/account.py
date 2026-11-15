"""The end-user self-service API, typed.

`/account/v1/*` on the issuer host, called with **the signed-in person's own
access token** — typically the bearer a request to your own API arrived with,
which `verify_access_token` has already checked. It is not an API key and there is
no administrative form of this client; the operator's surface is
`ManagementClient`.

Two things have to be true, and neither is this package's to decide:

1. **The Client lists `self_service` in `allowed_scopes`** — the consent.
   A Client that has not opted in cannot be granted the scope.
2. **The token carries `self_service`**, because the application asked for it when
   signing the person in. Without it every call raises `ApiError` with the type
   `…/insufficient-scope`.

Operations marked **sensitive** raise `…/reauth-required` unless the person has
re-authenticated in the last five minutes (`reauthenticate`). Registering a
passkey and linking a provider identity cannot be done from a customer's origin
at all; send the person to `account_portal_url` for those.

The client **wraps** `kleora._generated_account`, generated from
the self-service API's OpenAPI document, the way `ManagementClient` wraps
`kleora._generated`: every method below is a named call of one generated
operation, and `api()` hands back the generated client for anything else.

```python
from kleora import AccountClient

with AccountClient(issuer=ISSUER, access_token=bearer) as account:
    profile = account.get_profile()
```
"""

from __future__ import annotations

from collections.abc import Mapping
from types import TracebackType
from typing import Any

import httpx

from ._generated_account.api.account import (
    api_public_v1_account_deletion_cancel_deletion as cancel_deletion_operation,
)
from ._generated_account.api.account import (
    api_public_v1_account_deletion_request_deletion as request_deletion_operation,
)
from ._generated_account.api.account import (
    api_public_v1_account_identities_delete_identity as unlink_identity_operation,
)
from ._generated_account.api.account import (
    api_public_v1_account_identities_list_identities as list_identities_operation,
)
from ._generated_account.api.account import (
    api_public_v1_account_mfa_delete_mfa as remove_mfa_factor_operation,
)
from ._generated_account.api.account import (
    api_public_v1_account_mfa_enroll_confirm as confirm_totp_operation,
)
from ._generated_account.api.account import (
    api_public_v1_account_mfa_enroll_start as start_totp_operation,
)
from ._generated_account.api.account import (
    api_public_v1_account_mfa_list_mfa as list_mfa_operation,
)
from ._generated_account.api.account import (
    api_public_v1_account_mfa_regenerate_recovery as regenerate_recovery_operation,
)
from ._generated_account.api.account import (
    api_public_v1_account_passkeys_delete_passkey as remove_passkey_operation,
)
from ._generated_account.api.account import (
    api_public_v1_account_passkeys_list_passkeys as list_passkeys_operation,
)
from ._generated_account.api.account import (
    api_public_v1_account_password_change_password as change_password_operation,
)
from ._generated_account.api.account import (
    api_public_v1_account_password_read_password_policy as password_policy_operation,
)
from ._generated_account.api.account import (
    api_public_v1_account_portal_read_portal as portal_operation,
)
from ._generated_account.api.account import (
    api_public_v1_account_profile_confirm_email_change as confirm_email_operation,
)
from ._generated_account.api.account import (
    api_public_v1_account_profile_patch_profile as patch_profile_operation,
)
from ._generated_account.api.account import (
    api_public_v1_account_profile_read_email as read_email_operation,
)
from ._generated_account.api.account import (
    api_public_v1_account_profile_read_profile as read_profile_operation,
)
from ._generated_account.api.account import (
    api_public_v1_account_profile_request_email_change as request_email_operation,
)
from ._generated_account.api.account import (
    api_public_v1_account_profile_resend_verification as resend_verification_operation,
)
from ._generated_account.api.account import (
    api_public_v1_account_reauth_read_reauth as read_reauth_operation,
)
from ._generated_account.api.account import (
    api_public_v1_account_reauth_reauthenticate as reauthenticate_operation,
)
from ._generated_account.api.account import (
    api_public_v1_account_sessions_list_sessions as list_sessions_operation,
)
from ._generated_account.api.account import (
    api_public_v1_account_sessions_revoke_other_sessions as revoke_others_operation,
)
from ._generated_account.api.account import (
    api_public_v1_account_sessions_revoke_session as revoke_session_operation,
)
from ._generated_account.api.account import (
    api_public_v1_account_settings_delete_setting as reset_setting_operation,
)
from ._generated_account.api.account import (
    api_public_v1_account_settings_list_settings as list_settings_operation,
)
from ._generated_account.api.account import (
    api_public_v1_account_settings_put_setting as set_setting_operation,
)
from ._generated_account.client import AuthenticatedClient, Client
from ._generated_account.models.deletion_cancel_in import DeletionCancelIn
from ._generated_account.models.deletion_out import DeletionOut
from ._generated_account.models.email_change_in import EmailChangeIn
from ._generated_account.models.email_confirm_in import EmailConfirmIn
from ._generated_account.models.email_out import EmailOut
from ._generated_account.models.enroll_confirm_in import EnrollConfirmIn
from ._generated_account.models.enroll_start_out import EnrollStartOut
from ._generated_account.models.identities_out import IdentitiesOut
from ._generated_account.models.mfa_out import MfaOut
from ._generated_account.models.passkeys_out import PasskeysOut
from ._generated_account.models.password_in import PasswordIn
from ._generated_account.models.password_policy_out import PasswordPolicyOut
from ._generated_account.models.portal_out import PortalOut
from ._generated_account.models.profile_out import ProfileOut
from ._generated_account.models.profile_patch import ProfilePatch
from ._generated_account.models.reauth_in import ReauthIn
from ._generated_account.models.reauth_out import ReauthOut
from ._generated_account.models.recovery_codes_out import RecoveryCodesOut
from ._generated_account.models.resend_out import ResendOut
from ._generated_account.models.revoked_out import RevokedOut
from ._generated_account.models.session_page import SessionPage
from ._generated_account.models.setting_in import SettingIn
from ._generated_account.models.user_setting_document import UserSettingDocument
from ._generated_account.models.user_settings_document import UserSettingsDocument
from ._generated_account.types import UNSET, Response
from ._meta import USER_AGENT
from .errors import KleoraError
from .management import DEFAULT_TIMEOUT, _httpx_arguments, _raise_on_problem
from .portal import _absolute

ACCOUNT_PREFIX = "/account/v1"

PROFILE_FIELDS = frozenset({"name", "locale", "picture_url"})
"""The members `update_profile` may set — `ProfilePatch`'s, and no others."""

SettingValue = bool | int | float | str | None
"""A per-user setting's value: the `UserSettingValue` union of the document."""


def _nothing(_: httpx.Request) -> None:
    """The request hook slot `_httpx_arguments` fills; this client labels nothing."""


def _expect[T](parsed: object, kind: type[T], operation: str) -> T:
    """The typed result, or the reason there is none.

    A 4xx or 5xx never reaches here — the response hook has raised `ApiError` —
    so anything else is a 2xx that is not the declared shape.
    """

    if not isinstance(parsed, kind):
        raise KleoraError(f"{operation} did not answer with a {kind.__name__}")
    return parsed


def _done(response: Response[Any]) -> None:
    """A 204 operation: the hook raised for anything that was not a success."""

    del response


class AccountClient:
    """Every `/account/v1/*` operation, named for what it does. Sync, `httpx`."""

    def __init__(
        self,
        *,
        issuer: str,
        access_token: str,
        timeout: float = DEFAULT_TIMEOUT,
        httpx_args: Mapping[str, Any] | None = None,
    ) -> None:
        _absolute("issuer", issuer)
        if not access_token:
            raise KleoraError("invalid configuration: access_token must not be empty")
        self._issuer = issuer.rstrip("/")
        headers = {"User-Agent": USER_AGENT}
        arguments = _httpx_arguments(httpx_args, _nothing, _raise_on_problem)
        self._api = AuthenticatedClient(
            base_url=self._issuer,
            token=access_token,
            timeout=httpx.Timeout(timeout),
            headers=headers,
            httpx_args=arguments,
        )
        # The one anonymous operation, `DELETE /deletion`, gets a client that
        # holds no token at all rather than one that is asked not to send it.
        self._anonymous = Client(
            base_url=self._issuer,
            timeout=httpx.Timeout(timeout),
            headers=headers,
            httpx_args=_httpx_arguments(httpx_args, _nothing, _raise_on_problem),
        )

    @property
    def base_url(self) -> str:
        """`{issuer}/account/v1`."""

        return self._issuer + ACCOUNT_PREFIX

    def api(self) -> AuthenticatedClient:
        """The generated client, for calling `kleora._generated_account` directly."""

        return self._api

    def __repr__(self) -> str:
        return f"AccountClient(base_url={self.base_url!r})"

    # Profile and email ---------------------------------------------------

    def get_profile(self) -> ProfileOut:
        """`GET /profile`."""

        parsed = read_profile_operation.sync(client=self._api)
        return _expect(parsed, ProfileOut, "GET /profile")

    def update_profile(self, changes: Mapping[str, str | None]) -> ProfileOut:
        """`PATCH /profile` — `name`, `locale`, `picture_url`; `None` clears one."""

        unknown = set(changes) - PROFILE_FIELDS
        if unknown:
            raise KleoraError(
                f"update_profile takes {', '.join(sorted(PROFILE_FIELDS))}; "
                f"not {', '.join(sorted(unknown))}"
            )
        parsed = patch_profile_operation.sync(
            client=self._api, body=ProfilePatch.from_dict(dict(changes))
        )
        return _expect(parsed, ProfileOut, "PATCH /profile")

    def get_email(self) -> EmailOut:
        """`GET /email` — the address, whether it is verified, whether a change is pending."""

        return _expect(read_email_operation.sync(client=self._api), EmailOut, "GET /email")

    def request_email_change(self, email: str) -> ResendOut:
        """`POST /email` — mails a confirmation link to the new address. **Sensitive.**"""

        parsed = request_email_operation.sync(client=self._api, body=EmailChangeIn(email=email))
        return _expect(parsed, ResendOut, "POST /email")

    def confirm_email_change(self, token: str) -> None:
        """`POST /email/confirm` — the token from that link."""

        body = EmailConfirmIn(token=token)
        _done(confirm_email_operation.sync_detailed(client=self._api, body=body))

    def resend_verification_email(self) -> ResendOut:
        """`POST /email/resend` — on the shared per-person budget."""

        parsed = resend_verification_operation.sync(client=self._api)
        return _expect(parsed, ResendOut, "POST /email/resend")

    # Password and re-authentication ---------------------------------------

    def get_password_policy(self) -> PasswordPolicyOut:
        """`GET /password` — whether there is one, and the Environment's policy."""

        parsed = password_policy_operation.sync(client=self._api)
        return _expect(parsed, PasswordPolicyOut, "GET /password")

    def change_password(self, *, new_password: str, current_password: str | None = None) -> None:
        """`POST /password` — change it, or set one for a person who has none. **Sensitive.**"""

        body = PasswordIn(
            new_password=new_password,
            current_password=UNSET if current_password is None else current_password,
        )
        _done(change_password_operation.sync_detailed(client=self._api, body=body))

    def get_reauthentication(self) -> ReauthOut:
        """`GET /reauth` — what this person can re-authenticate with, and until when."""

        parsed = read_reauth_operation.sync(client=self._api)
        return _expect(parsed, ReauthOut, "GET /reauth")

    def reauthenticate(self, password: str) -> None:
        """`POST /reauth` — a password, and nothing else; opens the five-minute window."""

        body = ReauthIn(password=password)
        _done(reauthenticate_operation.sync_detailed(client=self._api, body=body))

    # Sessions ---------------------------------------------------------------

    def list_sessions(self, *, limit: int | None = None, cursor: str | None = None) -> SessionPage:
        """`GET /sessions` — live sessions, newest first, one cursor page."""

        parsed = list_sessions_operation.sync(
            client=self._api,
            limit=UNSET if limit is None else limit,
            cursor=UNSET if cursor is None else cursor,
        )
        return _expect(parsed, SessionPage, "GET /sessions")

    def revoke_session(self, session_id: str) -> None:
        """`DELETE /sessions/{id}` — may be the current one, which is a sign-out."""

        _done(revoke_session_operation.sync_detailed(session_id, client=self._api))

    def revoke_other_sessions(self) -> RevokedOut:
        """`POST /sessions/revoke-others` — every live session but this token's."""

        parsed = revoke_others_operation.sync(client=self._api)
        return _expect(parsed, RevokedOut, "POST /sessions/revoke-others")

    # Second factors, passkeys, linked accounts ------------------------------

    def list_mfa_factors(self) -> MfaOut:
        """`GET /mfa`."""

        return _expect(list_mfa_operation.sync(client=self._api), MfaOut, "GET /mfa")

    def start_totp_enrollment(self) -> EnrollStartOut:
        """`POST /mfa/enroll/start` — a secret and its `otpauth://` URI. **Sensitive.**"""

        parsed = start_totp_operation.sync(client=self._api)
        return _expect(parsed, EnrollStartOut, "POST /mfa/enroll/start")

    def confirm_totp_enrollment(self, code: str) -> RecoveryCodesOut:
        """`POST /mfa/enroll/confirm` — answers the recovery codes, once. **Sensitive.**"""

        parsed = confirm_totp_operation.sync(client=self._api, body=EnrollConfirmIn(code=code))
        return _expect(parsed, RecoveryCodesOut, "POST /mfa/enroll/confirm")

    def remove_mfa_factor(self, factor_id: str) -> None:
        """`DELETE /mfa/{id}`. **Sensitive.**"""

        _done(remove_mfa_factor_operation.sync_detailed(factor_id, client=self._api))

    def regenerate_recovery_codes(self) -> RecoveryCodesOut:
        """`POST /mfa/recovery/regenerate` — new codes, shown once. **Sensitive.**"""

        parsed = regenerate_recovery_operation.sync(client=self._api)
        return _expect(parsed, RecoveryCodesOut, "POST /mfa/recovery/regenerate")

    def list_passkeys(self) -> PasskeysOut:
        """`GET /passkeys`. Registering one is hosted-only (`account_portal_url`)."""

        return _expect(list_passkeys_operation.sync(client=self._api), PasskeysOut, "GET /passkeys")

    def remove_passkey(self, passkey_id: str) -> None:
        """`DELETE /passkeys/{id}`. **Sensitive.**"""

        _done(remove_passkey_operation.sync_detailed(passkey_id, client=self._api))

    def list_identities(self) -> IdentitiesOut:
        """`GET /identities`. Linking one is hosted-only (`account_portal_url`)."""

        parsed = list_identities_operation.sync(client=self._api)
        return _expect(parsed, IdentitiesOut, "GET /identities")

    def unlink_identity(self, identity_id: str) -> None:
        """`DELETE /identities/{id}`. **Sensitive.**"""

        _done(unlink_identity_operation.sync_detailed(identity_id, client=self._api))

    # Settings, the portal, deletion -----------------------------------------

    def list_settings(self) -> UserSettingsDocument:
        """`GET /settings` — the person's own settings, by access level."""

        parsed = list_settings_operation.sync(client=self._api)
        return _expect(parsed, UserSettingsDocument, "GET /settings")

    def set_setting(self, key: str, value: SettingValue) -> UserSettingDocument:
        """`PUT /settings/{key}`."""

        parsed = set_setting_operation.sync(key, client=self._api, body=SettingIn(value=value))
        return _expect(parsed, UserSettingDocument, "PUT /settings/{key}")

    def reset_setting(self, key: str) -> None:
        """`DELETE /settings/{key}` — back to the definition's default."""

        _done(reset_setting_operation.sync_detailed(key, client=self._api))

    def get_portal(self) -> PortalOut:
        """`GET /portal` — the hosted portal's entry URL and the sections offered."""

        return _expect(portal_operation.sync(client=self._api), PortalOut, "GET /portal")

    def request_deletion(self) -> DeletionOut:
        """`POST /deletion` — deleted permanently after 7 days, cancellable until then.

        **Sensitive.** Every session is revoked, this token's included.
        """

        parsed = request_deletion_operation.sync(client=self._api)
        return _expect(parsed, DeletionOut, "POST /deletion")

    def cancel_deletion(self, token: str) -> None:
        """`DELETE /deletion` — the emailed cancellation token. Sent with no bearer token."""

        _done(
            cancel_deletion_operation.sync_detailed(
                client=self._anonymous, body=DeletionCancelIn(token=token)
            )
        )

    # Lifecycle -----------------------------------------------------------

    def close(self) -> None:
        """Release both connection pools."""

        self._api.get_httpx_client().close()
        self._anonymous.get_httpx_client().close()

    def __enter__(self) -> AccountClient:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.close()
