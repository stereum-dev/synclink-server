# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_blinded_block_request_one_of_message import PublishBlindedBlockRequestOneOfMessage


class PublishBlindedBlockRequestOneOf(BaseModel):
    """PublishBlindedBlockRequestOneOf - a model defined in OpenAPI

        message: The message of this PublishBlindedBlockRequestOneOf [Optional].
        signature: The signature of this PublishBlindedBlockRequestOneOf [Optional].
    """

    message: Optional[PublishBlindedBlockRequestOneOfMessage] = Field(alias="message", default=None)
    signature: Optional[str] = Field(alias="signature", default=None)

    @validator("signature")
    def signature_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{192}$", value)
        return value

PublishBlindedBlockRequestOneOf.update_forward_refs()
