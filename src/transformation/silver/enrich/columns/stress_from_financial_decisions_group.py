import polars as pl
from src.transformation.silver.enrich.enrich_structure import EnrichStructure


class StressFromFinancialDecisionsGroup(EnrichStructure):

    def __init__(self) -> None:
        pass

    def name(self) -> str:
        return "STRESS_FROM_FINANCIAL_DECISIONS_LEVEL_GROUP"

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
        return df.with_columns(
            [
                pl.col("stress_from_financial_decisions_level")
                .qcut(quantiles=5, labels=labels)
                .alias(self.name().lower()),
            ]
        )
