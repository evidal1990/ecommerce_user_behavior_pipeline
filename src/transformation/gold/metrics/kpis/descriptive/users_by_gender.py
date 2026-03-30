from polars import col
from src.transformation.gold.metrics.strcutures.by_column_structure import ByColumnStructure


class PercentageUsersByGender(ByColumnStructure):
    def __init__(self) -> None:
        super().__init__(columns=["gender"])
