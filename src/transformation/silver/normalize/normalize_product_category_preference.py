import polars as pl
from src.transformation.silver.normalize.normalize_structure import NormalizeStructure


class NormalizeProductCategoryPreference(NormalizeStructure):
    def __init__(
        self,
        column: str,
    ) -> None:
        self.column = column

    def name(self) -> str:
        return "NORMALIZE_PRODUCT_CATEGORY_PREFERENCE"

    def execute(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        mapping = {
            "Groceries": "Alimentos",
            "Beauty": "Beleza",
            "Toys": "Brinquedos",
            "Home & Health": "Casa e Saúde",
            "Home & Kitchen": "Casa e Cozinha",
            "Sports": "Esportes",
            "Electronics": "Eletrônicos",
            "Fashion": "Moda",
            "Books": "Livros",
        }

        return df.with_columns(
            pl.col(self.column)
            .replace(mapping)
            .fill_null("Desconhecido")
            .alias(self.column)
        )
