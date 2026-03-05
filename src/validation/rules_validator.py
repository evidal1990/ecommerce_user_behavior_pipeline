import logging
from src.validation.rules.semantic_rule import SemanticRule
from src.validation.rules.business_rule import BusinessRule
from consts.validation_status import ValidationStatus


class RulesValidator:
    def __init__(
        self, rule_type: str, rules: list[SemanticRule | BusinessRule]
    ) -> None:
        self.rule_type = rule_type
        self.rules = rules

    def execute(self, df) -> dict:
        results = {}
        for rule in self.rules:
            result = rule.validate(df)
            results[rule.name()] = result
            status = result["status"]
            message = (
                f"[{self.rule_type.value}_RULES_VALIDATION]\n"
                f"rule={rule.name()}\n"
                f"status={status}\n"
                f"total_records={result['total_records']}\n"
                f"invalid_records={result['invalid_records']}\n"
                f"invalid_percentage={result['invalid_percentage']}\n"
                f"sample={result['sample']}"
            )
            log_lvl = (
                logging.info
                if status == ValidationStatus.PASS
                else (
                    logging.warning
                    if status == ValidationStatus.WARN
                    else logging.error
                )
            )
            log_lvl(message)
        return results
