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
        labels = [
            "Detractors",
            "Neutral",
            "Promoters",
        ]
        x_pieces = len(labels)
        return df.with_columns(
            [
                pl.col("brand_loyalty_score")
                .qcut(quantiles=x_pieces, labels=labels)
                .alias("brand_loyalty_score_group"),
                pl.col("brand_loyalty_score")
                .qcut(quantiles=x_pieces)
                .alias("brand_loyalty_score_range"),
            ]
        )
