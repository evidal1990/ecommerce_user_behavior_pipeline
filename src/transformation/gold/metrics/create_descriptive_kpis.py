import polars as pl
from src.transformation.gold.metrics.kpis.descriptive import (
    PercentageUsersByAgeGroup,
    PercentageUsersByGender,
    PercentageUsersByCountry,
    PercentageUsersByUrbanRural,
    PercentageUsersByAnnualIncome,
    PercentageUsersByEducationLevel,
    PercentageUsersByEmploymentStatus,
    PercentageUsersByDeviceType,
    PercentageUsersByHasChildren,
)

from src.transformation.gold.metrics.kpis.descriptive import (
    PercentageUsersByPremiumSubscription,
)


class CreateDescriptiveKpis:

    def __init__(self) -> None:
        self.kpis = [
            PercentageUsersByAgeGroup(),
            PercentageUsersByGender(),
            PercentageUsersByCountry(),
            PercentageUsersByUrbanRural(),
            PercentageUsersByAnnualIncome(),
            PercentageUsersByEducationLevel(),
            PercentageUsersByEmploymentStatus(),
            PercentageUsersByDeviceType(),
            PercentageUsersByHasChildren(),
            PercentageUsersByPremiumSubscription(),
        ]

    def execute(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        return pl.concat(kpi.calculate(df) for kpi in self.kpis)
