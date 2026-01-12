from datetime import datetime
from pydantic import BaseModel
from src.enums import IntervalType, CryptoType


class HistoricalScheme(BaseModel):
    is_success: bool = True
    interval: IntervalType
    crypto: CryptoType
    last_klin_date: datetime | None = None
