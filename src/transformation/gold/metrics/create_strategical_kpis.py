from src.transformation.gold.metrics.kpis.strategical import (
    AvgPurchaseConversionRate,
    AvgCartAbandonmentRate,
    ChurnRate,
    DailyActiveUsers,
    NetPromoterScore,
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
    "premium_subscription_group",
    "product_category_preference",
    "social_sharing_frequency_per_year_group",
    "last_purchase_date",
]


def _columns_without(*exclude: str) -> list[str]:
    return [c for c in COLUMNS if c not in set(exclude)]


class CreateStrategicalKpis(CreateKpis):

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
                        "class": AvgPurchaseConversionRate,
                        "dimensions": _columns_without(
                            "purchase_conversion_rate_group",
                        ),
                        "group_by": [],
                    },
                    {
                        "class": AvgCartAbandonmentRate,
                        "dimensions": _columns_without(
                            "cart_abandonment_rate_group",
                        ),
                        "group_by": [],
                    },
                    {
                        "class": ChurnRate,
                        "dimensions": ["last_purchase_date"],
                        "group_by": _columns_without(
                            "last_purchase_date",
                        ),
                    },
                    {
                        "class": DailyActiveUsers,
                        "dimensions": _columns_without(
                            "daily_session_time_minutes_group",
                        ),
                        "group_by": [],
                    },
                    {
                        "class": NetPromoterScore,
                        "dimensions": _columns_without(
                            "brand_loyalty_score_group",
                        ),
                        "group_by": [],
                    },
                ]
            ),
        )
