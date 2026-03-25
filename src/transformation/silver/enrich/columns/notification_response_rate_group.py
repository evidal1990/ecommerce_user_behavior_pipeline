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
        return df.with_columns(
            pl.col("notification_response_rate")
            .map_elements(self._classify)
            .alias(self.name().lower())
        )

    def _classify(
        self,
        notification_response_rate: int,
    ) -> str:
        if notification_response_rate <= 20:
            return "Unresponsive"
        elif notification_response_rate <= 40:
            return "Rarely Responsive"
        elif notification_response_rate <= 60:
            return "Occasionally Responsive"
        elif notification_response_rate <= 80:
            return "Responsive"
        return "Highly Responsive"
