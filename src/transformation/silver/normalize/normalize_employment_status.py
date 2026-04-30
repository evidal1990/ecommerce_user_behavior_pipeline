import polars as pl
from src.transformation.silver.normalize.normalize_structure import NormalizeStructure


class NormalizeEmploymentStatus(NormalizeStructure):
    def __init__(
        self,
        column: str,
    ) -> None:
        self.column = column

    def name(self) -> str:
        return "NORMALIZE_EMPLOYMENT_STATUS"

    def execute(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        mapping = {
            "Employed": "Empregado",
            "Unemployed": "Desempregado",
            "Retired": "Aposentado",
            "Student": "Estudante",
            "Self-employed": "Autônomo",
        }

        return df.with_columns(
            pl.col(self.column)
            .replace(mapping)
            .fill_null("Desconhecido")
            .alias(self.column)
        )
