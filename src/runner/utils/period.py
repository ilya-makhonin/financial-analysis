import math
from datetime import datetime
from src.utils import DateUtils
from src.enums import IntervalType
from src.schemes import PeriodScheme


def get_period_list(
    period_start: datetime,
    period_end: datetime,
    period_type: IntervalType,
    limit: int,
) -> list[PeriodScheme] | None:
    if period_start >= period_end:
        return None

    period_in = DateUtils.get_count_between(period_start, period_end, period_type)
    period_add = period_in % limit
    start_date = period_start
    result: list[PeriodScheme] = []

    for _ in range(math.floor(period_in / limit)):
        end_date = DateUtils.get_period_end_by_limit(start_date, period_type, limit)
        result.append(PeriodScheme(
            count=limit,
            start_date=start_date,
            end_date=end_date
        ))
        start_date = end_date

    if period_add:
        result.append(PeriodScheme(
            count=period_add,
            start_date=start_date,
            end_date=DateUtils.get_period_end_by_limit(
                start_date, period_type, period_add
            )
        ))

    return result
