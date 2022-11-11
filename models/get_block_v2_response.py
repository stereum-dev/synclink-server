# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_block_request import PublishBlockRequest


class GetBlockV2Response(BaseModel):
    """GetBlockV2Response - a model defined in OpenAPI

        version: The version of this GetBlockV2Response [Optional].
        execution_optimistic: The execution_optimistic of this GetBlockV2Response [Optional].
        data: The data of this GetBlockV2Response [Optional].
    """

    version: Optional[str] = Field(alias="version", default=None)
    execution_optimistic: Optional[bool] = Field(alias="execution_optimistic", default=None)
    data: Optional[PublishBlockRequest] = Field(alias="data", default=None)

GetBlockV2Response.update_forward_refs()
