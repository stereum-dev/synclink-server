# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class PublishAggregateAndProofsRequestInnerMessageAllOf1(BaseModel):
    """PublishAggregateAndProofsRequestInnerMessageAllOf1 - a model defined in OpenAPI

        selection_proof: The selection_proof of this PublishAggregateAndProofsRequestInnerMessageAllOf1 [Optional].
    """

    selection_proof: Optional[str] = Field(alias="selection_proof", default=None)

    @validator("selection_proof")
    def selection_proof_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{192}$", value)
        return value

PublishAggregateAndProofsRequestInnerMessageAllOf1.update_forward_refs()
