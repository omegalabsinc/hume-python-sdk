# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class PostedUserDefinedToolSpec(UniversalBaseModel):
    """
    A specific tool identifier to be posted to the server
    """

    id: str = pydantic.Field()
    """
    Identifier for a Tool. Formatted as a UUID.
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    Version number for a Tool.
    
    Tools, Configs, Custom Voices, and Prompts are versioned. This versioning system supports iterative development, allowing you to progressively refine tools and revert to previous versions if needed.
    
    Version numbers are integer values representing different iterations of the Tool. Each update to the Tool increments its version number.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow