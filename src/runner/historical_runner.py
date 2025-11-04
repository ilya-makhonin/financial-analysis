import asyncio
import logging

from datetime import datetime

from src.schemes import PeriodScheme, ByBitResponseScheme
from src.config import Config
from src.enums import IntervalType, CryptoType, SortType
from src.services import http_session
from src.utils import DateUtils
from src.database import OdmMethods, BaseDocument
from src.constants import CONSTANTS

from .utils.mapping import MappingParam
from .utils.period import get_period_list


logger = logging.getLogger(__name__)


async def get_historical_data(
    *
    config: Config,
    end_date: datetime,
    start_date: datetime = CONSTANTS.period.period_start,
    max_count: int = CONSTANTS.limit.max_limit,
    crypto_type: CryptoType = CryptoType.BTC,
    interval_type: IntervalType = IntervalType.DAY,
):
    last_kline: BaseDocument | None = await OdmMethods.get_last_kline(crypto_type, interval_type)
    now_date = datetime.now()

    max_limit: int = CONSTANTS.limit.max_limit
    min_date = DateUtils.period_inc(last_kline.start_date, interval_type)\
        if last_kline else CONSTANTS.period.period_start 
    max_date = now_date if end_date > now_date else end_date

    count = max_limit if max_count > max_limit else max_count
    period_start = min_date if start_date < min_date else start_date
    period_end = DateUtils.get_clear_datetime(max_date, interval_type)

    symbol = MappingParam.get_symbol(crypto_type)
    interval = MappingParam.get_interval(interval_type)
    sorttype = MappingParam.get_sort(SortType.SPOT)

    periods: list[PeriodScheme] | None = get_period_list(period_start, period_end, interval_type, count)

    print(f"LAST KLINE IN DB: {last_kline=}")
    print(f"PERIOD INFO: {period=}")

    if periods:
        async with http_session(True) as session:
            for period in periods:
                result = session.get_kline(
                    start=DateUtils.get_timestamp_ms(period.start_date),
                    end=DateUtils.get_timestamp_ms(period.end_date),
                    limit=period.count,
                    category=sorttype,
                    interval=interval,
                    symbol=symbol
                )

                data = ByBitResponseScheme.model_validate(result["result"])

                if data and data.data:
                    print(f"INSERTING KLINES: {len(data.data)}")
                    await OdmMethods.insert_klines(crypto_type, interval_type, data.data)
                await asyncio.sleep(1)
