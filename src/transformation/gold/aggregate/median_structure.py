import polars as pl


class MedianStructure:
    def __init__(self, column: str) -> None:
        self.column = column

    def aggregate(
        self,
    ) -> pl.Expr:
        return pl.col(self.column).median().round(2).alias(f"avg_{self.column}")
