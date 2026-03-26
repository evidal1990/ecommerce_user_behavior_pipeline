import polars as pl
from src.transformation.silver.enrich.enrich_structure import EnrichStructure


class ReturnRateGroup(EnrichStructure):

    def __init__(self) -> None:
        self.column = "return_rate"

    def name(self) -> str:
        return f"{self.column.upper()}_GROUP"

    def execute(
        self,
        df,
    ) -> pl.DataFrame:
        labels = [
            "Rare Returner",
            "Occasional Returner",
            "Frequent Returner",
            "Heavy Returner",
        ]
        return super().aggregate(df=df, column=self.column, labels=labels)
