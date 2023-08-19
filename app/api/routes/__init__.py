from fastapi import FastAPI

from .game import router as GameRouter
from .player import router as PlayerRouter

def build_routers(app: FastAPI):
    app.include_router(GameRouter)
    app.include_router(PlayerRouter)
