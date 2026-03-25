import polars as pl
from src.transformation.silver.enrich.enrich_structure import EnrichStructure


class PurchaseConversionRateGroup(EnrichStructure):

    def __init__(self) -> None:
        pass

    def name(self) -> str:
        return "PURCHASE_CONVERSION_RATE_GROUP"

    def execute(
        self,
        df,
    ) -> pl.DataFrame:
        return df.with_columns(
            pl.col("purchase_conversion_rate")
            .map_elements(self._classify)
            .alias(self.name().lower())
        )

    def _classify(
        self,
        return_rate: int,
    ) -> str:
        if return_rate <= 20:
            return "Rare Buyer"
        elif return_rate <= 40:
            return "Occasional Buyer"
        elif return_rate <= 60:
            return "Considered Buyer"
        elif return_rate <= 80:
            return "Frequent Buyer"
        return "Power Buyer"
