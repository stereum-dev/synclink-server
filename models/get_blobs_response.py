# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_block_request_one_of2_signed_blob_sidecars_inner_message import PublishBlockRequestOneOf2SignedBlobSidecarsInnerMessage


class GetBlobsResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GetBlobsResponse - a model defined in OpenAPI

        data: The data of this GetBlobsResponse [Optional].
    """

    data: Optional[List[PublishBlockRequestOneOf2SignedBlobSidecarsInnerMessage]] = Field(alias="data", default=None)

GetBlobsResponse.update_forward_refs()
