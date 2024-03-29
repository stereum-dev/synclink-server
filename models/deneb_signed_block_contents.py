# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_block_request_one_of2_signed_blob_sidecars_inner import PublishBlockRequestOneOf2SignedBlobSidecarsInner
from models.publish_block_request_one_of2_signed_block import PublishBlockRequestOneOf2SignedBlock


class DenebSignedBlockContents(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    DenebSignedBlockContents - a model defined in OpenAPI

        signed_block: The signed_block of this DenebSignedBlockContents [Optional].
        signed_blob_sidecars: The signed_blob_sidecars of this DenebSignedBlockContents [Optional].
    """

    signed_block: Optional[PublishBlockRequestOneOf2SignedBlock] = Field(alias="signed_block", default=None)
    signed_blob_sidecars: Optional[List[PublishBlockRequestOneOf2SignedBlobSidecarsInner]] = Field(alias="signed_blob_sidecars", default=None)

DenebSignedBlockContents.update_forward_refs()
