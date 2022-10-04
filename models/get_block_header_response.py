# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_block_headers_response_data_inner import GetBlockHeadersResponseDataInner


class GetBlockHeaderResponse(BaseModel):
    """GetBlockHeaderResponse - a model defined in OpenAPI

        execution_optimistic: The execution_optimistic of this GetBlockHeaderResponse [Optional].
        data: The data of this GetBlockHeaderResponse [Optional].
    """

    execution_optimistic: Optional[bool] = Field(alias="execution_optimistic", default=None)
    data: Optional[GetBlockHeadersResponseDataInner] = Field(alias="data", default=None)

GetBlockHeaderResponse.update_forward_refs()
