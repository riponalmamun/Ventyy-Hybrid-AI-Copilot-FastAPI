from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.ai_copilot import AICopilotService
from app.dependencies import db_service

router = APIRouter(prefix="/resolution", tags=["Resolution Center"])
ai_service = AICopilotService()

class AskRequest(BaseModel):
    user_id: int
    question: str

@router.post("/ask")
def ask_resolution_center(req: AskRequest):
    db = db_service.read_db()
    user_data = next((u for u in db["users"] if u["user_id"] == req.user_id), None)
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")

    context = f"User: {user_data['name']}\nPolicies: {db['policies']}"
    answer = ai_service.ask(req.question, context)
    return answer
