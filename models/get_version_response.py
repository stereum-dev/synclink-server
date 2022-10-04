# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_version_response_data import GetVersionResponseData


class GetVersionResponse(BaseModel):
    """GetVersionResponse - a model defined in OpenAPI

        data: The data of this GetVersionResponse [Optional].
    """

    data: Optional[GetVersionResponseData] = Field(alias="data", default=None)

GetVersionResponse.update_forward_refs()
