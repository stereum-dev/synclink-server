# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_genesis_response_data import GetGenesisResponseData


class GetGenesisResponse(BaseModel):
    """GetGenesisResponse - a model defined in OpenAPI

        data: The data of this GetGenesisResponse [Optional].
    """

    data: Optional[GetGenesisResponseData] = Field(alias="data", default=None)


GetGenesisResponse.update_forward_refs()
