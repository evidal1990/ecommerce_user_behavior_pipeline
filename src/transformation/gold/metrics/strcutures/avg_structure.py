import polars as pl
from src.transformation.gold.metrics.strcutures.base_structure import (
    BaseStructure,
)


class AvgStructure(BaseStructure):
    def __init__(
        self,
        metric: str,
        column: str,
        dimension_col: str,
        group_cols: list[str]=[],
    ) -> None:
        self.column = column
        super().__init__(
            metric=metric,
            metric_type="average",
            dimension_col=dimension_col,
            group_cols=group_cols,
        )

    def calculate(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        df = self._apply_filter(df)

        result = self._calculate_average(
            df,
            column=self.column,
        )

        return self._finalize_output(result)
