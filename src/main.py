import logging

from fastapi import FastAPI

from common.dto.api import MessageResponse

from auth.router import router as auth_router

logger = logging.getLogger(__name__)

# Initiate FastAPI
app = FastAPI(title="Supernova")

app.include_router(auth_router)


@app.get("/")
async def ping() -> MessageResponse:
    return MessageResponse(message="Pong!")
