import logging
from pathlib import Path
import polars as pl
from datetime import datetime


class CreateIsFutureDateColumn:

    def __init__(self, df: pl.DataFrame, settings: dict) -> None:
        self.df = df
        self.settings = settings
        self.current_date = datetime.now().date()
        self.total_records = self.df.height

    def _sufix(self) -> str:
        return "is_future"

    def execute(self, columns: list[str]) -> pl.DataFrame:
        for col in columns:
            new_col = f"{col}_{self._sufix()}"
            df = self._create(
                column=col,
                new_column=new_col,
            )
            self._save_file(
                df=df,
                column=col,
            )
            true_records, false_records = self._get_records(
                df=df,
                column=new_col,
            )
            self._log(
                column=new_col,
                true_records=true_records,
                false_records=false_records,
            )
        return df

    def _create(
        self,
        column: str,
        new_column: str,
    ) -> pl.DataFrame:
        return self.df.with_columns(
            (pl.col(column) > self.current_date).alias(new_column)
        )

    def _get_records(
        self,
        df: pl.DataFrame,
        column: str,
    ) -> tuple[int, int]:
        return df.select(
            [
                (pl.col(column).sum()).item().alias("true_records"),
                (pl.len() - pl.col(column).sum()).item().alias("false_records"),
            ]
        ).row(0)

    def _log(
        self,
        column: str,
        true_records: int,
        false_records: int,
    ) -> None:
        logging.info(
            (
                f"[CREATE_IS_FUTURE_DATE_COLUMN]\n"
                f"new_column={column}\n"
                f"records → True: {true_records} | False: {false_records}"
            )
        )

    def _save_file(self, df: pl.DataFrame, column: str) -> None:
        path = f"{self.settings}{column}_future_dates.csv"
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        df.filter(pl.col(column) > self.current_date).select(
            ["user_id", column]
        ).write_csv(path)
