# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_block_request_one_of_message_all_of_body_attestations_inner import PublishBlockRequestOneOfMessageAllOfBodyAttestationsInner


class PublishAggregateAndProofsRequestInnerMessageAllOf(BaseModel):
    """PublishAggregateAndProofsRequestInnerMessageAllOf - a model defined in OpenAPI

        aggregator_index: The aggregator_index of this PublishAggregateAndProofsRequestInnerMessageAllOf [Optional].
        aggregate: The aggregate of this PublishAggregateAndProofsRequestInnerMessageAllOf [Optional].
    """

    aggregator_index: Optional[str] = Field(alias="aggregator_index", default=None)
    aggregate: Optional[PublishBlockRequestOneOfMessageAllOfBodyAttestationsInner] = Field(alias="aggregate", default=None)

PublishAggregateAndProofsRequestInnerMessageAllOf.update_forward_refs()
