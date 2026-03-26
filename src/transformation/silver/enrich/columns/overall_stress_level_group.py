import polars as pl
from src.transformation.silver.enrich.enrich_structure import EnrichStructure


class OverallStressLevelGroup(EnrichStructure):

    def __init__(self) -> None:
        pass

    def name(self) -> str:
        return "OVERALL_STRESS_LEVEL_GROUP"

    def execute(
        self,
        df,
    ) -> pl.DataFrame:
        labels = [
            "Very Relaxed",
            "Relaxed",
            "Balanced",
            "Stressed",
            "Highly Stressed",
        ]
        return df.with_columns(
            [
                pl.col("overall_stress_level")
                .qcut(quantiles=5, labels=labels)
                .alias(self.name().lower()),
            ]
        )
