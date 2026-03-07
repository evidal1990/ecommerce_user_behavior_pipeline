import logging
import polars as pl
from src.transformation.silver.enrich.enrich_dataframe import EnrichDataFrame


class TransformationSilverExecutor:
    def __init__(self, settings: dict) -> None:
        data = settings.get("data")
        if not data or "silver" not in data:
            raise ValueError("Configuração de silver não encontrada")

        self._settings = data["silver"]

    def start(self, df:pl.DataFrame) -> pl.DataFrame:
        logging.info("Transformação da camada bronze iniciada")

        df = EnrichDataFrame().execute(df=df)
        self._write_silver(df=df)
        logging.info("Transformação da camada bronze finalizada\n")
        return df

    def _write_silver(self, df) -> None:
        pass
        # path = self._settings["data"]["silver"]["destination"]
        # Path(path).parent.mkdir(parents=True, exist_ok=True)
        # df.write_csv(path)
