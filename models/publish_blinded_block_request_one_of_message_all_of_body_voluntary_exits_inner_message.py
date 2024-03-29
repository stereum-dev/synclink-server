# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class PublishBlindedBlockRequestOneOfMessageAllOfBodyVoluntaryExitsInnerMessage(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    PublishBlindedBlockRequestOneOfMessageAllOfBodyVoluntaryExitsInnerMessage - a model defined in OpenAPI

        epoch: The epoch of this PublishBlindedBlockRequestOneOfMessageAllOfBodyVoluntaryExitsInnerMessage [Optional].
        validator_index: The validator_index of this PublishBlindedBlockRequestOneOfMessageAllOfBodyVoluntaryExitsInnerMessage [Optional].
    """

    epoch: Optional[str] = Field(alias="epoch", default=None)
    validator_index: Optional[str] = Field(alias="validator_index", default=None)

PublishBlindedBlockRequestOneOfMessageAllOfBodyVoluntaryExitsInnerMessage.update_forward_refs()
