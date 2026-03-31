from abc import abstractmethod
import polars as pl


class BaseStructure:
    def __init__(
        self,
        metric: str,
        metric_type: str,
        dimension_col: str,
        group_cols: list[str] | None = None,
    ) -> None:
        self.metric = metric
        self.metric_type = metric_type
        self.dimension_col = dimension_col
        self.group_cols = group_cols or []

    @property
    def all_group_cols(self) -> list[str]:
        return [self.dimension_col] + self.group_cols

    @abstractmethod
    def calculate(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        pass

    def _apply_filter(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        return df

    def _calculate_rate(
        self,
        df: pl.DataFrame,
        condition: pl.Expr,
    ) -> pl.DataFrame:
        return (
            df.with_columns(condition.cast(pl.Int8).alias("metric_value"))
            .group_by(self.all_group_cols)
            .agg(pl.col("metric_value").mean().round(2))
            .sort(by=self.all_group_cols)
        )

    def _calculate_percentage(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        total = df.select(pl.col("count_users").sum()).item()

        return df.group_by(self.all_group_cols).agg(
            (pl.col("count_users").sum() / total * 100).round(2).alias("metric_value")
        )

    # ✔️ MÉDIA (valor contínuo)
    def _calculate_average(
        self,
        df: pl.DataFrame,
        column: str,
    ) -> pl.DataFrame:
        return df.group_by(self.all_group_cols).agg(
            pl.col(column)
            .mul(pl.col("count_users"))
            .sum()
            .truediv(pl.col("count_users").sum())
            .round(2)
            .alias("metric_value")
        )

    def _calculate_count(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        return (
            df.group_by(self.all_group_cols)
            .agg(pl.count().alias("metric_value"))
            .sort(by=self.all_group_cols)
        )

    # ✔️ PADRONIZAÇÃO FINAL (único ponto de formatação)
    def _finalize_output(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        return df.with_columns(
            [
                pl.lit(self.metric).alias("metric"),
                pl.lit(self.metric_type).alias("metric_type"),
                pl.lit(self.dimension_col).alias("dimension"),
                pl.col(self.dimension_col).cast(pl.Utf8).alias("value"),
            ]
        ).select(
            [
                "metric",
                "metric_type",
                "dimension",
                "value",
                *self.group_cols,
                "metric_value",
            ]
        )
