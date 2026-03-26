import polars as pl
from src.transformation.silver.enrich.enrich_structure import EnrichStructure


class StressFromFinancialDecisionsGroup(EnrichStructure):

    def __init__(self) -> None:
        self.column = "stress_from_financial_decisions_level"

    def name(self) -> str:
        return f"{self.column.upper()}_GROUP"

    def execute(
        self,
        df,
    ) -> pl.DataFrame:
        labels = [
            "Financially Unconcerned",
            "Financially Comfortable",
            "Financially Aware",
            "Financially Stressed",
            "Financially Overwhelmed",
        ]
        return super().aggregate(df=df, column=self.column, labels=labels)
