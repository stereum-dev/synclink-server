# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_block_request_one_of_message_all_of_body_proposer_slashings_inner import PublishBlockRequestOneOfMessageAllOfBodyProposerSlashingsInner


class GetPoolProposerSlashingsResponse(BaseModel):
    """GetPoolProposerSlashingsResponse - a model defined in OpenAPI

        data: The data of this GetPoolProposerSlashingsResponse [Optional].
    """

    data: Optional[List[PublishBlockRequestOneOfMessageAllOfBodyProposerSlashingsInner]] = Field(alias="data", default=None)

GetPoolProposerSlashingsResponse.update_forward_refs()
