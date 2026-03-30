import polars as pl


class ByColumnStructure:
    def __init__(
        self,
        columns: list[str],
    ) -> None:
        self.columns = columns

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
        total = df.height
        return df.group_by(self.columns).agg(
            (pl.count() * 100 / total).round(2).alias("percentage")
        )

    def _add_dimension_and_value(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        main_col = self.columns[0]

        return df.with_columns(
            [
                pl.lit(main_col).alias("dimension"),
                pl.col(main_col).cast(pl.Utf8).alias("value"),
            ]
        )

    def _format_output(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        main_cols = ["dimension", "value"]
        other_cols = self.columns[1:]

        return df.select(main_cols + other_cols + ["percentage"])
