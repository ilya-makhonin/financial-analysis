from src.enums import IntervalType, CryptoType


class MappingParam:
    _interval: dict[IntervalType, str|int] = {
        IntervalType.DAY: "D",
        IntervalType.HOUR: 60,
    }
    _symbol: dict[CryptoType, str] = {
        CryptoType.BTC: "BTCUSDT",
        CryptoType.ETH: "ETHUSDT",
        CryptoType.LTC: "LTCUSDT",
        CryptoType.SOL: "SOLUSDT",
        CryptoType.XRP: "XRPUSDT",
        CryptoType.TON: "TONUSDT",
        CryptoType.DOG: "DOGEUSDT",
        CryptoType.TRX: "TRXUSDT",
    }

    @classmethod
    def get_interval(cls, interval: IntervalType):
        return cls._interval[interval]
    
    @classmethod
    def get_symbol(cls, crypto: CryptoType):
        return cls._symbol[crypto]
