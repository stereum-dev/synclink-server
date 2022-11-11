# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GetDebugChainHeadsResponseDataInner(BaseModel):
    """GetDebugChainHeadsResponseDataInner - a model defined in OpenAPI

        root: The root of this GetDebugChainHeadsResponseDataInner [Optional].
        slot: The slot of this GetDebugChainHeadsResponseDataInner [Optional].
    """

    root: Optional[str] = Field(alias="root", default=None)
    slot: Optional[str] = Field(alias="slot", default=None)

    @validator("root")
    def root_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{64}$", value)
        return value

GetDebugChainHeadsResponseDataInner.update_forward_refs()
