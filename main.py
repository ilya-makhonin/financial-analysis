import asyncio
import logging
import os
import sys

from datetime import datetime

from src.config import load_config
from src.enums import IntervalType, CryptoType
from src.database import get_mongo_session
from src.runner import get_historical_data


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
        if session:
            for interval in IntervalType:
                for crypto in CryptoType:
                    print("\n START GETTING DATA BY: ", crypto, interval)
                    await get_historical_data(
                        config,
                        crypto_type=crypto,
                        interval_type=interval,
                        start_date=datetime(2025, 11, 1, 0, 0, 0),
                        end_date=datetime.now(),
                    )
                    print("\n END GETTING DATA BY: ", crypto, interval)
                    await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
