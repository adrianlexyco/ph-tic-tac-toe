from typing import cast
from fastapi import APIRouter

from app.infrastructure.repositories import player_repository as player_repository_db

from app.core.protocols.player_repository import PlayerRepository

router = APIRouter(tags=["player"], prefix="/players")

from ...core.services import player_service

player_repository = cast(PlayerRepository, player_repository_db)


@router.post("/")
async def create_player(name: str):
    result = await player_service.create(player_repository=player_repository, name=name)
    return {"code": "success", "player": result}
