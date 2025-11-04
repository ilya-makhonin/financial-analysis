from enum import Enum, unique


@unique
class IntervalType(str, Enum):
    HOUR = "HOUR"
    DAY = "DAY"


@unique
class CryptoType(str, Enum):
    BTC = "BTC"
    ETH = "ETH"
    LTC = "LTC"
    SOL = "SOL"
    XRP = "XRP"
    TON = "TON"
    DOG = "DOG"
    TRX = "TRX"


@unique
class CurrencyType(str, Enum):
    RUB = "RUB"
    USD = "USD"


@unique
class SortType(str, Enum):
    LINEAR = "LINEAR"
    INVERSE = "INVERSE"
    SPOT = "SPOT"
