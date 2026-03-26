import polars as pl
from src.transformation.silver.enrich.enrich_structure import EnrichStructure


class AnnualIncomeGroup(EnrichStructure):

    def __init__(self) -> None:
        pass

    def name(self) -> str:
        return "ANNUAL_INCOME_GROUP"

    def execute(
        self,
        df,
    ) -> pl.DataFrame:
        x_pieces = 5
        labels = [
            "E (Lower Class)",
            "D (Lower Middle Class)",
            "C (Middle Class)",
            "B (Upper Middle Class)",
            "A (Upper Class)",
        ]
        return df.with_columns(
            [
                pl.col("annual_income")
                .qcut(quantiles=x_pieces, labels=labels)
                .alias("annual_income_group"),
                pl.col("annual_income")
                .qcut(quantiles=x_pieces)
                .alias("annual_income_range"),
            ]
        )
