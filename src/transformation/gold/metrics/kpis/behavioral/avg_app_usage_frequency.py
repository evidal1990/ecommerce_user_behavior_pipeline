from google_crc32c import value
import polars as pl
from src.transformation.gold.metrics.strcutures.base_structure import (
    BaseStructure,
)


class AvgAppUsageFrequency(BaseStructure):
    def __init__(
        self,
        dimension_col: str,
        segment_by: list[str] = [],
    ) -> None:
        super().__init__(
            metric="avg_app_usage_frequency_in_days",
            metric_type="average",
            dimension_col=dimension_col,
            group_cols=segment_by,
        )

    def calculate(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        df = self._apply_filter(df)

        result = self._calculate_average(
            df,
            column="avg_app_usage_frequency_per_week",
        )

        return self._finalize_output(result)

    def _apply_filter(
        self,
        df: pl.DataFrame,
    ) -> pl.Expr:
        return super()._apply_filter(df)
