import logging
from typing import Any
import polars as pl


class FillNumericColumns:

    def __init__(self) -> None:
        pass

    def execute(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        df_cleaned = self._fill(df=df)
        logging.info(
            (
                f"DATA_CLEANING_FIX_NUMERIC_REGISTRIES\n"
                f"Registros: {df_cleaned.height}\n"
                f"Registros inválidos antes da limpeza:\n"
                f"{self._invalid_registries(df=df)}\n"
                f"Registros inválidos depois da limpeza:\n"
                f"{self._invalid_registries(df=df_cleaned)}\n"
            )
        )

        return df

    def _invalid_registries(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        return (
            df.select(
                (pl.col(pl.Float64).is_null() | pl.col(pl.Float64).is_nan()).sum()
            )
            .unpivot(variable_name="coluna", value_name="invalidos")
            .filter(pl.col("invalidos") > 0)
        )

    def _fill(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        strategies = {
            pl.Float64: lambda column: (
                pl.when(pl.col(column) < 0)
                .then(None)
                .otherwise(pl.col(column))
                .fill_null(pl.col(column).median())
            ),
            pl.Int64: lambda column: (
                pl.when(pl.col(column) < 0)
                .then(None)
                .otherwise(pl.col(column))
                .fill_null(pl.col(column).median())
            ),
        }
        exprs = map(
            lambda item: strategies.get(
                item[1],
                lambda column: pl.col(
                    column,
                ),
            )(
                item[0]
            ).alias(item[0]),
            df.schema.items(),
        )
        return df.with_columns(list(exprs))
