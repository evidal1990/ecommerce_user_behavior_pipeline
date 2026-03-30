from src.transformation.gold.metrics.by_total_structure import PercentageStructure


class PremiumSubscriptionAdoption(PercentageStructure):
    def __init__(self) -> None:
        super().__init__(column="avg_daily_session_minutes")
