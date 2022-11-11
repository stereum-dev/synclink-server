# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_state_finality_checkpoints_response_data import GetStateFinalityCheckpointsResponseData


class GetStateFinalityCheckpointsResponse(BaseModel):
    """GetStateFinalityCheckpointsResponse - a model defined in OpenAPI

        execution_optimistic: The execution_optimistic of this GetStateFinalityCheckpointsResponse [Optional].
        data: The data of this GetStateFinalityCheckpointsResponse [Optional].
    """

    execution_optimistic: Optional[bool] = Field(alias="execution_optimistic", default=None)
    data: Optional[GetStateFinalityCheckpointsResponseData] = Field(alias="data", default=None)

GetStateFinalityCheckpointsResponse.update_forward_refs()
