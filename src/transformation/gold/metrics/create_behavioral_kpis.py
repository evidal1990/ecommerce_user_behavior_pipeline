import polars as pl
from src.transformation.gold.metrics.kpis.behavioral import (
    PremiumSubscriptionAdoption,
    AvgDailySessionTime,
    AvgAppUsageFrequency,
)
from .create_kpis import CreateKpis


class CreateBehavioralKpis(CreateKpis):

    def __init__(self) -> None:
        self.premium_subscription_adoption = [
            PremiumSubscriptionAdoption(segment_by=["country"]),
            PremiumSubscriptionAdoption(segment_by=["age_group"]),
            PremiumSubscriptionAdoption(segment_by=["annual_income_group"]),
            PremiumSubscriptionAdoption(segment_by=["education_level"]),
            PremiumSubscriptionAdoption(segment_by=["device_type"]),
        ]
        self.avg_daily_session_time = [
            AvgDailySessionTime(dimension_col="country"),
            AvgDailySessionTime(dimension_col="age_group"),
            AvgDailySessionTime(dimension_col="device_type"),
        ]
        self.app_usage_frequency = [
            AvgAppUsageFrequency(dimension_col="country"),
            AvgAppUsageFrequency(dimension_col="age_group"),
            AvgAppUsageFrequency(dimension_col="device_type"),
        ]
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
                *self.premium_subscription_adoption,
                *self.avg_daily_session_time,
                *self.app_usage_frequency,
            ],
        )
