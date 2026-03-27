import polars as pl


class MeanStructure:
    def __init__(self, column: str, agg_name: str) -> None:
        self.column = column

    def aggregate(
        self,
    ) -> pl.Expr:
        return pl.col(self.column).mean().round(2).alias(f"avg_{self.column}")
