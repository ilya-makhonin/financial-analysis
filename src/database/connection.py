import logging

from contextlib import asynccontextmanager
from urllib.parse import quote
from pymongo import AsyncMongoClient
from pymongo.asynchronous.database import AsyncDatabase
from beanie import init_beanie
from src.config import MongoSettings
from .documents import (
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
logging.getLogger("pymongo").setLevel(logging.ERROR)


def get_mongo_connection_uri(host: str, port: int, user: str, password: str) -> str:
    uri_conn = (
        f"mongodb://{quote(user, safe='')}:{quote(password, safe='')}@{host}:{port}/"
    )
    return uri_conn


def get_mongodb_client(host: str, port: int, user: str, password: str) -> AsyncMongoClient:
    try:
        uri_conn: str = get_mongo_connection_uri(host, port, user, password)
        mongo_client = AsyncMongoClient(uri_conn)
        return mongo_client
    except Exception as e:
        logger.warning(e)


async def init_database(settings: MongoSettings) -> AsyncMongoClient:
    try:
        client: AsyncMongoClient = get_mongodb_client(settings.host, settings.port, settings.user, settings.password)
        db: AsyncDatabase = client[settings.db]

        await init_beanie(database=db, document_models=[
            BtcDayKline, BtcHourKline,
            EthDayKline, EthHourKline,
            LtcDayKline, LtcHourKline,
            SolDayKline, SolHourKline,
            XrpDayKline, XrpHourKline,
            TonDayKline, TonHourKline,
            DogDayKline, DogHourKline,
            TrxDayKline, TrxHourKline,
            UsdCurrency
        ])

        return client
    except Exception as e:
        logger.warning(e)


@asynccontextmanager
async def get_mongo_session(settings: MongoSettings):
    try:
        client: AsyncMongoClient = await init_database(settings)

        yield client
    except Exception as e:
        logger.warning(e)
    finally:
        await client.close()
