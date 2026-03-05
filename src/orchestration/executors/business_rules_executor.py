import logging
import polars as pl
from pathlib import Path
from consts.rule_type import RuleType
from src.utils import file_io
from src.validation import RulesValidator
from src.validation.business.allowed_min_max_values import AllowedMinMaxValues
from src.validation.business.allowed_column_values import AllowedColumnValues
from src.validation.quality.not_allowed_null_columns import NotAllowedNullCount


BASE_DIR = Path(__file__).resolve().parents[3]


class BusinessRulesExecutor:
    def __init__(self) -> None:
        pass

    def start(self, df: pl.DataFrame) -> None:
        logging.info("Validação de regras de negócio iniciada")

        contract = self._get_contract()
        rules = []

        for column, config in contract["columns"].items():
            if "not_null" in config and config["not_null"]:
                rules.append(
                    NotAllowedNullCount(
                        column=column,
                    )
                )
            if "min" in config and "max" in config:
                rules.append(
                    AllowedMinMaxValues(
                        column=column, min=config["min"], max=config["max"]
                    )
                )
            if "values" in config:
                rules.append(
                    AllowedColumnValues(column=column, values=config["values"])
                )

        RulesValidator(RuleType.BUSINESS, rules).execute(df)
        logging.info("Validação de regras de negócio finalizada\n")

    def _get_contract(self) -> dict:
        path = BASE_DIR.joinpath(
            "src",
            "validation",
            "business",
            "schema.yaml",
        )
        try:
            return file_io.read_yaml(path)
        except FileNotFoundError:
            logging.error(f"Schema não encontrado em {path}")
            raise
