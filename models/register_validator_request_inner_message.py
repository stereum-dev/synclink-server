# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class RegisterValidatorRequestInnerMessage(BaseModel):
    """RegisterValidatorRequestInnerMessage - a model defined in OpenAPI

        fee_recipient: The fee_recipient of this RegisterValidatorRequestInnerMessage [Optional].
        gas_limit: The gas_limit of this RegisterValidatorRequestInnerMessage [Optional].
        timestamp: The timestamp of this RegisterValidatorRequestInnerMessage [Optional].
        pubkey: The pubkey of this RegisterValidatorRequestInnerMessage [Optional].
    """

    fee_recipient: Optional[str] = Field(alias="fee_recipient", default=None)
    gas_limit: Optional[str] = Field(alias="gas_limit", default=None)
    timestamp: Optional[str] = Field(alias="timestamp", default=None)
    pubkey: Optional[str] = Field(alias="pubkey", default=None)

    @validator("fee_recipient")
    def fee_recipient_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{40}$", value)
        return value

    @validator("pubkey")
    def pubkey_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{96}$", value)
        return value

RegisterValidatorRequestInnerMessage.update_forward_refs()
