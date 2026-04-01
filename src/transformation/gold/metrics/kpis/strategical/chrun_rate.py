import polars as pl
from datetime import datetime, timedelta
from src.transformation.gold.metrics.strcutures.percentage_structure import (
    PercentageStructure,
)


class ChurnRate(PercentageStructure):
    def __init__(
        self,
        dimension: str,
        group_by: list[str] = [],
    ) -> None:
        super().__init__(
            metric="churn_rate",
            dimension_col=dimension,
            group_cols=group_by,
        )

    def _apply_filter(
        self,
        df: pl.DataFrame,
    ) -> pl.Expr:
        current_date = datetime.now().date()
        start_date = current_date - timedelta(days=90)
        df = df.filter(
            (pl.col(self.dimension_col) >= start_date.replace(day=1))
            & (pl.col(self.dimension_col) <= current_date.replace(day=1))
        )
        return df

    def _prepare_dimension(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        return df.with_columns(
            pl.col(self.dimension_col).dt.truncate("1mo").alias(self.dimension_col)
        )

    def calculate(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        df = self._prepare_dimension(df)
        df = self._apply_filter(df)
        df = self._calculate_percentage(df)
        df = self._finalize_output(df)
        return df
