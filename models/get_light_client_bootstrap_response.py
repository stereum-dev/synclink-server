# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_light_client_bootstrap_response_data import GetLightClientBootstrapResponseData


class GetLightClientBootstrapResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GetLightClientBootstrapResponse - a model defined in OpenAPI

        version: The version of this GetLightClientBootstrapResponse [Optional].
        data: The data of this GetLightClientBootstrapResponse [Optional].
    """

    version: Optional[str] = Field(alias="version", default=None)
    data: Optional[GetLightClientBootstrapResponseData] = Field(alias="data", default=None)

GetLightClientBootstrapResponse.update_forward_refs()
