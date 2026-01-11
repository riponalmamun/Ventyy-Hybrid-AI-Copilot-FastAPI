from fastapi import FastAPI
from app.routers import resolution

app = FastAPI(title="Ventyy Hybrid AI Copilot")

# Include routers
app.include_router(resolution.router)

# Swagger UI: http://127.0.0.1:8000/docs
