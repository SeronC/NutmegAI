# FastAPI/Flask app entrypoint
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn

from config import settings
from routes import chatbot

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="AI-powered legal assistant for Grenadians, supporting Grenadian Creole",
    version="1.0.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(chatbot.router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
    return {
        "message": "Welcome to NutmegAI - Grenadian Legal Assistant",
        "version": "1.0.0",
        "description": "AI chatbot helping Grenadians with legal registry documents"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "NutmegAI Backend"}

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error", "message": str(exc)}
    )

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )