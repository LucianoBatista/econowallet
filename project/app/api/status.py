import os

from fastapi import APIRouter, Depends

from app.config import Settings, get_settings

router = APIRouter()
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")


@router.get("/status")
async def ping(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "version": APP_VERSION,
        "environment": settings.environment,
        "testing": settings.testing
    }