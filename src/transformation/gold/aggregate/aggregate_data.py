import polars as pl

# Count
from src.transformation.gold.aggregate.count import (
    CountTotalUsers,
    CountProductViewsPerDay,
    CountLastPurchaseDate,
)

# Sum
from src.transformation.gold.aggregate.sum import (
    SumDailySessionTimeMinutes,
    SumPremiumUsers,
    SumMonthlySpend,
    SumHasChildren,
    SumCheckoutAbandonmentsPerMonth,
)

# Avg
from src.transformation.gold.aggregate.avg import (
    AvgDailySessionTimeMinutes,
    AvgAppUsageFrequencyPerWeek,
    AvgAppUsageFrequencyPerWeekScaled,
    AvgProductViewsPerDay,
    AvgProductViewsPerDayScaled,
    AvgBrandLoyaltyScore,
    AvgCouponUsageFrequency,
    AvgReferralCount,
    AvgPurchaseConversionRate,
    AvgCartAbandonmentRate,
    AvgNotificationResponseRateScaled,
)


class AggregateData:
    def __init__(self) -> None:
        self.df = None

    def execute(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        self.df = df
        columns = [
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
            "relationship_status",
            "shopping_time_of_day",
            "social_sharing_frequency_per_year_group",
            "last_purchase_date",
        ]
        agg_result = []
        # Count
        agg_result.append(CountTotalUsers().aggregate())
        agg_result.append(CountProductViewsPerDay().aggregate())
        agg_result.append(CountLastPurchaseDate().aggregate())

        # Sum
        agg_result.append(SumPremiumUsers().aggregate())
        agg_result.append(SumMonthlySpend().aggregate())
        agg_result.append(SumHasChildren().aggregate())
        agg_result.append(SumCheckoutAbandonmentsPerMonth().aggregate())
        agg_result.append(SumDailySessionTimeMinutes().aggregate())

        # Avg
        agg_result.append(AvgDailySessionTimeMinutes().aggregate())
        agg_result.append(AvgAppUsageFrequencyPerWeek().aggregate())
        agg_result.append(AvgAppUsageFrequencyPerWeekScaled().aggregate())
        agg_result.append(AvgProductViewsPerDay().aggregate())
        agg_result.append(AvgProductViewsPerDayScaled().aggregate())
        agg_result.append(AvgBrandLoyaltyScore().aggregate())
        agg_result.append(AvgCouponUsageFrequency().aggregate())
        agg_result.append(AvgReferralCount().aggregate())
        agg_result.append(AvgPurchaseConversionRate().aggregate())
        agg_result.append(AvgCartAbandonmentRate().aggregate())
        agg_result.append(AvgNotificationResponseRateScaled().aggregate())

        return df.group_by(columns).agg(agg_result).sort(by=columns)
