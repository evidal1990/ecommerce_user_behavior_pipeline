from src.transformation.gold.metrics.by_total_structure import PercentageStructure


class PercentageUsersByEmploymentStatus(PercentageStructure):
    def __init__(self) -> None:
        super().__init__(column="employment_status")
