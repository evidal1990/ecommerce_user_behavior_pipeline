import polars as pl
from src.transformation.silver.enrich.enrich_structure import EnrichStructure


class ReturnRateGroup(EnrichStructure):

    def __init__(self) -> None:
        pass

    def name(self) -> str:
        return "RETURN_RATE_GROUP"

    def execute(
        self,
        df,
    ) -> pl.DataFrame:
        return df.with_columns(
            pl.col("return_rate")
            .map_elements(self._classify)
            .alias(self.name().lower())
        )

    def _classify(
        self,
        return_rate: int,
    ) -> str:
        if return_rate <= 20:
            return "Rare Returner"
        elif return_rate <= 40:
            return "Occasional Returner"
        elif return_rate <= 60:
            return "Moderate Returner"
        elif return_rate <= 80:
            return "Frequent Returner"
        return "Heavy Returner"
