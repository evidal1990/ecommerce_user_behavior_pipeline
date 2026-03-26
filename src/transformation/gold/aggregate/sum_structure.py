import polars as pl


class SumStructure:
    def __init__(self, column: str, agg_name: str) -> None:
        self.column = column
        self.agg_name = agg_name

    def aggregate(self) -> pl.Expr:
        return pl.col(self.column).sum().alias(self.agg_name)
