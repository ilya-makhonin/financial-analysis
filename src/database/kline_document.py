from typing_extensions import Self
from datetime import datetime, timedelta
from pydantic import BaseModel, model_validator


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
        if self.end_date is None and self.interval:
            hours = 23 if self.interval == "day" else 0 
            self.end_date = self.start_date + timedelta(hours=hours, minutes=59, seconds=59)
        return self
