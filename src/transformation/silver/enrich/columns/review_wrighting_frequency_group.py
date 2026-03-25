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
        return df.with_columns(
            pl.col("review_writing_frequency_per_year")
            .map_elements(self._classify)
            .alias(self.name().lower())
        )

    def _classify(
        self,
        review_writing_frequency_per_year: int,
    ) -> str:
        if review_writing_frequency_per_year <= 1:
            return "Non-Reviewer"
        elif review_writing_frequency_per_year <= 4:
            return "Rare Reviewer"
        elif review_writing_frequency_per_year <= 7:
            return "Occasional Contributor"
        elif review_writing_frequency_per_year <= 10:
            return "Active Contributor"
        return "Power Contributor"
