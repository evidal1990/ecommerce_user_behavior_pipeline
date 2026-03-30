from polars import col
from src.transformation.gold.metrics.strcutures.by_column_structure import ByColumnStructure


class PercentageUsersByPremiumSubscription(ByColumnStructure):
    def __init__(self) -> None:
        super().__init__(columns=["premium_subscription_group"])
