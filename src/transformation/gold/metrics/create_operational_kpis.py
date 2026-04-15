from src.transformation.gold.metrics.kpis.operational import (
    AvgBrandLoyaltyScore,
    AvgCouponUsageFrequency,
    AvgReferralCountActivity,
)
from .create_kpis import CreateKpis

COLUMNS = [
    "gender",
    "country",
    "urban_rural",
    "education_level",
    "employment_status",
    "device_type",
    "preferred_payment_method",
    "age_group",
    "annual_income_group",
    "household_size_group",
    "brand_loyalty_score_group",
    "impulse_buying_score_group",
    "social_media_influence_score_group",
    "stress_from_financial_decisions_level_group",
    "referral_count_group",
    "impulse_purchases_per_month_group",
    "browse_to_buy_ratio_group",
    "return_rate_group",
    "purchase_conversion_rate_group",
    "cart_abandonment_rate_group",
    "app_usage_frequency_per_week_group",
    "has_children_group",
    "last_purchase_date",
]

class CreateOperationalKpis(CreateKpis):

    def __init__(self) -> None:
        super().__init__(
            standard_columns=[
                "metric",
                "metric_type",
                "dimension",
                "value",
                *COLUMNS,
                "metric_value",
            ],
            kpis=self.build_kpis(
                [
                    {
                        "class": AvgBrandLoyaltyScore,
                        "dimensions": COLUMNS,
                        "group_by": [],
                    },
                    {
                        "class": AvgCouponUsageFrequency,
                        "dimensions": COLUMNS,
                        "group_by": [],
                    },
                    {
                        "class": AvgReferralCountActivity,
                        "dimensions": COLUMNS,
                        "group_by": [],
                    },
                ]
            ),
        )
