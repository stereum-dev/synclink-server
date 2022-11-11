# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_block_request_one_of import PublishBlockRequestOneOf
from models.publish_block_request_one_of1 import PublishBlockRequestOneOf1
from models.publish_block_request_one_of2 import PublishBlockRequestOneOf2
from models.publish_block_request_one_of2_message import PublishBlockRequestOneOf2Message


class PublishBlockRequest(BaseModel):
    """PublishBlockRequest - a model defined in OpenAPI

        message: The message of this PublishBlockRequest [Optional].
        signature: The signature of this PublishBlockRequest [Optional].
    """

    message: Optional[PublishBlockRequestOneOf2Message] = Field(alias="message", default=None)
    signature: Optional[str] = Field(alias="signature", default=None)

    @validator("signature")
    def signature_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{192}$", value)
        return value

PublishBlockRequest.update_forward_refs()
