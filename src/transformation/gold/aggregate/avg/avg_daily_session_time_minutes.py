from src.transformation.gold.aggregate.median_structure import MedianStructure


class AvgDailySessionTimeMinutes(MedianStructure):
    def __init__(self) -> None:
        super().__init__(column="daily_session_time_minutes")
