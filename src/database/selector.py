import logging

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


logger = logging.getLogger(__name__)


def get_crypto_document(crypto: CryptoType, interval: IntervalType) -> BaseDocument | None:
    if interval == IntervalType.DAY:
        match crypto:
            case CryptoType.BTC: return BtcDayKline
            case CryptoType.ETH: return EthDayKline
            case CryptoType.LTC: return LtcDayKline
            case CryptoType.SOL: return SolDayKline
            case CryptoType.XRP: return XrpDayKline
            case CryptoType.TON: return TonDayKline
            case CryptoType.DOG: return DogDayKline
            case CryptoType.TRX: return TrxDayKline
    elif interval == IntervalType.HOUR:
        match crypto:
            case CryptoType.BTC: return BtcHourKline
            case CryptoType.ETH: return EthHourKline
            case CryptoType.LTC: return LtcHourKline
            case CryptoType.SOL: return SolHourKline
            case CryptoType.XRP: return XrpHourKline
            case CryptoType.TON: return TonHourKline
            case CryptoType.DOG: return DogHourKline
            case CryptoType.TRX: return TrxHourKline

    logger.warning(f"No Document for {crypto} and {interval}")
    return None


def get_currency_document(currency: CurrencyType) -> BaseDocument | None:
    if currency == CurrencyType.USD:
        return UsdCurrency

    logger.warning(f"No Document for {currency}")
    return None
