import polars as pl
from src.transformation.silver.enrich.enrich_structure import EnrichStructure


class AgeGroup(EnrichStructure):

    def __init__(self) -> None:
        pass

    def name(self) -> str:
        return "AGE_GROUP"

    def execute(
        self,
        df,
    ) -> pl.DataFrame:
        labels = [
            "Early Adopters",
            "Early Career Professionals",
            "Professional Consolidation",
            "High Financial Stability",
            "Pre-Retirement",
            "Low Digital Adoption",
        ]
        x_pieces = len(labels)
        return df.with_columns(
            [
                pl.col("age")
                .qcut(quantiles=x_pieces, labels=labels)
                .alias("age_group"),
                pl.col("age").qcut(quantiles=x_pieces).alias("age_range"),
            ]
        )
