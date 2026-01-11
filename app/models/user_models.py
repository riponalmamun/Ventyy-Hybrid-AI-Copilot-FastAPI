from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    user_id: int
    name: str
    tickets: List[int] = []
    balance: float = 0.0
