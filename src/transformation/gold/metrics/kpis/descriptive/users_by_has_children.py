from src.transformation.gold.metrics.strcutures.by_column_structure import ByColumnStructure


class PercentageUsersByHasChildren(ByColumnStructure):
    def __init__(self) -> None:
        super().__init__(columns=["has_children_group"])
