from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from services.chatbot import get_streaming_response

router = APIRouter()


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: list[Message]


@router.post("")
async def chat(request: ChatRequest):
    """
    Chat endpoint with streaming response.
    Receives conversation history and returns AI response in real-time.
    """
    # Convert Pydantic models to dicts
    messages = [{"role": m.role, "content": m.content} for m in request.messages]

    return StreamingResponse(
        get_streaming_response(messages),
        media_type="text/event-stream"
    )
