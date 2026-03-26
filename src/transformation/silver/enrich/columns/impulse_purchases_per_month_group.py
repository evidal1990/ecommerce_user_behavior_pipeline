import polars as pl
from src.transformation.silver.enrich.enrich_structure import EnrichStructure


class ImpulsePurchasesPerMonthGroup(EnrichStructure):

    def __init__(self) -> None:
        pass

    def name(self) -> str:
        return "IMPULSE_PURCHASES_PER_MONTH_GROUP"

    def execute(
        self,
        df,
    ) -> pl.DataFrame:
        labels = [
            "Non-impulsive",
            "Occasional Impulse Buyer",
            "Moderate Impulse Buyer",
            "Frequent Impulse Buyer",
        ]
        return df.with_columns(
            [
                pl.col("impulse_purchases_per_month")
                .qcut(quantiles=4, labels=labels)
                .alias(self.name().lower()),
            ]
        )
