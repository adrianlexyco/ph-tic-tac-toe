from typing import Optional
from uuid import UUID

from app.core.models.game import Game

from ..models.game import Game as GameModel


async def create(player1_id: UUID, player2_id: UUID, board_size: str ) -> Game:
    game = await GameModel(player1_id=player1_id, player2_id=player2_id, board_size=board_size).create()

    return game


async def fetch_by_id(id: UUID) -> Optional[Game]:
    game = await GameModel.find_one(GameModel.id == id)

    if not game:
        return None

    return game
