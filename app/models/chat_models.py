from pydantic import BaseModel
from typing import List

class ChatMessage(BaseModel):
    sender_id: int
    content: str
    timestamp: str
