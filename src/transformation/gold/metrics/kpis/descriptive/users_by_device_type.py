import polars as pl
from src.transformation.gold.metrics.strcutures.base_structure import BaseStructure


class PercentageUsersByDeviceType(BaseStructure):
    def __init__(
        self,
        segment_by: list[str] = [],
    ) -> None:
        super().__init__(
            metric="users_by_device_type",
            metric_type="percentage",
            dimension_col="device_type",
            group_cols=segment_by,
        )

    def calculate(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        df = self._apply_filter(df)
        result = self._calculate_percentage(df)
        return self._finalize_output(result)
