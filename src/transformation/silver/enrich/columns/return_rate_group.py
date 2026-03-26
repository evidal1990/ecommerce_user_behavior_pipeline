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
        labels = [
            "Rare Returner",
            "Occasional Returner",
            "Frequent Returner",
            "Heavy Returner",
        ]
        return df.with_columns(
            [
                pl.col("return_rate")
                .qcut(quantiles=4, labels=labels)
                .alias(self.name().lower()),
            ]
        )
