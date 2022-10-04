# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_block_request_one_of1_message import PublishBlockRequestOneOf1Message
from models.publish_block_request_one_of2_message import PublishBlockRequestOneOf2Message
from models.publish_block_request_one_of2_message_all_of_body import PublishBlockRequestOneOf2MessageAllOfBody
from models.publish_block_request_one_of_message import PublishBlockRequestOneOfMessage


class ProduceBlockV2ResponseData(BaseModel):
    """ProduceBlockV2ResponseData - a model defined in OpenAPI

        slot: The slot of this ProduceBlockV2ResponseData [Optional].
        proposer_index: The proposer_index of this ProduceBlockV2ResponseData [Optional].
        parent_root: The parent_root of this ProduceBlockV2ResponseData [Optional].
        state_root: The state_root of this ProduceBlockV2ResponseData [Optional].
        body: The body of this ProduceBlockV2ResponseData [Optional].
    """

    slot: Optional[str] = Field(alias="slot", default=None)
    proposer_index: Optional[str] = Field(alias="proposer_index", default=None)
    parent_root: Optional[str] = Field(alias="parent_root", default=None)
    state_root: Optional[str] = Field(alias="state_root", default=None)
    body: Optional[PublishBlockRequestOneOf2MessageAllOfBody] = Field(alias="body", default=None)

ProduceBlockV2ResponseData.update_forward_refs()
