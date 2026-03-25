import polars as pl
from src.transformation.silver.enrich.enrich_structure import EnrichStructure


class HouseholdSizeGroup(EnrichStructure):

    def __init__(self) -> None:
        pass

    def name(self) -> str:
        return "HOUSEHOLD_SIZE_GROUP"

    def execute(
        self,
        df,
    ) -> pl.DataFrame:
        return df.with_columns(
            pl.col("household_size")
            .map_elements(self._classify)
            .alias(self.name().lower())
        )

    def _classify(
        self,
        household_size: int,
    ) -> str:
        if household_size == 1:
            return "Single-person Household"
        elif household_size <= 3:
            return "Small Household (2–3)"
        elif household_size <= 5:
            return "Medium Household (4–5)"
        return "Large Household (6+)"
