# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GetSpecResponse(BaseModel):
    """GetSpecResponse - a model defined in OpenAPI

        data: The data of this GetSpecResponse [Optional].
    """

    data: Optional[Dict[str, Any]] = Field(alias="data", default=None)

GetSpecResponse.update_forward_refs()
