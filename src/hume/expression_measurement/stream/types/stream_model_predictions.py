# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .stream_model_predictions_job_details import StreamModelPredictionsJobDetails
from .stream_model_predictions_burst import StreamModelPredictionsBurst
from .stream_model_predictions_face import StreamModelPredictionsFace
from .stream_model_predictions_facemesh import StreamModelPredictionsFacemesh
from .stream_model_predictions_language import StreamModelPredictionsLanguage
from .stream_model_predictions_prosody import StreamModelPredictionsProsody
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class StreamModelPredictions(UniversalBaseModel):
    """
    Model predictions
    """

    payload_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    If a payload ID was passed in the request, the same payload ID will be sent back in the response body.
    """

    job_details: typing.Optional[StreamModelPredictionsJobDetails] = pydantic.Field(default=None)
    """
    If the job_details flag was set in the request, details about the current streaming job will be returned in the response body.
    """

    burst: typing.Optional[StreamModelPredictionsBurst] = pydantic.Field(default=None)
    """
    Response for the vocal burst emotion model.
    """

    face: typing.Optional[StreamModelPredictionsFace] = pydantic.Field(default=None)
    """
    Response for the facial expression emotion model.
    """

    facemesh: typing.Optional[StreamModelPredictionsFacemesh] = pydantic.Field(default=None)
    """
    Response for the facemesh emotion model.
    """

    language: typing.Optional[StreamModelPredictionsLanguage] = pydantic.Field(default=None)
    """
    Response for the language emotion model.
    """

    prosody: typing.Optional[StreamModelPredictionsProsody] = pydantic.Field(default=None)
    """
    Response for the speech prosody emotion model.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
