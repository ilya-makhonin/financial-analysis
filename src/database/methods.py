import logging

from datetime import datetime
from pymongo.results import InsertManyResult
from src.enums import CryptoType, IntervalType
from src.schemes import KlineScheme
from .documents import BaseDocument
from .selector import get_crypto_document


logger = logging.getLogger(__name__)


class OdmMethods:
    @classmethod
    async def insert_klines(cls, crypto: CryptoType, interval: IntervalType, data: list[KlineScheme]) -> bool:
        try:
            DocumentClass: BaseDocument = get_crypto_document(crypto, interval)

            if DocumentClass:
                data_list: list[BaseDocument] = [ DocumentClass(**item.model_dump()) for item in data ]
                result: InsertManyResult = await DocumentClass.insert_many(data_list)
            else:
                result = None

            return True if result and result.inserted_ids else False
        except Exception as e:
            logger.warning("None", e)

    @classmethod
    async def insert_kline(cls, crypto: CryptoType, interval: IntervalType, data: KlineScheme) -> BaseDocument | None:
        try:
            DocumentClass: BaseDocument = get_crypto_document(crypto, interval)

            if DocumentClass:
                doc: BaseDocument = DocumentClass(**data.model_dump())
                result: BaseDocument = await doc.insert()
                return result
            return None
        except Exception as e:
            logger.warning("None", e)

    @classmethod
    async def get_klines(cls, crypto: CryptoType, interval: IntervalType) -> list[BaseDocument] | None:
        try:
            DocumentClass: BaseDocument = get_crypto_document(crypto, interval)

            if DocumentClass:
                result: list[BaseDocument] = await DocumentClass.find({}).to_list()
                return result
            return None
        except Exception as e:
            logger.warning("None", e)

    @classmethod
    async def get_klines_by_period(cls, crypto: CryptoType, interval: IntervalType, period_start: datetime, period_end: datetime) -> list[BaseDocument] | None:
        try:
            DocumentClass: BaseDocument = get_crypto_document(crypto, interval)

            if DocumentClass:
                result: list[BaseDocument] = await DocumentClass.find(
                    BaseDocument.start_date >= period_start,
                    BaseDocument.start_date <= period_end
                ).to_list()

                return result
            return None
        except Exception as e:
            logger.warning("None", e)

    @classmethod
    async def get_limit_klines(cls, crypto: CryptoType, interval: IntervalType, limit: int) -> list[BaseDocument] | None:
        try:
            DocumentClass: BaseDocument = get_crypto_document(crypto, interval)

            if DocumentClass:
                result: list[BaseDocument] = await DocumentClass.find({}).limit(limit).to_list()
                return result
            return None
        except Exception as e:
            logger.warning("None", e)

    @classmethod
    async def get_last_kline(cls, crypto: CryptoType, interval: IntervalType) -> BaseDocument | None:
        try:
            DocumentClass: BaseDocument = get_crypto_document(crypto, interval)

            if DocumentClass:
                result: BaseDocument | None = await DocumentClass.find({}).sort("-_id").first_or_none()
                return result
            return None
        except Exception as e:
            logger.warning("None", e)
