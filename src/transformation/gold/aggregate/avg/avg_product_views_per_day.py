import polars as pl
from src.transformation.gold.aggregate.median_structure import MedianStructure


class AvgProductViewsPerDay(MedianStructure):
    def __init__(self) -> None:
        pass

    def aggregate(
        self,
    ) -> pl.Expr:
        return super().aggregate(column="product_views_per_day")
