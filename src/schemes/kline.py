from datetime import datetime
from pydantic import BaseModel


class KlineScheme(BaseModel):
    start_date: datetime
    open_price: float
    high_price: float
    low_price: float
    close_price: float
    volume: float
    turnover: float
