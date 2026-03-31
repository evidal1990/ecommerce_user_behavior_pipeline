import polars as pl
from src.transformation.gold.metrics.strcutures.percentage_structure import (
    PercentageStructure,
)


class PremiumSubscriptionAdoption(PercentageStructure):
    def __init__(
        self,
        dimension:str,
        group_by: list[str]=[],
    ) -> None:
        super().__init__(
            metric="premium_adoption",
            dimension_col=dimension,
            group_cols=group_by,
        )

    def _apply_filter(
        self,
        df: pl.DataFrame,
    ) -> pl.Expr:
        return df.filter(pl.col(self.dimension_col) == "Yes")
