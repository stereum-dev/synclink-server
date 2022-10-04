# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_block_request_one_of_message_all_of_body_deposits_inner_data import PublishBlockRequestOneOfMessageAllOfBodyDepositsInnerData


class PublishBlockRequestOneOfMessageAllOfBodyDepositsInner(BaseModel):
    """PublishBlockRequestOneOfMessageAllOfBodyDepositsInner - a model defined in OpenAPI

        proof: The proof of this PublishBlockRequestOneOfMessageAllOfBodyDepositsInner [Optional].
        data: The data of this PublishBlockRequestOneOfMessageAllOfBodyDepositsInner [Optional].
    """

    proof: Optional[List[str]] = Field(alias="proof", default=None)
    data: Optional[PublishBlockRequestOneOfMessageAllOfBodyDepositsInnerData] = Field(alias="data", default=None)

PublishBlockRequestOneOfMessageAllOfBodyDepositsInner.update_forward_refs()
