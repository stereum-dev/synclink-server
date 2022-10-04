# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GetDebugChainHeadsResponse1DataInner(BaseModel):
    """GetDebugChainHeadsResponse1DataInner - a model defined in OpenAPI

        root: The root of this GetDebugChainHeadsResponse1DataInner [Optional].
        slot: The slot of this GetDebugChainHeadsResponse1DataInner [Optional].
        execution_optimistic: The execution_optimistic of this GetDebugChainHeadsResponse1DataInner [Optional].
    """

    root: Optional[str] = Field(alias="root", default=None)
    slot: Optional[str] = Field(alias="slot", default=None)
    execution_optimistic: Optional[bool] = Field(alias="execution_optimistic", default=None)

    @validator("root")
    def root_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{64}$", value)
        return value

GetDebugChainHeadsResponse1DataInner.update_forward_refs()
