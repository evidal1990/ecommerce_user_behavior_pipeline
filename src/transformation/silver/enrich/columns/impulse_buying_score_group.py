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
        return df.with_columns(
            pl.col("impulse_buying_score")
            .map_elements(self._classify)
            .alias(self.name().lower())
        )

    def _classify(
        self,
        impulse_buying_score: int,
    ) -> str:
        if impulse_buying_score < 0:
            return "Unknown"
        elif impulse_buying_score <= 2:
            return "Highly Deliberate"
        elif impulse_buying_score <= 4:
            return "Considered Buyer"
        elif impulse_buying_score <= 6:
            return "Balanced Buyer"
        elif impulse_buying_score <= 8:
            return "Impulse-Prone"
        return "Highly Impulsive"
