import polars as pl
from src.transformation.silver.normalize.normalize_structure import NormalizeStructure


class NormalizeEducationLevel(NormalizeStructure):
    def __init__(
        self,
        column: str,
    ) -> None:
        self._col = column

    def name(self) -> str:
        return "NORMALIZE_EDUCATION_LEVEL"

    def column(self) -> str:
        return self._col

    def execute(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        mapping = {
            "High School": "Ensino Médio",
            "Bachelor": "Bacharel",
            "Master": "Mestre",
            "PhD": "Doutor",
            "Associate Degree": "Associado",
        }

        return df.with_columns(
            pl.col(self._col)
            .replace(mapping)
            .fill_null("Desconhecido")
            .alias(self._col)
        )
