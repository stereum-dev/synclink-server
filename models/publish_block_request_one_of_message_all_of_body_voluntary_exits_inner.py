# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_block_request_one_of_message_all_of_body_voluntary_exits_inner_message import PublishBlockRequestOneOfMessageAllOfBodyVoluntaryExitsInnerMessage


class PublishBlockRequestOneOfMessageAllOfBodyVoluntaryExitsInner(BaseModel):
    """PublishBlockRequestOneOfMessageAllOfBodyVoluntaryExitsInner - a model defined in OpenAPI

        message: The message of this PublishBlockRequestOneOfMessageAllOfBodyVoluntaryExitsInner [Optional].
        signature: The signature of this PublishBlockRequestOneOfMessageAllOfBodyVoluntaryExitsInner [Optional].
    """

    message: Optional[PublishBlockRequestOneOfMessageAllOfBodyVoluntaryExitsInnerMessage] = Field(alias="message", default=None)
    signature: Optional[str] = Field(alias="signature", default=None)

    @validator("signature")
    def signature_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{192}$", value)
        return value

PublishBlockRequestOneOfMessageAllOfBodyVoluntaryExitsInner.update_forward_refs()
