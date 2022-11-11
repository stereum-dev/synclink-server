# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GetStateRootResponseData(BaseModel):
    """GetStateRootResponseData - a model defined in OpenAPI

        root: The root of this GetStateRootResponseData [Optional].
    """

    root: Optional[str] = Field(alias="root", default=None)

GetStateRootResponseData.update_forward_refs()
