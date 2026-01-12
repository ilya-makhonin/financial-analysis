import asyncio
import logging

from datetime import datetime
from typing import AsyncGenerator

from src.schemes import ByBitResponseScheme, HistoricalScheme
from src.config import Config
from src.enums import IntervalType, CryptoType, SortType
from src.services import http_session
from src.utils import DateUtils
from src.database import OdmMethods, BaseDocument
from src.constants import CONSTANTS

from .utils.mapping import MappingParam
from .utils.period import get_period_list


logger = logging.getLogger(__name__)


class HistoricalRunner:
    def __init__(self, config: Config, start: datetime | None = None, end: datetime | None = None):
        self.config = config

        self.base_start = CONSTANTS.period.period_start
        self.limit = CONSTANTS.limit.max_limit

        self.end = end if end else datetime.now()
        self.start = start if start else self.base_start

    async def _get_historical_data(
        self, max_count: int, crypto_type: CryptoType, interval_type: IntervalType,
    ) -> HistoricalScheme:
        now_date = datetime.now()
        last_kline: BaseDocument | None = await OdmMethods.get_last_kline(crypto_type, interval_type)
        max_date = now_date if self.end > now_date else self.end
        min_date = DateUtils.period_inc(last_kline.start_date, interval_type) if last_kline else self.base_start
        count = self.limit if max_count > self.limit else max_count

        period_start = min_date if self.start < min_date else self.start
        period_end = DateUtils.get_clear_datetime(max_date, interval_type)

        parse_result = HistoricalScheme(
            interval=interval_type,
            crypto=crypto_type,
            last_klin_date=min_date,
        )

        try:
            if periods := get_period_list(period_start, period_end, interval_type, count):
                async with http_session(True) as session:
                    for period in periods:
                        result = session.get_kline(
                            start=DateUtils.get_timestamp_ms(period.start_date),
                            end=DateUtils.get_timestamp_ms(period.end_date),
                            category=MappingParam.get_sort(SortType.SPOT),
                            interval=MappingParam.get_interval(interval_type),
                            symbol=MappingParam.get_symbol(crypto_type),
                            limit=period.count,
                        )

                        data = ByBitResponseScheme.model_validate(result["result"])

                        if data and data.data:
                            await OdmMethods.insert_klines(crypto_type, interval_type, data.data)
                        await asyncio.sleep(1)

                if kline := await OdmMethods.get_last_kline(crypto_type, interval_type):
                    parse_result.last_klin_date = kline.end_date
                return parse_result
            return parse_result
        except Exception as e:
            logger.warning(e)
            parse_result.is_success = False
            return parse_result
        
    async def run_once(
        self,
        crypto_type: CryptoType = CryptoType.BTC,
        interval_type: IntervalType = IntervalType.DAY,
    ):
        logger.info("START GETTING DATA BY: [%s - %s]", crypto_type, interval_type)
        result = await self._get_historical_data(
            crypto_type=crypto_type,
            interval_type=interval_type,
            max_count=self.limit
        )
        logger.info("END GETTING DATA BY: [%s - %s]", crypto_type, interval_type)
        return result

    async def run_iterator(
        self,
        items: list[tuple[IntervalType, CryptoType]] | None = None
    ) -> AsyncGenerator[HistoricalScheme, None]:
        crypto_list = items if items else [ (i, j) for i in IntervalType for j in CryptoType ]

        for interval, crypto in crypto_list:
            logger.info("START GETTING DATA BY: [%s - %s]", crypto, interval)
            result = await self._get_historical_data(
                crypto_type=crypto,
                interval_type=interval,
                max_count=self.limit
            )
            logger.info("END GETTING DATA BY: [%s - %s]", crypto, interval)
            yield result
