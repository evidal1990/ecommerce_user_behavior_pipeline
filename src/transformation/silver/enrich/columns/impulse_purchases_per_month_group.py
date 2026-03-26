import polars as pl
from src.transformation.silver.enrich.enrich_structure import EnrichStructure


class ImpulsePurchasesPerMonthGroup(EnrichStructure):

    def __init__(self) -> None:
        self.column = "impulse_purchases_per_month"

    def name(self) -> str:
        return f"{self.column.upper()}_GROUP"

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
        return super().aggregate(df=df, column=self.column, labels=labels)
