# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.beacon_block_all_of_body_signed_header1 import BeaconBlockAllOfBodySignedHeader1


class BeaconBlockAllOfBodyProposerSlashings(BaseModel):
    """BeaconBlockAllOfBodyProposerSlashings - a model defined in OpenAPI

        signed_header_1: The signed_header_1 of this BeaconBlockAllOfBodyProposerSlashings [Optional].
        signed_header_2: The signed_header_2 of this BeaconBlockAllOfBodyProposerSlashings [Optional].
    """

    signed_header_1: Optional[BeaconBlockAllOfBodySignedHeader1] = Field(alias="signed_header_1", default=None)
    signed_header_2: Optional[BeaconBlockAllOfBodySignedHeader1] = Field(alias="signed_header_2", default=None)

BeaconBlockAllOfBodyProposerSlashings.update_forward_refs()
