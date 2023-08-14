# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.produce_block_v3_response_data import ProduceBlockV3ResponseData


class ProduceBlockV3Response(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ProduceBlockV3Response - a model defined in OpenAPI

        version: The version of this ProduceBlockV3Response [Optional].
        execution_payload_blinded: The execution_payload_blinded of this ProduceBlockV3Response [Optional].
        execution_payload_value: The execution_payload_value of this ProduceBlockV3Response [Optional].
        data: The data of this ProduceBlockV3Response [Optional].
    """

    version: Optional[str] = Field(alias="version", default=None)
    execution_payload_blinded: Optional[bool] = Field(alias="execution_payload_blinded", default=None)
    execution_payload_value: Optional[str] = Field(alias="execution_payload_value", default=None)
    data: Optional[ProduceBlockV3ResponseData] = Field(alias="data", default=None)

ProduceBlockV3Response.update_forward_refs()