import polars as pl
from src.transformation.silver.normalize.normalize_structure import NormalizeStructure


class NormalizeGender(NormalizeStructure):
    def __init__(
        self,
        column: str,
    ) -> None:
        self.column = column

    def name(self) -> str:
        return "NORMALIZE_GENDER"

    def execute(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        mapping = {
            "Male": "Masculino",
            "Female": "Feminino",
            "Non-binary": "Não Binário",
            "Other": "Outro",
        }

        return df.with_columns(
            pl.col(self.column)
            .replace(mapping)
            .fill_null("Desconhecido")
            .alias(self.column)
        )
