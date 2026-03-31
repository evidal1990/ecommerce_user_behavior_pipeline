class BaseKPI:
    def __init__(
        self,
        metric: str,
        value_col: str,
        dimension_col: str,
        group_by: list[str] | None = None,
    ) -> None:
        self.metric = metric
        self.value_col = value_col
        self.dimension_col = dimension_col
        self.group_by = group_by or []
