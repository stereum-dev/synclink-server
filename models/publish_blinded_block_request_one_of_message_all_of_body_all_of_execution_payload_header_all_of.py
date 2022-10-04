# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class PublishBlindedBlockRequestOneOfMessageAllOfBodyAllOfExecutionPayloadHeaderAllOf(BaseModel):
    """PublishBlindedBlockRequestOneOfMessageAllOfBodyAllOfExecutionPayloadHeaderAllOf - a model defined in OpenAPI

        transactions_root: The transactions_root of this PublishBlindedBlockRequestOneOfMessageAllOfBodyAllOfExecutionPayloadHeaderAllOf [Optional].
    """

    transactions_root: Optional[str] = Field(alias="transactions_root", default=None)

    @validator("transactions_root")
    def transactions_root_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{64}$", value)
        return value

PublishBlindedBlockRequestOneOfMessageAllOfBodyAllOfExecutionPayloadHeaderAllOf.update_forward_refs()
