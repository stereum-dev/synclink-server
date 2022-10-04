# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_block_request_one_of_message_all_of_body_attestations_inner import PublishBlockRequestOneOfMessageAllOfBodyAttestationsInner


class PublishAggregateAndProofsRequestInnerMessage(BaseModel):
    """PublishAggregateAndProofsRequestInnerMessage - a model defined in OpenAPI

        aggregator_index: The aggregator_index of this PublishAggregateAndProofsRequestInnerMessage [Optional].
        aggregate: The aggregate of this PublishAggregateAndProofsRequestInnerMessage [Optional].
        selection_proof: The selection_proof of this PublishAggregateAndProofsRequestInnerMessage [Optional].
    """

    aggregator_index: Optional[str] = Field(alias="aggregator_index", default=None)
    aggregate: Optional[PublishBlockRequestOneOfMessageAllOfBodyAttestationsInner] = Field(alias="aggregate", default=None)
    selection_proof: Optional[str] = Field(alias="selection_proof", default=None)

    @validator("selection_proof")
    def selection_proof_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{192}$", value)
        return value

PublishAggregateAndProofsRequestInnerMessage.update_forward_refs()
