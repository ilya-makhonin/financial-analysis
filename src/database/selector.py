from src.enums import CryptoType, CurrencyType, IntervalType
from .documents import (
    BaseDocument,
    BtcDayKline, BtcHourKline,
    EthDayKline, EthHourKline,
    LtcDayKline, LtcHourKline,
    SolDayKline, SolHourKline,
    XrpDayKline, XrpHourKline,
    TonDayKline, TonHourKline,
    DogDayKline, DogHourKline,
    TrxDayKline, TrxHourKline,
    UsdCurrency
)


def get_crypto_document(crypto: CryptoType, interval: IntervalType) -> BaseDocument | None:
    if interval == IntervalType.DAY:
        if crypto == CryptoType.BTC: return BtcDayKline
        if crypto == CryptoType.ETH: return EthDayKline
        if crypto == CryptoType.LTC: return LtcDayKline
        if crypto == CryptoType.SOL: return SolDayKline
        if crypto == CryptoType.XRP: return XrpDayKline
        if crypto == CryptoType.TON: return TonDayKline
        if crypto == CryptoType.DOG: return DogDayKline
        if crypto == CryptoType.TRX: return TrxDayKline
    elif interval == IntervalType.HOUR:
        if crypto == CryptoType.BTC: return BtcHourKline
        if crypto == CryptoType.ETH: return EthHourKline
        if crypto == CryptoType.LTC: return LtcHourKline
        if crypto == CryptoType.SOL: return SolHourKline
        if crypto == CryptoType.XRP: return XrpHourKline
        if crypto == CryptoType.TON: return TonHourKline
        if crypto == CryptoType.DOG: return DogHourKline
        if crypto == CryptoType.TRX: return TrxHourKline

    print("No Document")
    return None


def get_currency_document(currency: CurrencyType) -> BaseDocument | None:
    if currency == CurrencyType.USD:
        return UsdCurrency

    print("No Document")
    return None
