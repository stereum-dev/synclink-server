# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GetDepositSnapshotResponseData(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GetDepositSnapshotResponseData - a model defined in OpenAPI

        finalized: The finalized of this GetDepositSnapshotResponseData [Optional].
        deposit_root: The deposit_root of this GetDepositSnapshotResponseData [Optional].
        deposit_count: The deposit_count of this GetDepositSnapshotResponseData [Optional].
        execution_block_hash: The execution_block_hash of this GetDepositSnapshotResponseData [Optional].
        execution_block_height: The execution_block_height of this GetDepositSnapshotResponseData [Optional].
    """

    finalized: Optional[List[str]] = Field(alias="finalized", default=None)
    deposit_root: Optional[str] = Field(alias="deposit_root", default=None)
    deposit_count: Optional[str] = Field(alias="deposit_count", default=None)
    execution_block_hash: Optional[str] = Field(alias="execution_block_hash", default=None)
    execution_block_height: Optional[str] = Field(alias="execution_block_height", default=None)

    @validator("deposit_root")
    def deposit_root_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{64}$", value)
        return value

    @validator("execution_block_hash")
    def execution_block_hash_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{64}$", value)
        return value

GetDepositSnapshotResponseData.update_forward_refs()