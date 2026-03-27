import polars as pl


class PercentageStructure:
    def __init__(
        self,
        column: str,
    ) -> None:
        self.column = column

    def calculate(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        df_agg = self._calculate_percentage(df)
        df_enriched = self._add_dimension_and_value(df_agg)
        return self._format_output(df_enriched)

    def _calculate_percentage(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        return df.group_by(self.column).agg(
            (pl.count() * 100 / df.height).round(2).alias("percentage")
        )

    def _add_dimension_and_value(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        return df.with_columns(
            [
                pl.lit(self.column).cast(pl.Utf8).alias("dimension"),
                pl.col(self.column).cast(pl.Utf8).alias("value"),
            ]
        )

    def _format_output(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        return df.select(["dimension", "value", "percentage"])
