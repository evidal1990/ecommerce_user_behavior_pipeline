import polars as pl

from src.transformation.silver.normalize.normalize_structure import NormalizeStructure


class MinMaxScaling(NormalizeStructure):
    def __init__(self, column: str) -> None:
        self.col = column

    def name(self) -> str:
        return "MIN_MAX"

    def column(self) -> str:
        return f"{self.col}_scaled"

    def execute(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        min = df.select(pl.col(self.col).min()).item()
        max = df.select(pl.col(self.col).max()).item()
        return df.with_columns(
            ((pl.col(self.col) - min) / (max - min)).alias(f"{self.col}_scaled")
        )
