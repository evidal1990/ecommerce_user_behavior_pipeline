import polars as pl
from src.transformation.gold.metrics.strcutures.percentage_structure import (
    PercentageStructure,
)


class DailyActiveUsers(PercentageStructure):
    def __init__(
        self,
        dimension: str,
        group_by: list[str] = [],
    ) -> None:
        super().__init__(
            metric="daily_active_users",
            dimension_col=dimension,
            group_cols=group_by,
        )

    def _apply_filter(
        self,
        df: pl.DataFrame,
    ) -> pl.Expr:
        return df.filter((pl.col("avg_daily_session_time_minutes") >= 10))

    def calculate(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        df = self._apply_filter(df)
        df = self._calculate_percentage(df)
        df = self._finalize_output(df)
        return df
