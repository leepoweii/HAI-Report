import os
from openai import AsyncOpenAI
from prompts.guide import get_system_prompt

# Initialize OpenAI client (lazy initialization to handle missing key gracefully)
_client = None

def get_client():
    global _client
    if _client is None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set")
        _client = AsyncOpenAI(api_key=api_key)
    return _client

# Model configuration
MODEL = os.getenv("OPENAI_MODEL", "gpt-5-mini")
USE_WEB_SEARCH = os.getenv("USE_WEB_SEARCH", "true").lower() == "true"


async def get_streaming_response(messages: list[dict], use_web_search: bool = None):
    """
    Stream response using OpenAI Responses API with optional web search.

    Args:
        messages: Conversation history as list of {role, content} dicts
        use_web_search: Whether to enable web search tool (defaults to env var)

    Yields:
        Text chunks as they arrive from the API
    """
    if use_web_search is None:
        use_web_search = USE_WEB_SEARCH

    tools = [{"type": "web_search"}] if use_web_search else []

    try:
        client = get_client()
        # Use OpenAI Responses API with streaming
        stream = await client.responses.create(
            model=MODEL,
            instructions=get_system_prompt(),
            input=messages,
            tools=tools,
            stream=True
        )

        async for event in stream:
            # Handle different event types from Responses API
            if hasattr(event, 'type'):
                if event.type == 'response.output_text.delta':
                    if hasattr(event, 'delta') and event.delta:
                        yield event.delta
                elif event.type == 'response.output_text.done':
                    break
            # Fallback for simpler event structure
            elif hasattr(event, 'delta') and event.delta:
                yield event.delta

    except Exception as e:
        print(f"OpenAI API error: {e}")
        yield f"Sorry, I encountered an error: {str(e)}"


async def get_full_response(messages: list[dict], use_web_search: bool = False) -> str:
    """
    Get full response (non-streaming) for LINE bot and other uses.

    Args:
        messages: Conversation history as list of {role, content} dicts
        use_web_search: Whether to enable web search tool

    Returns:
        Complete response text
    """
    tools = [{"type": "web_search"}] if use_web_search else []

    try:
        client = get_client()
        response = await client.responses.create(
            model=MODEL,
            instructions=get_system_prompt(),
            input=messages,
            tools=tools
        )
        return response.output_text

    except Exception as e:
        print(f"OpenAI API error: {e}")
        return f"Sorry, I encountered an error. Please try again later."
