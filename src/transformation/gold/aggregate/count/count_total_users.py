import polars as pl

from src.transformation.gold.aggregate.count_structure import CountStructure


class CountTotalUsers(CountStructure):

    def __init__(self) -> None:
        super().__init__(column="user_id", agg_name="total_users")
