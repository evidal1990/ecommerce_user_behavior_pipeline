from abc import abstractmethod
from datetime import date
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

    def _finalize_output(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        dimension_cols = [
            col for col in self.group_cols if col != "reference_date" and col in df.columns
        ]
        reference_date_expr = (
            pl.col("reference_date").cast(pl.Utf8)
            if "reference_date" in df.columns
            else pl.lit(date.today().isoformat(), dtype=pl.Utf8)
        )
        dimensions_expr = (
            pl.struct([pl.col(col) for col in dimension_cols]).struct.json_encode()
            if dimension_cols
            else pl.lit("{}")
        )

        return df.with_columns(
            [
                pl.lit(self.metric).alias("kpi_name"),
                pl.lit(self.metric_type).alias("kpi_type"),
                pl.lit(self.dimension_col).alias("dimension_name"),
                pl.col(self.dimension_col).cast(pl.Utf8).alias("dimension_value"),
                pl.col("metric_value").alias("kpi_value"),
                dimensions_expr.alias("dimensions"),
                reference_date_expr.alias("reference_date"),
            ]
        ).select(
            [
                "kpi_name",
                "kpi_type",
                "dimension_name",
                "dimension_value",
                "kpi_value",
                "dimensions",
                "reference_date",
            ]
        )
