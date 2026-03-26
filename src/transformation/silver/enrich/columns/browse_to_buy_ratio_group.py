import polars as pl
from src.transformation.silver.enrich.enrich_structure import EnrichStructure


class BrowseToBuyRatioGroup(EnrichStructure):

    def __init__(self) -> None:
        self.column = "browse_to_buy_ratio"

    def name(self) -> str:
        return f"{self.column.upper()}_GROUP"

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
        return super().aggregate(df=df, column=self.column, labels=labels)
