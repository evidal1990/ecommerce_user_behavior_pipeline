import polars as pl
from src.transformation.silver.enrich.enrich_structure import EnrichStructure


class PurchaseConversionRateGroup(EnrichStructure):

    def __init__(self) -> None:
        pass

    def name(self) -> str:
        return "PURCHASE_CONVERSION_RATE_GROUP"

    def execute(
        self,
        df,
    ) -> pl.DataFrame:
        labels = [
            "Rare Buyer",
            "Occasional Buyer",
            "Considered Buyer",
            "Frequent Buyer",
            "Power Buyer",
        ]
        return df.with_columns(
            [
                pl.col("purchase_conversion_rate")
                .qcut(quantiles=5, labels=labels)
                .alias(self.name().lower()),
            ]
        )
