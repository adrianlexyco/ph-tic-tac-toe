from beanie import init_beanie
from fastapi import FastAPI

from motor.motor_asyncio import AsyncIOMotorClient
from app.infrastructure.models.game import Game

from app.infrastructure.models.player import Player
from .routes import build_routers

app = FastAPI()

async def setup_beanie():
    # TODO: extract into .env
    client = AsyncIOMotorClient("mongodb://testing_db:testing_db@db_mongo:27017")
    await init_beanie(database=client['testing_db'], document_models=[Player, Game])

@app.on_event("startup")
async def startup_event():
    await setup_beanie()
    build_routers(app)

@app.get("/")
def read_root():
    return {"message": "Hello"}
