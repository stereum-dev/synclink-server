# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_state_validator_balances_response_data_inner import GetStateValidatorBalancesResponseDataInner


class GetStateValidatorBalancesResponse(BaseModel):
    """GetStateValidatorBalancesResponse - a model defined in OpenAPI

        execution_optimistic: The execution_optimistic of this GetStateValidatorBalancesResponse [Optional].
        data: The data of this GetStateValidatorBalancesResponse [Optional].
    """

    execution_optimistic: Optional[bool] = Field(alias="execution_optimistic", default=None)
    data: Optional[List[GetStateValidatorBalancesResponseDataInner]] = Field(alias="data", default=None)

GetStateValidatorBalancesResponse.update_forward_refs()
