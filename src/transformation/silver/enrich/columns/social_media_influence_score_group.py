import polars as pl
from src.transformation.silver.enrich.enrich_structure import EnrichStructure


class SocialMediaInfluenceScoreGroup(EnrichStructure):

    def __init__(self) -> None:
        pass

    def name(self) -> str:
        return "SOCIAL_MEDIA_INFLUENCE_SCORE_GROUP"

    def execute(
        self,
        df,
    ) -> pl.DataFrame:
        labels = [
            "Independent",
            "Influence-Aware",
            "Highly Influenced",
        ]
        x_pieces = len(labels)
        return df.with_columns(
            [
                pl.col("social_media_influence_score")
                .qcut(quantiles=x_pieces, labels=labels)
                .alias("social_media_influence_score_group"),
                pl.col("social_media_influence_score")
                .qcut(quantiles=x_pieces)
                .alias("social_media_influence_score_range"),
            ]
        )
