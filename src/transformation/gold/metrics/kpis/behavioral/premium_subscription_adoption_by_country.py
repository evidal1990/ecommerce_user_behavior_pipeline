from transformation.gold.metrics.strcutures.premium_sunscription_adoption_structure import (
    PremiumSunscriptionAdoptionStructure,
)


class PremiumSubscriptionAdoptionByContry(PremiumSunscriptionAdoptionStructure):
    def __init__(self) -> None:
        super().__init__(columns=["country"])
