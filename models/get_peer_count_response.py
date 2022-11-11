# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_peer_count_response_data import GetPeerCountResponseData


class GetPeerCountResponse(BaseModel):
    """GetPeerCountResponse - a model defined in OpenAPI

        data: The data of this GetPeerCountResponse [Optional].
    """

    data: Optional[GetPeerCountResponseData] = Field(alias="data", default=None)

GetPeerCountResponse.update_forward_refs()
