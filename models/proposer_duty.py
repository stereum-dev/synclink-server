# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class ProposerDuty(BaseModel):
    """ProposerDuty - a model defined in OpenAPI

        pubkey: The pubkey of this ProposerDuty [Optional].
        validator_index: The validator_index of this ProposerDuty [Optional].
        slot: The slot of this ProposerDuty [Optional].
    """

    pubkey: Optional[str] = Field(alias="pubkey", default=None)
    validator_index: Optional[str] = Field(alias="validator_index", default=None)
    slot: Optional[str] = Field(alias="slot", default=None)

    @validator("pubkey")
    def pubkey_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{96}$", value)
        return value

ProposerDuty.update_forward_refs()
