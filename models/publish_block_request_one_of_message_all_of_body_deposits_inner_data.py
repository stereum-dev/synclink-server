# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class PublishBlockRequestOneOfMessageAllOfBodyDepositsInnerData(BaseModel):
    """PublishBlockRequestOneOfMessageAllOfBodyDepositsInnerData - a model defined in OpenAPI

        pubkey: The pubkey of this PublishBlockRequestOneOfMessageAllOfBodyDepositsInnerData [Optional].
        withdrawal_credentials: The withdrawal_credentials of this PublishBlockRequestOneOfMessageAllOfBodyDepositsInnerData [Optional].
        amount: The amount of this PublishBlockRequestOneOfMessageAllOfBodyDepositsInnerData [Optional].
        signature: The signature of this PublishBlockRequestOneOfMessageAllOfBodyDepositsInnerData [Optional].
    """

    pubkey: Optional[str] = Field(alias="pubkey", default=None)
    withdrawal_credentials: Optional[str] = Field(alias="withdrawal_credentials", default=None)
    amount: Optional[str] = Field(alias="amount", default=None)
    signature: Optional[str] = Field(alias="signature", default=None)

    @validator("pubkey")
    def pubkey_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{96}$", value)
        return value

PublishBlockRequestOneOfMessageAllOfBodyDepositsInnerData.update_forward_refs()
