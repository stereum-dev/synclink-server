# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_epoch_sync_committees_response_data import GetEpochSyncCommitteesResponseData


class GetEpochSyncCommitteesResponse(BaseModel):
    """GetEpochSyncCommitteesResponse - a model defined in OpenAPI

        execution_optimistic: The execution_optimistic of this GetEpochSyncCommitteesResponse [Optional].
        data: The data of this GetEpochSyncCommitteesResponse [Optional].
    """

    execution_optimistic: Optional[bool] = Field(alias="execution_optimistic", default=None)
    data: Optional[GetEpochSyncCommitteesResponseData] = Field(alias="data", default=None)

GetEpochSyncCommitteesResponse.update_forward_refs()
