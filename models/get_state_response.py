# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_state_response_data import GetStateResponseData


class GetStateResponse(BaseModel):
    """GetStateResponse - a model defined in OpenAPI

        data: The data of this GetStateResponse [Optional].
    """

    data: Optional[GetStateResponseData] = Field(alias="data", default=None)

GetStateResponse.update_forward_refs()
