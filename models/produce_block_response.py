# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_block_request_one_of_message import PublishBlockRequestOneOfMessage


class ProduceBlockResponse(BaseModel):
    """ProduceBlockResponse - a model defined in OpenAPI

        data: The data of this ProduceBlockResponse [Optional].
    """

    data: Optional[PublishBlockRequestOneOfMessage] = Field(alias="data", default=None)

ProduceBlockResponse.update_forward_refs()
