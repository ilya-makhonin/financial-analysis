from datetime import datetime
from pydantic import BaseModel


class PeriodScheme(BaseModel):
    count: int
    start_date: datetime
    end_date: datetime
