"""Package identity: the version and the `User-Agent` every request carries.

Every Kleora SDK sends `User-Agent: kleora-{package}/{version}` on every
request it makes. The distribution is named `kleora` for
PyPI, so the package token here is `python` — what the header has to say is
which of the five SDKs is calling, not the distribution name twice.
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("kleora")
except PackageNotFoundError:  # pragma: no cover - only when running from a source tree
    __version__ = "0.0.0"

USER_AGENT = f"kleora-python/{__version__}"
