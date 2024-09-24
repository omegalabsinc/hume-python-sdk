# This file was auto-generated by Fern from our API Definition.

from ..core.client_wrapper import SyncClientWrapper
from .tools.client import ToolsClient
from .prompts.client import PromptsClient
from .custom_voices.client import CustomVoicesClient
from .configs.client import ConfigsClient
from .chats.client import ChatsClient
from .chat_groups.client import ChatGroupsClient
from ..core.client_wrapper import AsyncClientWrapper
from .tools.client import AsyncToolsClient
from .prompts.client import AsyncPromptsClient
from .custom_voices.client import AsyncCustomVoicesClient
from .configs.client import AsyncConfigsClient
from .chats.client import AsyncChatsClient
from .chat_groups.client import AsyncChatGroupsClient


class EmpathicVoiceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.tools = ToolsClient(client_wrapper=self._client_wrapper)
        self.prompts = PromptsClient(client_wrapper=self._client_wrapper)
        self.custom_voices = CustomVoicesClient(client_wrapper=self._client_wrapper)
        self.configs = ConfigsClient(client_wrapper=self._client_wrapper)
        self.chats = ChatsClient(client_wrapper=self._client_wrapper)
        self.chat_groups = ChatGroupsClient(client_wrapper=self._client_wrapper)


class AsyncEmpathicVoiceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.tools = AsyncToolsClient(client_wrapper=self._client_wrapper)
        self.prompts = AsyncPromptsClient(client_wrapper=self._client_wrapper)
        self.custom_voices = AsyncCustomVoicesClient(client_wrapper=self._client_wrapper)
        self.configs = AsyncConfigsClient(client_wrapper=self._client_wrapper)
        self.chats = AsyncChatsClient(client_wrapper=self._client_wrapper)
        self.chat_groups = AsyncChatGroupsClient(client_wrapper=self._client_wrapper)