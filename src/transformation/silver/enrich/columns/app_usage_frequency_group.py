import polars as pl
from src.transformation.silver.enrich.enrich_structure import EnrichStructure


class AppUsageFrequencyGroup(EnrichStructure):

    def __init__(self) -> None:
        pass

    def name(self) -> str:
        return "APP_USAGE_FREQUENCY_PER_WEEK_GROUP"

    def execute(
        self,
        df,
    ) -> pl.DataFrame:
        labels = [
            "Light User",
            "Regular User",
            "Heavy User",
        ]
        return df.with_columns(
            [
                pl.col("app_usage_frequency_per_week")
                .qcut(quantiles=3, labels=labels)
                .alias(self.name().lower()),
            ]
        )
