# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_peers_response_data_inner import GetPeersResponseDataInner


class GetPeerResponse(BaseModel):
    """GetPeerResponse - a model defined in OpenAPI

        data: The data of this GetPeerResponse [Optional].
    """

    data: Optional[GetPeersResponseDataInner] = Field(alias="data", default=None)

GetPeerResponse.update_forward_refs()
