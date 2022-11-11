# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_block_request_one_of1_message_all_of_body import PublishBlockRequestOneOf1MessageAllOfBody


class PublishBlockRequestOneOf1Message(BaseModel):
    """PublishBlockRequestOneOf1Message - a model defined in OpenAPI

        slot: The slot of this PublishBlockRequestOneOf1Message [Optional].
        proposer_index: The proposer_index of this PublishBlockRequestOneOf1Message [Optional].
        parent_root: The parent_root of this PublishBlockRequestOneOf1Message [Optional].
        state_root: The state_root of this PublishBlockRequestOneOf1Message [Optional].
        body: The body of this PublishBlockRequestOneOf1Message [Optional].
    """

    slot: Optional[str] = Field(alias="slot", default=None)
    proposer_index: Optional[str] = Field(alias="proposer_index", default=None)
    parent_root: Optional[str] = Field(alias="parent_root", default=None)
    state_root: Optional[str] = Field(alias="state_root", default=None)
    body: Optional[PublishBlockRequestOneOf1MessageAllOfBody] = Field(alias="body", default=None)

PublishBlockRequestOneOf1Message.update_forward_refs()
