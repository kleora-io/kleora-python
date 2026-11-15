# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from enum import Enum


class UserOutAvatarColor(str, Enum):
    AMBER = "amber"
    BLUE = "blue"
    CYAN = "cyan"
    EMERALD = "emerald"
    FUCHSIA = "fuchsia"
    GREEN = "green"
    INDIGO = "indigo"
    LIME = "lime"
    ORANGE = "orange"
    PINK = "pink"
    PURPLE = "purple"
    RED = "red"
    ROSE = "rose"
    SKY = "sky"
    TEAL = "teal"
    VIOLET = "violet"
    YELLOW = "yellow"

    def __str__(self) -> str:
        return str(self.value)
