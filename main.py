from datetime import datetime
import json
import asyncio
from src.config import load_config
from src.database import init_database
from src.runner.historical_runner import get_historical_data


config = load_config()


async def main():
    client = await init_database()
    await get_historical_data()
    # await init_database(config.mongo)
    # with open("/Users/ilyamakhonin/Desktop/Projects/Python/stocks-basics/stocks-elt/bybit_Btc_1m.json", mode="r") as file:
    #     data = json.loads(file.read())
    #     result = data["result"]
    #     
    #     a = ByBitResponse.model_validate(result)
    #     b = EthHourKline(**a.data[0].model_dump())
    #     await b.insert()


if __name__ == "__main__":
    asyncio.run(main())
