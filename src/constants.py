from typing import Final
from datetime import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class PeriodConstants:
    period_start: datetime


@dataclass(frozen=True)
class LimitConstants:
    max_limit: int


@dataclass(frozen=True)
class CurrencyNameConstants:
    usd_currency: str


@dataclass(frozen=True)
class CryptoNameConstants:
    btc_hour: str
    btc_day: str
    eth_hour: str
    eth_day: str
    ltc_hour: str
    ltc_day: str
    sol_hour: str
    sol_day: str
    xrp_hour: str
    xrp_day: str
    ton_hour: str
    ton_day: str
    dog_hour: str
    dog_day: str
    trx_hour: str
    trx_day: str


@dataclass(frozen=True)
class Constants:
    period: PeriodConstants
    crypto: CryptoNameConstants
    currency: CurrencyNameConstants
    limit: LimitConstants


CONSTANTS: Final[Constants] = Constants(
    period=PeriodConstants(period_start=datetime(2020, 1, 1, 0, 0, 0)),
    currency=CurrencyNameConstants(usd_currency="usd_currency"),
    limit=LimitConstants(max_limit=1000),
    crypto=CryptoNameConstants(
        btc_hour="btc_hour",
        btc_day="btc_day",
        eth_hour="eth_hour",
        eth_day="eth_day",
        ltc_hour="ltc_hour",
        ltc_day="ltc_day",
        sol_hour="sol_hour",
        sol_day="sol_day",
        xrp_hour="xrp_hour",
        xrp_day="xrp_day",
        ton_hour="ton_hour",
        ton_day="ton_day",
        dog_hour="dog_hour",
        dog_day="dog_day",
        trx_hour="trx_hour",
        trx_day="trx_day",
    ),
)
