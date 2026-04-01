from src.transformation.gold.metrics.kpis.operational import (
    AvgBrandLoyaltyScore,
    AvgCouponUsageFrequency,
    AvgReferralCountActivity,
)
from .create_kpis import CreateKpis


class CreateOperationalKpis(CreateKpis):

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
                "premium_subscription_group",
                "brand_loyalty_score_group",
                " preferred_payment_method",
                "social_sharing_frequency_per_year_group",
                "app_usage_frequency_per_week_group",
                "metric_value",
            ],
            kpis=self.build_kpis(
                [
                    {
                        "class": AvgBrandLoyaltyScore,
                        "dimensions": [
                            "country",
                            "age_group",
                            "annual_income_group",
                            "premium_subscription_group",
                        ],
                        "group_by": [],
                    },
                    {
                        "class": AvgCouponUsageFrequency,
                        "dimensions": [
                            "annual_income_group",
                            "brand_loyalty_score_group",
                            "preferred_payment_method",
                        ],
                        "group_by": [],
                    },
                    {
                        "class": AvgReferralCountActivity,
                        "dimensions": [
                            "age_group",
                            "brand_loyalty_score_group",
                            "social_sharing_frequency_per_year_group",
                            "premium_subscription_group",
                            "app_usage_frequency_per_week_group",
                        ],
                        "group_by": [],
                    },
                ]
            ),
        )
