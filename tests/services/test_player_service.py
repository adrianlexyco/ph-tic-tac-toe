import unittest
from unittest.mock import AsyncMock

from uuid import UUID
from app.core.services.exceptions import GenericError
from app.core.services.player_service import create, fetch_by_id
from app.core.protocols.player_repository import PlayerRepository
from app.core.models.player import Player

player_name = "Adrian"
player_id = "c0259b25-a2df-44cd-a946-26e58d11a301"

class PlayerServiceTest(unittest.TestCase):
    @AsyncMock(PlayerRepository, "create")
    async def test_create(self, mock_create):
        mock_create.return_value = Player(id=player_id, name=player_name)

        result = await create(PlayerRepository, player_name)

        self.assertEqual(result.id, player_id)
        self.assertEqual(result.name, player_name)

    @AsyncMock(PlayerRepository, "fetch_by_id")
    async def test_fetch_by_id(self, mock_fetch):
        
        mock_fetch.return_value = Player(id=player_id, name=player_name)

        result = await fetch_by_id(PlayerRepository, UUID(player_id))

        self.assertEqual(result.id, player_id)
        self.assertEqual(result.name, player_name)

    @AsyncMock(PlayerRepository, "fetch_by_id")
    async def test_fetch_by_id_not_found(self, mock_fetch):
        mock_fetch.return_value = None

        with self.assertRaises(GenericError):
            await fetch_by_id(PlayerRepository, UUID(player_id))


if __name__ == "__main__":
    unittest.main()