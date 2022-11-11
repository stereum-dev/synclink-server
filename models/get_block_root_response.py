# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_block_root_response_data import GetBlockRootResponseData


class GetBlockRootResponse(BaseModel):
    """GetBlockRootResponse - a model defined in OpenAPI

        execution_optimistic: The execution_optimistic of this GetBlockRootResponse [Optional].
        data: The data of this GetBlockRootResponse [Optional].
    """

    execution_optimistic: Optional[bool] = Field(alias="execution_optimistic", default=None)
    data: Optional[GetBlockRootResponseData] = Field(alias="data", default=None)

GetBlockRootResponse.update_forward_refs()
