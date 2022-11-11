# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_syncing_status_response_data import GetSyncingStatusResponseData


class GetSyncingStatusResponse(BaseModel):
    """GetSyncingStatusResponse - a model defined in OpenAPI

        data: The data of this GetSyncingStatusResponse [Optional].
    """

    data: Optional[GetSyncingStatusResponseData] = Field(alias="data", default=None)

GetSyncingStatusResponse.update_forward_refs()
