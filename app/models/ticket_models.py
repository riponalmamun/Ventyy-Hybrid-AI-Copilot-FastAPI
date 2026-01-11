from pydantic import BaseModel

class Ticket(BaseModel):
    ticket_id: int
    event_name: str
    user_id: int
    price: float
    age_restriction: int = 0
