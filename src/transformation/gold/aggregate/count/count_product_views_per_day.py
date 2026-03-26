import polars as pl

from src.transformation.gold.aggregate.count_structure import CountStructure


class CountProductViewsPerDay(CountStructure):

    def __init__(self) -> None:
        super().__init__(column="user_id", agg_name="product_views_per_day")
