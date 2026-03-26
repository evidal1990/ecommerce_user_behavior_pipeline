import polars as pl

from src.transformation.gold.aggregate.sum_structure import SumStructure


class SumHasChildren(SumStructure):

    def __init__(self) -> None:
        super().__init__(column="has_children", agg_name="total_has_children")
