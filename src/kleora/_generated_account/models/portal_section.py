# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed self-service API document
# (https://id.kleora.eu/account/v1/openapi.json). `kleora.account` wraps this tree; nothing outside the
# package imports it.
from enum import Enum


class PortalSection(str, Enum):
    DANGER = "danger"
    PASSWORD = "password"
    PROFILE = "profile"
    SECURITY = "security"
    SESSIONS = "sessions"

    def __str__(self) -> str:
        return str(self.value)
