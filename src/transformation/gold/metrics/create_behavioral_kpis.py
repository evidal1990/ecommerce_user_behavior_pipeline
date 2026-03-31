import polars as pl
from src.transformation.gold.metrics.kpis.behavioral import (
    PremiumSubscriptionAdoption,
    AvgDailySessionTime,
    AvgAppUsageFrequency,
    AvgProductViewsPerDay,
    PreferredProductCategory,
    PreferredPaymentMethod,
    AvgBrandLoyaltyScore,
    AvgCouponUsageFrequency,
    AvgReferralCountActivity,
    AvgPurchaseConversionRate,
    AvgCartAbandonmentRate,
    ChurnRate,
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
                "cart_abandonment_rate_group",
                "premium_subscription_group",
                "brand_loyalty_score_group",
                "preferred_payment_method",
                "social_sharing_frequency_per_year_group",
                "app_usage_frequency_per_week_group",
                "browse_to_buy_ratio_group",
                "stress_from_financial_decisions_level_group",
                "return_rate_group",
                "impulse_buying_score_group",
                "metric_value",
            ],
            kpis=self.build_kpis(
                [
                    {
                        "class": PremiumSubscriptionAdoption,
                        "dimensions": ["premium_subscription_group"],
                        "group_by": [
                            "country",
                            "age_group",
                            "annual_income_group",
                            "education_level",
                            "device_type",
                        ],
                    },
                    {
                        "class": AvgDailySessionTime,
                        "dimensions": [
                            "country",
                            "age_group",
                            "device_type",
                        ],
                        "group_by": [],
                    },
                    {
                        "class": AvgAppUsageFrequency,
                        "dimensions": [
                            "country",
                            "age_group",
                            "device_type",
                        ],
                        "group_by": [],
                    },
                    {
                        "class": AvgProductViewsPerDay,
                        "dimensions": [
                            "country",
                            "age_group",
                            "device_type",
                        ],
                        "group_by": [],
                    },
                    {
                        "class": PreferredProductCategory,
                        "dimensions": ["product_category_preference"],
                        "group_by": [
                            "country",
                            "age_group",
                            "device_type",
                        ],
                    },
                    {
                        "class": PreferredPaymentMethod,
                        "dimensions": ["preferred_payment_method"],
                        "group_by": [
                            "country",
                            "age_group",
                            "annual_income_group",
                            "device_type",
                            "cart_abandonment_rate_group",
                        ],
                    },
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
                    {
                        "class": AvgPurchaseConversionRate,
                        "dimensions": [
                            "country",
                            "device_type",
                            "app_usage_frequency_per_week_group",
                            "brand_loyalty_score_group",
                            "browse_to_buy_ratio_group",
                            "social_sharing_frequency_per_year_group",
                        ],
                        "group_by": [],
                    },
                    {
                        "class": AvgCartAbandonmentRate,
                        "dimensions": [
                            "annual_income_group",
                            "preferred_payment_method",
                            "stress_from_financial_decisions_level_group",
                        ],
                        "group_by": [],
                    },
                    {
                        "class": ChurnRate,
                        "dimensions": ["last_purchase_date"],
                        "group_by": [
                            "country",
                            "age_group",
                            "device_type",
                            "premium_subscription_group",
                            "return_rate_group",
                            "impulse_buying_score_group",
                            "app_usage_frequency_per_week_group",
                            "brand_loyalty_score_group",
                        ],
                    },
                ]
            ),
        )
