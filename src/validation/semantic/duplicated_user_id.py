import polars as pl
from src.validation.interfaces.semantic_rule import SemanticRule


class DuplicatedUserId(SemanticRule):
    def __init__(self, sample_size: int = 10) -> None:
        super().__init__(sample_size)
        self._df = None

    def name(self) -> str:
        return "DUPLICATED_USER_ID"

    def sample_column(self) -> str:
        return "user_id"

    def invalid_df(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.filter(pl.col("user_id").is_duplicated()).select("user_id").unique()
