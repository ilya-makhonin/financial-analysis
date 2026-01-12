import asyncio
import logging
import os
import sys

from datetime import datetime

from src.config import load_config
from src.database import get_mongo_session
from src.runner import HistoricalRunner
from src.enums import IntervalType, CryptoType


config = load_config()


logging.basicConfig(
    level=logging.getLevelName(level=config.log.level),
    format=config.log.format,
    handlers=[logging.FileHandler(config.log.file), logging.StreamHandler()],
)

if sys.platform.startswith("win") or os.name == "nt":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def main():
    async with get_mongo_session(config.mongo) as session:
        historical_runner = HistoricalRunner(config)

        async for result in historical_runner.run_iterator():
            print(result)


if __name__ == "__main__":
    asyncio.run(main())
