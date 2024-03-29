# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class CapellaWithdrawal(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CapellaWithdrawal - a model defined in OpenAPI

        index: The index of this CapellaWithdrawal [Optional].
        validator_index: The validator_index of this CapellaWithdrawal [Optional].
        address: The address of this CapellaWithdrawal [Optional].
        amount: The amount of this CapellaWithdrawal [Optional].
    """

    index: Optional[str] = Field(alias="index", default=None)
    validator_index: Optional[str] = Field(alias="validator_index", default=None)
    address: Optional[str] = Field(alias="address", default=None)
    amount: Optional[str] = Field(alias="amount", default=None)

    @validator("address")
    def address_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{40}$", value)
        return value

CapellaWithdrawal.update_forward_refs()
