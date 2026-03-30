import polars as pl


class CreateKpis:

    def __init__(
        self,
        kpis: list,
        standard_columns: list,
    ) -> None:
        self.kpis = kpis
        self.standard_columns = standard_columns

    def execute(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:

        return pl.concat(
            [self._standardize_schema(kpi.calculate(df)) for kpi in self.kpis]
        )

    def _standardize_schema(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        for col in self.standard_columns:
            if col not in df.columns:
                df = df.with_columns(pl.lit("All").cast(pl.Utf8).alias(col))

        df = df.with_columns(
            [
                pl.col(col).cast(pl.Utf8)
                for col in self.standard_columns
                if col != "percentage"
            ]
            + [pl.col("percentage").cast(pl.Float64)]
        )

        return df.select(self.standard_columns)
