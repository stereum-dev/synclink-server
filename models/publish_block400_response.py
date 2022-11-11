# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class PublishBlock400Response(BaseModel):
    """PublishBlock400Response - a model defined in OpenAPI

        code: The code of this PublishBlock400Response [Optional].
        message: The message of this PublishBlock400Response [Optional].
        stacktraces: The stacktraces of this PublishBlock400Response [Optional].
    """

    code: Optional[float] = Field(alias="code", default=None)
    message: Optional[str] = Field(alias="message", default=None)
    stacktraces: Optional[List[str]] = Field(alias="stacktraces", default=None)

PublishBlock400Response.update_forward_refs()
