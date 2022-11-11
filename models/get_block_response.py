# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_block_request_one_of import PublishBlockRequestOneOf


class GetBlockResponse(BaseModel):
    """GetBlockResponse - a model defined in OpenAPI

        data: The data of this GetBlockResponse [Optional].
    """

    data: Optional[PublishBlockRequestOneOf] = Field(alias="data", default=None)

GetBlockResponse.update_forward_refs()
