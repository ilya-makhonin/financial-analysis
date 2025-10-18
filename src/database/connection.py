from contextlib import asynccontextmanager
from urllib.parse import quote
from pymongo import AsyncMongoClient
from pymongo.asynchronous.database import AsyncDatabase
from beanie import init_beanie
from src.config import MongoSettings
from .documents import (
    BtcDayKline, BtcHourKline,
    EthDayKline, EthHourKline,
    UsdCurrency
)


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
        raise (e)


async def init_database(settings: MongoSettings) -> AsyncMongoClient:
    try:
        client: AsyncMongoClient = get_mongodb_client(settings.host, settings.port, settings.user, settings.password)
        db: AsyncDatabase = client[settings.db]

        await init_beanie(database=db, document_models=[
            BtcHourKline, BtcDayKline,
            EthHourKline, EthDayKline,
            UsdCurrency
        ])

        return client
    except Exception as e:
        raise (e)


@asynccontextmanager
async def get_mongo_session(settings: MongoSettings):
    try:
        client: AsyncMongoClient = get_mongodb_client(settings.host, settings.port, settings.user, settings.password)
        db: AsyncDatabase = client[settings.db]

        await init_beanie(database=db, document_models=[
            BtcHourKline, BtcDayKline,
            EthHourKline, EthDayKline,
            UsdCurrency
        ])

        yield client
    except Exception as e:
        raise (e)
    finally:
        await client.close()
