from typing import List, Optional

from models.get_spec_response import GetSpecResponseData
from models.get_state_fork_response_data import GetStateForkResponseData
from pydantic import BaseModel


class DepositContract(BaseModel):
    address: Optional[str]
    chain_id: Optional[str]


class Config(BaseModel):
    spec: Optional[GetSpecResponseData]
    fork_epochs: Optional[List[GetStateForkResponseData]]
    deposit_contract: Optional[DepositContract]
