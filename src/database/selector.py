from src.enums import CryptoType, CurrencyType, IntervalType
from .documents import (
    BaseDocument,
    BtcDayKline, BtcHourKline,
    EthDayKline, EthHourKline,
    UsdCurrency
)


def get_crypto_document(crypto: CryptoType, interval: IntervalType) -> BaseDocument | None:
    if interval == IntervalType.DAY:
        if crypto == CryptoType.BTC: return BtcDayKline
        if crypto == CryptoType.ETH: return EthDayKline
    elif interval == IntervalType.HOUR:
        if crypto == CryptoType.BTC: return BtcHourKline
        if crypto == CryptoType.ETH: return EthHourKline

    print("No Document")
    return None


def get_currency_document(currency: CurrencyType) -> BaseDocument | None:
    if currency == CurrencyType.USD:
        return UsdCurrency

    print("No Document")
    return None
 