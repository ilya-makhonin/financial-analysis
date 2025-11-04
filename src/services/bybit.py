import logging

from contextlib import asynccontextmanager
from pybit.unified_trading import HTTP, WebSocket


logger = logging.getLogger(__name__)


def connection_http(
    is_testnet: bool,
    key: str | None = None, secret: str | None = None
) -> HTTP:
    if key and secret and not is_testnet:
        config = {
            "testnet": is_testnet,
            "api_key": key,
            "api_secret": secret,
        }
    else:
        config = { "testnet": True }

    session = HTTP(**config)
    return session


def connection_websocket(
    is_testnet: bool, channel: str = "spot",
    key: str | None = None, secret: str | None = None
) -> WebSocket:
    config = { "testnet": is_testnet, "channel_type": channel }

    if key and secret:
        config = {
            **config,
            "api_key": key,
            "api_secret": secret,
        }

    session = WebSocket(**config)
    return session


@asynccontextmanager
async def http_session(is_testnet: bool):
    try:
        session = connection_http(is_testnet=is_testnet)
        yield session
    except Exception as e:
        print("http_session: ", e)


@asynccontextmanager
async def ws_session(is_testnet: bool):
    try:
        session = connection_websocket(is_testnet=is_testnet)
        yield session
    except Exception as e:
        print(e)
    finally:
        if session and not session.exited:
            session.exit()
