# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class PublishBlockRequestOneOf2MessageAllOfBodyAllOf1ExecutionPayloadAllOf1(BaseModel):
    """PublishBlockRequestOneOf2MessageAllOfBodyAllOf1ExecutionPayloadAllOf1 - a model defined in OpenAPI

        transactions: The transactions of this PublishBlockRequestOneOf2MessageAllOfBodyAllOf1ExecutionPayloadAllOf1 [Optional].
    """

    transactions: Optional[List[str]] = Field(alias="transactions", default=None)

PublishBlockRequestOneOf2MessageAllOfBodyAllOf1ExecutionPayloadAllOf1.update_forward_refs()
