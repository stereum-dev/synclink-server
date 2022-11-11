# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.register_validator_request_inner_message import RegisterValidatorRequestInnerMessage


class RegisterValidatorRequestInner(BaseModel):
    """RegisterValidatorRequestInner - a model defined in OpenAPI

        message: The message of this RegisterValidatorRequestInner [Optional].
        signature: The signature of this RegisterValidatorRequestInner [Optional].
    """

    message: Optional[RegisterValidatorRequestInnerMessage] = Field(alias="message", default=None)
    signature: Optional[str] = Field(alias="signature", default=None)

    @validator("signature")
    def signature_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{192}$", value)
        return value

RegisterValidatorRequestInner.update_forward_refs()
