# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from .return_chat import ReturnChat
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class ReturnChatGroupPagedChats(UniversalBaseModel):
    """
    A description of chat_group and its status with a paginated list of each chat in the chat_group
    """

    id: str = pydantic.Field()
    """
    Identifier for the chat group. Any chat resumed from this chat will have the same chat_group_id. Formatted as a UUID.
    """

    first_start_timestamp: int = pydantic.Field()
    """
    The timestamp when the first chat in this chat group started, formatted as a Unix epoch milliseconds.
    """

    most_recent_start_timestamp: int = pydantic.Field()
    """
    The timestamp when the most recent chat in this chat group started, formatted as a Unix epoch milliseconds.
    """

    num_chats: int = pydantic.Field()
    """
    The total number of chats in this chat group.
    """

    page_number: int = pydantic.Field()
    """
    The page number of the returned results.
    """

    page_size: int = pydantic.Field()
    """
    The number of results returned per page.
    """

    total_pages: int = pydantic.Field()
    """
    The total number of pages in the collection
    """

    pagination_direction: str = pydantic.Field()
    """
    The direction of the pagination (ASC or DESC).
    """

    chats_page: typing.List[ReturnChat] = pydantic.Field()
    """
    List of chats and their metadata returned for the specified page number and page size.
    """

    active: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow