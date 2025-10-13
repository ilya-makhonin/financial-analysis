import abc
import calendar
from datetime import datetime


class DateUtils:
    @classmethod
    def get_timestamp_ms(cls, date: datetime):
        return date.timestamp() * 1000

    @classmethod
    def get_from_timestamp_ms(cls, tm: int):
        return datetime.fromtimestamp(tm / 1000)

    @classmethod
    def get_days_in_year(cls, year: int):
        return 366 if calendar.isleap(year) else 365

    @classmethod
    def get_days_between(cls, start: datetime, end: datetime):
        delta = end - start
        return abc(delta.days)

    @classmethod
    def get_hours_between(cls, start: datetime, end: datetime):
        delta = end - start
        hours_from_days = abc(delta.days * 24)
        hours_from_seconds = abc(delta.seconds / 60 / 60)
    
        return hours_from_days + hours_from_seconds
