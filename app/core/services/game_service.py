from enum import Enum
import math
from typing import Optional, List
from uuid import UUID
from app.core.models.game import Game, GameDetails, GameMovements
from app.core.protocols.game_repository import GameRepository
from app.core.services.exceptions import GenericError
from app.core.services.utils import build_user_board, column_winner, main_diagonal_winner, row_winner, secondary_diagonal_winner


async def create(
    game_repository: GameRepository, player1_id: UUID, player2_id: UUID, board_size: str
) -> Game:
    game = await game_repository.create(
        player1_id=player1_id, player2_id=player2_id, board_size=board_size
    )

    return game


async def fetch_by_id(
    game_repository: GameRepository, id: UUID
) -> Optional[GameDetails]:
    game = await game_repository.fetch_by_id(id=id)

    if not game:
        raise GenericError(error="game.not.found")

    return GameDetails(
        id=game.id,
        board_size=game.board_size,
        player1_id=game.player1_id,
        player2_id=game.player2_id,
        movements=game.movements,
        status=calculate_game_status(game),
    )


async def add_movement(
    game_repository: GameRepository, id: UUID, board_position: int, player: UUID
) -> Optional[Game]:
    game = await game_repository.fetch_by_id(id=id)

    if not game:
        raise GenericError(error="game.not.found")

    if player not in [game.player1_id, game.player2_id]:
        raise GenericError(error="user.not.player")

    if board_position < 1 or board_position > game.board_size * game.board_size:
        raise GenericError(error="movement.not.available")

    if len(game.movements) > 0 and game.movements[-1].player == player:
        raise GenericError(error="user.already.played")

    if board_position in [position.board_position for position in game.movements]:
        raise GenericError(error="movement.already.played")

    add_movement = await game_repository.add_movement(
        id=id, board_position=board_position, player=player
    )

    if not add_movement:
        raise GenericError(error="movement.not.played")

    return add_movement


def calculate_game_status(game: Game) -> str:
    if len(game.movements) < 6:
        return "game.not.finished"

    board = build_user_board(board_size=game.board_size, movements=game.movements)

    for player in [game.player1_id, game.player2_id]:
        if (
            row_winner(game.board_size, board, player)
            or column_winner(game.board_size, board, player)
            or main_diagonal_winner(game.board_size, board, player)
            or secondary_diagonal_winner(game.board_size, board, player)
        ):
            return "game.winner."+str(player)

    if len(game.movements) == game.board_size**2:
        return "game.draw"
    
    return "game.not.finished"
