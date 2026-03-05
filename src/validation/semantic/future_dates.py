import polars as pl
from src.validation.rules.semantic_rule import SemanticRule
from datetime import datetime


class FutureDates(SemanticRule):
    def __init__(
        self, column: str, date_limit: datetime, sample_size: int = 10
    ) -> None:
        self.column = column
        self.date_limit = date_limit
        self.sample_size = sample_size

    def name(self) -> str:
        return "FUTURE_DATES"

    def sample_column(self) -> str:
        return self.column

    def invalid_df(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.filter(pl.col(self.column) > self.date_limit).select([self.column])
