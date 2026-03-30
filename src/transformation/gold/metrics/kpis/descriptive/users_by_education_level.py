from src.transformation.gold.metrics.strcutures.by_column_structure import ByColumnStructure


class PercentageUsersByEducationLevel(ByColumnStructure):
    def __init__(self) -> None:
        super().__init__(columns=["education_level"])
