import polars as pl
from src.transformation.silver.normalize.normalize_structure import NormalizeStructure


class NormalizeShoppingTimeOfDay(NormalizeStructure):
    def __init__(
        self,
        column: str,
    ) -> None:
        self.column = column

    def name(self) -> str:
        return "NORMALIZE_SHOPPING_TIME_OF_DAY"

    def execute(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        mapping = {
            "Morning": "Manhã",
            "Afternoon": "Tarde",
            "Evening": "Noite",
            "Night": "Madrugada",
        }

        return df.with_columns(
            pl.col(self.column)
            .replace(mapping)
            .fill_null("Desconhecido")
            .alias(self.column)
        )
