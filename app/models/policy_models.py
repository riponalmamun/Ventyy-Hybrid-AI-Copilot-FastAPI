from pydantic import BaseModel
from typing import List, Dict

class Policy(BaseModel):
    ticket_rules: List[str]
    refund_policy: List[str]
    escrow_rules: List[str]
    account_help: List[str]
    visual_forms: Dict
