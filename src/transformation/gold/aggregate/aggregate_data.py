import polars as pl

# Count
from .count.count_total_users import CountTotalUsers
from .count.count_product_views_per_day import CountProductViewsPerDay

# Avg
from .avg.avg_daily_session_time_minutes import AvgDailySessionTimeMinutes
from .avg.avg_app_usage_frequency_per_week import AvgAppUsageFrequencyPerWeek
from .avg.avg_product_views_per_day import AvgProductViewsPerDay

# Sum
from .sum.sum_premium_users import SumPremiumUsers
from .sum.sum_monthly_spend import SumMonthlySpend
from .sum.sum_has_children import SumHasChildren


class AggregateData:
    def __init__(self) -> None:
        self.df = None

    def execute(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        self.df = df
        columns = [
            "age_group",
            "gender",
            "country",
            "urban_rural",
            "annual_income_group",
            "education_level",
            "employment_status",
            "device_type",
            "preferred_payment_method",
            "cart_abandonment_rate_group",
        ]
        agg_result = []
        agg_result.append(CountTotalUsers().aggregate())
        agg_result.append(CountProductViewsPerDay().aggregate())
        agg_result.append(AvgDailySessionTimeMinutes().aggregate())
        agg_result.append(AvgAppUsageFrequencyPerWeek().aggregate())
        agg_result.append(AvgProductViewsPerDay().aggregate())
        agg_result.append(SumPremiumUsers().aggregate())
        agg_result.append(SumMonthlySpend().aggregate())
        agg_result.append(SumHasChildren().aggregate())

        return df.group_by(columns).agg(agg_result).sort(by=columns)
