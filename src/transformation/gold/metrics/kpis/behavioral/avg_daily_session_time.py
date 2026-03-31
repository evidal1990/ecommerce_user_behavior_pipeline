from google_crc32c import value
import polars as pl
from src.transformation.gold.metrics.strcutures.base_structure import (
    BaseStructure,
)


class AvgDailySessionTime(BaseStructure):
    def __init__(
        self,
        dimension_col: str,
        segment_by: list[str]=[],
    ) -> None:
        super().__init__(
            metric="avg_daily_session_time_in_mninutes",
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
            column="avg_daily_session_time_minutes",
        )

        return self._finalize_output(result)

    def _apply_filter(
        self,
        df: pl.DataFrame,
    ) -> pl.Expr:
        return super()._apply_filter(df)
