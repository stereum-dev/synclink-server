# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GetBlockRootResponseData(BaseModel):
    """GetBlockRootResponseData - a model defined in OpenAPI

        root: The root of this GetBlockRootResponseData [Optional].
    """

    root: Optional[object] = Field(alias="root", default=None)

GetBlockRootResponseData.update_forward_refs()
