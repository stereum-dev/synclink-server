# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class PrepareBeaconProposerRequestInner(BaseModel):
    """PrepareBeaconProposerRequestInner - a model defined in OpenAPI

        validator_index: The validator_index of this PrepareBeaconProposerRequestInner [Optional].
        fee_recipient: The fee_recipient of this PrepareBeaconProposerRequestInner [Optional].
    """

    validator_index: Optional[str] = Field(alias="validator_index", default=None)
    fee_recipient: Optional[str] = Field(alias="fee_recipient", default=None)

    @validator("fee_recipient")
    def fee_recipient_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{40}$", value)
        return value

PrepareBeaconProposerRequestInner.update_forward_refs()
