# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.sync_committee_selection_request_inner import SyncCommitteeSelectionRequestInner


class SyncCommitteeSelectionResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SyncCommitteeSelectionResponse - a model defined in OpenAPI

        data: The data of this SyncCommitteeSelectionResponse [Optional].
    """

    data: Optional[List[SyncCommitteeSelectionRequestInner]] = Field(alias="data", default=None)

SyncCommitteeSelectionResponse.update_forward_refs()