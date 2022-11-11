# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_block_request_one_of1_message_all_of_body import PublishBlockRequestOneOf1MessageAllOfBody


class PublishBlockRequestOneOf1MessageAllOf(BaseModel):
    """PublishBlockRequestOneOf1MessageAllOf - a model defined in OpenAPI

        body: The body of this PublishBlockRequestOneOf1MessageAllOf [Optional].
    """

    body: Optional[PublishBlockRequestOneOf1MessageAllOfBody] = Field(alias="body", default=None)

PublishBlockRequestOneOf1MessageAllOf.update_forward_refs()
