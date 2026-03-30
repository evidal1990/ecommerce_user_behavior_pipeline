import polars as pl


class BaseStructure:
    def __init__(
        self,
        dimension_col: str,
        group_cols: list[str] | None = None,
    ) -> None:
        self.dimension_col = dimension_col
        self.group_cols = group_cols or []

    @property
    def all_group_cols(self) -> list[str]:
        return [self.dimension_col] + self.group_cols

    def calculate(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        df_filtered = self._apply_filter(df)
        df_agg = self._calculate_percentage(df_filtered, df_filtered.height)
        df_enriched = self._add_dimension_and_value(df_agg)
        return self._format_output(df_enriched)

    # 🔥 HOOK METHOD (sobrescrito pelas filhas)
    def _apply_filter(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        return df  # padrão: sem filtro

    def _calculate_percentage(
        self,
        df: pl.DataFrame,
        total: int,
    ) -> pl.DataFrame:
        return df.group_by(self.all_group_cols).agg(
            (pl.count() * 100 / total).round(2).alias("percentage")
        ).sort(by=self.all_group_cols)

    def _add_dimension_and_value(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        return df.with_columns(
            [
                pl.lit(self.dimension_col).alias("dimension"),
                pl.col(self.dimension_col).cast(pl.Utf8).alias("value"),
            ]
        )

    def _format_output(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        main_cols = ["dimension", "value"]
        other_cols = self.group_cols

        expected_cols = main_cols + other_cols + ["percentage"]

        for col in expected_cols:
            if col not in df.columns:
                df = df.with_columns(pl.lit("All").alias(col))

        return df.select(expected_cols)
