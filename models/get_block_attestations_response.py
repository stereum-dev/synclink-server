# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_block_request_one_of_message_all_of_body_attestations_inner import PublishBlockRequestOneOfMessageAllOfBodyAttestationsInner


class GetBlockAttestationsResponse(BaseModel):
    """GetBlockAttestationsResponse - a model defined in OpenAPI

        execution_optimistic: The execution_optimistic of this GetBlockAttestationsResponse [Optional].
        data: The data of this GetBlockAttestationsResponse [Optional].
    """

    execution_optimistic: Optional[bool] = Field(alias="execution_optimistic", default=None)
    data: Optional[List[PublishBlockRequestOneOfMessageAllOfBodyAttestationsInner]] = Field(alias="data", default=None)

GetBlockAttestationsResponse.update_forward_refs()
