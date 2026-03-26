import polars as pl
from src.transformation.silver.enrich.enrich_structure import EnrichStructure


class AnnualIncomeGroup(EnrichStructure):

    def __init__(self) -> None:
        self.column = "annual_income"

    def name(self) -> str:
        return f"{self.column.upper()}_GROUP"

    def execute(
        self,
        df,
    ) -> pl.DataFrame:
        labels = [
            "E (Lower Class)",
            "D (Lower Middle Class)",
            "C (Middle Class)",
            "B (Upper Middle Class)",
            "A (Upper Class)",
        ]
        return super().aggregate(df=df, column=self.column, labels=labels)
