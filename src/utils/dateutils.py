import calendar
from datetime import datetime, timedelta, time
from src.enums import IntervalType


class DateUtils:
    @classmethod
    def get_timestamp_ms(cls, date: datetime):
        return date.timestamp() * 1000

    @classmethod
    def get_from_timestamp_ms(cls, tm: int):
        return datetime.fromtimestamp(tm / 1000)

    @classmethod
    def get_period_end_by_limit(cls, start: datetime, type: IntervalType, limit: int):
        if type == IntervalType.DAY:
            delta = timedelta(days=limit)
        else:
            delta = timedelta(hours=limit)

        return start + delta

    @classmethod
    def get_clear_end(cls, date: datetime, type: IntervalType):
        if type == IntervalType.DAY:
            day_ended = date.hour == 23 and date.minute > 56
            base = datetime.combine(date.date(), time(hour=0, minute=0, second=0))
            return base + timedelta(days=float(day_ended))

        hour_ended = date.minute > 56
        base = datetime.combine(date.date(), time(hour=date.hour, minute=0, second=0))
        return base + timedelta(hours=float(hour_ended))

    @classmethod
    def period_inc(cls, date: datetime, type: IntervalType) -> datetime:
        if type == IntervalType.DAY:
            delta = timedelta(days=1)
        else:
            delta = timedelta(hours=1)

        return date + delta

    @classmethod
    def get_days_in_year(cls, year: int):
        return 366 if calendar.isleap(year) else 365

    @classmethod
    def get_days_between(cls, start: datetime, end: datetime):
        delta = end - start
        return abs(delta.days)

    @classmethod
    def get_hours_between(cls, start: datetime, end: datetime):
        delta = end - start
        hours_from_days = abs(delta.days * 24)
        hours_from_seconds = abs(delta.seconds / 60 / 60)
    
        return int(hours_from_days + hours_from_seconds)
    
    @classmethod
    def get_count_between(cls, start: datetime, end: datetime, interval: IntervalType):
        if interval == IntervalType.DAY:
            return cls.get_days_between(start, end)
        return cls.get_hours_between(start, end)
