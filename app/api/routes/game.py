from typing import Optional, cast
from uuid import UUID
from fastapi import APIRouter, HTTPException
from app.core.protocols.player_repository import PlayerRepository
from app.core.protocols.game_repository import GameRepository
from app.core.services.exceptions import GenericError

router = APIRouter(tags=["games"], prefix="/games")

from app.infrastructure.repositories import player_repository as player_repository_db
from app.infrastructure.repositories import game_repository as game_repository_db

from ...core.services import game_service

player_repository = cast(PlayerRepository, player_repository_db)
game_repository = cast(GameRepository, game_repository_db)


@router.post("/")
async def create_game(player1_id: UUID, player2_id: UUID, board_size: Optional[str]):
    result = await game_service.create(
        game_repository=game_repository,
        player1_id=player1_id,
        player2_id=player2_id,
        board_size=board_size,
    )
    return {"code": "success", "game": result}


@router.get("/{id}")
async def get_game(id: UUID):
    try:
        result = await game_service.fetch_by_id(game_repository=game_repository, id=id)
        return {"code": "success", "game": result}
    except GenericError as error:
        raise HTTPException(status_code=404, detail=error.code)


@router.put("/{id}")
async def add_movement(id: UUID, board_position: int, player: UUID):
    try:
        result = await game_service.add_movement(
            game_repository=game_repository,
            id=id,
            board_position=board_position,
            player=player,
        )
        return {"code": "success", "game": result}
    except GenericError as error:
        raise HTTPException(status_code=404, detail=error.code)
