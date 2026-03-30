import polars as pl

from src.transformation.gold.metrics.strcutures.base_structure import BaseStructure

class PremiumSunscriptionAdoptionStructure(BaseStructure):
    def __init__(self, columns: list[str]) -> None:
        super().__init__(
            dimension_col="premium_subscription_group",
            group_cols=columns,
        )

    def _apply_filter(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.filter(pl.col("premium_subscription_group") == "Yes")
