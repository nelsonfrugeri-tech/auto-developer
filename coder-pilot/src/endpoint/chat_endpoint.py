from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from src.runner.runner import Runner


class ChatRequest(BaseModel):
    query: str


chat_router = APIRouter()
runner = Runner()


@chat_router.post("/v1/chat", response_class=StreamingResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        return StreamingResponse(runner.run(request.query), media_type="text/plain")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
