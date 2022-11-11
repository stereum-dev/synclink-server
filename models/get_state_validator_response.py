# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_state_validators_response_data_inner import GetStateValidatorsResponseDataInner


class GetStateValidatorResponse(BaseModel):
    """GetStateValidatorResponse - a model defined in OpenAPI

        execution_optimistic: The execution_optimistic of this GetStateValidatorResponse [Optional].
        data: The data of this GetStateValidatorResponse [Optional].
    """

    execution_optimistic: Optional[bool] = Field(alias="execution_optimistic", default=None)
    data: Optional[GetStateValidatorsResponseDataInner] = Field(alias="data", default=None)

GetStateValidatorResponse.update_forward_refs()
