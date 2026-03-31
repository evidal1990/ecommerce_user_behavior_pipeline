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
            kpis=self.build_kpis(
                [
                    {
                        "class": PercentageUsersByAgeGroup,
                        "dimensions": ["age_group"],
                        "group_by": [],
                    },
                    {
                        "class": PercentageUsersByGender,
                        "dimensions": ["gender"],
                        "group_by": [],
                    },
                    {
                        "class": PercentageUsersByCountry,
                        "dimensions": ["country"],
                        "group_by": [],
                    },
                    {
                        "class": PercentageUsersByUrbanRural,
                        "dimensions": ["urban_rural"],
                        "group_by": [],
                    },
                    {
                        "class": PercentageUsersByAnnualIncome,
                        "dimensions": ["annual_income_group"],
                        "group_by": [],
                    },
                    {
                        "class": PercentageUsersByEducationLevel,
                        "dimensions": ["education_level"],
                        "group_by": [],
                    },
                    {
                        "class": PercentageUsersByEmploymentStatus,
                        "dimensions": ["employment_status"],
                        "group_by": [],
                    },
                    {
                        "class": PercentageUsersByDeviceType,
                        "dimensions": ["device_type"],
                        "group_by": [],
                    },
                    {
                        "class": PercentageUsersByHasChildren,
                        "dimensions": ["has_children_group"],
                        "group_by": [],
                    },
                    {
                        "class": PercentageUsersByPremiumSubscription,
                        "dimensions": ["premium_subscription_group"],
                        "group_by": [],
                    },
                ]
            ),
        )
