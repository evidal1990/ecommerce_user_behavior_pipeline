import polars as pl
from src.validation.interfaces.rule import Rule
from consts.validation_status import ValidationStatus


class RequiredColumns(Rule):
    def __init__(self, column: str, contract: dict) -> None:
        self.column = column
        self._contract = contract

    def name(self) -> str:
        return f"{self.column}_REQUIRED_COLUMN_RULE"

    def validate(self, df: pl.DataFrame) -> dict:
        required = self._contract["columns"][self.column].get("required", False)
        if not required:
            return {}
        return {
            "status": (
                ValidationStatus.PASS
                if self.column in df.columns
                else ValidationStatus.FAIL
            )
        }
