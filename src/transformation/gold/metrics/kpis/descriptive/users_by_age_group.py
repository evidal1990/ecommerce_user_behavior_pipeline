from src.transformation.gold.metrics.strcutures.by_column_structure import ByColumnStructure


class PercentageUsersByAgeGroup(ByColumnStructure):
    def __init__(self) -> None:
        super().__init__(columns=["age_group"])
