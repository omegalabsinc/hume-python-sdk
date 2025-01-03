import logging
from contextlib import asynccontextmanager
from typing import AsyncContextManager, AsyncIterator, Optional, Any
from unittest.mock import Mock

import websockets.client
from pytest import MonkeyPatch

from hume.client import AsyncHumeClient
from hume.empathic_voice.chat.socket_client import ChatWebsocketConnection
from hume.expression_measurement.stream.socket_client import StreamWebsocketConnection

logger = logging.getLogger(__name__)


# pylint: disable=unused-argument
def get_mock_connect(connection_string: str, assert_max_size: bool = False) -> Any:
    def mock_connect(
        uri: str,
        additional_headers: Optional[dict[str, str]] = None,
        open_timeout: Optional[int] = None,
        close_timeout: Optional[int] = None,
        max_size: Optional[int] = None,
        max_queue: Optional[int] = None,
    ) -> AsyncContextManager[Mock]:
        assert uri.startswith(connection_string)
        assert isinstance(additional_headers, dict)
        assert additional_headers.get("X-Fern-Language") == "Python"
        assert isinstance(additional_headers.get("X-Fern-SDK-Version"), str)
        if assert_max_size:
            assert max_size == 16777216

        @asynccontextmanager
        async def mock_connection() -> AsyncIterator[Mock]:
            yield Mock()

        return mock_connection()

    return mock_connect


async def test_chat_connect_basic(monkeypatch: MonkeyPatch) -> None:
    hu = AsyncHumeClient(api_key="0000-0000-0000-0000")
    monkeypatch.setattr(
        websockets,
        "connect",
        get_mock_connect("wss://api.hume.ai/v0/evi/chat", assert_max_size=True),
    )
    async with hu.empathic_voice.chat.connect() as socket:
        assert isinstance(socket, ChatWebsocketConnection)


async def test_stream_models_connect_basic(monkeypatch: MonkeyPatch) -> None:
    hu = AsyncHumeClient(api_key="0000-0000-0000-0000")
    monkeypatch.setattr(
        websockets,
        "connect",
        get_mock_connect("wss://api.hume.ai/v0/stream/models"),
    )
    async with hu.expression_measurement.stream.connect() as socket:
        assert isinstance(socket, StreamWebsocketConnection)
