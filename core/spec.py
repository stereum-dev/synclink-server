from typing import List, Optional

from models.get_spec_response import GetSpecResponseData
from models.get_state_fork_response_data import GetStateForkResponseData
from pydantic import BaseModel


class DepositContract(BaseModel):
    address: Optional[str]
    chain_id: Optional[int]


class Spec(GetSpecResponseData):
    FORK_EPOCHS: Optional[List[GetStateForkResponseData]]
    DEPOSIT_CONTRACT: Optional[DepositContract]
