import polars as pl
from src.transformation.silver.normalize.normalize_structure import NormalizeStructure


class NormalizeNeighborhood(NormalizeStructure):
    def __init__(
        self,
        column: str,
    ) -> None:
        self.column = column

    def execute(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        mapping = {
            "Urban": "Urbano",
            "Rural": "Rural",
            "Suburban": "Suburbano",
        }

        return df.with_columns(
            pl.col(self.column)
            .replace(mapping)
            .fill_null("Desconhecido")
            .alias(self.column)
        )
