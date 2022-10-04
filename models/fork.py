# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class Fork(BaseModel):
    """Fork - a model defined in OpenAPI

        previous_version: The previous_version of this Fork [Optional].
        current_version: The current_version of this Fork [Optional].
        epoch: The epoch of this Fork [Optional].
    """

    previous_version: Optional[str] = Field(alias="previous_version", default=None)
    current_version: Optional[str] = Field(alias="current_version", default=None)
    epoch: Optional[str] = Field(alias="epoch", default=None)

    @validator("previous_version")
    def previous_version_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{8}$", value)
        return value

    @validator("current_version")
    def current_version_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{8}$", value)
        return value

Fork.update_forward_refs()
