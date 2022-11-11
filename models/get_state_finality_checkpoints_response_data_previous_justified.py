# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GetStateFinalityCheckpointsResponseDataPreviousJustified(BaseModel):
    """GetStateFinalityCheckpointsResponseDataPreviousJustified - a model defined in OpenAPI

        epoch: The epoch of this GetStateFinalityCheckpointsResponseDataPreviousJustified [Optional].
        root: The root of this GetStateFinalityCheckpointsResponseDataPreviousJustified [Optional].
    """

    epoch: Optional[str] = Field(alias="epoch", default=None)
    root: Optional[str] = Field(alias="root", default=None)

    @validator("root")
    def root_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{64}$", value)
        return value

GetStateFinalityCheckpointsResponseDataPreviousJustified.update_forward_refs()
