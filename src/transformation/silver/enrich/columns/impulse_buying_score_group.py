import polars as pl
from src.transformation.silver.enrich.enrich_structure import EnrichStructure


class ImpulseBuyingScoreGroup(EnrichStructure):

    def __init__(self) -> None:
        pass

    def name(self) -> str:
        return "IMPULSE_BUYING_SCORE_GROUP"

    def execute(
        self,
        df,
    ) -> pl.DataFrame:
        labels = [
            "Highly Deliberate",
            "Considered Buyer",
            "Balanced Buyer",
            "Impulse-Prone",
            "Highly Impulsive",
        ]
        x_pieces = len(labels)
        return df.with_columns(
            [
                pl.col("impulse_buying_score")
                .qcut(quantiles=x_pieces, labels=labels)
                .alias("impulse_buying_score_group"),
                pl.col("impulse_buying_score")
                .qcut(quantiles=x_pieces)
                .alias("impulse_buying_score_range"),
            ]
        )
