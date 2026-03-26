import polars as pl
from src.transformation.silver.enrich.enrich_structure import EnrichStructure


class ExerciseFrequencyGroup(EnrichStructure):

    def __init__(self) -> None:
        pass

    def name(self) -> str:
        return "EXERCISE_FREQUENCY_PER_WEEK_GROUP"

    def execute(
        self,
        df,
    ) -> pl.DataFrame:
        labels = [
            "Sedentary",
            "Lightly Active",
            "Moderately Active",
            "Highly Active",
        ]
        x_pieces = len(labels)
        return df.with_columns(
            [
                pl.col("exercise_frequency_per_week")
                .qcut(quantiles=x_pieces, labels=labels)
                .alias("exercise_frequency_per_week_group"),
                pl.col("exercise_frequency_per_week")
                .qcut(quantiles=x_pieces)
                .alias("exercise_frequency_per_week_range"),
            ]
        )
