# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_block_request_one_of_message_all_of_body_attestations_inner import PublishBlockRequestOneOfMessageAllOfBodyAttestationsInner


class GetPoolAttestationsResponse(BaseModel):
    """GetPoolAttestationsResponse - a model defined in OpenAPI

        data: The data of this GetPoolAttestationsResponse [Optional].
    """

    data: Optional[List[PublishBlockRequestOneOfMessageAllOfBodyAttestationsInner]] = Field(alias="data", default=None)

GetPoolAttestationsResponse.update_forward_refs()
