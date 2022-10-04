# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_blinded_block_request_one_of import PublishBlindedBlockRequestOneOf
from models.publish_blinded_block_request_one_of_message import PublishBlindedBlockRequestOneOfMessage
from models.publish_block_request_one_of import PublishBlockRequestOneOf
from models.publish_block_request_one_of1 import PublishBlockRequestOneOf1


class PublishBlindedBlockRequest(BaseModel):
    """PublishBlindedBlockRequest - a model defined in OpenAPI

        message: The message of this PublishBlindedBlockRequest [Optional].
        signature: The signature of this PublishBlindedBlockRequest [Optional].
    """

    message: Optional[PublishBlindedBlockRequestOneOfMessage] = Field(alias="message", default=None)
    signature: Optional[str] = Field(alias="signature", default=None)

    @validator("signature")
    def signature_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{192}$", value)
        return value

PublishBlindedBlockRequest.update_forward_refs()
