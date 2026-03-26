import polars as pl
from src.transformation.silver.enrich.enrich_structure import EnrichStructure


class ReviewWrightingFrequencyGroup(EnrichStructure):

    def __init__(self) -> None:
        pass

    def name(self) -> str:
        return "REVIEW_WRITING_FREQUENCY_PER_YEAR_GROUP"

    def execute(
        self,
        df,
    ) -> pl.DataFrame:
        labels = [
            "Rare Reviewer",
            "Occasional Contributor",
            "Active Contributor",
            "Power Contributor",
        ]
        return df.with_columns(
            [
                pl.col("review_writing_frequency_per_year")
                .qcut(quantiles=4, labels=labels)
                .alias(self.name().lower()),
            ]
        )
