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
        return df.with_columns(
            pl.col("social_sharing_frequency_per_year")
            .map_elements(self._classify)
            .alias(self.name().lower())
        )

    def _classify(
        self,
        social_sharing_frequency_per_year: int,
    ) -> str:
        if social_sharing_frequency_per_year < 0:
            return "Other"
        elif social_sharing_frequency_per_year <= 4:
            return "Low"
        elif social_sharing_frequency_per_year <= 8:
            return "Moderate"
        return "High"
