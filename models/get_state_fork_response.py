# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_state_fork_response_data import GetStateForkResponseData


class GetStateForkResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GetStateForkResponse - a model defined in OpenAPI

        execution_optimistic: The execution_optimistic of this GetStateForkResponse [Optional].
        finalized: The finalized of this GetStateForkResponse [Optional].
        data: The data of this GetStateForkResponse [Optional].
    """

    execution_optimistic: Optional[bool] = Field(alias="execution_optimistic", default=None)
    finalized: Optional[bool] = Field(alias="finalized", default=None)
    data: Optional[GetStateForkResponseData] = Field(alias="data", default=None)

GetStateForkResponse.update_forward_refs()
