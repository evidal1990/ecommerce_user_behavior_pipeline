from src.transformation.gold.aggregate.median_structure import MedianStructure


class AvgReferralCount(MedianStructure):
    def __init__(self) -> None:
        super().__init__(column="referral_count")
