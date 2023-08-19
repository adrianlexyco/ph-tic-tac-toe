from typing import cast
from uuid import UUID

from fastapi import APIRouter, HTTPException

from app.core.protocols.player_repository import PlayerRepository
from app.core.services.exceptions import GenericError
from app.infrastructure.repositories import player_repository as player_repository_db

router = APIRouter(tags=["player"], prefix="/players")

from ...core.services import player_service

player_repository = cast(PlayerRepository, player_repository_db)


@router.post("/")
async def create_player(name: str):
    result = await player_service.create(player_repository=player_repository, name=name)
    return {"code": "success", "player": result}


@router.get("/{id}")
async def get_player(id: UUID):
    try:
        result = await player_service.fetch_by_id(
            player_repository=player_repository, id=id
        )
        return {"code": "success", "player": result}
    except GenericError as error:
        raise HTTPException(status_code=404, detail=error.code)
