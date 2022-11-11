# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_epoch_committees_response_data_inner import GetEpochCommitteesResponseDataInner


class GetEpochCommitteesResponse(BaseModel):
    """GetEpochCommitteesResponse - a model defined in OpenAPI

        execution_optimistic: The execution_optimistic of this GetEpochCommitteesResponse [Optional].
        data: The data of this GetEpochCommitteesResponse [Optional].
    """

    execution_optimistic: Optional[bool] = Field(alias="execution_optimistic", default=None)
    data: Optional[List[GetEpochCommitteesResponseDataInner]] = Field(alias="data", default=None)

GetEpochCommitteesResponse.update_forward_refs()
