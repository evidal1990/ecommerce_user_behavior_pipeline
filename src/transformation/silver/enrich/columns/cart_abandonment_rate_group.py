import polars as pl
from src.transformation.silver.enrich.enrich_structure import EnrichStructure


class CartAbandonmentRateGroup(EnrichStructure):

    def __init__(self) -> None:
        pass

    def name(self) -> str:
        return "CART_ABANDONMENT_RATE_GROUP"

    def execute(
        self,
        df,
    ) -> pl.DataFrame:
        labels = [
            "Rare Abandoner",
            "Occasional Abandoner",
            "Frequent Abandoner",
            "Heavy Abandoner",
        ]
        return df.with_columns(
            [
                pl.col("cart_abandonment_rate")
                .qcut(quantiles=4, labels=labels)
                .alias(self.name().lower()),
            ]
        )
