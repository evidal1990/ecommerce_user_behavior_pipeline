from src.transformation.gold.metrics.strcutures.by_column_structure import ByColumnStructure


class PercentageUsersByAnnualIncome(ByColumnStructure):
    def __init__(self) -> None:
        super().__init__(columns=["annual_income_group"])
