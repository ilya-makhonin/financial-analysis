from beanie import Document
from pydantic import Field
from src.enums import IntervalType, CryptoType, CurrencyType
from src.constants import CONSTANTS
from .kline_document import Kline


class BaseDocument(Document, Kline):
    symbol: CryptoType
    interval: IntervalType


class BtcHourKline(BaseDocument):
    symbol: CryptoType = Field(default=CryptoType.BTC)
    interval: IntervalType = Field(default=IntervalType.HOUR)

    class Settings:
        name = CONSTANTS.crypto.btc_hour


class BtcDayKline(BaseDocument):
    symbol: CryptoType = Field(default=CryptoType.BTC)
    interval: IntervalType = Field(default=IntervalType.DAY)

    class Settings:
        name = CONSTANTS.crypto.btc_day


class EthHourKline(BaseDocument):
    symbol: CryptoType = Field(default=CryptoType.ETH)
    interval: IntervalType = Field(default=IntervalType.HOUR)

    class Settings:
        name = CONSTANTS.crypto.eth_hour


class EthDayKline(BaseDocument):
    symbol: CryptoType = Field(default=CryptoType.ETH)
    interval: IntervalType = Field(default=IntervalType.DAY)

    class Settings:
        name = CONSTANTS.crypto.eth_day


class UsdCurrency(BaseDocument):
    symbol: CurrencyType = Field(default=CurrencyType.USD)
    interval: IntervalType = Field(default=IntervalType.DAY)

    class Settings:
        name = CONSTANTS.currency.usd_currency
