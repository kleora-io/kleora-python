# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from enum import Enum


class EmailTemplateOutKind(str, Enum):
    ACCOUNT_DELETED = "account_deleted"
    ACCOUNT_DELETION_CANCELLED = "account_deletion_cancelled"
    ACCOUNT_DELETION_REQUESTED = "account_deletion_requested"
    EMAIL_CHANGE_COMPLETED = "email_change_completed"
    EMAIL_CHANGE_REQUESTED = "email_change_requested"
    INVITATION = "invitation"
    MFA_ENROLLED = "mfa_enrolled"
    MFA_REMOVED = "mfa_removed"
    PASSWORD_CHANGED = "password_changed"
    RESET_PASSWORD = "reset_password"
    VERIFY_EMAIL = "verify_email"

    def __str__(self) -> str:
        return str(self.value)
