import polars as pl
from src.transformation.silver.normalize.normalize_structure import NormalizeStructure


class NormalizePreferredPaymentMethod(NormalizeStructure):
    def __init__(
        self,
        column: str,
    ) -> None:
        self.column = column

    def name(self) -> str:
        return "NORMALIZE_PREFERRED_PAYMENT_METHOD"

    def execute(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        mapping = {
            "Credit Card": "Cartão de Crédito",
            "Debit Card": "Cartão de Débito",
            "Apple Pay": "Apple Pay",
            "Google Pay": "Google Pay",
            "PayPal": "PayPal",
            "Bank Transfer": "Transferência Bancária",
            "Other": "Outro",
        }

        return df.with_columns(
            pl.col(self.column)
            .replace(mapping)
            .fill_null("Desconhecido")
            .alias(self.column)
        )
