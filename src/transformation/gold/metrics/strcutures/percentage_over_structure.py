import polars as pl
from src.transformation.gold.metrics.strcutures.base_structure import (
    BaseStructure,
)


class PercentageOverStructure(BaseStructure):
    def __init__(
        self,
        metric: str,
        dimension_col: str,
        group_cols: list[str],
    ) -> None:
        super().__init__(
            metric=metric,
            metric_type="percentage",
            dimension_col=dimension_col,
            group_cols=group_cols,
        )

    def calculate_percentage_over_total(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        df = self._aggregate(df)
        df = self._calculate_percentage(df)
        df = self._sort_output(df)
        return df

    def _aggregate(
        self,
        df: pl.DataFrame,
    ) -> int:
        return df.group_by(self.all_group_cols).agg(
            pl.col("count_users").sum().alias("count_users")
        )

    def _calculate_percentage(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        return df.with_columns(
            (
                pl.col("count_users")
                / pl.col("count_users").sum().over(self.dimension_col)
                * 100
            )
            .round(2)
            .alias("metric_value")
        )

    def _sort_output(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        return df.sort(by=self.all_group_cols)
