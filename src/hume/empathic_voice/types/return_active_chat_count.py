# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from .return_active_chat_count_per_tag import ReturnActiveChatCountPerTag
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class ReturnActiveChatCount(UniversalBaseModel):
    """
    A description of current chat chat sessions for a user
    """

    timestamp: int = pydantic.Field()
    """
    The timestamp for when chat status was measured. Formatted as a Unix epoch milliseconds.
    """

    total_user_active_chats: int = pydantic.Field()
    """
    The total number of active chats for this user.
    """

    max_allowed_active_chats: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum number of concurrent active chats for this user.
    """

    more_active_chats_allowed: bool = pydantic.Field()
    """
    Boolean indicating if the user is allowed to start more chats.
    """

    per_tag: typing.Optional[typing.List[typing.Optional[ReturnActiveChatCountPerTag]]] = pydantic.Field(default=None)
    """
    Optional List of chat counts per tag.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow