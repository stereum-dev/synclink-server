# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_blinded_block_request_one_of_message import PublishBlindedBlockRequestOneOfMessage
from models.publish_blinded_block_request_one_of_message_all_of_body import PublishBlindedBlockRequestOneOfMessageAllOfBody
from models.publish_block_request_one_of1_message import PublishBlockRequestOneOf1Message
from models.publish_block_request_one_of_message import PublishBlockRequestOneOfMessage


class ProduceBlindedBlockResponseData(BaseModel):
    """ProduceBlindedBlockResponseData - a model defined in OpenAPI

        slot: The slot of this ProduceBlindedBlockResponseData [Optional].
        proposer_index: The proposer_index of this ProduceBlindedBlockResponseData [Optional].
        parent_root: The parent_root of this ProduceBlindedBlockResponseData [Optional].
        state_root: The state_root of this ProduceBlindedBlockResponseData [Optional].
        body: The body of this ProduceBlindedBlockResponseData [Optional].
    """

    slot: Optional[str] = Field(alias="slot", default=None)
    proposer_index: Optional[str] = Field(alias="proposer_index", default=None)
    parent_root: Optional[str] = Field(alias="parent_root", default=None)
    state_root: Optional[str] = Field(alias="state_root", default=None)
    body: Optional[PublishBlindedBlockRequestOneOfMessageAllOfBody] = Field(alias="body", default=None)

ProduceBlindedBlockResponseData.update_forward_refs()
