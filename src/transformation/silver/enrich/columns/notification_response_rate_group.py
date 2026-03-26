import polars as pl
from src.transformation.silver.enrich.enrich_structure import EnrichStructure


class NotificationResponseRateGroup(EnrichStructure):

    def __init__(self) -> None:
        pass

    def name(self) -> str:
        return "NOTIFICATION_RESPONSE_RATE_GROUP"

    def execute(
        self,
        df,
    ) -> pl.DataFrame:
        labels = [
            "Rarely Responsive",
            "Occasionally Responsive",
            "Responsive",
            "Highly Responsive",
        ]
        return df.with_columns(
            [
                pl.col("notification_response_rate")
                .qcut(quantiles=4, labels=labels)
                .alias(self.name().lower()),
            ]
        )