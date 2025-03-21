from fastapi import APIRouter
from src.endpoint.chat_endpoint import chat_router

main_router = APIRouter()

main_router.include_router(chat_router, prefix="/multi-agent")
