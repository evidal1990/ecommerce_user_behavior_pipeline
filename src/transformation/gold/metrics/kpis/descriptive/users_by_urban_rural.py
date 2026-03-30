from src.transformation.gold.metrics.strcutures.by_column_structure import ByColumnStructure


class PercentageUsersByUrbanRural(ByColumnStructure):
    def __init__(self) -> None:
        super().__init__(columns=["urban_rural"])
