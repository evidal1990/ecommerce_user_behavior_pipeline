import polars as pl
from src.validation.interfaces.business_rule import BusinessRule


class AllowedMinMaxValues(BusinessRule):
    def __init__(self, column: str, min: int, max: int, sample_size: int = 30) -> None:
        self.column = column
        self.min = min
        self.max = max
        self.sample_size = sample_size

    def name(self) -> str:
        return f"ALLOWED_MIN_MAX_VALUES_{self.column}"

    def sample_column(self) -> str:
        return self.column

    def invalid_df(self, df: pl.DataFrame) -> pl.DataFrame:
        min, max = df.select(
            pl.col(self.column).min().alias("min_value"),
            pl.col(self.column).max().alias("max_value"),
        ).row(0)

        if min >= self.min and max <= self.max:
            return df.clear()
        return df.filter(
            (pl.col(self.column) < self.min) | (pl.col(self.column) > self.max)
        ).select(
            [
                self.column,
            ]
        )
