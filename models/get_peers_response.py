# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_peers_response_data_inner import GetPeersResponseDataInner
from models.get_peers_response_meta import GetPeersResponseMeta


class GetPeersResponse(BaseModel):
    """GetPeersResponse - a model defined in OpenAPI

        data: The data of this GetPeersResponse [Optional].
        meta: The meta of this GetPeersResponse [Optional].
    """

    data: Optional[List[GetPeersResponseDataInner]] = Field(alias="data", default=None)
    meta: Optional[GetPeersResponseMeta] = Field(alias="meta", default=None)

GetPeersResponse.update_forward_refs()
