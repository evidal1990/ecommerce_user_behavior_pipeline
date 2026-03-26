import polars as pl
from src.transformation.silver.enrich.enrich_structure import EnrichStructure


class BrowseToBuyRatioGroup(EnrichStructure):

    def __init__(self) -> None:
        pass

    def name(self) -> str:
        return "BROWSE_TO_BUY_RATIO_GROUP"

    def execute(
        self,
        df,
    ) -> pl.DataFrame:
        labels = [
            "Heavy Browser",
            "Casual Browser",
            "Considering Buyer",
            "Intentional Buyer",
            "Decisive Buyer",
        ]
        return df.with_columns(
            [
                pl.col("browse_to_buy_ratio")
                .qcut(quantiles=5, labels=labels)
                .alias(self.name().lower()),
            ]
        )
