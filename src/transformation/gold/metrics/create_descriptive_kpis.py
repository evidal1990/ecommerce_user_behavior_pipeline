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
                        "dimension": "age_group",
                        "group_by": [],
                    },
                    {
                        "class": PercentageUsersByGender,
                        "dimension": "gender",
                        "group_by": [],
                    },
                    {
                        "class": PercentageUsersByCountry,
                        "dimension": "country",
                        "group_by": [],
                    },
                    {
                        "class": PercentageUsersByUrbanRural,
                        "dimension": "urban_rural",
                        "group_by": [],
                    },
                    {
                        "class": PercentageUsersByAnnualIncome,
                        "dimension": "annual_income_group",
                        "group_by": [],
                    },
                    {
                        "class": PercentageUsersByEducationLevel,
                        "dimension": "education_level",
                        "group_by": [],
                    },
                    {
                        "class": PercentageUsersByEmploymentStatus,
                        "dimension": "employment_status",
                        "group_by": [],
                    },
                    {
                        "class": PercentageUsersByDeviceType,
                        "dimension": "device_type",
                        "group_by": [],
                    },
                    {
                        "class": PercentageUsersByHasChildren,
                        "dimension": "has_children_group",
                        "group_by": [],
                    },
                    {
                        "class": PercentageUsersByPremiumSubscription,
                        "dimension": "premium_subscription_group",
                        "group_by": [],
                    },
                ]
            ),
        )
