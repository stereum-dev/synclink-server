# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_state_finality_checkpoints_response_data_previous_justified import GetStateFinalityCheckpointsResponseDataPreviousJustified


class GetStateFinalityCheckpointsResponseData(BaseModel):
    """GetStateFinalityCheckpointsResponseData - a model defined in OpenAPI

        previous_justified: The previous_justified of this GetStateFinalityCheckpointsResponseData [Optional].
        current_justified: The current_justified of this GetStateFinalityCheckpointsResponseData [Optional].
        finalized: The finalized of this GetStateFinalityCheckpointsResponseData [Optional].
    """

    previous_justified: Optional[GetStateFinalityCheckpointsResponseDataPreviousJustified] = Field(alias="previous_justified", default=None)
    current_justified: Optional[GetStateFinalityCheckpointsResponseDataPreviousJustified] = Field(alias="current_justified", default=None)
    finalized: Optional[GetStateFinalityCheckpointsResponseDataPreviousJustified] = Field(alias="finalized", default=None)

GetStateFinalityCheckpointsResponseData.update_forward_refs()
