from src.transformation.gold.aggregate.median_structure import MedianStructure


class AvgCouponUsageFrequency(MedianStructure):
    def __init__(self) -> None:
        super().__init__(column="coupon_usage_frequency")
