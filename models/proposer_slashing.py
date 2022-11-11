# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_block_headers_response_data_inner_header import GetBlockHeadersResponseDataInnerHeader


class ProposerSlashing(BaseModel):
    """ProposerSlashing - a model defined in OpenAPI

        signed_header_1: The signed_header_1 of this ProposerSlashing [Optional].
        signed_header_2: The signed_header_2 of this ProposerSlashing [Optional].
    """

    signed_header_1: Optional[GetBlockHeadersResponseDataInnerHeader] = Field(alias="signed_header_1", default=None)
    signed_header_2: Optional[GetBlockHeadersResponseDataInnerHeader] = Field(alias="signed_header_2", default=None)

ProposerSlashing.update_forward_refs()
