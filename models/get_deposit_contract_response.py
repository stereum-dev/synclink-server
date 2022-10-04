# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_deposit_contract_response_data import GetDepositContractResponseData


class GetDepositContractResponse(BaseModel):
    """GetDepositContractResponse - a model defined in OpenAPI

        data: The data of this GetDepositContractResponse [Optional].
    """

    data: Optional[GetDepositContractResponseData] = Field(alias="data", default=None)

GetDepositContractResponse.update_forward_refs()
