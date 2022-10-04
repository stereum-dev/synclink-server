# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.produce_block_v2_response_data import ProduceBlockV2ResponseData


class ProduceBlockV2Response(BaseModel):
    """ProduceBlockV2Response - a model defined in OpenAPI

        version: The version of this ProduceBlockV2Response [Optional].
        data: The data of this ProduceBlockV2Response [Optional].
    """

    version: Optional[str] = Field(alias="version", default=None)
    data: Optional[ProduceBlockV2ResponseData] = Field(alias="data", default=None)

ProduceBlockV2Response.update_forward_refs()
