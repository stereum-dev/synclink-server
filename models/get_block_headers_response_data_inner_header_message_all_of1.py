# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GetBlockHeadersResponseDataInnerHeaderMessageAllOf1(BaseModel):
    """GetBlockHeadersResponseDataInnerHeaderMessageAllOf1 - a model defined in OpenAPI

        body_root: The body_root of this GetBlockHeadersResponseDataInnerHeaderMessageAllOf1 [Optional].
    """

    body_root: Optional[str] = Field(alias="body_root", default=None)

GetBlockHeadersResponseDataInnerHeaderMessageAllOf1.update_forward_refs()
