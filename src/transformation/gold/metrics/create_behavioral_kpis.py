import polars as pl
from src.transformation.gold.metrics.kpis.behavioral import (
    PremiumSubscriptionAdoption,
    AvgDailySessionTime,
)
from .create_kpis import CreateKpis


class CreateBehavioralKpis(CreateKpis):

    def __init__(self) -> None:
        super().__init__(
            standard_columns=[
                "metric",
                "metric_type",
                "dimension",
                "value",
                "country",
                "age_group",
                "annual_income_group",
                "education_level",
                "device_type",
                "metric_value",
            ],
            kpis=[
                PremiumSubscriptionAdoption(segment_by=["country"]),
                PremiumSubscriptionAdoption(segment_by=["age_group"]),
                PremiumSubscriptionAdoption(segment_by=["annual_income_group"]),
                PremiumSubscriptionAdoption(segment_by=["education_level"]),
                PremiumSubscriptionAdoption(segment_by=["device_type"]),
                AvgDailySessionTime(dimension_col="country"),
                AvgDailySessionTime(dimension_col="age_group"),
                AvgDailySessionTime(dimension_col="device_type"),
            ],
        )
