import polars as pl
from src.transformation.silver.enrich.enrich_structure import EnrichStructure


class SocialSharingFrequencyGroup(EnrichStructure):

    def __init__(self) -> None:
        pass

    def name(self) -> str:
        return "SOCIAL_SHARING_FREQUENCY_PER_YEAR_GROUP"

    def execute(
        self,
        df,
    ) -> pl.DataFrame:
        labels = [
            "Rare Sharer",
            "Occasional Sharer",
            "Frequent Sharer",
            "Heavy Sharer",
        ]
        return df.with_columns(
            [
                pl.col("social_sharing_frequency_per_year")
                .qcut(quantiles=4, labels=labels)
                .alias(self.name().lower()),
            ]
        )
