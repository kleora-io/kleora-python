# GENERATED — do not edit. `uv run python scripts/generate_client.py`.
#
# `openapi-python-client` over the deployed management API document
# (https://api.kleora.io/api/v1/openapi.json). `kleora`'s own surface wraps this tree; nothing outside
# the package imports it.
from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.environment_stats_day import EnvironmentStatsDay
    from ..models.environment_stats_setup import EnvironmentStatsSetup
    from ..models.environment_stats_totals import EnvironmentStatsTotals


T = TypeVar("T", bound="EnvironmentStats")


@_attrs_define
class EnvironmentStats:
    """The body of `GET /apps/{app_id}/environments/{environment_id}/stats`.

    The figures are cached for 60 seconds; `computed_at` is when they were computed, not when they
    were requested.

        Attributes:
            computed_at (datetime.datetime):
            series (list[EnvironmentStatsDay]):
            setup (EnvironmentStatsSetup): The four "is this App set up" facts behind the overview's checklist.

                Booleans rather than counts: the checklist asks whether a thing has ever
                happened, and it disappears when all four are true.
            totals (EnvironmentStatsTotals): What the environment holds now: current counts, not counts over the requested
                range.

                `users` excludes erased users, `api_keys` counts active keys, and `active_sessions` counts live
                sessions.
    """

    computed_at: datetime.datetime
    series: list[EnvironmentStatsDay]
    setup: EnvironmentStatsSetup
    totals: EnvironmentStatsTotals
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        computed_at = self.computed_at.isoformat()

        series = []
        for series_item_data in self.series:
            series_item = series_item_data.to_dict()
            series.append(series_item)

        setup = self.setup.to_dict()

        totals = self.totals.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "computed_at": computed_at,
                "series": series,
                "setup": setup,
                "totals": totals,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.environment_stats_day import EnvironmentStatsDay
        from ..models.environment_stats_setup import EnvironmentStatsSetup
        from ..models.environment_stats_totals import EnvironmentStatsTotals

        d = dict(src_dict)
        computed_at = datetime.datetime.fromisoformat(d.pop("computed_at"))

        series = []
        _series = d.pop("series")
        for series_item_data in _series:
            series_item = EnvironmentStatsDay.from_dict(series_item_data)

            series.append(series_item)

        setup = EnvironmentStatsSetup.from_dict(d.pop("setup"))

        totals = EnvironmentStatsTotals.from_dict(d.pop("totals"))

        environment_stats = cls(
            computed_at=computed_at,
            series=series,
            setup=setup,
            totals=totals,
        )

        environment_stats.additional_properties = d
        return environment_stats

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
