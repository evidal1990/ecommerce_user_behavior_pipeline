from src.transformation.gold.aggregate.median_structure import MedianStructure


class AvgBrandLoyaltyScore(MedianStructure):
    def __init__(self) -> None:
        super().__init__(column="brand_loyalty_score")
