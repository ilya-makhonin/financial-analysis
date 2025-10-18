import json
import asyncio

from datetime import datetime, time
import math
from src.config import load_config
from src.services import http_session
from src.utils import DateUtils
from src.enums import IntervalType
from src.schemes import ByBitResponseScheme
from src.constants import CONSTANTS


config = load_config()


async def main():
   async with http_session(True) as session:
        start = CONSTANTS.period.period_start
        end = DateUtils.get_clear_end(datetime.now(), IntervalType.HOUR)
        period_in = DateUtils.get_hours_between(start, end)
        period_add = period_in % CONSTANTS.limit.max_limit

        period_list = [
            CONSTANTS.limit.max_limit
            for _ in range(math.floor(period_in / CONSTANTS.limit.max_limit))
        ]

        if period_add:
            period_list.append(period_add)

        for i in period_list:
            end = DateUtils.get_period_end_by_limit(start, IntervalType.HOUR, i)
            print(i, start, end)
            start = end

        '''
        a = session.get_kline(
            category="inverse",
            symbol="BTCUSDT",
            interval="D",
            start=start,
            end=end,
            limit=3
        )

        a1 = ByBitResponseScheme.model_validate(a["result"])

        print(f"{a1.data=}")
        print(a1.data[-1].start_date)
        print(a1.data[0].start_date)

        await asyncio.sleep(1)

        b = session.get_kline(
            category="linear",
            symbol="BTCUSDT",
            interval="D",
            start=end,
            end=DateUtils.get_timestamp_ms(datetime(2025, 10, 6)),
            limit=3
        )

        b1 = ByBitResponseScheme.model_validate(b["result"])

        print(f"{b1.data=}")
        print(b1.data[-1].start_date)
        print(b1.data[0].start_date)

        
        await asyncio.sleep(1)

        c = session.get_kline(
            category="linear",
            symbol="BTCUSDT",
            interval="D",
            start=start,
            end=end,
            limit=3
        )
        '''


if __name__ == "__main__":
    asyncio.run(main())
