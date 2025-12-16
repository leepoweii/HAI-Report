import os
import asyncio
from fastapi import APIRouter, Request, HTTPException

router = APIRouter()

# LINE Bot configuration - only initialize if credentials are provided
LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET")
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")


@router.post("/webhook")
async def line_webhook(request: Request):
    """
    LINE Bot webhook endpoint.
    Receives messages from LINE and responds using the chatbot.
    """
    # Check if LINE credentials are configured
    if not LINE_CHANNEL_SECRET or not LINE_CHANNEL_ACCESS_TOKEN:
        return {"status": "LINE Bot not configured"}

    # Import LINE SDK only if credentials are available
    from linebot.v3 import WebhookHandler
    from linebot.v3.messaging import (
        Configuration,
        ApiClient,
        MessagingApi,
        ReplyMessageRequest,
        TextMessage
    )
    from linebot.v3.webhooks import MessageEvent, TextMessageContent
    from linebot.v3.exceptions import InvalidSignatureError

    from services.chatbot import get_full_response

    # Initialize LINE Bot
    configuration = Configuration(access_token=LINE_CHANNEL_ACCESS_TOKEN)
    handler = WebhookHandler(LINE_CHANNEL_SECRET)

    signature = request.headers.get("X-Line-Signature", "")
    body = await request.body()
    body_text = body.decode()

    try:
        # Process webhook events
        events = handler.parser.parse(body_text, signature)

        for event in events:
            if isinstance(event, MessageEvent) and isinstance(event.message, TextMessageContent):
                user_message = event.message.text

                # Get response from chatbot (non-streaming)
                response_text = await get_full_response([
                    {"role": "user", "content": user_message}
                ])

                # Reply to user
                with ApiClient(configuration) as api_client:
                    line_bot_api = MessagingApi(api_client)
                    line_bot_api.reply_message(
                        ReplyMessageRequest(
                            reply_token=event.reply_token,
                            messages=[TextMessage(text=response_text)]
                        )
                    )

        return {"status": "OK"}

    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Invalid signature")
    except Exception as e:
        print(f"LINE webhook error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
