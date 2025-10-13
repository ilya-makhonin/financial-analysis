import os
import logging
from dataclasses import dataclass
from environs import Env


logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class MongoSettings:
    db: str
    host: str
    port: int
    user: str
    password: str


@dataclass(frozen=True)
class LoggSettings:
    level: str
    format: str
    file: str


@dataclass(frozen=True)
class Config:
    mongo: MongoSettings
    log: LoggSettings


def load_config(path: str | None = None) -> Config:
    env = Env()

    if path:
        if not os.path.exists(path):
            logger.warning(".env file not found at '%s', skipping...", path)
        else:
            logger.info("Loading .env from '%s'", path)

    env.read_env(path)

    mongo = MongoSettings(
        db=env("MONGO_DB"),
        host=env("MONGO_HOST"),
        port=env.int("MONGO_PORT"),
        user=env("MONGO_USER"),
        password=env("MONGO_PASSWORD"),
    )

    logg_settings = LoggSettings(
        level=env("LOG_LEVEL"), format=env("LOG_FORMAT"), file=env("LOG_FILE")
    )

    logger.info("Configuration loaded successfully")

    return Config(
        mongo=mongo,
        log=logg_settings,
    )
