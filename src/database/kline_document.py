from typing_extensions import Self
from datetime import datetime, timedelta, time
from pydantic import BaseModel, model_validator
from src.enums import IntervalType


class Kline(BaseModel):
    start_date: datetime
    open_price: float
    high_price: float
    low_price: float
    close_price: float
    volume: float
    turnover: float
    end_date: datetime | None = None

    @model_validator(mode='after')
    def after_end_date(self) -> Self:
        if self.start_date and self.end_date is None and self.interval:
            res = self.start_date + timedelta(hours=0, minutes=59, seconds=59)\
                if self.interval == IntervalType.HOUR\
                else datetime.combine(self.start_date.date(), time(23, 59, 59))
            self.end_date = res
        return self
