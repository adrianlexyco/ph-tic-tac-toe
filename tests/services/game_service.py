from datetime import datetime
import unittest
from uuid import UUID

from unittest.mock import AsyncMock
from app.core.models.game import Game, GameMovements
from app.core.protocols.game_repository import GameRepository
from app.core.services.game_service import (
    add_movement,
    calculate_game_status,
    create,
    fetch_by_id,
)

game_id = "c0259b25-a2df-44cd-a946-26e58d11a300"
player1_id = "c0259b25-a2df-44cd-a946-26e58d11a301"
player2_id = "c0259b25-a2df-44cd-a946-26e58d11a302"

board_configurations = {
    "game.winner."
    + str(player1_id): {
        "row": [1, 4, 2, 7, 3],
        "column": [2, 1, 5, 9, 8],
        "main_diagonal": [1, 2, 5, 3, 9],
        "secondary_diagonal": [3, 1, 5, 2, 7],
    },
    "game.winner."
    + str(player2_id): {
        "row": [1, 4, 2, 5, 9, 6],
        "column": [2, 1, 3, 4, 9, 7],
        "main_diagonal": [8, 1, 4, 5, 6, 9],
        "secondary_diagonal": [1, 3, 2, 5, 4, 7],
    },
    "game.draw": {"draw": [1, 3, 5, 4, 6, 8, 7, 9, 2]},
    "game.not.finished": {
        "few_movements": {1, 2},
        "not_finished": {1, 2, 3, 4, 5, 6},
    },
}


class GameServiceTest(unittest.TestCase):
    @AsyncMock(GameRepository, "create")
    async def test_create(self, mock_create):
        mock_create.return_value = Game(
            id=game_id,
            board_size=3,
            player1_id=player1_id,
            player2_id=player2_id,
            movements=[],
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )

        result = await create(GameRepository, player1_id, player2_id, "3")

        self.assertEqual(result.id, game_id)
        self.assertEqual(result.board_size, 3)
        self.assertEqual(result.player1_id, player1_id)
        self.assertEqual(result.player2_id, player2_id)

    @AsyncMock(GameRepository, "fetch_by_id")
    async def test_fetch_by_id(self, mock_fetch):
        mock_fetch.return_value = Game(
            id=game_id,
            board_size=3,
            player1_id=player1_id,
            player2_id=player2_id,
            movements=[],
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )

        result = fetch_by_id(GameRepository, UUID(game_id))

        self.assertEqual(result.id, game_id)
        self.assertEqual(result.board_size, 3)
        self.assertEqual(result.player1_id, player1_id)
        self.assertEqual(result.player2_id, player2_id)

    @AsyncMock(GameRepository, "fetch_by_id")
    @AsyncMock(GameRepository, "add_movement")
    async def test_add_movement(self, mock_fetch, mock_add):
        movements = GameMovements(UUID(player1_id), 1)
        mock_fetch.return_value = Game(
            id=game_id,
            board_size=3,
            player1_id=player1_id,
            player2_id=player2_id,
            movements=[movements],
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        mock_add.return_value = True

        result = await add_movement(GameRepository, UUID(game_id), 2, UUID(player2_id))

        self.assertEqual(result.movements[-1].board_position, 2)
        self.assertEqual(result.movements[-1].player, UUID(player2_id))

    def test_calculate_game_status_winner(self):
        for game_status, game_configs in board_configurations.items():
            for config, positions in game_configs.items():
                with self.subTest(game_status=game_status, config=config):
                    movements = []
                    for i, position in enumerate(positions):
                        player_id = player1_id if i % 2 == 0 else player2_id
                        movements.append(
                            GameMovements(board_position=position, player=player_id)
                        )
                    game = Game(
                        id=game_id,
                        board_size=3,
                        player1_id=player1_id,
                        player2_id=player2_id,
                        movements=movements,
                    )

                    result = calculate_game_status(game)

                    self.assertEqual(result, game_status)


if __name__ == "__main__":
    unittest.main()
