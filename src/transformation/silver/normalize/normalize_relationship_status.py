import polars as pl
from src.transformation.silver.normalize.normalize_structure import NormalizeStructure


class NormalizeRelationshipStatus(NormalizeStructure):
    def __init__(
        self,
        column: str,
    ) -> None:
        self.column = column

    def name(self) -> str:
        return "NORMALIZE_RELATIONSHIP_STATUS"

    def execute(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        mapping = {
            "Single": "Solteiro(a)",
            "In a relationship": "Em um relacionamento",
            "Married": "Casado(a)",
            "Divorced": "Divorciado(a)",
            "Widowed": "Viúvo(a)",
        }

        return df.with_columns(
            pl.col(self.column)
            .replace(mapping)
            .fill_null("Desconhecido")
            .alias(self.column)
        )
