import polars as pl
from .create_kpis import CreateKpis
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
    PercentageUsersByPremiumSubscription,
)


class CreateDescriptiveKpis(CreateKpis):

    def __init__(self) -> None:
        super().__init__(
            standard_columns=[
                "metric",
                "metric_type",
                "dimension",
                "value",
                "metric_value",
            ],
            kpis=[
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
            ],
        )
