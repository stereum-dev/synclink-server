# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.produce_blinded_block_response_data import ProduceBlindedBlockResponseData


class ProduceBlindedBlockResponse(BaseModel):
    """ProduceBlindedBlockResponse - a model defined in OpenAPI

        version: The version of this ProduceBlindedBlockResponse [Optional].
        data: The data of this ProduceBlindedBlockResponse [Optional].
    """

    version: Optional[str] = Field(alias="version", default=None)
    data: Optional[ProduceBlindedBlockResponseData] = Field(alias="data", default=None)

ProduceBlindedBlockResponse.update_forward_refs()
