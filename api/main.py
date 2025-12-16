from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from routers import chat, line

# Load environment variables
load_dotenv()

app = FastAPI(
    title="HAI Chatbot API",
    description="API for Human-Robot Interaction Virtual Exhibition chatbot",
    version="1.0.0"
)

# CORS middleware - allow frontend to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(chat.router, prefix="/chat", tags=["chat"])
app.include_router(line.router, prefix="/line", tags=["line"])


@app.get("/")
async def root():
    return {
        "message": "HAI Chatbot API",
        "docs": "/docs",
        "status": "running"
    }


@app.get("/health")
async def health():
    return {"status": "healthy"}
