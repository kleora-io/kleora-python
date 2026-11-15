# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from enum import Enum


class MauAllowanceOutScope(str, Enum):
    ACCOUNT = "account"
    APP = "app"

    def __str__(self) -> str:
        return str(self.value)
