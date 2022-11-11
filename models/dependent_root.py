# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class DependentRoot(BaseModel):
    """DependentRoot - a model defined in OpenAPI

    """


DependentRoot.update_forward_refs()
