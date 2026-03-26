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
        labels = [
            "Very Small Household",
            "Small Household",
            "Medium Household",
            "Large Household",
            "Very Large Household",
        ]
        x_pieces = len(labels)
        return df.with_columns(
            [
                pl.col("household_size")
                .qcut(quantiles=x_pieces, labels=labels)
                .alias("household_size_group"),
                pl.col("household_size")
                .qcut(quantiles=x_pieces)
                .alias("household_size_range"),
            ]
        )
