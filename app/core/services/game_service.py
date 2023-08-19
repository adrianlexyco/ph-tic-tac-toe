from typing import Optional
from uuid import UUID
from app.core.models.game import Game
from app.core.protocols.game_repository import GameRepository
from app.core.services.exceptions import GenericError


async def create(game_repository: GameRepository, player1_id: UUID, player2_id: UUID, board_size: str) -> Game:
    game = await game_repository.create(player1_id=player1_id, player2_id=player2_id, board_size=board_size)

    return game

async def fetch_by_id(game_repository: GameRepository, id: UUID) -> Optional[Game]:
    game = await game_repository.fetch_by_id(id=id)

    if not game:
        raise GenericError(error="game.not.found")

    return game
