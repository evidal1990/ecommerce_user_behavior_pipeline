import logging
import polars as pl
from pathlib import Path
from consts.rule_type import RuleType
from consts.employment_status import EmploymentStatus
from src.utils import file_io
from src.validation import RulesValidator
from src.validation.business.employment_status_income import IncomePerEmploymentStatus
from src.validation.semantic.allowed_min_value import AllowedMinValue
from src.validation.semantic.allowed_max_value import AllowedMaxValue
from src.validation.semantic.allowed_column_values import AllowedColumnValues


BASE_DIR = Path(__file__).resolve().parents[3]


class BusinessRulesExecutor:
    def __init__(self) -> None:
        pass

    def start(self, df: pl.DataFrame) -> None:
        logging.info("Validação de regras de negócio iniciada")

        contract = self._get_contract()
        rules = []
        rules.append(
            IncomePerEmploymentStatus(
                status=EmploymentStatus.EMPLOYED,
            )
        )
        rules.append(
            IncomePerEmploymentStatus(
                status=EmploymentStatus.SELF_EMPLOYED,
            )
        )
        rules.append(
            IncomePerEmploymentStatus(
                status=EmploymentStatus.UNEMPLOYED,
            )
        )

        for column, config in contract["columns"].items():
            if "min" in config:
                rules.append(
                    AllowedMinValue(
                        column=column,
                        min=config["min"],
                    )
                )
            if "max" in config:
                rules.append(
                    AllowedMaxValue(
                        column=column,
                        max=config["max"],
                    )
                )
            if "values" in config:
                rules.append(
                    AllowedColumnValues(
                        column=column,
                        values=config["values"],
                    )
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
