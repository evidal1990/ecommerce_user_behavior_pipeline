import polars as pl
from src.transformation.silver.enrich.enrich_structure import EnrichStructure


class AgeGroup(EnrichStructure):

    def __init__(self) -> None:
        self.column = "age"

    def name(self) -> str:
        return f"{self.column.upper()}_GROUP"

    def execute(
        self,
        df,
    ) -> pl.DataFrame:
        labels = [
            "Early Adopters",
            "Early Career Professionals",
            "Professional Consolidation",
            "High Financial Stability",
            "Pre-Retirement",
            "Low Digital Adoption",
        ]
        return super().aggregate(df=df, column=self.column, labels=labels)
