import polars as pl


class PremiumSunscriptionAdoptionStructure:
    def __init__(
        self,
        columns: list[str],
    ) -> None:
        columns.insert(0, "premium_subscription_group")
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
        return (
            df.filter(pl.col("premium_subscription_group") == "Yes")
            .group_by(self.columns)
            .agg((pl.count() * 100 / total).round(2).alias("percentage"))
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

        expected_cols = main_cols + other_cols + ["percentage"]

        # adiciona colunas que não existem
        for col in expected_cols:
            if col not in df.columns:
                df = df.with_columns(pl.lit(None).alias(col))

        # garante ordem final
        return df.select(expected_cols)
