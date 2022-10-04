# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_block_request_one_of_message_all_of_body import PublishBlockRequestOneOfMessageAllOfBody


class PublishBlockRequestOneOfMessageAllOf(BaseModel):
    """PublishBlockRequestOneOfMessageAllOf - a model defined in OpenAPI

        body: The body of this PublishBlockRequestOneOfMessageAllOf [Optional].
    """

    body: Optional[PublishBlockRequestOneOfMessageAllOfBody] = Field(alias="body", default=None)

PublishBlockRequestOneOfMessageAllOf.update_forward_refs()
