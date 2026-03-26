import polars as pl


class AggregateData:
    def __init__(self) -> None:
        pass

    def execute(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        columns = [
            "age_group",
            "gender",
            "country",
            "urban_rural",
            "",
            "",
        ]
        return df.group_by(columns).agg(
            [pl.col("user_id").count().alias("total_users")]
        )
