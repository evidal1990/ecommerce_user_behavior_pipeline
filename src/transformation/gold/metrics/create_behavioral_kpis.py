import polars as pl
from src.transformation.gold.metrics.kpis.behavioral import PremiumSubscriptionAdoption
from .create_kpis import CreateKpis


class CreateBehavioralKpis(CreateKpis):

    def __init__(self) -> None:
        super().__init__(
            standard_columns=[
                "dimension",
                "value",
                "country",
                "age_group",
                "annual_income_group",
                "education_level",
                "device_type",
                "percentage",
            ],
            kpis=[
                PremiumSubscriptionAdoption(segment_by=["country"]),
                PremiumSubscriptionAdoption(segment_by=["age_group"]),
                PremiumSubscriptionAdoption(segment_by=["annual_income_group"]),
                PremiumSubscriptionAdoption(segment_by=["education_level"]),
            ],
        )
