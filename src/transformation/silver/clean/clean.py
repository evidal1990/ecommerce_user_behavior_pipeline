import polars as pl
import logging
from .format import FormatData
from .remove_duplicates import RemoveDuplicates
from .fill_columns import FillColumns


class CleanData:
    def __init__(self) -> None:
        pass

    def execute(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        df = RemoveDuplicates().execute(df=df)
        df = FormatData().execute(df=df)
        logging.info("Formatação de strings finalizada")

        df = FillColumns().execute(df=df)
        logging.info("Tratamento de dados numéricos finalizado")
        return df
