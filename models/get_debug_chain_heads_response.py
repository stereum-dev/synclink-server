# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_debug_chain_heads_response_data_inner import GetDebugChainHeadsResponseDataInner


class GetDebugChainHeadsResponse(BaseModel):
    """GetDebugChainHeadsResponse - a model defined in OpenAPI

        data: The data of this GetDebugChainHeadsResponse [Optional].
    """

    data: Optional[List[GetDebugChainHeadsResponseDataInner]] = Field(alias="data", default=None)

GetDebugChainHeadsResponse.update_forward_refs()
