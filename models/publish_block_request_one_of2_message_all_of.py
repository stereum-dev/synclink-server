# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_block_request_one_of2_message_all_of_body import PublishBlockRequestOneOf2MessageAllOfBody


class PublishBlockRequestOneOf2MessageAllOf(BaseModel):
    """PublishBlockRequestOneOf2MessageAllOf - a model defined in OpenAPI

        body: The body of this PublishBlockRequestOneOf2MessageAllOf [Optional].
    """

    body: Optional[PublishBlockRequestOneOf2MessageAllOfBody] = Field(alias="body", default=None)

PublishBlockRequestOneOf2MessageAllOf.update_forward_refs()
