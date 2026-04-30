import polars as pl
import logging
from consts.action_status import ActionStatus
from src.transformation.silver.normalize.normalize_structure import NormalizeStructure


class Normalize:
    def __init__(
        self,
        actions: list[NormalizeStructure],
    ) -> None:
        self.actions = actions

    def execute(
        self,
        df,
    ) -> pl.DataFrame:

        for action in self.actions:
            df = action.execute(df)
            if df.shape[0] == 0:
                status = ActionStatus.FAIL
                log_lvl = logging.error
            else:
                status = ActionStatus.PASS
                log_lvl = logging.info
            col = action.column()
            message = (
                f"[NORMALIZE_DATA_{action.name()}]\n"
                f"status={status}\n"
                f"column={col}\n"
                f"min={df[col].min()}\n"
                f"max={df[col].max()}\n"
            )
            log_lvl(message)
        return df
