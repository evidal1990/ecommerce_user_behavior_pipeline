import polars as pl
from src.transformation.silver.enrich.enrich_structure import EnrichStructure


class PhysicalActivityLevelGroup(EnrichStructure):

    def __init__(self) -> None:
        pass

    def name(self) -> str:
        return "PHYSICAL_ACTIVITY_LEVEL_GROUP"

    def execute(
        self,
        df,
    ) -> pl.DataFrame:
        labels = [
            "Lightly Activity",
            "Moderate Activity",
            "Intense Activity",
            "Very Intense Activity",
        ]
        return df.with_columns(
            [
                pl.col("physical_activity_level")
                .qcut(quantiles=4, labels=labels)
                .alias(self.name().lower()),
            ]
        )
