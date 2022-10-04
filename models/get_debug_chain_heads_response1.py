# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_debug_chain_heads_response1_data_inner import GetDebugChainHeadsResponse1DataInner


class GetDebugChainHeadsResponse1(BaseModel):
    """GetDebugChainHeadsResponse1 - a model defined in OpenAPI

        data: The data of this GetDebugChainHeadsResponse1 [Optional].
    """

    data: Optional[List[GetDebugChainHeadsResponse1DataInner]] = Field(alias="data", default=None)

GetDebugChainHeadsResponse1.update_forward_refs()
