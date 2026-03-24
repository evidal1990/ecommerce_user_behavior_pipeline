import logging
from os import name
import polars as pl
from src.transformation.silver.enrich.enrich_structure import EnrichStructure


class BrandLoyaltyScoreGroup(EnrichStructure):

    def __init__(self) -> None:
        pass

    def name(self) -> str:
        return "BRAND_LOYALTY_SCORE_GROUP"

    def execute(
        self,
        df,
    ) -> pl.DataFrame:
        return df.with_columns(
            pl.col("brand_loyalty_score")
            .map_elements(self._classify)
            .alias("brand_loyalty_score_group")
        )

    def _classify(
        self,
        household_size: int,
    ) -> str:
        if household_size < 0:
            return "Other"
        elif household_size <= 6:
            return "Detractors"
        elif household_size <= 8:
            return "Neutral"
        return "Promoters"
