# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GetSyncingStatusResponseData(BaseModel):
    """GetSyncingStatusResponseData - a model defined in OpenAPI

        head_slot: The head_slot of this GetSyncingStatusResponseData [Optional].
        sync_distance: The sync_distance of this GetSyncingStatusResponseData [Optional].
        is_syncing: The is_syncing of this GetSyncingStatusResponseData [Optional].
        is_optimistic: The is_optimistic of this GetSyncingStatusResponseData [Optional].
    """

    head_slot: Optional[object] = Field(alias="head_slot", default=None)
    sync_distance: Optional[object] = Field(alias="sync_distance", default=None)
    is_syncing: Optional[bool] = Field(alias="is_syncing", default=None)
    is_optimistic: Optional[bool] = Field(alias="is_optimistic", default=None)

GetSyncingStatusResponseData.update_forward_refs()
