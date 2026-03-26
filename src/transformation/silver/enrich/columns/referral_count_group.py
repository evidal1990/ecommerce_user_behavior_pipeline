import polars as pl
from src.transformation.silver.enrich.enrich_structure import EnrichStructure


class ReferralCountGroup(EnrichStructure):

    def __init__(self) -> None:
        pass

    def name(self) -> str:
        return "REFERRAL_COUNT_GROUP"

    def execute(
        self,
        df,
    ) -> pl.DataFrame:
        labels = [
            "Rare Referrer",
            "Occasional Referrer",
            "Active Referrer",
            "Advocate",
        ]
        return df.with_columns(
            [
                pl.col("referral_count")
                .qcut(quantiles=4, labels=labels)
                .alias(self.name().lower()),
            ]
        )