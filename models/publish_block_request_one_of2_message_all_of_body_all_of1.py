# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_block_request_one_of2_message_all_of_body_all_of1_execution_payload import PublishBlockRequestOneOf2MessageAllOfBodyAllOf1ExecutionPayload


class PublishBlockRequestOneOf2MessageAllOfBodyAllOf1(BaseModel):
    """PublishBlockRequestOneOf2MessageAllOfBodyAllOf1 - a model defined in OpenAPI

        execution_payload: The execution_payload of this PublishBlockRequestOneOf2MessageAllOfBodyAllOf1 [Optional].
    """

    execution_payload: Optional[PublishBlockRequestOneOf2MessageAllOfBodyAllOf1ExecutionPayload] = Field(alias="execution_payload", default=None)

PublishBlockRequestOneOf2MessageAllOfBodyAllOf1.update_forward_refs()
