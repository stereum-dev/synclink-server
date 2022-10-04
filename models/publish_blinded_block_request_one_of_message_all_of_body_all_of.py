# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_blinded_block_request_one_of_message_all_of_body_all_of_execution_payload_header import PublishBlindedBlockRequestOneOfMessageAllOfBodyAllOfExecutionPayloadHeader


class PublishBlindedBlockRequestOneOfMessageAllOfBodyAllOf(BaseModel):
    """PublishBlindedBlockRequestOneOfMessageAllOfBodyAllOf - a model defined in OpenAPI

        execution_payload_header: The execution_payload_header of this PublishBlindedBlockRequestOneOfMessageAllOfBodyAllOf [Optional].
    """

    execution_payload_header: Optional[PublishBlindedBlockRequestOneOfMessageAllOfBodyAllOfExecutionPayloadHeader] = Field(alias="execution_payload_header", default=None)

PublishBlindedBlockRequestOneOfMessageAllOfBodyAllOf.update_forward_refs()
