import logging
import os

from fastapi import FastAPI

from src.common.dto.api import MessageResponse
from src.common.storage.postgres.postgres_service import PostgresService

from src.auth.router import router as auth_router


database_url = os.environ.get("DATABASE_URI", "postgresql://postgres:postgres@postgres:5432/postgres")
db_service = PostgresService(database_url)
db_service.init_database()

logger = logging.getLogger(__name__)

#Initiate FastAPI
app = FastAPI(title="Supernova")

app.include_router(auth_router)

@app.get("/")
async def ping() -> MessageResponse:
    return MessageResponse(message="Pong!")

if os.getenv("DEBUG"):
    logger.critical("!!! RUNNING IN DEBUG MODE !!!")
    @app.post("/debug/drop")
    def drop() -> None:
        db_service.drop_database()
        db_service.init_database()