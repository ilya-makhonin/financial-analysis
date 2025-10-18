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


class LtcHourKline(BaseDocument):
    symbol: CryptoType = Field(default=CryptoType.LTC)
    interval: IntervalType = Field(default=IntervalType.HOUR)

    class Settings:
        name = CONSTANTS.crypto.ltc_hour


class LtcDayKline(BaseDocument):
    symbol: CryptoType = Field(default=CryptoType.LTC)
    interval: IntervalType = Field(default=IntervalType.DAY)

    class Settings:
        name = CONSTANTS.crypto.ltc_day


class SolHourKline(BaseDocument):
    symbol: CryptoType = Field(default=CryptoType.SOL)
    interval: IntervalType = Field(default=IntervalType.HOUR)

    class Settings:
        name = CONSTANTS.crypto.sol_hour


class SolDayKline(BaseDocument):
    symbol: CryptoType = Field(default=CryptoType.SOL)
    interval: IntervalType = Field(default=IntervalType.DAY)

    class Settings:
        name = CONSTANTS.crypto.sol_day


class XrpHourKline(BaseDocument):
    symbol: CryptoType = Field(default=CryptoType.XRP)
    interval: IntervalType = Field(default=IntervalType.HOUR)

    class Settings:
        name = CONSTANTS.crypto.xrp_hour


class XrpDayKline(BaseDocument):
    symbol: CryptoType = Field(default=CryptoType.XRP)
    interval: IntervalType = Field(default=IntervalType.DAY)

    class Settings:
        name = CONSTANTS.crypto.xrp_day


class TonHourKline(BaseDocument):
    symbol: CryptoType = Field(default=CryptoType.TON)
    interval: IntervalType = Field(default=IntervalType.HOUR)

    class Settings:
        name = CONSTANTS.crypto.ton_hour


class TonDayKline(BaseDocument):
    symbol: CryptoType = Field(default=CryptoType.TON)
    interval: IntervalType = Field(default=IntervalType.DAY)

    class Settings:
        name = CONSTANTS.crypto.ton_day


class DogHourKline(BaseDocument):
    symbol: CryptoType = Field(default=CryptoType.DOG)
    interval: IntervalType = Field(default=IntervalType.HOUR)

    class Settings:
        name = CONSTANTS.crypto.dog_hour


class DogDayKline(BaseDocument):
    symbol: CryptoType = Field(default=CryptoType.DOG)
    interval: IntervalType = Field(default=IntervalType.DAY)

    class Settings:
        name = CONSTANTS.crypto.dog_day


class TrxHourKline(BaseDocument):
    symbol: CryptoType = Field(default=CryptoType.TRX)
    interval: IntervalType = Field(default=IntervalType.HOUR)

    class Settings:
        name = CONSTANTS.crypto.trx_hour


class TrxDayKline(BaseDocument):
    symbol: CryptoType = Field(default=CryptoType.TRX)
    interval: IntervalType = Field(default=IntervalType.DAY)

    class Settings:
        name = CONSTANTS.crypto.trx_day


class UsdCurrency(BaseDocument):
    symbol: CurrencyType = Field(default=CurrencyType.USD)
    interval: IntervalType = Field(default=IntervalType.DAY)

    class Settings:
        name = CONSTANTS.currency.usd_currency
