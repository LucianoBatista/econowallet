import logging

from fastapi import FastAPI

from project.app.api import status
from project.app.database.database_session import global_init

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(
        status.router,
        tags=["Hello"],
        prefix="/api/v1"
    )
    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    global_init()
