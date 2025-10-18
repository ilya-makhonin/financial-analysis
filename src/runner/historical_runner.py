from datetime import datetime
from src.config import Config
from src.enums import IntervalType, CryptoType, SortType
from src.services import http_session
from src.utils import DateUtils
from src.database import OdmMethods
from src.constants import CONSTANTS
from .utils.mapping import MappingParam


async def get_historical_data(
    *
    config: Config,
    start_date: datetime = CONSTANTS.period.period_start,
    end_date: datetime = datetime.now(),
    crypto_type: CryptoType = CryptoType.BTC,
    interval_type: IntervalType = IntervalType.DAY,
    sort_type: SortType = SortType.INVERSE
):
    
    first = CONSTANTS.period.period_start 
    last = datetime.now()
    period_start = first if start_date < first else start_date
    period_end = last if end_date > last else end_date

    symbol = MappingParam.get_symbol(crypto_type)
    interval = MappingParam.get_interval(interval_type)
    sorttype = MappingParam.get_sort(sort_type)

    base_count_element = DateUtils.get_days_between(period_start, period_end)\
        if interval_type == IntervalType.DAY\
        else DateUtils.get_hours_between(period_start, period_end)
    
    async with http_session(True) as session:  
        result = session.get_kline(
            start=DateUtils.get_timestamp_ms(period_start),
            end=DateUtils.get_timestamp_ms(period_end),
            category=sorttype, # TODO
            interval=interval,
            symbol=symbol,
            limit=1000 # TODO
        )
