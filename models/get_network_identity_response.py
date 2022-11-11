# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_network_identity_response_data import GetNetworkIdentityResponseData


class GetNetworkIdentityResponse(BaseModel):
    """GetNetworkIdentityResponse - a model defined in OpenAPI

        data: The data of this GetNetworkIdentityResponse [Optional].
    """

    data: Optional[GetNetworkIdentityResponseData] = Field(alias="data", default=None)

GetNetworkIdentityResponse.update_forward_refs()
