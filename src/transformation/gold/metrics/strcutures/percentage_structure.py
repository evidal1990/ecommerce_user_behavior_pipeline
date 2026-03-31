import polars as pl
from src.transformation.gold.metrics.strcutures.base_structure import (
    BaseStructure,
)


class PercentageStructure(BaseStructure):
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

    def calculate(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        df = self._apply_filter(df)

        result = self._calculate_percentage(df)

        return self._finalize_output(result)
