from src.transformation.gold.metrics.strcutures.premium_sunscription_adoption_structure import (
    PremiumSunscriptionAdoptionStructure,
)


class PremiumSubscriptionAdoption(PremiumSunscriptionAdoptionStructure):
    def __init__(self, segment_by: list[str]) -> None:
        super().__init__(columns=segment_by)
