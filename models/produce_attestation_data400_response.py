# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class ProduceAttestationData400Response(BaseModel):
    """ProduceAttestationData400Response - a model defined in OpenAPI

        code: The code of this ProduceAttestationData400Response [Optional].
        message: The message of this ProduceAttestationData400Response [Optional].
        stacktraces: The stacktraces of this ProduceAttestationData400Response [Optional].
    """

    code: Optional[float] = Field(alias="code", default=None)
    message: Optional[str] = Field(alias="message", default=None)
    stacktraces: Optional[List[str]] = Field(alias="stacktraces", default=None)

ProduceAttestationData400Response.update_forward_refs()
